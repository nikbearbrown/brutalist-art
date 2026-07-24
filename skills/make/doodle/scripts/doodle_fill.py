#!/usr/bin/env python3
"""
doodle_fill.py — resolve a reel's doodle beats into renderable Remotion props
=============================================================================
Reads <reel>/beat_sheet.json. For every beat carrying a `doodle` block, it:

  1. resolves each requested icon (search terms) against the organized-svg
     manifest (icons.json — run build_index.py first),
  2. inlines the matched SVG file text into `shot.remotion.props.items[]`
     (DoodleScene) or passes chart data through (DoodleChart),
  3. sets `shot.remotion.pattern` and copies the beat's measured
     `actual_duration_s` into `props.durationS` (audio-first: audio is the
     master clock — generate audio BEFORE filling),
  4. writes the beat sheet back.

Beats whose icons can't be resolved are SKIPPED, never guessed: the beat is
left untouched (it stays a slate) and a MISSING line is printed naming the
unmatched terms and the closest candidates — add an icon to the library (+
re-run build_index.py) or change the terms, then re-run. This mirrors the
fill-in/request-card philosophy: the machine never forces a match.

After filling, render as usual:
    python3 runtime/scripts/remotion_scenes.py <reel>          # renders media/<BID>.mp4
    ./art run <reel>                                           # compile the cut

The `doodle` block, authored in the beat sheet (see the skill's SKILL.md):

  "doodle": {
    "icons": [ {"terms": "anatomical heart", "label": "the heart",
                "accent": true, "xPct": 50, "yPct": 44, "widthPct": 24,
                "mode": "drawon"} ],
    "caption": "your heart is a pump",
    "eyebrow": "",
    "chart": { "kind": "bar", "title": "...", "unit": "%", "accentIndex": 2,
               "data": [{"label": "A", "value": 12}, ...] }
  }

icons+caption  -> DoodleScene.   chart -> DoodleChart (icons ignored).

Usage:
    python3 skills/make/doodle/scripts/doodle_fill.py <reel> [--list] [--only B04]
                                                       [--library <dir>] [--force]
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ART_HOME = Path(__file__).resolve().parents[4]  # brutalist-art/
# Library lives at doodles/svg (renamed 2026-07 from svg/organized-svg);
# probe candidates so a half-finished rename never strands the scripts.
def _find_library() -> Path:
    for cand in ("doodles/svg", "svg/svg", "svg/organized-svg", "doodles/organized-svg"):
        p = ART_HOME / cand
        if (p / "icons.json").exists() or any(p.glob("*/*.svg")) if p.is_dir() else False:
            return p
    return ART_HOME / "doodles" / "svg"


DEFAULT_LIBRARY = _find_library()

STOP = {
    "the", "a", "an", "of", "to", "and", "with", "in", "on", "at", "as",
    "is", "it", "its", "for", "into", "that", "this", "one", "two",
}

# Search-term word -> extra library tokens worth trying. Keep small and
# obvious; the fix for a bad match is a better term or a new icon, not a
# giant synonym table.
SYNONYMS = {
    "doctor": ["stethoscope", "nurse"],
    "medicine": ["capsule", "pill"],
    "germ": ["bacterium", "virus"],
    "computer": ["laptop"],
    "money": ["dollar", "coin"],
    "idea": ["lightbulb", "bulb"],
    "insect": ["beetle", "bug"],
    "planet": ["saturn", "earth"],
    "star": ["stars", "sparkle"],
}


def load_manifest(library: Path) -> dict:
    manifest = library / "icons.json"
    if not manifest.exists():
        sys.exit(
            f"[doodle] no manifest at {manifest} — run "
            "`python3 skills/make/doodle/scripts/build_index.py` first"
        )
    return json.loads(manifest.read_text())


def term_words(terms: str) -> list[str]:
    words = [w.lower() for w in re.split(r"[^a-zA-Z]+", terms) if w]
    out = [w for w in words if w not in STOP]
    for w in list(out):
        out.extend(SYNONYMS.get(w, []))
    return out


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
    # small tiebreaker: fewer tokens = more specific icon
    return exact, s - 0.01 * len(toks)


def resolve(icons: list[dict], words: list[str]) -> tuple[dict | None, list[dict]]:
    ranked = sorted(icons, key=lambda i: score(i, words)[1], reverse=True)
    best = ranked[0] if ranked else None
    # require at least one EXACT token hit — prefix grazes alone never match
    if best is None or score(best, words)[0] < 1:
        return None, ranked[:3]
    return best, ranked[:3]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("reel", type=Path)
    ap.add_argument("--library", type=Path, default=DEFAULT_LIBRARY)
    ap.add_argument("--list", action="store_true", help="show doodle beats and their state")
    ap.add_argument("--only", help="fill a single beat id")
    ap.add_argument("--force", action="store_true", help="refill beats already carrying a pattern")
    a = ap.parse_args()

    folder = a.reel.resolve()
    sheet_path = folder / "beat_sheet.json"
    if not sheet_path.exists():
        sys.exit(f"[doodle] no beat sheet at {sheet_path}")
    sheet = json.loads(sheet_path.read_text())
    library = a.library.resolve()
    manifest = load_manifest(library)
    lib_icons = manifest["icons"]

    cands = [b for b in sheet.get("beats", []) if b.get("doodle")]
    if a.only:
        cands = [b for b in cands if b.get("beat_id") == a.only]
    if not cands:
        print("[doodle] no beats carry a `doodle` block — nothing to do")
        return 0

    if a.list:
        for b in cands:
            rem = (b.get("shot", {}) or {}).get("remotion") or {}
            state = "filled" if rem.get("pattern", "").startswith("Doodle") else "todo"
            kind = "chart" if (b["doodle"].get("chart")) else f"{len(b['doodle'].get('icons', []))} icon(s)"
            print(f"  {b['beat_id']:5} {state:6} {kind}")
        return 0

    changed = False
    missing: list[str] = []
    shopping: list[tuple[str, str, str]] = []  # (beat_id, terms, closest)
    for b in cands:
        bid = b["beat_id"]
        d = b["doodle"]
        shot = b.setdefault("shot", {"type": "REMOTION"})
        rem = shot.get("remotion") or {}
        if rem.get("pattern") and not a.force:
            print(f"[doodle] {bid}: already filled ({rem['pattern']}) — skip (--force to refill)")
            continue

        duration = b.get("actual_duration_s") or b.get("estimated_duration_s") or 0

        if d.get("chart"):
            chart = dict(d["chart"])
            chart.setdefault("caption", d.get("caption", ""))
            chart["durationS"] = float(duration)
            shot["remotion"] = {"pattern": "DoodleChart", "props": chart,
                                "provenance": "doodle-skill"}
            shot.setdefault("type", "REMOTION")
            print(f"[doodle] {bid}: DoodleChart ({chart['kind']}, {len(chart['data'])} data)")
            changed = True
            continue

        items = []
        unresolved = []
        for spec in d.get("icons", []):
            words = term_words(spec.get("terms", ""))
            # Tier 1: the SVG library. Tier 2: the PNG fallback library.
            svg_icons = [i for i in lib_icons if i.get("kind", "svg") == "svg"]
            png_icons = [i for i in lib_icons if i.get("kind") == "png"]
            best, top3 = resolve(svg_icons, words)
            kind = "svg"
            if best is None and png_icons:
                best, top3 = resolve(png_icons, words)
                kind = "png"
            if best is None:
                near = ", ".join(i["id"] for i in top3) or "none"
                unresolved.append(f"'{spec.get('terms', '')}' (closest: {near})")
                shopping.append((bid, spec.get("terms", ""), near))
                continue
            item = {
                "label": spec.get("label", ""),
                "accent": bool(spec.get("accent", False)),
                "mode": spec.get("mode", "drawon"),
            }
            if kind == "svg":
                item["svg"] = (library / best["file"]).read_text()
            else:
                # copy into the Remotion public/ folder (house precedent: the
                # per-reel mp3 folders live there too) and reference via
                # staticFile. PNGs render pasted-in (popin; drawon is SVG-only).
                src = (library / best["file"]).resolve()
                pub = ART_HOME / "runtime" / "remotion" / "public" / "doodle-png"
                pub.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, pub / src.name)
                item["svg"] = ""
                item["pngSrc"] = f"doodle-png/{src.name}"
                if item["mode"] == "drawon":
                    item["mode"] = "popin"
            for k in ("xPct", "yPct", "widthPct", "delayS"):
                if k in spec:
                    item[k] = spec[k]
            items.append(item)
            print(f"[doodle] {bid}: '{spec.get('terms', '')}' -> {best['id']} ({kind})")

        if unresolved:
            missing.append(f"MISSING: {bid} — unmatched icon(s): " + "; ".join(unresolved))
            continue  # leave the beat a slate; never force a match
        if not items and not (d.get("caption") or d.get("title")):
            missing.append(f"MISSING: {bid} — doodle block has no icons, no chart, no title/caption")
            continue

        # accent law: at most ONE red item per beat (teardown grammar)
        accents = [i for i in items if i["accent"]]
        for extra in accents[1:]:
            extra["accent"] = False
        if len(accents) > 1:
            print(f"[doodle] {bid}: >1 accent requested — kept the first (one-accent law)")

        props = {
            "items": items,
            "title": d.get("title", ""),
            "caption": d.get("caption", ""),
            "eyebrow": d.get("eyebrow", ""),
            "durationS": float(duration),
        }
        if "seed" in d:
            props["seed"] = d["seed"]
        shot["remotion"] = {"pattern": "DoodleScene", "props": props,
                            "provenance": "doodle-skill"}
        shot.setdefault("type", "REMOTION")
        changed = True

    if changed:
        sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
        print(f"[doodle] wrote {sheet_path}")
        print("[doodle] next: python3 runtime/scripts/remotion_scenes.py "
              f"{folder}  (renders media/<BID>.mp4)")
    for line in missing:
        print(line)

    # Tier 3: the shopping list — a request card per unresolved icon, appended
    # to the reel's SHOPPING.md (deduped). The beat stays a slate until the
    # human drops an asset into the library and re-runs index + fill.
    if shopping:
        shop = folder / "SHOPPING.md"
        existing = shop.read_text() if shop.exists() else ""
        cards = []
        for bid, terms, near in shopping:
            key = f"doodle needed for: '{terms}' ({bid})"
            if key in existing:
                continue
            slug = re.sub(r"[^a-z0-9]+", "-", terms.lower()).strip("-") or "asset"
            cards.append(
                f"- [ ] {key}\n"
                f"      preferred: a monochrome doodle SVG -> doodles/svg/<category>/<category>-{slug}-01.svg\n"
                f"      fallback:  a PNG (white/transparent bg) -> doodles/png/{slug}-01.png\n"
                f"      closest existing: {near}\n"
                f"      then: python3 skills/make/doodle/scripts/build_index.py "
                f"&& python3 skills/make/doodle/scripts/doodle_fill.py {folder.name} --only {bid}\n"
            )
        if cards:
            header = "" if existing else "# SHOPPING — assets this reel still needs\n\n"
            shop.write_text(existing + ("\n" if existing else "") + header + "\n".join(cards))
            print(f"[doodle] shopping list updated: {shop} (+{len(cards)} card(s))")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
