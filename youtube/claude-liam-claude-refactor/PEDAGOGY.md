# PEDAGOGY — claude-liam-claude-refactor
# "Claude, Retrofitted." | claude-refactor skill teardown

## Learning goal
Viewer leaves knowing: (1) claude-refactor adds only new beats — cold open, ASK→RESULT micro-beats, handoff, outro — and never re-renders inner media; (2) the ASK→RESULT law applied retroactively makes the prompts visible without touching the original footage; (3) GATE P + per-video human approval are hard stops between audit and spend.

## Prediction beat
B03 poses: you ask Claude to retrofit 30 videos to the Claude brand. What prevents it from accidentally re-rendering inner beats and overwriting paid Higgsfield and Manim footage? Viewer predicts before B04/B05 reveal: the skill's hard rule — "reuse before you regenerate: an existing inner beat's media is never re-rendered unless the human asks."

## Concrete before abstract
B04 shows the real scope scan — 59 books × 6393 reels with beat sheets across all non-brutalist youtube/ dirs — before B05/B06/B07 state the abstract reuse / ASK→RESULT / gate laws.

## Self-demo check
B04 is genuinely free: runs `find . -path "*/youtube/*/beat_sheet.json"` against the books root — pure filesystem read, no writes, no audio spend, no network.

## ILLUSTRATE LAW
- UI beats (5): B00, B03, BVDT, BHTF, BOUT
- Illustration beats (6): B01, B02, B04, B05, B06, B07

## VERDICT: PASS
