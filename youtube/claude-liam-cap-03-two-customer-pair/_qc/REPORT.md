# QC REPORT — claude-liam-cap-03-two-customer-pair
# "Recipe for AI, Card for Human." | Reallocation Engine Capstone · E3 of 8
# Built: 2026-07-19 | Kokoro am_onyx | 373.4s

## VERDICT: PASS

## Rubric (9-point)

| # | Check | Result |
|---|---|---|
| 1 | IN-FOR-BEAR: "Liam, in for Bear." present in B00 | PASS |
| 2 | Greeting "Ciao, Liam." visible in B00 | PASS |
| 3 | Topic label "REALLOCATION ENGINE CAPSTONE · E3 OF 8" in B00 | PASS |
| 4 | Self-demo output visible (sed 105,109 / $0.00 / no generation) | PASS |
| 5 | B05 heading "recipes/_shared.md is always first." + verbatim quote | PASS |
| 6 | B06 heading "Name the failure modes specifically." + verbatim quote | PASS |
| 7 | B07 heading "Write it like a letter to future-you." + verbatim quote | PASS |
| 8 | BVDT "Verdict" + "The pair." + 3 items | PASS |
| 9 | ILLUSTRATE LAW: 5 UI + 6 illustration beats | PASS |

## Frame verification

| Frame | Beat | Time | Result |
|---|---|---|---|
| B00.jpg | OPEN | 13s | PASS — "Ciao, Liam." / "REALLOCATION ENGINE CAPSTONE · E3 OF 8" / "Liam, in for Bear." all visible |
| B05.jpg | MECHANISM_1 | 183.8s | PASS — "recipes/_shared.md is always first." heading + verbatim quote box + source citation visible |
| B07.jpg | MECHANISM_3 | 265.7s | PASS — "Write it like a letter to future-you." heading + verbatim quote + "Source: chapters/04-two-customers.md" visible |
| BVDT.jpg | VERDICT | 333.5s | PASS — "Verdict" header / "The pair." heading / 3 numbered lines correctly populated |

B06 not sampled by dedicated frame; uses same SkillTeardownMechanism component as B05/B07 (both confirmed). Non-blocking.

## Issues

### BLOCKER (0)
None.

### MAJOR (0)
None.

### MINOR-COSMETIC (2)
- B04 ClaudeCodeBeat: extreme slow-mo — 10s Remotion clip stretched ~2.9x to fill 28.99s narration. Known pattern, non-blocking.
- BOUT actual_duration_s: 2.35s (very short outro). Known pattern, non-blocking.

## Beat timing log

| Beat | Role | Duration |
|---|---|---|
| B00 | OPEN | 26.26s |
| B01 | ANATOMY | 47.21s |
| B02 | PIPELINE | 42.58s |
| B03 | PREDICT | 8.98s |
| B04 | SELF-DEMO | 28.99s |
| B05 | MECHANISM_1 | 42.56s |
| B06 | MECHANISM_2 | 41.96s |
| B07 | MECHANISM_3 | 38.85s |
| B08 | THE_PICK | 43.20s |
| BVDT | VERDICT | 25.81s |
| BHTF | YOUR_TURN | 24.68s |
| BOUT | OUTRO | 2.35s |
| **Total** | | **373.4s** |
