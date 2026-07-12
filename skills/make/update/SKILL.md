---
name: update
description: Bring already-built reels up to the latest specs — migrate the old green-screen mascot outro to the new Remotion outro, delete out-of-sync audio, and regenerate only the new audio. Use when the user types `update`, `update <reel>`, `update all`, `migrate outros`, or says built reels are out of date after a spec change. Dry-run by default; --apply deletes files (runs on the Mac).
---

# update — reconcile built reels to the latest specs

The outro spec changed: the green-screen mascot outro (`vox_outro.py` rebrands the last
CARD beat) is being replaced by **Remotion outros** — `OutroSeries` (from the book's
`ABOUT.MD`) and `OutroCTA` (like/comment/subscribe, from `AUTHOR.MD`). The ~164 built
reels still carry the old outro. `update` migrates them.

## What it does, per reel
1. **Detect drift** — old mascot outro present? out-of-sync (padded) audio? orphan mp3s
   (audio for beats no longer in the sheet)? missing audio?
2. **Strip the non-Remotion outro (FREE — no credits, no network)** — delete the mascot
   `media/<bid>.mp4` and its compiled clip; **restore the pristine, un-padded narration**
   from `clips/_work/outro-orig-<bid>.mp3` over the silence-padded `mp3/beat-<bid>.mp3`;
   reset that beat's `actual_duration_s`; clean the outro work files. The last CARD beat
   reverts to a normal recap card.
3. **Delete orphan audio** — mp3s whose beat id is gone from the sheet.
4. **(next phase) Append the Remotion outro + generate only its audio** — add the
   `OutroSeries` + `OutroCTA` beats (content from `ABOUT.MD` / `AUTHOR.MD`), then
   `generate_audio.py --only <new beat ids>` so **only the two new beats bill** — the
   body's audio is never re-generated. Then `remotion pass` renders them and `vox_run.sh`
   produces a fresh, up-to-date slate cut. This step activates once the `OutroSeries` /
   `OutroCTA` compositions exist in `aspects/remotion-pass/remotion/`.

## Commands
```bash
python3 scripts/vox_update.py <REEL>          # dry-run one reel (plan only)
python3 scripts/vox_update.py --all           # dry-run every reel -> vox/UPDATE.md
python3 scripts/vox_update.py <REEL> --apply   # strip this reel to spec
python3 scripts/vox_update.py --all --apply    # strip every drifted reel
```

## Gates & safety
- **Dry-run by default.** It prints the plan and writes `UPDATE.md`; it changes nothing.
- **`--apply` deletes files**, so it runs on the Mac (via Claude Code), not the Cowork
  sandbox. The strip is recoverable in spirit — it restores the saved pristine narration
  it was going to pad; it does not re-spend audio credits.
- **Credit discipline:** the strip spends nothing. Only the *new* outro beats ever get
  new audio, via `generate_audio.py --only` (which still honors GATE P / `PEDAGOGY.md`).
- **Idempotent:** a reel with no mascot outro and no orphans is reported clean and
  skipped; re-running is safe.

## Sequence to fully migrate the fleet
1. Build the `OutroSeries` + `OutroCTA` Remotion compositions (the remotion-pass next
   phase) so step 4 can append + render the new outro.
2. `update --all` (dry-run) — review `UPDATE.md`.
3. `update --all --apply` — strip the old outros across the fleet.
4. Append the new outro beats + `generate_audio.py --only` + `remotion pass` + `vox_run`
   per reel (the finalize loop; the audit's worklist tracks progress).
