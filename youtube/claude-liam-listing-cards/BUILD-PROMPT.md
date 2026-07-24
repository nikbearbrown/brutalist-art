# BUILD-PROMPT — claude-liam-listing-cards
# "Claude, Listed." | listing-cards skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 195.7s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-listing-cards
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-listing-cards
python3 runtime/scripts/compile.py youtube/claude-liam-listing-cards --height 1080
open youtube/claude-liam-listing-cards/claude-liam-listing-cards.mp4
```

## Key decisions
- **Self-demo**: `higgsfield account status` — genuinely free: no image generated, no credits spent, confirms setup is live. Real output: bear@bearbrown.co / ultra plan / 1668.23 credits / CLI 0.2.3.
- **Greeting**: Ahoj (Czech) — unique in this batch run for video 44.
- **Title**: "Claude, Listed." — the backend-owns-prompts + scope-first + minimal-interaction triad is the artifact; "Claude never writes the generation prompt" is the law.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat slow-mo — known, non-blocking.
- **Prop schemas**: All beats used correct zod schema field names throughout (no re-render needed).
