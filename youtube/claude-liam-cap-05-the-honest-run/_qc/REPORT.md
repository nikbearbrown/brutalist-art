# QC REPORT — claude-liam-cap-05-the-honest-run
# "The Honest Run." | Reallocation Engine Capstone · E5 of 8
# Built: 2026-07-19 | Kokoro am_onyx | 351.8s

## VERDICT: PASS

## Rubric (9-point)

| # | Check | Result |
|---|---|---|
| 1 | IN-FOR-BEAR: "Liam, in for Bear." present in B00 | PASS |
| 2 | Greeting "Namaste, Liam." visible in B00 | PASS |
| 3 | Topic label "REALLOCATION ENGINE CAPSTONE · E5 OF 8" in B00 | PASS |
| 4 | Self-demo output visible (sed 128,148 / five deliverables / break attempt / $0.00) | PASS |
| 5 | B05 heading "The audit catches what fluency hides." + verbatim quote | PASS |
| 6 | B06 heading "Skip rate ≥50%: the filter working." + verbatim quote | PASS |
| 7 | B07 heading "Name what the machine could not know." + verbatim quote | PASS |
| 8 | BVDT "Verdict" + "The run." + 3 items | PASS |
| 9 | ILLUSTRATE LAW: 5 UI + 6 illustration beats | PASS |

## Frame verification

| Frame | Beat | Time | Result |
|---|---|---|---|
| B00.jpg | OPEN | 12s | PASS — "Namaste, Liam." / "REALLOCATION ENGINE CAPSTONE · E5 OF 8" / "Liam, in for Bear." / five deliverables in output panel |
| B05.jpg | MECHANISM_1 | 176s | PASS — "The audit catches what fluency hides." heading + verbatim quote + "Source: chapters/16-the-build-and-the-honest-run.md" |
| B07.jpg | MECHANISM_3 | 258s | PASS — "Name what the machine could not know." heading + verbatim quote + source citation |
| BVDT.jpg | VERDICT | 323s | PASS — "Verdict" header / "The run." heading / 3 numbered lines correctly populated |

B06 not sampled by dedicated frame; uses same SkillTeardownMechanism component as B05/B07 (both confirmed). Non-blocking.

## Issues

### BLOCKER (0)
None.

### MAJOR (0)
None.

### MINOR-COSMETIC (2)
- B04 ClaudeCodeBeat: moderate slow-mo — 10s Remotion clip stretched 2.78x to fill 27.9s narration. Known pattern, non-blocking.
- BOUT actual_duration_s: 1.02s (very short outro). Known pattern, non-blocking.

## Beat timing log

| Beat | Role | Duration |
|---|---|---|
| B00 | OPEN | 23.66s |
| B01 | ANATOMY | 49.81s |
| B02 | PIPELINE | 48.92s |
| B03 | PREDICT | 6.06s |
| B04 | SELF-DEMO | 27.90s |
| B05 | MECHANISM_1 | 41.13s |
| B06 | MECHANISM_2 | 38.38s |
| B07 | MECHANISM_3 | 43.01s |
| B08 | THE_PICK | 32.83s |
| BVDT | VERDICT | 21.46s |
| BHTF | YOUR_TURN | 17.60s |
| BOUT | OUTRO | 1.02s |
| **Total** | | **351.8s** |
