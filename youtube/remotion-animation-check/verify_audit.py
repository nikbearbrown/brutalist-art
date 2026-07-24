#!/usr/bin/env python3
"""verify_audit.py — Post-run verification and log cleanup.

Run after run_audit.py completes to:
1. Deduplicate CHECK-LOG.md
2. Verify all expected decks have deck.html
3. Print a summary
"""
from pathlib import Path
import json

OUT_DIR = Path(__file__).resolve().parent

# 1. Deduplicate log
log = OUT_DIR / "CHECK-LOG.md"
if log.exists():
    lines = log.read_text().splitlines(keepends=True)
    seen = set()
    out = []
    for l in lines:
        k = l.strip()
        if k.startswith("- ") and k in seen:
            continue
        seen.add(k)
        out.append(l)
    log.write_text("".join(out))
    entry_count = sum(1 for l in out if l.strip().startswith("- "))
    print(f"[verify] CHECK-LOG.md: {entry_count} unique entries (deduped from {len(lines)-1} lines)")

# 2. Verify deck folders
deck_dirs = sorted([d for d in OUT_DIR.iterdir() if d.is_dir() and d.name.isdigit()])
print(f"\n[verify] Deck folders found: {len(deck_dirs)}")

ok = 0
missing_html = []
missing_audio = []

for d in deck_dirs:
    has_html  = (d / "deck.html").exists()
    has_bs    = (d / "beat_sheet.json").exists()
    audio_dir = d / "audio"
    audio_cnt = len(list(audio_dir.glob("*.mp3"))) if audio_dir.exists() else 0

    if not has_html:
        missing_html.append(d.name)
    elif audio_cnt < 15:
        missing_audio.append(f"{d.name} ({audio_cnt}/15 audio)")
    else:
        ok += 1

print(f"[verify] Complete (deck.html + 15 audio): {ok}")
if missing_html:
    print(f"[verify] MISSING deck.html:  {', '.join(missing_html)}")
if missing_audio:
    print(f"[verify] LOW AUDIO count: {', '.join(missing_audio)}")

# 3. Total beats covered by logs
total_beats = 0
for l in out:
    if l.strip().startswith("- "):
        import re
        m = re.search(r"(\d+) beats", l)
        if m:
            total_beats += int(m.group(1))

print(f"\n[verify] Total beats accounted for in log: {total_beats}")
print(f"[verify] Expected: 861 (from pre-run count)")

# 4. Report existence
rep = OUT_DIR / "CHECK-REPORT.md"
print(f"\n[verify] CHECK-REPORT.md: {'exists' if rep.exists() else 'MISSING'}")
if rep.exists():
    print(f"         size: {rep.stat().st_size} bytes")

print("\n[verify] DONE")
