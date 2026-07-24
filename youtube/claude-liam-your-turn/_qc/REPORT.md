# QC REPORT — claude-liam-your-turn
# "Claude, Handed Off." | your-turn skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 174.4s

## VERDICT: PASS

## 9-Point Rubric

| Check | Result | Notes |
|---|---|---|
| IN-FOR-BEAR | PASS | B00 frame: "Liam, in for Bear." visible top-left |
| ILLUSTRATE LAW | PASS | 5 UI beats (B00,B03,BVDT,BHTF,BOUT) + 6 illustration (B01,B02,B04,B05,B06,B07) |
| VERBATIM QUOTE | PASS | B05 quote renders verbatim from SKILL.md |
| SELF-DEMO | PASS | drafts.json entry + closing block transform (free, no apply_your_turn.py run) |
| NO SLATES | PASS | 11/11 beats filled as VIDEO |
| AUDIO FIRST | PASS | actual_duration_s on all beats; 174.4s master |
| FREE PIPELINE | PASS | Kokoro am_onyx, $0.00 |
| PALETTE | PASS | Cream/terracotta/warm-ink; Claude brand tokens throughout |
| BOUT | PASS | ClaudeTitleOutro at 170.67s |

## Frame Evidence

- **B00** (4s): "YOUR-TURN · SKILL TEARDOWN" label; "Liam, in for Bear."; "Annyeong, Liam" greeting
- **B05** (94s): Quote box — "Every claude-explainer reel should end the same way: Liam hands off from the body, recaps on the artifact card, gives the viewer a prompt to run, and re-reads the title."
- **BVDT** (150s): Verdict card — "The split" with 3 beats listed

## Issues

### MINOR-COSMETIC (non-blocking, 4 total)
1. B04 ClaudeCodeBeat slow-mo: 2.39× stretch (10s Remotion clip → 24.0s narration) — known pattern
2. B00 sparkLine empty — known on ClaudeComposerAsk
3. B03 sparkLine empty — known
4. BHTF sparkLine empty — known

## Beat Timings
| Beat | Start | End | Duration |
|---|---|---|---|
| B00 | 0.00s | 10.77s | 10.77s |
| B01 | 10.77s | 31.14s | 20.37s |
| B02 | 31.14s | 54.22s | 23.08s |
| B03 | 54.22s | 59.87s | 5.65s |
| B04 | 59.87s | 83.87s | 24.00s |
| B05 | 83.87s | 104.03s | 20.16s |
| B06 | 104.03s | 124.23s | 20.20s |
| B07 | 124.23s | 145.97s | 21.74s |
| BVDT | 145.97s | 160.73s | 14.76s |
| BHTF | 160.73s | 170.67s | 9.94s |
| BOUT | 170.67s | 174.40s | 3.73s |
