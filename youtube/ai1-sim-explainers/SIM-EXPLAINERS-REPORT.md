# SIM-EXPLAINERS REPORT

Generated: 2026-07-15 (full run + retry — complete)

## Summary

| metric | count |
|--------|-------|
| Total sims | 108 |
| Built (this session) | 103 |
| Pre-built / carried over | 5 |
| Failed | 0 |
| Missing review mp4 | 0 |

**All 108 sims have a review mp4. Run is complete.**

## Pipeline

- Voice: Medhavy / Kokoro `af_kore` / Wonder register
- Channel: `claude-medhavy` / `@Medhavy`
- Spine: COLD OPEN → PROBLEM → ASK → CODE → OUTPUT → CHANGE → OUTPUT2 → SUMMARY → NEXT STEPS → HANDOFF → OUTRO
- Output dir: `brutalist-art/youtube/ai1-sim-explainers/<sim-slug>/`
- Each reel: `<slug>-review.mp4` (1.1–3.9 MB)

## Notes

- Phase-0 capture smoke test: PASSED
- 6 sims had transient capture failures in the first batch pass (port contention / resource exhaustion); all resolved on retry — 0 failures remain
- Sims with no range slider fell back to button/hold capture and still produced valid screen recordings
- gene-drive-spread had an ffmpeg codec error on first compile; rebuilt cleanly on retry

## Open next step

Review cuts are previz-grade: the CODE beat (B03) uses a slate placeholder
for the Onda code-block, and the CHANGE beat (B05) is a narrated slate.
To upgrade any reel:
- B03 CODE: drop an Onda code-block render of the core JS (stored in `beat_sheet.json → beats[3].code_snippet`)
- B05 CHANGE: replace slate with a title card or annotated second screen recording
- Final cut: run `compile.py <reel_dir>` (no `--review`) after all slates filled

See SIM-EXPLAINERS-LOG.md for per-sim `open` commands.
