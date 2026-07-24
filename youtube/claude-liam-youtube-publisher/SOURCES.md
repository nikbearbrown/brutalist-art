# SOURCES — claude-liam-youtube-publisher
# "Claude, Published." | youtube-publisher skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "Keep the NotebookLM body untouched. The value of this skill is that it doesn't re-encode or re-narrate the deep dive; it only bookends and publishes it."
- Source: skills/upload/youtube-publisher/SKILL.md — Notes on judgment section
- Role: the body-untouched law — B50 skips TTS and Remotion, goes into sandwich as-is; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "a wrong match silently reorders the playlist"
- Source: skills/upload/youtube-publisher/SKILL.md — Step 2 (Match to a chapter — HUMAN GATE)
- Role: the chapter-match gate law — TF-IDF auto-match must be human-confirmed; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "Treat steps 2, 8, and 9 as the places to slow down."
- Source: skills/upload/youtube-publisher/SKILL.md — Notes on judgment section
- Role: the three-human-gates law — chapter match, description rewrite, upload confirm; stated once, in B07

## Self-demo source
- Phase: dry-run from PUBLISH-LOG.md — real output of publish_playlist.py --dry-run
- Reference: SKILL.md — Step 9 (Publish in chapter order) dry-run preview
- Output: B04 ClaudeCodeBeat showing ch1 What is Brutalist?, ch2 Installs, ch3 When Cowork → PLG9H-C6rp5RU, no upload, no quota, $0.00
- Not faked: output reproduced verbatim from youtube/PUBLISH-LOG.md (2026-07-13 session); 5 videos were subsequently actually uploaded to YouTube
