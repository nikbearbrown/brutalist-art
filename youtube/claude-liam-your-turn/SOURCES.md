# SOURCES — claude-liam-your-turn
# "Claude, Handed Off." | your-turn skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "Every claude-explainer reel should end the same way: Liam hands off from the body, recaps on the artifact card, gives the viewer a prompt to run, and re-reads the title."
- Source: skills/make/your-turn/SKILL.md — Closing block structure
- Role: the structural law — three closing beats are mandatory and ordered; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "The prompt must be RELEVANT to the video, so it is drafted per reel, never templated."
- Source: skills/make/your-turn/SKILL.md — YOUR TURN prompt requirement
- Role: the anti-template law — the human drafts the prompt per reel, not a fill-in; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "Audio-first — the handoff, the read prompt, and the title re-read are new Liam lines: regenerate audio, then conform. Never hand-time."
- Source: skills/make/your-turn/SKILL.md — Audio conformance rule
- Role: the audio-first constraint — new beats require new Kokoro audio, not manual timing; stated once, in B07

## Self-demo source
- Phase: dry-run census + drafts.json entry + closing block transform for claude-liam-scout — free, no apply_your_turn.py execution
- Reference: SKILL.md — census phase, drafts.json gate, VERDICT→YOUR TURN→TITLE closing block
- Output: B04 ClaudeCodeBeat showing apply_your_turn.py dry-run output (36 reels scanned, 18 needs_update, 4 needs_prompt) + claude-liam-scout drafts.json entry + 3-beat rewrite preview
- Not faked: census logic matches SKILL.md; drafts.json structure matches SKILL.md gate spec; no ElevenLabs call, no apply executed
