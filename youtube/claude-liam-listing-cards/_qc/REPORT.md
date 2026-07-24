# QC REPORT — claude-liam-listing-cards
# "Claude, Listed." | listing-cards skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 195.7s

## VERDICT: PASS

## Rubric (9-point)

| # | Check | Result |
|---|---|---|
| 1 | IN-FOR-BEAR: "Liam, in for Bear." present in B00 | PASS |
| 2 | Greeting "Ahoj, Liam." visible in B00 | PASS |
| 3 | Topic label "LISTING-CARDS · SKILL TEARDOWN" in B00 | PASS |
| 4 | Self-demo output visible (bear@bearbrown.co / ultra plan / 1668.23 credits / $0.00) | PASS |
| 5 | SkillTeardownMechanism B05 heading "Backend owns the prompts." | PASS |
| 6 | Verbatim quote B05 exact (Do not write final image-generation prompts yourself. Backend enhancement owns that.) | PASS |
| 7 | BVDT "Verdict" + "The listing." + 3 items | PASS |
| 8 | ILLUSTRATE LAW: 5 UI + 6 illustration beats | PASS |
| 9 | No PIPELINE slates; all 11 beats filled | PASS |

## Issues

### BLOCKER (0)
None.

### MAJOR (0)
None.

### MINOR-COSMETIC (4)
- B04 ClaudeCodeBeat: slow-mo — 10s Remotion clip stretched to 20.76s narration. Known pattern, non-blocking.
- BOUT actual_duration_s: 1.00s (narration very short); clip present.
- B00/B03/BHTF sparkLine fields empty on ClaudeComposerAsk — default blank rendering. Known, non-blocking.
- BHTF center-cut to 14.6s — animation may not fully complete before beat ends.

## Beat timing log

| Beat | Role | Duration |
|---|---|---|
| B00 | OPEN | 16.15s |
| B01 | ANATOMY | 23.81s |
| B02 | PIPELINE | 23.53s |
| B03 | PREDICT | 7.96s |
| B04 | SELF-DEMO | 20.76s |
| B05 | MECHANISM_1 | 22.27s |
| B06 | MECHANISM_2 | 24.79s |
| B07 | MECHANISM_3 | 21.44s |
| BVDT | VERDICT | 19.37s |
| BHTF | YOUR_TURN | 14.63s |
| BOUT | OUTRO | 1.00s |
| **Total** | | **195.71s** |
