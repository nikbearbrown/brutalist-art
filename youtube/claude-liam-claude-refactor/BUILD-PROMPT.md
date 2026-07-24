# BUILD-PROMPT — claude-liam-claude-refactor
# "Claude, Retrofitted." | claude-refactor skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 195.5s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-claude-refactor
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-claude-refactor
python3 runtime/scripts/compile.py youtube/claude-liam-claude-refactor --height 1080
open youtube/claude-liam-claude-refactor/claude-liam-claude-refactor.mp4
```

## Key decisions
- **Self-demo**: Scope scan — `find . -path '*/youtube/*/beat_sheet.json'` across all non-brutalist books. Genuinely free: pure filesystem read, <1s, $0.00. Result: 6393 beat sheets across 59 books.
- **Greeting**: Jambo (Swahili) — unique in this batch run for video 41.
- **Title**: "Claude, Retrofitted." — the reuse-before-regenerate + ASK→RESULT retroactive + Gate P triad is the artifact; the "new beats wrap old ones" insight is the law.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat slow-mo — known, non-blocking.
- **Prop schemas**: All beats used correct zod schema field names throughout (no re-render needed).
