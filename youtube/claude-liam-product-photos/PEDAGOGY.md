# PEDAGOGY — claude-liam-product-photos
# "Claude, Photographed." | product-photos skill teardown

## Learning goal
Viewer leaves knowing: (1) product-photos never writes the gpt_image_2 prompt — the backend assembles it from mode-specific templates; (2) mode selection goes by intent, not surface keyword — 10 modes cover studio to surreal; (3) the pre-generation interview is 3-4 labeled questions max, and you skip ones whose answer is obvious from context.

## Prediction beat
B03 poses: you call `higgsfield generate create gpt_image_2 --prompt "..."` directly instead of going through `product-photoshoot create`. Why does the result look noticeably worse? Viewer predicts before B04/B05 reveal: bypassing product-photoshoot bypasses the backend prompt enhancer — the private photography vocabulary and structural templates that make the output brand-quality.

## Concrete before abstract
B04 shows the actual `higgsfield product-photoshoot --help` output (mode/command confirmed live) + concrete mode routing examples before B05/B06/B07 state the abstract backend-owns / mode-by-intent / interview-short laws.

## Self-demo check
B04 is genuinely free: runs `higgsfield product-photoshoot --help` — no image generated, no credits spent. Confirms the command is live. Also shows concrete routing examples from the SKILL.md.

## ILLUSTRATE LAW
- UI beats (5): B00, B03, BVDT, BHTF, BOUT
- Illustration beats (6): B01, B02, B04, B05, B06, B07

## VERDICT: PASS
