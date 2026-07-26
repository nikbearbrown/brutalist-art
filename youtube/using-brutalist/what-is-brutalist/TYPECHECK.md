# TYPECHECK.md — GATE T

Reel: `what-is-brutalist`  |  Checked: 2026-07-25T01:09  |  Overall: PASS  |  Beats checked: 9  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| A1 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| VERDICT | ? | min-size §8.1: min text-run height 76px >= floor 35px | PASS | — |
| HANDOFF | ? | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| OUTRO | ? | min-size §8.1: min text-run height 66px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 5 | 0 |
| min-size §8.1 | 9 | 0 |
| overflow §8.2 | 9 | 0 |
| contrast §8.3 | 9 | 0 |
| kerning §8.4 | 0 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
