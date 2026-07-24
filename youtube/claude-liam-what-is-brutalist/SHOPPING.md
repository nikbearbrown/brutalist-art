# SHOPPING.md — Gate D2 manifest

Written: 2026-07-22 (after audio lock — timings sourced from mp3/timings.json)

## Pantry status: NOTHING TO SOURCE

This reel has **zero VOX beats** (`shot.type: STILL` or `COMPOSITE` with
`shot.source: archive` or `ai`). Every beat is either:

- **MANIM** — rendered by `animated_graphics.py` from `scenes.py` (machine-made)
- **REMOTION** — rendered by `remotion_scenes.py` from registered Remotion
  components (machine-made)

No pantry stills are needed. The machine has handled every slot.

## Locked beat durations (from mp3/timings.json)

| Beat | Locked duration | Slot type |
|---|---|---|
| B00 | 14.42 s | REMOTION — BrutalistTerminalOpen |
| B00B | 18.97 s | MANIM — B00B_ReviewLabel |
| B01 | 8.34 s | MANIM — B01_OneClickSlop |
| B02 | 6.21 s | MANIM — B02_CannotWatch |
| B03 | 10.86 s | MANIM — B03_TasteGaps |
| B04 | 7.30 s | REMOTION — NikBearBrownCodeBlock |
| B05 | 12.05 s | MANIM — B05_TwentyHourBug |
| B06 | 14.95 s | MANIM — B06_TwoFailureModes |
| B07 | 4.91 s | MANIM — B07_YouAreTheConductor |
| B08 | 11.86 s | MANIM — B08_ScoreAndPlaying |
| B08B | 13.03 s | MANIM — B08B_FixTheBoxes |
| B09 | 7.77 s | MANIM — B09_BeatSheetHeart |
| B10 | 12.97 s | REMOTION — NikBearBrownTerminalAsk |
| B11 | 16.34 s | MANIM — B11_RequestCardPantry |
| B12 | 4.65 s | REMOTION — NikBearBrownTerminalAsk |
| B13 | 4.42 s | REMOTION — NikBearBrownCodeBlock |
| B14 | 12.84 s | MANIM — B14_ThePlaylist |
| B99 | 8.90 s | REMOTION — BrutalistCommentCTA |
| **Total** | **190.8 s (3:11)** | |

## Skin lint notes (intentional — log for the record)

The pipeline flags two skin warnings that are correct by design:

- **B00**: `BrutalistTerminalOpen` instead of `ClaudeComposerAsk` — this is a
  Brutalist meta-series video on @NikBearBrown, not a claude-liam audience
  episode. The terminal-cold-open is the series' signature brand choice.
- **B99**: `BrutalistCommentCTA` instead of `ClaudeTitleOutro` — same reason;
  the Brutalist outro is the correct closing block for this channel.

These are not defects. Document in BUILD-LOG.md and proceed.

## Gate D2 status

**PASSED** — pantry is complete by design; zero entries unresolved.
The review cut may proceed once you have watched the previz.
