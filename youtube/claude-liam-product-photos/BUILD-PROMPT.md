# BUILD-PROMPT — claude-liam-product-photos
# "Claude, Photographed." | product-photos skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 200.3s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-product-photos
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-product-photos
python3 runtime/scripts/compile.py youtube/claude-liam-product-photos --height 1080
open youtube/claude-liam-product-photos/claude-liam-product-photos.mp4
```

## Key decisions
- **Self-demo**: `higgsfield product-photoshoot --help` + mode routing examples from SKILL.md — genuinely free: no image generated, no credits spent. Confirms CLI is live and shows concrete intent→mode mapping.
- **Greeting**: Shalom (Hebrew) — unique in this batch run for video 45. Final video in the batch.
- **Title**: "Claude, Photographed." — the backend-owns-prompt + mode-by-intent + interview-short triad is the artifact; "use product-photoshoot, never bypass to generate create" is the law.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat slow-mo — known, non-blocking.
- **Prop schemas**: All beats used correct zod schema field names throughout (no re-render needed).
