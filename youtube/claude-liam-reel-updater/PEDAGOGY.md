# PEDAGOGY — claude-liam-reel-updater
# "Claude, Updated." | reel-updater skill teardown

## Learning goal
Viewer leaves knowing: (1) reel-updater migrates existing reels from old mascot outro to new Remotion outros — strip the old, append the new; (2) dry-run by default, --apply on the Mac, idempotent; (3) credit discipline: the strip spends nothing; only the two new outro beats ever bill.

## Prediction beat
B03 poses: the old mascot outro is detected on a reel. What happens to the audio? Viewer predicts before B04/B05/B06/B07 reveal: (1) pristine narration is restored from outro-orig-<bid>.mp3, (2) the silence-padded mp3 is overwritten, (3) actual_duration_s is reset.

## Concrete before abstract
B04 shows the drift-detection scan across youtube/ (reading beat_sheets for old outro pattern — free) before B05/B06/B07 state the abstract dry-run / credit-discipline / idempotent laws.

## Self-demo check
B04 is genuinely free: python3 scan of all claude-liam beat_sheets checking for old mascot outro pattern (source=outro). No files deleted, no audio generated.

## ILLUSTRATE LAW
- UI beats (5): B00, B03, BVDT, BHTF, BOUT
- Illustration beats (6): B01, B02, B04, B05, B06, B07

## VERDICT: PASS
