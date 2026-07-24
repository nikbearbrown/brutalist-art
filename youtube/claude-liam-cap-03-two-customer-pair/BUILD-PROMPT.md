# BUILD-PROMPT — claude-liam-cap-03-two-customer-pair
# "Recipe for AI, Card for Human." | Reallocation Engine Capstone · E3 of 8
# Built: 2026-07-19 | Kokoro am_onyx | 373.4s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-cap-03-two-customer-pair
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-cap-03-two-customer-pair
python3 runtime/scripts/compile.py youtube/claude-liam-cap-03-two-customer-pair --height 1080
open youtube/claude-liam-cap-03-two-customer-pair/claude-liam-cap-03-two-customer-pair.mp4
```

## Key decisions
- **Greeting**: Ciao (Italian) — E3 of 8.
- **Title**: "Recipe for AI, Card for Human." — the two-customer pair structure is the deliverable; writing the same contribution twice for two different readers is the skill.
- **Prediction gate (B03)**: asks which human card section gets skipped most often — directly targets failure modes, revealed in B06. Genuine germane friction.
- **Self-demo**: `sed -n '105,109p'` on assignment file — shows all nine recipe sections and card fields in 5 lines. Real, free, no generation.
- **Three verbatim quotes across B05–B07**: shared contract doctrine (Ch 4), failure modes as skipped section (Ch 4), future-you as reader (Ch 4). All three from same chapter, which is the authoritative source for the two-customer pair.
- **B08 (THE_PICK)**: same-commit enforcement doctrine — the naming of "human doc not updated when recipe changes" as a failure mode is itself the enforcement mechanism. No verbatim quote (quote: "", cite: "").
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat extreme slow-mo (known pattern, non-blocking).
