# SOURCES — claude-liam-claude-refactor
# "Claude, Retrofitted." | claude-refactor skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "an existing inner beat's media is never re-rendered unless the human asks"
- Source: skills/make/claude-refactor/SKILL.md — Hard rules section
- Role: the reuse-before-regenerate law — new beats added, inner footage never overwritten; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "insert a composer micro-beat showing a realistic Claude prompt that could generate that scene"
- Source: skills/make/claude-refactor/SKILL.md — Per-video procedure, step 5
- Role: the ASK→RESULT retroactive law — prompt visible before each generated visual, footage untouched; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "Never posts without per-video human approval."
- Source: skills/make/claude-refactor/SKILL.md — skill description / Hard rules section
- Role: the gate P + per-video approval law — PEDAGOGY.md addendum before spend, explicit approval before post; stated once, in B07

## Self-demo source
- Phase: scope scan — `find . -path '*/youtube/*/beat_sheet.json'` across books root
- Reference: SKILL.md — inventory step (step 2 of what the generator does)
- Output: B04 ClaudeCodeBeat showing 6393 beat sheets across 59 books (excluding brutalist-art, brand-variant dirs, lecture folders)
- Not faked: find command runs against live filesystem; numbers (6393, 59) are exact counts at build time; no files written, no audio generated
