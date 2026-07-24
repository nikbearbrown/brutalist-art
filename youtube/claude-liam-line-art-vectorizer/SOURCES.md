# SOURCES — claude-liam-line-art-vectorizer
# "Claude, Vectorized." | line-art-vectorizer skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "A bad vector is worse than none. Simple art comes out clean; complex art is rejected with a reason, not faked."
- Source: skills/assets/line-art-vectorizer/SKILL.md — governing rule
- Role: the core toss-if-bad law — the gate exists to prevent shipping bad vectors; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "Don't expect simplify to manufacture simplicity that was never generated."
- Source: skills/assets/line-art-vectorizer/SKILL.md — Simplify, Honest limit
- Role: the simplify escalation limit — reduces detail but doesn't redraw; fix upstream; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "Never embed a raster inside an `<svg>` — that's a fake vector and the gate fails it."
- Source: skills/assets/line-art-vectorizer/SKILL.md — Output contract
- Role: the audit gate rule — wrapped PNG is not a vector; the Madison cover mistake origin; stated once, in B07

## Self-demo source
- Phase: hand-authored atom SVG from primitives — free, no trace, no vtracer call
- Reference: SKILL.md Premium path section (atom = ellipses + circle; 937B vs ~29KB traced)
- Output: B04 ClaudeCodeBeat showing complete SVG source code for atom icon (3 ellipses + 1 circle, grouped, viewBox present, role="img", <title>)
- Not faked: SVG structure matches SKILL.md premium path description exactly (grouped orbits + nucleus, 937B benchmark cited); no API call, no trace run made
