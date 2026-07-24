#!/usr/bin/env python3
"""
build_index.py — index the organized-svg doodle library into icons.json
=======================================================================
Walks svg/organized-svg/<category>/*.svg and writes svg/organized-svg/icons.json:
one entry per icon with its id, category, relative path, and search tokens
derived from the filename (category prefix + words, numbers stripped).

Deterministic and idempotent: same library in, same manifest out (entries
sorted by id). Run it after adding/renaming icons; doodle_fill.py refuses to
run without a manifest newer than the newest SVG unless --stale-ok.

Usage:
    python3 skills/make/doodle/scripts/build_index.py            # from brutalist-art/
    python3 skills/make/doodle/scripts/build_index.py --library svg/organized-svg
"""
from __future__ import annotations

import argparse
import json
import re
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

# Filename words too generic to be search signal.
STOP = {"word", "sign", "icon", "outline", "symbol"}


def tokens_for(category: str, stem: str) -> list[str]:
    """medical-heart-01 -> ['medical', 'heart']  (category kept as a token)."""
    words = [w for w in re.split(r"[-_]+", stem) if w]
    out: list[str] = []
    for w in words:
        w = w.lower()
        if w.isdigit() or w in STOP:
            continue
        out.append(w)
    # de-dup, preserve order
    seen: set[str] = set()
    return [w for w in out if not (w in seen or seen.add(w))]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--library", type=Path, default=DEFAULT_LIBRARY)
    a = ap.parse_args()
    lib = a.library.resolve()
    if not lib.is_dir():
        print(f"[index] library not found: {lib}", file=sys.stderr)
        return 2

    entries = []
    for svg in sorted(lib.glob("*/*.svg")):
        category = svg.parent.name
        stem = svg.stem
        entries.append(
            {
                "id": stem,
                "kind": "svg",
                "category": category,
                "file": f"{category}/{svg.name}",
                "tokens": tokens_for(category, stem),
                "bytes": svg.stat().st_size,
            }
        )

    # Tier-2 PNG fallback library: doodles/png/ (flat or categorized).
    png_lib = lib.parent / "png"
    if png_lib.is_dir():
        for png in sorted(png_lib.rglob("*.png")):
            rel = png.relative_to(png_lib)
            category = rel.parts[0] if len(rel.parts) > 1 else "png"
            entries.append(
                {
                    "id": png.stem,
                    "kind": "png",
                    "category": category,
                    "file": f"../png/{rel}",
                    "tokens": tokens_for(category if category != "png" else "", png.stem),
                    "bytes": png.stat().st_size,
                }
            )

    # Still library: <lib>/images/ — generated PNG stills. Doodle treats
    # these as tier-2 (pasted-in) candidates; the vox/explainer pantry
    # searches them via runtime/scripts/pantry_search.py before writing a
    # SHOPPING/SHOTLIST request card.
    img_lib = lib / "images"
    if img_lib.is_dir():
        for png in sorted(img_lib.glob("*.png")):
            entries.append(
                {
                    "id": png.stem,
                    "kind": "png",
                    "category": "images",
                    "file": f"images/{png.name}",
                    "tokens": tokens_for("", png.stem),
                    "bytes": png.stat().st_size,
                }
            )

    out = lib / "icons.json"
    out.write_text(
        json.dumps(
            {"library": str(lib.name), "count": len(entries), "icons": entries},
            indent=1,
        )
    )
    cats: dict[str, int] = {}
    for e in entries:
        cats[e["category"]] = cats.get(e["category"], 0) + 1
    print(f"[index] {len(entries)} icons -> {out}")
    for c in sorted(cats):
        print(f"  {c:14} {cats[c]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
