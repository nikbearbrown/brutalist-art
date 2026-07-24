#!/usr/bin/env python3
"""inventory.py — audit every book's youtube/ reels and write YOUTUBE.MD.

Deterministic and idempotent: it is a pure function of what's on disk. If Claude
Code hits a limit / restarts, just re-run it — it always regenerates the full,
current report; there is no partial state to resume.

State per reel (by file presence, aspect by ffprobe):
  planned    beat_sheet.json exists, no review cut yet
  slate-cut  <slug>-slate.mp4 exists (preview with slates)
  16:9       a landscape final cut exists in mp4/ (master; slates filled)
  9:16       a portrait final cut exists in mp4/ (the short)
  complete   both 16:9 and 9:16 present
  [BLOCKED]  a layout_audit.md is present (a gate failed)

Usage:
  python3 scripts/inventory.py [BOOKS_ROOT] [--out PATH]
  (defaults: BOOKS_ROOT = the books/ dir above the toolkit, out = YOUTUBE.MD)
"""
import argparse, json, shutil, subprocess, sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]        # runtime/
FFPROBE = shutil.which("ffprobe")


def probe_wh(path):
    if not FFPROBE:
        return None, None
    r = subprocess.run([FFPROBE, "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "stream=width,height", "-of", "csv=p=0",
                        str(path)], capture_output=True, text=True)
    try:
        w, h = r.stdout.strip().splitlines()[0].split(",")[:2]
        return int(w), int(h)
    except Exception:
        return None, None


def classify_cut(path):
    """Return '16:9', '9:16', or None for a final-cut mp4."""
    w, h = probe_wh(path)
    if w and h:
        return "16:9" if w >= h else "9:16"
    n = path.name.lower()                          # ffprobe-less fallback
    if any(k in n for k in ("short", "916", "9x16", "vert", "portrait")):
        return "9:16"
    return "16:9"


def analyze_reel(reel: Path):
    slug = reel.name
    try:
        sheet = json.loads((reel / "beat_sheet.json").read_text())
    except Exception:
        sheet = {"beats": []}
    beats = sheet.get("beats", [])
    dur = sum(float(b.get("actual_duration_s") or 0) for b in beats)

    review = bool(list(reel.glob("*-slate.mp4"))) or \
        (reel / "mp4").is_dir() and bool(list((reel / "mp4").glob("*-slate.mp4")))

    cuts = []
    mp4dir = reel / "mp4"
    if mp4dir.is_dir():
        cuts += [f for f in mp4dir.glob("*.mp4") if "slate" not in f.name.lower()]
    _final = reel / f"{slug}.mp4"
    if _final.exists():
        cuts.append(_final)
    kinds = {classify_cut(f) for f in cuts}
    has169, has916 = "16:9" in kinds, "9:16" in kinds

    open_slates = 0
    for b in beats:
        bid = b.get("beat_id", "")
        filled = any((reel / rel).exists() for rel in (
            f"media/{bid}.mp4", f"manim/{bid}.mp4", f"manim/{bid}.mov",
            f"media/{bid}.png", f"media/{bid}.jpg"))
        if not filled:
            open_slates += 1

    blocked = (reel / "layout_audit.md").exists()
    if has169 and has916:
        state = "complete"
    elif has169:
        state = "16:9 only"
    elif review:
        state = "slate-cut"
    else:
        state = "planned"
    return {"slug": slug, "beats": len(beats), "dur": dur, "review": review,
            "has169": has169, "has916": has916, "open_slates": open_slates,
            "blocked": blocked, "state": state}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("books_root", nargs="?", type=Path, default=HERE.parent)
    ap.add_argument("--out", type=Path, default=HERE / "YOUTUBE.MD")
    a = ap.parse_args()
    root = a.books_root.resolve()

    books, empty = {}, []
    for book_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        yt = book_dir / "youtube"
        if not yt.is_dir():
            continue
        reels = sorted(d for d in yt.iterdir()
                       if d.is_dir() and (d / "beat_sheet.json").exists())
        if not reels:
            empty.append(book_dir.name)
            continue
        books[book_dir.name] = [analyze_reel(r) for r in reels]

    all_reels = [r for rs in books.values() for r in rs]
    n = len(all_reels)
    def cnt(pred): return sum(1 for r in all_reels if pred(r))
    tot = {
        "books": len(books), "reels": n,
        "complete": cnt(lambda r: r["has169"] and r["has916"]),
        "m169": cnt(lambda r: r["has169"]),
        "m916": cnt(lambda r: r["has916"]),
        "slate": cnt(lambda r: r["review"] and not r["has169"]),
        "planned": cnt(lambda r: not r["review"]),
        "blocked": cnt(lambda r: r["blocked"]),
    }

    L = []
    L.append("# YOUTUBE.MD — video state across all books")
    L.append("")
    L.append(f"_Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} by "
             f"`scripts/inventory.py` — deterministic, re-run anytime._")
    L.append("")
    L.append("## Summary")
    L.append("")
    L.append(f"- **{tot['reels']}** built reels across **{tot['books']}** books "
             f"(+{len(empty)} books with an empty `youtube/`)")
    L.append(f"- **{tot['complete']}** complete (16:9 **and** 9:16) · "
             f"**{tot['m169']}** have a 16:9 master · **{tot['m916']}** have a 9:16 short")
    L.append(f"- **{tot['slate']}** slate-cut only (review done, not finalized) · "
             f"**{tot['planned']}** planned (no review yet) · "
             f"**{tot['blocked']}** blocked")
    L.append("")

    attn = [(b, r) for b, rs in books.items() for r in rs
            if r["blocked"] or (r["review"] and not r["has169"])]
    if attn:
        L.append("## Needs attention")
        L.append("")
        L.append("| Book | Reel | State | Open slates | Note |")
        L.append("|---|---|---|--:|---|")
        for b, r in attn:
            note = "BLOCKED — see layout_audit.md" if r["blocked"] else \
                   ("finalize: fill slates + final cut" if r["open_slates"]
                    else "finalize: run `final cut`")
            L.append(f"| {b} | {r['slug']} | {r['state']} | {r['open_slates']} | {note} |")
        L.append("")

    L.append("## Full inventory")
    L.append("")
    L.append("| Book | Reel | Beats | Dur (s) | Review | 16:9 | 9:16 | Slates | State |")
    L.append("|---|---|--:|--:|:-:|:-:|:-:|--:|---|")
    y = "✓"
    for b in sorted(books):
        for r in books[b]:
            L.append(f"| {b} | {r['slug']} | {r['beats']} | {r['dur']:.0f} | "
                     f"{y if r['review'] else ''} | {y if r['has169'] else ''} | "
                     f"{y if r['has916'] else ''} | {r['open_slates']} | "
                     f"{r['state']}{' [BLOCKED]' if r['blocked'] else ''} |")
    L.append("")
    if empty:
        L.append(f"## Books with an empty `youtube/` ({len(empty)})")
        L.append("")
        L.append("_Scaffolded, no reels built yet._")
        L.append("")
        L.append(", ".join(f"`{e}`" for e in sorted(empty)))
        L.append("")

    a.out.write_text("\n".join(L))
    print(f"[audit] {tot['reels']} reels / {tot['books']} books -> {a.out}")
    print(f"[audit] complete:{tot['complete']} 16:9:{tot['m169']} "
          f"9:16:{tot['m916']} slate-only:{tot['slate']} blocked:{tot['blocked']}")


if __name__ == "__main__":
    main()
