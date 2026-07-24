# BUILD-PROMPT — claude-liam-session
# "Claude, Directed." | session skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 187.7s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-session
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-session
python3 runtime/scripts/compile.py youtube/claude-liam-session --height 1080
open youtube/claude-liam-session/claude-liam-session.mp4
```

## Key decisions
- **Self-demo**: Read existing STYLE box from session-karaoke-audiogram — genuinely free: pure filesystem read, $0.00. Shows the real output of `./art suno` command, not invented output.
- **Greeting**: Sawubona (Zulu) — unique in this batch run for video 42.
- **Title**: "Claude, Directed." — the direction/breath-rule/delivery-field triad is the artifact; "a stop sign is not a direction" is the insight.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat slow-mo — known, non-blocking.
- **Prop schemas**: All beats used correct zod schema field names throughout (no re-render needed).
