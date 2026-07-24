# BUILD-PROMPT — claude-liam-cap-06-ship-the-pr
# "Fork. Branch. Verify. Ship." | Reallocation Engine Capstone · E6 of 8
# Built: 2026-07-19 | Kokoro am_onyx | 357.4s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-cap-06-ship-the-pr
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-cap-06-ship-the-pr
python3 runtime/scripts/compile.py youtube/claude-liam-cap-06-ship-the-pr --height 1080
open youtube/claude-liam-cap-06-ship-the-pr/claude-liam-cap-06-ship-the-pr.mp4
```

## Key decisions
- **Greeting**: Olá (Portuguese) — E6 of 8.
- **Title**: "Fork. Branch. Verify. Ship." — four imperative verbs = four of the five Step 5 requirements as a structure.
- **Prediction gate (B03)**: asks consequence of PR failing conformance or leaking private data — reveals in B05 that it is not gradeable (hard stop, not a point deduction).
- **Self-demo**: grep for branch naming, not-gradeable, verify+doctor, PR description fields — shows all of Step 5's key requirements in 8 lines. Real, free, no generation.
- **Three verbatim quotes across B05–B07**: not-gradeable condition (assignment Step 5), tight-correct doctrine (assignment criteria), maintainer/hiring-manager standard (assignment preamble). All three from the assignment — the primary source for Step 5 discipline.
- **B08 (THE_PICK)**: limitation field as the proof of professional judgment — harder than listing features, most valuable field in the description. No verbatim quote.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat slow-mo (known pattern, non-blocking).
