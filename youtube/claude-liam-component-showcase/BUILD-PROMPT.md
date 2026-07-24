# BUILD-PROMPT — claude-liam-component-showcase
# "Claude, Riffing." | component-showcase skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 175.7s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-component-showcase
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-component-showcase
python3 runtime/scripts/compile.py youtube/claude-liam-component-showcase --height 1080
open youtube/claude-liam-component-showcase/claude-liam-component-showcase.mp4
```

## Key decisions
- **Self-demo**: Fixture + riff script for SkillTeardownMechanism — free, no harness render, no ElevenLabs. Shows quantum tunneling fixture + NBB riff script structure.
- **Greeting**: Hej (Swedish) — unique in this batch run for video 36.
- **Title**: "Claude, Riffing." — the riff script is the artifact; the refusal to promote is the insight.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 2.28× slow-mo — known, non-blocking.
