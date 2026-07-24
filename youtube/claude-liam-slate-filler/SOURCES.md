# SOURCES — claude-liam-slate-filler
# "Claude, Slated." | slate-filler skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "Keep the media economy honest — do not turn every plate into generic kinetic filler."
- Source: skills/make/slate-filler/SKILL.md — Template-first section
- Role: the anti-filler law — template-first means honest selection, not mechanical fill; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "A scene can pass the machine gate (ships) and fail the human gate (too specific → stays reel-local, never promoted)."
- Source: skills/make/slate-filler/SKILL.md — The two gates section
- Role: the gates distinction law — shipping and promoting are separate decisions; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "Generalize at promotion time, not build time."
- Source: skills/make/slate-filler/SKILL.md — Promotion discipline section
- Role: the promotion discipline law — build specific, generalize only at the gate; stated once, in B07

## Self-demo source
- Phase: consumers.json blast-radius check — free, no Remotion render, no ElevenLabs call
- Reference: SKILL.md — triage section (blast radius, consumers.json reverse index)
- Output: B04 ClaudeCodeBeat showing python3 query of runtime/remotion/_bench/consumers.json — SkillTeardownMechanism: 111 consumers, bench: 473 patterns, total refs: 6012
- Not faked: query runs against the live consumers.json; numbers (111, 473, 6012, 1073) are exact values from the file at build time
