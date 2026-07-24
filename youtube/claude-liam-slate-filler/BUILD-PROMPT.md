# BUILD-PROMPT — claude-liam-slate-filler
# "Claude, Slated." | slate-filler skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 206.4s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-slate-filler
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-slate-filler
python3 runtime/scripts/compile.py youtube/claude-liam-slate-filler --height 1080
open youtube/claude-liam-slate-filler/claude-liam-slate-filler.mp4
```

## Key decisions
- **Self-demo**: consumers.json blast-radius check for SkillTeardownMechanism — free, no render. Shows: 111 consumers, 473 patterns, 6012 refs, 1073 videos in bench. Demonstrates the triage decision: pattern issue vs instance issue.
- **Greeting**: Namaste (Hindi) — unique in this batch run for video 38.
- **Title**: "Claude, Slated." — the template-first selection + two-gate discipline is the artifact; the generalize-at-promotion-time rule is the insight.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 3.14× slow-mo — known, non-blocking.

## Prop schema fix
Initial render used wrong prop names for ClaudeComposerAsk and ClaudeVerdictArtifact. Fixed:
- ClaudeComposerAsk: `topic`, `segment`, `greeting`, `command`, `runningText`, `output` (NOT label/prompt/outputLines)
- ClaudeVerdictArtifact: `artifactTitle`, `artifactHeading`, `artifactLines` (NOT verdict/title/items)
- SkillTeardownAnatomy: `skillName`, `files` array of {indent,icon,name,size,accent,tag} (NOT skill/subtitle/parts)
- SkillTeardownPipeline: `phases` array of {label,desc,accent} (NOT steps)
- ClaudeCodeBeat: `title`, `code`, `sparkLine` (NOT prompt/outputLines/insight)
- ClaudeTitleOutro: `title`, `handle`, `subline` (NOT tagLine)
Resolved with --force re-render after correcting beat_sheet.json.
