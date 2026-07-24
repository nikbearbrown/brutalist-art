# BUILD-PROMPT — claude-liam-youtube-publisher
# "Claude, Published." | youtube-publisher skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 196.0s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-youtube-publisher
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-youtube-publisher
python3 runtime/scripts/compile.py youtube/claude-liam-youtube-publisher --height 1080
open youtube/claude-liam-youtube-publisher/claude-liam-youtube-publisher.mp4
```

## Key decisions
- **Self-demo**: Dry-run output from PUBLISH-LOG.md (2026-07-13 real session) — genuinely free: references existing log, no upload, no quota, $0.00. 5 real uploads followed.
- **Greeting**: Privet (Russian) — unique in this batch run for video 43.
- **Title**: "Claude, Published." — the body-untouched + chapter-match-gate + three-human-gates triad is the artifact; "dry-run first" is the discipline.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat slow-mo — known, non-blocking.
- **Prop schemas**: All beats used correct zod schema field names throughout (no re-render needed).
