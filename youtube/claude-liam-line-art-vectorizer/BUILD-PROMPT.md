# BUILD-PROMPT — claude-liam-line-art-vectorizer
# "Claude, Vectorized." | line-art-vectorizer skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 193.2s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-line-art-vectorizer
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-line-art-vectorizer
python3 runtime/scripts/compile.py youtube/claude-liam-line-art-vectorizer --height 1080
open youtube/claude-liam-line-art-vectorizer/claude-liam-line-art-vectorizer.mp4
```

## Key decisions
- **Self-demo**: Hand-authored atom SVG from primitives — free, no trace. 3 ellipses + circle, 937B, grouped, animatable. Demonstrates premium path vs 29KB blob from tracing.
- **Greeting**: Hallo (German) — unique in this batch run for video 35.
- **Title**: "Claude, Vectorized." — the gate decision (KEEP/toss) is the artifact; the premium path is the insight.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 2.25× slow-mo — known, non-blocking.
