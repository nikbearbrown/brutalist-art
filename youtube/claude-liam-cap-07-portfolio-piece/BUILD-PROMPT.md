# BUILD-PROMPT — claude-liam-cap-07-portfolio-piece
# "One Honest Metric." | Reallocation Engine Capstone · E7 of 8
# Built: 2026-07-19 | Kokoro am_onyx | 354.1s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-cap-07-portfolio-piece
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-cap-07-portfolio-piece
python3 runtime/scripts/compile.py youtube/claude-liam-cap-07-portfolio-piece --height 1080
open youtube/claude-liam-cap-07-portfolio-piece/claude-liam-cap-07-portfolio-piece.mp4
```

## Key decisions
- **Greeting**: Annyeong (Korean) — E7 of 8.
- **Title**: "One Honest Metric." — the single most important discipline in Step 6 is the before/after number traced to a script, not claimed.
- **Prediction gate (B03)**: asks which of the six portfolio elements is "the strongest thing on the page" — counterintuitive reveal in B06 that it is the failure modes + limitation section, not the demo or the metric.
- **Self-demo**: grep for honest metric/strongest thing/outlives in the assignment file — shows all three Step 6 quality signals in one command. Real, free, no generation.
- **Three verbatim quotes across B05–B07**: all from assignment Step 6 — honest-metric doctrine, naming-limitation-as-strength, portfolio-outlives-course framing. Source is primary (the graded document).
- **B08 (THE_PICK)**: calibrated verbs doctrine — "improved" requires evidence, "appears to improve" is an inference signal. The language choice is auditable; the portfolio is not vague.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat slow-mo (known pattern, non-blocking).
