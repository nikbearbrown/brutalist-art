#!/usr/bin/env python3
"""
pantry_search.py — library-first pantry sourcing
================================================
Search the local image library (SVG icons + generated-still stock) AND any
registered archival-image adapter (Smithsonian, NASA, Wellcome, NLM IHM).

Local hits can be copied directly into a reel's pantry/ with --copy --beat.
Archival hits require a fetch step — the script prints the image_fetch.py
command to run (download + Topaz upscale + shelve).

Doctrine: before a SHOPPING.md / SHOTLIST.md request card is written for a
still, search here first. LOOK at every candidate before accepting it —
a token match is a lead, not a verdict. An archival hit is a lead; open the
thumbnail URL and judge register fit (greyscale/duotone + Ken Burns crop) before
fetching. No good match -> write the card as usual.

Usage (from brutalist-art/ or books/ — the script resolves its own home):
    python3 runtime/scripts/pantry_search.py "UNIVAC computer console"
    python3 runtime/scripts/pantry_search.py "Otto Warburg portrait"
    python3 runtime/scripts/pantry_search.py "young bear" --kind png --top 15
    python3 runtime/scripts/pantry_search.py "young bear" \\
        --copy ../physics-quantum-mechanics/youtube/my-reel --beat B14
    python3 runtime/scripts/pantry_search.py "" --pick young-01 \\
        --copy <reel> --beat B14      # copy a specific id, no search rank

    # Single source only:
    python3 runtime/scripts/pantry_search.py "Apollo" --source nasa
    python3 runtime/scripts/pantry_search.py "Koch portrait" --source wellcome
    python3 runtime/scripts/pantry_search.py "bear" --source local

--copy copies PNGs only (the pantry eats pngs/mp4s; SVG hits are doodle-tier
assets — use them through doodle_fill, not the pantry). Destination name:
<reel>/pantry/<BID>-<id>.png (pantry.py keys on the beat-id prefix).

Deterministic: same manifest + terms -> same ranking. Requires icons.json —
run  python3 skills/make/doodle/scripts/build_index.py  after adding images.

Smithsonian index:
run  python3 runtime/scripts/smithsonian_index.py --api-key KEY  to build it.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ART_HOME = Path(__file__).resolve().parents[2]  # brutalist-art/
SI_INDEX = ART_HOME / "library" / "smithsonian" / "index.jsonl"

# Archival adapter registry (load lazily — network not required for local search)
_ARCHIVE_SOURCES = ["smithsonian", "nasa", "wellcome", "nlm_ihm"]
_ALL_SOURCES = ["all", "local"] + _ARCHIVE_SOURCES


def _find_library() -> Path:
    for cand in ("doodles/svg", "svg/svg", "svg/organized-svg", "doodles/organized-svg"):
        p = ART_HOME / cand
        if p.is_dir() and (p / "icons.json").exists():
            return p
    return ART_HOME / "svg" / "svg"


STOP = {
    "the", "a", "an", "of", "to", "and", "with", "in", "on", "at", "as",
    "is", "it", "its", "for", "into", "that", "this", "one", "two",
    "national", "museum", "collection", "smithsonian", "institution",
}


def term_words(terms: str) -> list[str]:
    words = [w.lower() for w in re.split(r"[^a-zA-Z]+", terms) if w]
    return [w for w in words if w not in STOP and len(w) >= 3]


def score(icon: dict, words: list[str]) -> tuple[int, float]:
    """(exact_hits, ranking_score) — deterministic token overlap."""
    exact = 0
    s = 0.0
    toks = icon["tokens"]
    for w in words:
        if w in toks:
            exact += 1
            s += 3.0
        elif any(t.startswith(w) or w.startswith(t) for t in toks if len(t) > 3 and len(w) > 3):
            s += 1.0
    return exact, s - 0.01 * len(toks)


_APPARATUS_TYPES = {
    "computer", "mainframe", "console", "instrument", "apparatus",
    "device", "machine", "equipment", "calculator", "terminal",
    "processor", "component", "circuit", "hardware", "unit",
    "system", "workstation", "printer", "display", "monitor",
}
_EPHEMERA_TYPES = {
    "documentation", "pamphlet", "manual", "publication", "brochure",
    "report", "catalog", "catalogue", "document", "paper", "book",
    "booklet", "journal", "newsletter", "flyer", "advertisement",
    "photograph", "postcard", "poster", "press release",
}


def _si_object_type_bonus(rec: dict) -> float:
    ot = rec.get("object_type", "").lower()
    if not ot:
        return 0.0
    for atype in _APPARATUS_TYPES:
        if atype in ot:
            return 1.5
    for etype in _EPHEMERA_TYPES:
        if etype in ot:
            return -1.0
    return 0.0


def _si_score(rec: dict, words: list[str]) -> float:
    """Score a Smithsonian index record against search words."""
    toks = set(rec.get("tokens", []))
    title_words = set(
        w.lower() for w in re.split(r"[^a-zA-Z]+", rec.get("title", "")) if w
    )
    s = 0.0
    for w in words:
        if w in title_words:
            s += 4.0   # title match weights more
        elif w in toks:
            s += 2.0
        elif any(t.startswith(w) or w.startswith(t) for t in toks if len(t) > 3 and len(w) > 3):
            s += 0.5
    s += _si_object_type_bonus(rec)
    return s


def _search_smithsonian(words: list[str], top: int) -> list[dict]:
    """Search the SI index. Returns [] if index doesn't exist yet."""
    if not SI_INDEX.exists():
        return []
    hits: list[tuple[float, dict]] = []
    with SI_INDEX.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            s = _si_score(rec, words)
            if s > 0:
                hits.append((s, rec))
    hits.sort(key=lambda t: t[0], reverse=True)
    return [r for _, r in hits[:top]]


