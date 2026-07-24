# BUILD-PROMPT — claude-liam-reel-updater
# "Claude, Updated." | reel-updater skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 202.3s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-reel-updater
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-reel-updater
python3 runtime/scripts/compile.py youtube/claude-liam-reel-updater --height 1080
open youtube/claude-liam-reel-updater/claude-liam-reel-updater.mp4
```

## Key decisions
- **Self-demo**: Migration audit scan — glob across all books/*/youtube/* for outro-orig files (83 reels migrated) + beat_sheet drift check (2761 scanned, 0 remaining). Genuinely free: reads files, checks patterns, no side effects.
- **Greeting**: Merhaba (Turkish) — unique in this batch run for video 39.
- **Title**: "Claude, Updated." — the dry-run + credit discipline + idempotency is the artifact; the migrate-only-what-bills law is the insight.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 2.42× slow-mo — known, non-blocking.
