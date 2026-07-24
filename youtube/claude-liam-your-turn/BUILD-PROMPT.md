# BUILD-PROMPT — claude-liam-your-turn
# "Claude, Handed Off." | your-turn skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 174.4s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-your-turn
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-your-turn
python3 runtime/scripts/compile.py youtube/claude-liam-your-turn --height 1080
open youtube/claude-liam-your-turn/claude-liam-your-turn.mp4
```

## Key decisions
- **Self-demo**: Dry-run census + drafts.json entry + closing block transform for claude-liam-scout — free, no apply_your_turn.py execution. Shows the three-beat rewrite preview (VERDICT → YOUR TURN → TITLE).
- **Greeting**: Annyeong (Korean) — unique in this batch run for video 37.
- **Title**: "Claude, Handed Off." — the hand-off structure is the artifact; the per-reel prompt requirement is the insight.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 2.39× slow-mo — known, non-blocking.
