# BUILD-PROMPT — claude-liam-cap-01-pick-and-clear-the-bar
# "Pick and Clear the Bar." | Reallocation Engine Capstone · E1 of 8
# Built: 2026-07-19 | Kokoro am_onyx | 432.0s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-cap-01-pick-and-clear-the-bar
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-cap-01-pick-and-clear-the-bar
python3 runtime/scripts/compile.py youtube/claude-liam-cap-01-pick-and-clear-the-bar --height 1080
open youtube/claude-liam-cap-01-pick-and-clear-the-bar/claude-liam-cap-01-pick-and-clear-the-bar.mp4
```

## Key decisions
- **12-beat structure** (B00–B08 + BVDT + BHTF + BOUT): expanded from 11-beat skill-teardown format to reach ~7 min target; B08 (THE_PICK) added as 4th mechanism beat. ILLUSTRATE LAW satisfied: 5 UI + 6 illustration.
- **Self-demo**: `grep -n "^[0-9]\." assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md` — genuinely free: reads local file, real output, no generation, no credits. Confirmed 7 criteria at lines 76–85.
- **Greeting**: Bonjour (French) — E1 of 8 new greetings for the capstone series.
- **Title**: "Pick and Clear the Bar." — the 7-point bar is the gating artifact; cleared before any code is written.
- **Verbatim quotes**: prime directive (B05), gate-decoration law (B06), zero condition criterion 7 (B07) — all from the assignment file verified on disk.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat extreme slow-mo (10s clip stretched 3.5x to 34.7s). Known pattern, non-blocking.
- **Content grounded on**: local assignment file + chapters 03, 04, 15, 16 in the-reallocation-engine/chapters/. SNICKERDOODLE.md and DATA_CONTRACT.md referenced by name as per the assignment's "engine" paragraph; not present in local repo copy — referenced correctly from what the assignment states.
