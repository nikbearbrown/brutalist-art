# TYPECHECK.md — GATE T

Reel: `make-it-move`  |  Checked: 2026-07-25T01:47  |  Overall: **FAIL**  |  Beats checked: 9  |  FAILs: 1

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| A1 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| VERDICT | ? | min-size §8.1: smallest text run 27px < floor 35px (3.2% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| HANDOFF | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| OUTRO | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

### VERDICT (?)
- **min-size §8.1**: smallest text run 27px < floor 35px (3.2% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 5 | 0 |
| min-size §8.1 | 9 | 1 |
| overflow §8.2 | 9 | 0 |
| contrast §8.3 | 9 | 0 |
| kerning §8.4 | 0 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