def _search_adapter(adapter_id: str, query: str, top: int) -> list[dict]:
    """Search a single archival adapter. Returns [] on failure."""
    try:
        import importlib
        mod = importlib.import_module(f"sources.{adapter_id}")
        return mod.search(query, top=top)
    except Exception as exc:
        print(f"[pantry-search] {adapter_id} error: {exc}")
        return []


def _print_archival_hits(hits: list[dict], source_label: str,
                         fetch_source: str, reel_hint: str = "",
                         beat_hint: str = "") -> None:
    """Print archival hits with fetch command."""
    print(f"\n[pantry-search] {source_label}: {len(hits)} candidate(s)")
    for h in hits:
        ot = f"  [{h.get('object_type','')}]" if h.get("object_type") else ""
        date = f"  {h['date']}" if h.get("date") else ""
        print(f"  [{h.get('adapter', fetch_source)}]  "
              f"{h['id']:<35} {h.get('unit',''):<8}  "
              f"{h.get('title','')[:50]}{ot}{date}")
        print(f"        Credit: {h.get('credit','')[:65]}")
        if h.get("thumbnail_url"):
            print(f"        Thumbnail: {h['thumbnail_url']}")
    lic = hits[0].get("license", "?") if hits else "?"
    print()
    print(f"  LOOK at the thumbnail before accepting — register fit matters.")
    print(f"  License: {lic}  ·  Sidecar is the provenance record.")
    print()
    print("  To fetch + Topaz-upscale + shelve + drop into pantry:")
    copy_arg = f" --copy {reel_hint}" if reel_hint else ""
    beat_arg = f" --beat {beat_hint}" if beat_hint else ""
    print(f"    python3 runtime/scripts/image_fetch.py \\")
    print(f"        --source {fetch_source} --id <ID>{copy_arg}{beat_arg}")
    print()
    print("  To fetch without pantry copy:")
    print(f"    python3 runtime/scripts/image_fetch.py \\")
    print(f"        --source {fetch_source} --id <ID>")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("terms", help="search terms (may be empty when using --pick)")
    ap.add_argument("--library", type=Path, default=None)
    ap.add_argument("--kind", choices=["svg", "png"], default=None,
                    help="filter local results (png = images/ stills + png fallback lib)")
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--source",
                    choices=_ALL_SOURCES,
                    default="all",
                    help="which libraries to search (default: all)")
    ap.add_argument("--copy", type=Path, default=None, metavar="REEL",
                    help="reel folder — copy a LOCAL match into REEL/pantry/")
    ap.add_argument("--beat", default=None, metavar="BID",
                    help="beat id for the pantry filename prefix (required with --copy)")
    ap.add_argument("--pick", default=None, metavar="ID",
                    help="copy this exact LOCAL icon id instead of the top-ranked hit")
    a = ap.parse_args()

    words = term_words(a.terms)

    # ── Local library search ──────────────────────────────────────────────────
    local_hits: list[dict] = []
    if a.source in ("all", "local"):
        lib = (a.library or _find_library()).resolve()
        manifest = lib / "icons.json"
        if not manifest.exists():
            if a.source == "local":
                sys.exit(f"[pantry-search] no manifest at {manifest} — run "
                         "`python3 skills/make/doodle/scripts/build_index.py` first")
            # In "all" mode, silently skip local if no manifest
        else:
            icons = json.loads(manifest.read_text())["icons"]
            if a.kind:
                icons = [i for i in icons if i.get("kind", "svg") == a.kind]
            if words:
                ranked = sorted(icons, key=lambda i: score(i, words)[1], reverse=True)
                local_hits = [i for i in ranked if score(i, words)[0] >= 1][: a.top]

    # ── Archival source search ────────────────────────────────────────────────
    # Map adapter_id -> list[dict]
    archival_hits: dict[str, list[dict]] = {}
    if words:
        sources_to_search = (
            _ARCHIVE_SOURCES if a.source == "all"
            else ([a.source] if a.source in _ARCHIVE_SOURCES else [])
        )
        for src_id in sources_to_search:
            if src_id == "smithsonian":
                hits = _search_smithsonian(words, a.top)
                # annotate with adapter field for unified printing
                for h in hits:
                    h.setdefault("adapter", "smithsonian")
                    h.setdefault("source_label", "Smithsonian Open Access (CC0)")
                archival_hits["smithsonian"] = hits
            else:
                hits = _search_adapter(src_id, a.terms, a.top)
                archival_hits[src_id] = hits

    all_archival = [h for hits in archival_hits.values() for h in hits]

    # ── Print results ─────────────────────────────────────────────────────────
    any_results = bool(local_hits or all_archival or a.pick)

    if words:
        # Local
        if a.source in ("all", "local"):
            if local_hits:
                print(f"[pantry-search] Local library: {len(local_hits)} candidate(s)")
                for i in local_hits:
                    print(f"  [local]  {i['id']:<40} {i.get('kind','svg'):<4} {i['file']}")
                print("  LOOK at the file before copying — a token match is a lead, not a verdict.")
            else:
                print(f"[pantry-search] Local library: no match for '{a.terms}'")

        # Archival sources
        reel_str = str(a.copy) if a.copy else ""
        for src_id, hits in archival_hits.items():
            label_map = {
                "smithsonian": "Smithsonian Open Access (CC0)",
                "nasa":        "NASA Image & Video Library (public domain)",
                "wellcome":    "Wellcome Collection (mixed open license)",
                "nlm_ihm":     "NLM Digital Collections (public domain)",
            }
            label = label_map.get(src_id, src_id)
            if hits:
                _print_archival_hits(hits, label, src_id,
                                     reel_hint=reel_str, beat_hint=a.beat or "")
            elif src_id == "smithsonian":
                if SI_INDEX.exists():
                    print(f"\n[pantry-search] Smithsonian index: no match for '{a.terms}' "
                          f"({SI_INDEX.stat().st_size // 1024} KB index)")
                else:
                    print("\n[pantry-search] Smithsonian index not built yet.")
                    print("  Build: python3 runtime/scripts/smithsonian_index.py --api-key KEY")
                    print("  (or --s3; key is free at https://api.data.gov/signup/)")
            else:
                print(f"\n[pantry-search] {label}: no match for '{a.terms}'")

    if a.copy is None:
        return 0 if any_results else 1

    # ── --copy: local assets only ─────────────────────────────────────────────
    if not a.beat:
        sys.exit("[pantry-search] --copy requires --beat BID")

    # Reload icons for copy path (need lib reference)
    lib = (a.library or _find_library()).resolve()
    manifest = lib / "icons.json"
    if not manifest.exists():
        sys.exit(f"[pantry-search] no manifest at {manifest} — run "
                 "`python3 skills/make/doodle/scripts/build_index.py` first")
    icons = json.loads(manifest.read_text())["icons"]

    chosen = None
    if a.pick:
        chosen = next((i for i in icons if i["id"] == a.pick), None)
        if chosen is None:
            sys.exit(f"[pantry-search] no icon id '{a.pick}' in manifest")
    elif local_hits:
        chosen = local_hits[0]
    elif all_archival:
        # Remind the user to use image_fetch instead
        h = all_archival[0]
        src_id = h.get("adapter", "smithsonian")
        print(f"\n[pantry-search] Top result is an archival hit — use image_fetch:")
        print(f"  python3 runtime/scripts/image_fetch.py \\")
        print(f"      --source {src_id} --id {h['id']} --copy {a.copy} --beat {a.beat}")
        return 0
    else:
        sys.exit("[pantry-search] nothing to copy (no local hits; use --pick ID or "
                 "smithsonian_fetch for SI hits)")

    src = (lib / chosen["file"]).resolve()
    if src.suffix.lower() != ".png":
        sys.exit(f"[pantry-search] {chosen['id']} is {src.suffix} — pantry copies "
                 "PNGs only; SVG icons go through doodle_fill, not the pantry.")
    pantry = a.copy / "pantry"
    pantry.mkdir(parents=True, exist_ok=True)
    dst = pantry / f"{a.beat}-{chosen['id']}.png"
    shutil.copy2(src, dst)
    print(f"[pantry-search] {chosen['id']} -> {dst}")
    print("  next: LOOK at it; if it holds, run the pantry intake "
          "(runtime/scripts/pantry.py <reel>). If not, delete it and write the card.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
