You are Claude Code, building ONE video end to end, unattended. Work only inside this repo. Follow
the render contract. Do not ask for confirmation between steps.

SCOPE: work ONLY inside `brutalist-art/`. Never reach outside it. Keys are in `./.env`. If something
you need isn't in this folder, write a `MISSING: <what> — blocks <beat/step>` line to the BUILD-LOG
and stop that thread. First read `EXAMPLES-CAMPAIGN.md` — especially the **Standing rules**.

LOG HUMAN FEEDBACK FIRST: any instruction the human gives mid-build → append it verbatim under a
`## HUMAN FEEDBACK — <date>` heading in `BUILD-LOG.md` BEFORE acting on it.

LOG EVERYTHING (append-only) to `youtube/posting-to-youtube/BUILD-LOG.md`.

SOURCE DOC: this video is the spoken form of `docs/posting-to-youtube.md`, built from the real
publish session in `youtube/PUBLISH-LOG.md`. Read both first.

REPO: the `brutalist-art` toolkit (you are at its root).
VIDEO FOLDER: `youtube/posting-to-youtube/` — self-contained.
SPEC: its `beat_sheet.json` is the heart. Read it, then `docs/posting-to-youtube.md`,
`runtime/README.md`, and `runtime/manim/animated_graphics.py` before writing anything.

RENDER CONTRACT (per scene): attempt; retry ≤5×, fixing the error between tries; if it still fails,
leave that beat a slate and move on. Palette `teardown`: white #FFFFFF, ink #2A1A0E, one red
#C8102E, teal #1F6F5C as the single "good/kept" accent. Never more than two accents.

STEP 1 — `scenes.py` (Manim). One `Scene` per GRAPHIC beat with `shot.source=="own"`:
B01, B02, B04, B07, B08, B09, B10, B11, B12. Class name = the beat's `graphic.manim`. Build each from
its `graphic.production_viz` (`label`, `mechanic`, `colors`) as clean progressive-disclosure line
art. Resolve the shared lib:
    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "runtime" / "manim"))
    from animated_graphics import *
Read durations from `beat_sheet.json`. Size every box to the FULL text stack
(SurroundingRectangle(VGroup(all lines), buff=…)); verify by frame. B12 (`B12_TheSplit`) is the HERO
— most care; it's the conductor split (machine posts / human decides), echoing videos 1–3.

STEP 2 — the three gate files: `FACTCHECK.md` (the real figures are the three youtu.be IDs
xXKgCXc1nm4 / 7rUcwkFOhvM / AhdmP75PBY0, "1,600 units", "10,000/day", "~6/day", "3 uploaded, 1 bug" —
all real from PUBLISH-LOG.md; label terminal blocks "real session output, lightly trimmed"),
`SHOTLIST.md` (one row per beat), `PROMPTS.md` ("No open media slots — all beats pipeline-rendered").

STEP 3 — Remotion beats: B00, B03, B05, B06, B13, B99.
- `cd runtime/remotion && npm install` (first time only), then back to repo root.
- RENDER WITH THE HELPER, foreground, never by hand:
      python3 runtime/scripts/remotion_scenes.py youtube/posting-to-youtube
  (`--force` to re-render, `--only B06` for one). NEVER hand-roll `npx remotion render`, NEVER
  background a render, NEVER poll `ps`/`grep`.
- The beat sheet's `shot.remotion.props` are ALREADY matched to each component's zod schema, all with
  `topic="POSTING TO YOUTUBE"`. Don't strip those keys or the beat renders Root.tsx demo defaults.

STEP 4 — Audio: if `ELEVENLABS_API_KEY` set, `python3 runtime/scripts/generate_audio.py
youtube/posting-to-youtube` (voice `ELEVENLABS_VOICE_NIKBEARBROWN`), then conform scenes to measured
audio. Else silent cut, and say so.

STEP 5 — Compile: `./art run youtube/posting-to-youtube`. Apply the render contract.

STEP 6 — VERIFY BY LOOKING: read `qc-sheet.png`; confirm every beat shows THIS video's content — no
`Root.tsx` placeholder (photoelectric/cancer). If any beat wears another video's text, its props
didn't match the schema — fix and re-render `--force`.

STEP 7 — Report: `python3 runtime/scripts/todo.py youtube/posting-to-youtube`, print the ledger, list
any slate/rough beat. Don't claim done if any beat is a slate.

FINALLY — append a `## REFACTOR FEEDBACK — posting-to-youtube — <date>` block to BOTH this folder's
BUILD-LOG.md and repo-root CAMPAIGN-FEEDBACK.md.
