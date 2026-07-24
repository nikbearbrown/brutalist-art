#!/usr/bin/env python3
"""
smithsonian_index.py — build/update the Smithsonian Open Access metadata index
================================================================================
Writes CC0 + has-image object metadata for the vox-register units to:

    brutalist-art/library/smithsonian/index.jsonl

ARCHITECTURE NOTE — image URLs are NOT stored in the index.
The SI search API does not reliably return full-resolution download URLs.
The index stores the record_id; full-res URLs are resolved at fetch time by
hitting the content-detail endpoint (/content/{id}).
Thumbnail URLs are stored for the LOOK step (preview before committing to fetch).

Each row: id, title, unit, credit, object_type, date, cc0, thumbnail_url, tokens.
MEDIA IS NEVER DOWNLOADED — this is metadata only.

Why object_type matters: a search for "UNIVAC" returns ~227 CC0 rows, but most
are paper documentation/pamphlets/ID-plates. object_type lets the runtime
pre-rank apparatus (mainframe computer, console) over ephemera (documentation,
pamphlet) even before keyword scoring.

Mode A (API):  needs a free api.data.gov key (SI_API_KEY env var or --api-key).
               Targeted and fast; only the register slice is fetched.
               Full-res URL resolution at fetch time requires the same key.
Mode B (S3):   streams the SI Open Access S3 NDJSON dumps line-by-line.
               No key required. Full EDAN records → stores image_url directly
               so fetch works without hitting the API again.

Usage (from brutalist-art/ or books/):
    # API mode (recommended):
    python3 runtime/scripts/smithsonian_index.py --api-key YOUR_KEY
    python3 runtime/scripts/smithsonian_index.py    # reads SI_API_KEY from env

    # S3 streaming mode (no key, slower):
    python3 runtime/scripts/smithsonian_index.py --s3

    # Resume / append after interruption:
    python3 runtime/scripts/smithsonian_index.py --api-key KEY --resume

    # Specific units only:
    python3 runtime/scripts/smithsonian_index.py --api-key KEY --units NMAH NPG

    # Stats only:
    python3 runtime/scripts/smithsonian_index.py --stats
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ART_HOME = Path(__file__).resolve().parents[2]  # brutalist-art/
LIBRARY  = ART_HOME / "library" / "smithsonian"
INDEX    = LIBRARY / "index.jsonl"
META     = LIBRARY / "index_meta.json"

SI_API_BASE = "https://api.si.edu/openaccess/api/v1.0"
S3_HTTP     = "https://smithsonian-open-access.s3.amazonaws.com/metadata/edan"

# Register units — the only units we index.
REGISTER_UNITS: dict[str, str] = {
    "NMAH":   "National Museum of American History",
    "NASM":   "National Air and Space Museum",
    "NPG":    "National Portrait Gallery",
    "NMAAHC": "National Museum of African American History and Culture",
    "SIL":    "Smithsonian Institution Libraries",
    "SIA":    "Smithsonian Institution Archives",
    "SAAM":   "Smithsonian American Art Museum",
}

S3_UNIT_FILES = {k: k.lower() for k in REGISTER_UNITS}

STOP_WORDS = {
    "the", "a", "an", "of", "to", "and", "with", "in", "on", "at", "as",
    "is", "it", "its", "for", "into", "that", "this", "from", "or", "by",
    "not", "was", "are", "has", "had", "but", "one", "two", "three",
    "national", "museum", "collection", "smithsonian", "institution",
}


# ─── Extraction helpers ───────────────────────────────────────────────────────

def _tokens(title: str, subjects: list[str] | None = None) -> list[str]:
    text = title + " " + " ".join(subjects or [])
    words = [w.lower() for w in re.split(r"[^a-zA-Z]+", text) if w]
    seen: set[str] = set()
    out: list[str] = []
    for w in words:
        if len(w) < 3 or w in STOP_WORDS or w in seen:
            continue
        seen.add(w)
        out.append(w)
    return out[:40]


def _extract_object_type(content: dict) -> str:
    """
    Pull the first object_type value — used for apparatus-vs-ephemera ranking.
    Tries indexedStructured first (clean strings), then freetext.objectType.
    """
    idx = content.get("indexedStructured", {})
    ot_list = idx.get("object_type", [])
    if ot_list and isinstance(ot_list, list):
        return str(ot_list[0]).lower().strip()

    freetext = content.get("freetext", {})
    for item in freetext.get("objectType", []):
        if isinstance(item, dict) and item.get("content"):
            return item["content"].lower().strip()
    return ""


def _extract_date(content: dict) -> str:
    """Best-effort date extraction."""
    dnr = content.get("descriptiveNonRepeating", {})
    for key in ("date", "year"):
        val = dnr.get(key, "")
        if val:
            return str(val).strip()
    idx = content.get("indexedStructured", {})
    dates = idx.get("date", [])
    if dates:
        return str(dates[0]).strip()
    return ""


def _npg_url_valid(url: str) -> bool:
    """
    NPG IDS delivery-service URLs come in two formats:
      Working:  ...?id=NPG-S_NPG.82.67   (has S_ before the record number)
      Dead-end: ...?id=NPG-NPG_78.164    (no S_; returns HTTP 404)
    Returns True only for the working S_ format.
    Non-NPG URLs always pass.
    """
    if not url or "NPG" not in url:
        return True
    # If URL contains NPG-NPG_ it's the dead-end format
    if "NPG-NPG_" in url:
        return False
    return True


def _extract_record_api(obj: dict) -> dict | None:
    """
    Parse one SI search API row into an index record.
    Does NOT store image_url — full-res URL is resolved at fetch time
    via /content/{id}. Stores thumbnail_url for the LOOK step.
    Returns None if the record lacks a CC0 image or required fields.
    NPG records with dead-end NPG-NPG_* URLs are skipped (they 404).
    """
    oid   = obj.get("id", "").strip()
    title = obj.get("title", "").strip()
    unit  = obj.get("unitCode", obj.get("unit_code", "")).strip()

    if not oid or not title or unit not in REGISTER_UNITS:
        return None

    content = obj.get("content", {})
    dnr     = content.get("descriptiveNonRepeating", {})
    media_list = dnr.get("online_media", {}).get("media", [])

    thumbnail_url = ""
    has_cc0_image = False
    for m in media_list:
        if m.get("type", "").lower() not in ("images", "image"):
            continue
        usage = m.get("usage", {})
        if isinstance(usage, dict) and usage.get("access") == "CC0":
            candidate_url = m.get("thumbnail") or m.get("content") or ""
            # P3: skip NPG records whose image URL is the dead-end NPG-NPG_* format
            if unit == "NPG" and not _npg_url_valid(candidate_url):
                continue
            has_cc0_image = True
            # thumbnail field is a deliveryService URL — good enough for LOOK
            thumbnail_url = candidate_url
            break

    if not has_cc0_image:
        return None

    credit_raw = dnr.get("credit_line", {})
    if isinstance(credit_raw, dict):
        credit = credit_raw.get("content", "")
    elif isinstance(credit_raw, list):
        credit = credit_raw[0].get("content", "") if credit_raw else ""
    else:
        credit = str(credit_raw)

    subjects: list[str] = []
    freetext = content.get("freetext", {})
    for key in ("topic", "name", "place"):
        for item in freetext.get(key, []):
            if isinstance(item, dict):
                subjects.append(item.get("content", ""))

    return {
        "id":            oid,
        "title":         title,
        "unit":          unit,
        "credit":        credit.strip(),
        "object_type":   _extract_object_type(content),
        "date":          _extract_date(content),
        "cc0":           True,
        "thumbnail_url": thumbnail_url,
        # image_url intentionally omitted — resolved at fetch time via /content/{id}
        "tokens":        _tokens(title, subjects),
    }


def _extract_record_s3(obj: dict) -> dict | None:
    """
    Parse one full EDAN record from the S3 dump.
    S3 records ARE full records, so we CAN extract the image_url directly —
    this lets fetch skip the content-detail API call (useful in no-key setups).
    """
    if "_source" in obj and isinstance(obj["_source"], dict):
        obj = obj["_source"]

    oid   = obj.get("id", "").strip()
    title = obj.get("title", "").strip()
    unit  = obj.get("unitCode", obj.get("unit_code", "")).strip()

    if not oid or not title or unit not in REGISTER_UNITS:
        return None

    content = obj.get("content", {})
    dnr     = content.get("descriptiveNonRepeating", {})
    media_list = dnr.get("online_media", {}).get("media", [])

    image_url     = ""
    thumbnail_url = ""
    has_cc0_image = False
    for m in media_list:
        if m.get("type", "").lower() not in ("images", "image"):
            continue
        usage = m.get("usage", {})
        if isinstance(usage, dict) and usage.get("access") == "CC0":
            has_cc0_image = True
            image_url     = m.get("content") or m.get("url") or ""
            thumbnail_url = m.get("thumbnail") or ""
            break

    if not has_cc0_image or not image_url:
        return None

    credit_raw = dnr.get("credit_line", {})
    if isinstance(credit_raw, dict):
        credit = credit_raw.get("content", "")
    elif isinstance(credit_raw, list):
        credit = credit_raw[0].get("content", "") if credit_raw else ""
    else:
        credit = str(credit_raw)

    subjects: list[str] = []
    freetext = content.get("freetext", {})
    for key in ("topic", "name", "place"):
        for item in freetext.get(key, []):
            if isinstance(item, dict):
                subjects.append(item.get("content", ""))

    return {
        "id":            oid,
        "title":         title,
        "unit":          unit,
        "credit":        credit.strip(),
        "object_type":   _extract_object_type(content),
        "date":          _extract_date(content),
        "cc0":           True,
        "thumbnail_url": thumbnail_url,
        "image_url":     image_url,   # available from full S3 record; omitted in API mode
        "tokens":        _tokens(title, subjects),
    }


# ─── API mode ────────────────────────────────────────────────────────────────

def _build_api(api_key: str,
               resume_ids: set[str],
               units: list[str] | None) -> tuple[int, dict[str, int]]:
    try:
        import requests
    except ImportError:
        sys.exit("[si-index] 'requests' not installed — pip install requests")

    target = units or list(REGISTER_UNITS)
    total_new = 0
    by_unit: dict[str, int] = {}

    with INDEX.open("a", encoding="utf-8") as fout:
        for unit in target:
            print(f"[si-index] API: {unit} — {REGISTER_UNITS.get(unit, '?')} ...")
            # All filters in a single q string — the SI API ignores fq params.
            # numFound in the response is always 0/None; paginate until rows < page.
            q = (f"unit_code:{unit} AND "
                 f"online_media_type:Images AND "
                 f"metadata_usage:CC0")

            # Sanity probe: if start=500k returns records, the filter isn't scoping
            # correctly and we'd ingest the full catalog. Check before writing anything.
            try:
                probe = requests.get(f"{SI_API_BASE}/search",
                                     params={"api_key": api_key, "q": q,
                                             "rows": 1, "start": 500_000},
                                     timeout=30)
                probe.raise_for_status()
                probe_rows = probe.json().get("response", {}).get("rows", [])
                if probe_rows:
                    print(f"[si-index]   ABORT {unit} — filter bleed: records exist "
                          f"beyond start=500k (full-catalog leak). Skipping unit.")
                    continue
            except Exception as exc:
                print(f"[si-index]   Sanity probe failed ({exc}); proceeding cautiously")

            start    = 0
            page     = 500
            unit_new = 0
            scanned  = 0

            while True:
                params = {
                    "api_key": api_key,
                    "q":       q,
                    "rows":    page,
                    "start":   start,
                }
                try:
                    resp = requests.get(f"{SI_API_BASE}/search",
                                        params=params, timeout=30)
                    resp.raise_for_status()
                    data = resp.json()
                except Exception as exc:
                    print(f"[si-index]   ERROR at start={start}: {exc}")
                    break

                rows = data.get("response", {}).get("rows", [])
                if not rows:
                    break

                for obj in rows:
                    oid = obj.get("id", "")
                    if oid and oid in resume_ids:
                        continue
                    rec = _extract_record_api(obj)
                    if rec:
                        fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
                        resume_ids.add(rec["id"])
                        unit_new += 1

                scanned += len(rows)
                start   += len(rows)
                if scanned % 5000 < page:
                    print(f"[si-index]   {unit}: {scanned:,} scanned, "
                          f"{unit_new:,} CC0-image records indexed")

                # API never returns numFound — stop when page is not full
                if len(rows) < page:
                    break
                time.sleep(0.2)

            total_new += unit_new
            by_unit[unit] = unit_new
            print(f"[si-index]   {unit}: done — {unit_new} records added")

    return total_new, by_unit


# ─── S3 streaming mode ───────────────────────────────────────────────────────

def _build_s3(resume_ids: set[str],
              units: list[str] | None) -> tuple[int, dict[str, int]]:
    try:
        import requests
    except ImportError:
        sys.exit("[si-index] 'requests' not installed — pip install requests")

    target = units or list(S3_UNIT_FILES)
    total_new = 0
    by_unit: dict[str, int] = {}

    with INDEX.open("a", encoding="utf-8") as fout:
        for unit in target:
            fname = S3_UNIT_FILES.get(unit)
            if not fname:
                print(f"[si-index] S3: no file mapping for '{unit}', skipping")
                continue

            url = f"{S3_HTTP}/{fname}.txt"
            print(f"[si-index] S3: streaming {url} ...")
            try:
                resp = requests.get(url, stream=True, timeout=120)
                resp.raise_for_status()
            except Exception as exc:
                print(f"[si-index]   S3 ERROR: {exc}")
                continue

            unit_new   = 0
            line_count = 0
            for raw in resp.iter_lines():
                if not raw:
                    continue
                line_count += 1
                try:
                    obj = json.loads(raw)
                except (json.JSONDecodeError, UnicodeDecodeError):
                    continue

                if "unitCode" not in obj and "_source" not in obj:
                    obj["unitCode"] = unit

                oid = obj.get("id", "") or obj.get("_source", {}).get("id", "")
                if oid and oid in resume_ids:
                    continue

                rec = _extract_record_s3(obj)
                if rec:
                    fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    resume_ids.add(rec["id"])
                    unit_new += 1

                if line_count % 100_000 == 0:
                    print(f"[si-index]   {unit}: {line_count:,} lines, "
                          f"{unit_new:,} indexed so far")

            total_new += unit_new
            by_unit[unit] = unit_new
            print(f"[si-index]   {unit}: done — {unit_new:,} CC0-image records "
                  f"from {line_count:,} total lines")

    return total_new, by_unit


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _load_resume_ids() -> set[str]:
    if not INDEX.exists():
        return set()
    ids: set[str] = set()
    with INDEX.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                ids.add(json.loads(line)["id"])
            except (json.JSONDecodeError, KeyError):
                pass
    return ids


def _count_index() -> tuple[int, dict[str, int]]:
    if not INDEX.exists():
        return 0, {}
    total    = 0
    by_unit: dict[str, int] = {}
    with INDEX.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                u = rec.get("unit", "?")
                by_unit[u] = by_unit.get(u, 0) + 1
                total += 1
            except json.JSONDecodeError:
                pass
    return total, by_unit


def _stats() -> None:
    total, by_unit = _count_index()
    if total == 0:
        print("[si-index] No index yet — run without --stats to build it.")
        return
    print(f"[si-index] Index: {total:,} records in {INDEX}")
    for unit in sorted(by_unit):
        print(f"  {unit:<10} {by_unit[unit]:>8,}  {REGISTER_UNITS.get(unit, '')}")
    if META.exists():
        m = json.loads(META.read_text())
        print(f"  Built: {m.get('built_at', '?')}  Mode: {m.get('mode', '?')}")


# ─── Main ────────────────────────────────────────────────────────────────────

def _load_env_key() -> str:
    """Read SI_API_KEY or SMITHSONIAN_API_KEY from .env or environment."""
    for name in ("SI_API_KEY", "SMITHSONIAN_API_KEY"):
        if os.environ.get(name):
            return os.environ[name]
    env_file = ART_HOME / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("#"):
                continue
            for name in ("SI_API_KEY=", "SMITHSONIAN_API_KEY="):
                if line.startswith(name):
                    val = line[len(name):].strip().strip('"').strip("'")
                    if val:
                        return val
    return ""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--api-key",
                    default=_load_env_key(),
                    metavar="KEY",
                    help="api.data.gov key (or set SI_API_KEY / SMITHSONIAN_API_KEY env var)")
    ap.add_argument("--s3", action="store_true",
                    help="stream metadata from S3 (no key, slower; stores image_url)")
    ap.add_argument("--units", nargs="*", metavar="UNIT",
                    help="limit to these unit codes (default: all register units)")
    ap.add_argument("--resume", action="store_true",
                    help="skip already-indexed ids; safe to re-run after interruption")
    ap.add_argument("--stats", action="store_true",
                    help="print index stats and exit")
    a = ap.parse_args()

    if a.stats:
        _stats()
        return 0

    if a.units:
        unknown = [u for u in a.units if u not in REGISTER_UNITS]
        if unknown:
            print(f"[si-index] Unknown unit(s): {unknown}")
            print(f"           Known: {list(REGISTER_UNITS)}")
            return 1

    LIBRARY.mkdir(parents=True, exist_ok=True)

    resume_ids = _load_resume_ids() if a.resume else set()
    if resume_ids:
        print(f"[si-index] Resume: {len(resume_ids):,} ids already indexed, skipping")

    if a.s3:
        new_rows, by_unit = _build_s3(resume_ids, a.units)
        mode = "s3"
    elif a.api_key:
        new_rows, by_unit = _build_api(a.api_key, resume_ids, a.units)
        mode = "api"
    else:
        print("[si-index] No API key found.")
        print("  Option A — paste your key:")
        print("    python3 runtime/scripts/smithsonian_index.py --api-key YOUR_KEY")
        print("  Option B — add to .env:  SI_API_KEY=YOUR_KEY")
        print("  Option C — no key, stream from S3 (slower):")
        print("    python3 runtime/scripts/smithsonian_index.py --s3")
        print("  Get a free key: https://api.data.gov/signup/")
        return 1

    total, final_by_unit = _count_index()
    print(f"\n[si-index] Done. New rows added: {new_rows:,}")
    print(f"[si-index] Index total: {total:,} records at {INDEX}")

    META.write_text(json.dumps({
        "built_at":      datetime.now(timezone.utc).isoformat(),
        "mode":          mode,
        "total_records": total,
        "by_unit":       final_by_unit,
    }, indent=2))

    _stats()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
