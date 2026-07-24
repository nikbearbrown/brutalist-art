# PEDAGOGY — claude-liam-listing-cards
# "Claude, Listed." | listing-cards skill teardown

## Learning goal
Viewer leaves knowing: (1) listing-cards routes user intent to the Higgsfield CLI — it does not write image generation prompts itself, because the backend enhancer owns that; (2) the --scope flag selects pre-built bundles (main, product-images, aplus, full-set) so you don't have to assemble individual assets; (3) the skill asks at most one confirmation question before running.

## Prediction beat
B03 poses: you pass a short product description to listing-cards. Why doesn't Claude write the actual generation prompts that go to Higgsfield? Viewer predicts before B04/B05 reveal: the backend enhancer owns that — it applies marketplace compliance rules and private templates that Claude should never guess at.

## Concrete before abstract
B04 shows the actual `higgsfield account status` output (ultra plan, ~1668 credits) before B05/B06/B07 state the abstract backend-owned / scope-selection / minimal-interaction laws.

## Self-demo check
B04 is genuinely free: runs `higgsfield account status` — no image generation, no credits spent, confirms setup is live.

## ILLUSTRATE LAW
- UI beats (5): B00, B03, BVDT, BHTF, BOUT
- Illustration beats (6): B01, B02, B04, B05, B06, B07

## VERDICT: PASS
