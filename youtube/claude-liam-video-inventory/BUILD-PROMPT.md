# BUILD-PROMPT — claude-liam-video-inventory
# "Claude, Audited." | video-inventory skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 182.6s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-video-inventory
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-video-inventory
python3 runtime/scripts/compile.py youtube/claude-liam-video-inventory --height 1080
open youtube/claude-liam-video-inventory/claude-liam-video-inventory.mp4
```

## Key decisions
- **Self-demo**: Live `inventory.py` audit — reads every youtube/ dir across 49 books (2762 reels), checks file presence, writes YOUTUBE.MD. Genuinely free: pure filesystem read, ~1s, $0.00. No LLM call, no network, no context window.
- **Greeting**: Yassou (Greek) — unique in this batch run for video 40.
- **Title**: "Claude, Audited." — the deterministic + pure-function + idempotent triad is the artifact; the "script not LLM" distinction is the insight.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 2.42× slow-mo — known, non-blocking.
- **Prop schemas**: All beats used correct zod schema field names throughout (no re-render needed). Reference saved in memory/feedback_remotion_prop_names.md.
