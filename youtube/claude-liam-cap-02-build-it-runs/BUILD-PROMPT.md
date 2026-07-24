# BUILD-PROMPT — claude-liam-cap-02-build-it-runs
# "Build It So It Runs." | Reallocation Engine Capstone · E2 of 8
# Built: 2026-07-19 | Kokoro am_onyx | 407.8s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-cap-02-build-it-runs
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-cap-02-build-it-runs
python3 runtime/scripts/compile.py youtube/claude-liam-cap-02-build-it-runs --height 1080
open youtube/claude-liam-cap-02-build-it-runs/claude-liam-cap-02-build-it-runs.mp4
```

## Key decisions
- **Greeting**: Hola (Spanish) — E2 of 8.
- **Title**: "Build It So It Runs." — testable handoff conditions are the artifact; "looks done" is rejected.
- **Gate-as-vote bug as B05 centerpiece**: Ch 16's named build failure is exactly what phase 3 integration must catch; made the prediction question (B03) target it directly.
- **Self-demo**: grep for "handoff\|It works\|two-customer" — shows the 90-pt split directly from the assignment file. Real, free, no generation.
- **Three verbatim quotes across B05–B07**: handoff condition doctrine (Ch 16), builds go wrong (Ch 16), drift structural property (Ch 4).
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat extreme slow-mo (known pattern, non-blocking).
