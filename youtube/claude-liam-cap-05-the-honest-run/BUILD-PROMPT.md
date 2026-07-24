# BUILD-PROMPT — claude-liam-cap-05-the-honest-run
# "The Honest Run." | Reallocation Engine Capstone · E5 of 8
# Built: 2026-07-19 | Kokoro am_onyx | 351.8s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-cap-05-the-honest-run
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-cap-05-the-honest-run
python3 runtime/scripts/compile.py youtube/claude-liam-cap-05-the-honest-run --height 1080
open youtube/claude-liam-cap-05-the-honest-run/claude-liam-cap-05-the-honest-run.mp4
```

## Key decisions
- **Greeting**: Namaste (Hindi) — E5 of 8.
- **Title**: "The Honest Run." — the assignment's framing: not just a run, but an honest one; "running" and "reporting honestly" are different things.
- **Prediction gate (B03)**: asks which of five deliverables is worth more than a clean run. Answer is the break attempt — most surprising to students who assume a clean run is the goal.
- **Self-demo**: `sed -n '128,148p'` on assignment — shows all five Step 4 deliverables with exact requirements including "The break attempt is worth more than a clean run." Real, free, no generation.
- **Three verbatim quotes across B05–B07**: gate-as-vote / fluency hides (Ch 16), skip-rate dial (Ch 15), what the machine could not know (Ch 16). Two from Ch 16, one from Ch 15 — the two chapters that define the honest run.
- **B08 (THE_PICK)**: break attempt is the proof of rigor — not a nice-to-have but the proof that you understand where your own contribution fails. No verbatim quote.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat moderate slow-mo (known pattern, non-blocking).
