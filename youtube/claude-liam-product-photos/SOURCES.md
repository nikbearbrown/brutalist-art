# SOURCES — claude-liam-product-photos
# "Claude, Photographed." | product-photos skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "Never write the gpt_image_2 prompt yourself — backend assembles it."
- Source: skills/assets/product-photos/SKILL.md — UX Rules section, Rule 5
- Role: the backend-owns-prompt law — bypassing product-photoshoot bypasses the prompt enhancer; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "Pick by intent, not surface keyword."
- Source: skills/assets/product-photos/SKILL.md — Mode selection section
- Role: the mode-by-intent law — platform wins over scene, format wins over content; tie-breakers in SKILL.md; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "Skip questions whose answer is obvious from context (uploaded image, prior turn, brand memory)."
- Source: skills/assets/product-photos/SKILL.md — Pre-generation interview section
- Role: the interview-short law — 3-4 labeled questions; skip what's obvious from upload or prior context; stated once, in B07

## Self-demo source
- Phase: help output + mode routing examples — `higgsfield product-photoshoot --help`
- Reference: SKILL.md — Bootstrap step 1 (confirm CLI present) + Mode selection section (tie-breaker examples)
- Output: B04 ClaudeCodeBeat showing command confirmed live + routing examples: kitchen counter → lifestyle_scene; Pinterest pin → moodboard_pin; hero banner → hero_banner
- Not faked: help command run against live Higgsfield CLI at build time; mode routing examples reproduced verbatim from SKILL.md tie-breaker section
