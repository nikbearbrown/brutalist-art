# PEDAGOGY — claude-liam-video-inventory
# "Claude, Audited." | video-inventory skill teardown

## Learning goal
Viewer leaves knowing: (1) video-inventory audits the entire fleet — every reel, every book — in ~1s by reading the filesystem; (2) it is a pure function with no state, no credits, no network; (3) the audit cannot "run out of context" because it's a deterministic script, not an LLM pass.

## Prediction beat
B03 poses: you ask Claude to audit 2762 reels across 49 books. What prevents it from hitting a context limit or rate limit? Viewer predicts before B04/B05 reveal: the audit is a script, not an LLM pass — it runs in one shot, instant, and can be re-run safely anytime.

## Concrete before abstract
B04 shows the actual `inventory.py` output (2762 reels / 49 books, complete:19, 16:9:255, blocked:193) before B05/B06/B07 state the abstract deterministic / pure-function / idempotent laws.

## Self-demo check
B04 is genuinely free: runs `python3 runtime/scripts/inventory.py <books_root>` live — no credits, no network, ~1s. Output is the real current state of the fleet.

## ILLUSTRATE LAW
- UI beats (5): B00, B03, BVDT, BHTF, BOUT
- Illustration beats (6): B01, B02, B04, B05, B06, B07

## VERDICT: PASS
