# SOURCES — claude-liam-listing-cards
# "Claude, Listed." | listing-cards skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "Do not write final image-generation prompts yourself. Backend enhancement owns that."
- Source: skills/assets/listing-cards/SKILL.md — UX Rules section, Rule 4
- Role: the backend-owns-prompts law — Claude routes intent; backend applies private compliance rules and templates; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "Use --scope when the user asks for a common bundle"
- Source: skills/assets/listing-cards/SKILL.md — Scope Selection section
- Role: the scope-first law — pick a pre-built bundle before assembling individual assets; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "Ask at most one concise confirmation question before running."
- Source: skills/assets/listing-cards/SKILL.md — UX Rules section, Rule 2
- Role: the minimal-interaction law — clear product details → run; stated once, in B07

## Self-demo source
- Phase: account status check — `higgsfield account status`
- Reference: SKILL.md — Bootstrap section (confirm auth before generating)
- Output: B04 ClaudeCodeBeat showing bear@bearbrown.co / ultra plan / 1668.23 credits / CLI 0.2.3
- Not faked: command run against live Higgsfield account at build time; no image generated, no credits spent
