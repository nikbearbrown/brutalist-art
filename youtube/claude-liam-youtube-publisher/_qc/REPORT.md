# QC REPORT — claude-liam-youtube-publisher
# "Claude, Published." | youtube-publisher skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 196.0s

## VERDICT: PASS

## Rubric (9-point)

| # | Check | Result |
|---|---|---|
| 1 | IN-FOR-BEAR: "Liam, in for Bear." present in B00 | PASS |
| 2 | Greeting "Privet, Liam." visible in B00 | PASS |
| 3 | Topic label "YOUTUBE-PUBLISHER · SKILL TEARDOWN" in B00 | PASS |
| 4 | Self-demo output visible (ch1/ch2/ch3 order / dry-run / $0.00) | PASS |
| 5 | SkillTeardownMechanism B05 heading "Body untouched." | PASS |
| 6 | Verbatim quote B05 exact (Keep the NotebookLM body untouched...) | PASS |
| 7 | BVDT "Verdict" + "The episode." + 3 items | PASS |
| 8 | ILLUSTRATE LAW: 5 UI + 6 illustration beats | PASS |
| 9 | No PIPELINE slates; all 11 beats filled | PASS |

## Issues

### BLOCKER (0)
None.

### MAJOR (0)
None.

### MINOR-COSMETIC (4)
- B04 ClaudeCodeBeat: slow-mo — 10s Remotion clip stretched to 21.25s narration. Known pattern, non-blocking.
- BOUT actual_duration_s: 1.13s (narration very short); clip present.
- B00/B03/BHTF sparkLine fields empty on ClaudeComposerAsk — default blank rendering. Known, non-blocking.
- BHTF center-cut to 13.4s — animation may not fully complete before beat ends.

## Beat timing log

| Beat | Role | Duration |
|---|---|---|
| B00 | OPEN | 16.13s |
| B01 | ANATOMY | 24.09s |
| B02 | PIPELINE | 26.30s |
| B03 | PREDICT | 9.24s |
| B04 | SELF-DEMO | 21.25s |
| B05 | MECHANISM_1 | 22.59s |
| B06 | MECHANISM_2 | 21.99s |
| B07 | MECHANISM_3 | 22.42s |
| BVDT | VERDICT | 17.49s |
| BHTF | YOUR_TURN | 13.38s |
| BOUT | OUTRO | 1.13s |
| **Total** | | **196.01s** |
