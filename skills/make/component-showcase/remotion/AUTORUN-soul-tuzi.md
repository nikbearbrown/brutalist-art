# AUTORUN — render the "Same Person?" mp4 riff (Higgsfield Soul ID · tuzi)

You are Claude Code on Bear's Mac, working directory
`$ART_HOME/skills/make/component-showcase/remotion` (= `$PROJECT`).

**Goal:** render the mp4 riff to `$PROJECT/out/riff-soul-tuzi.mp4` so Bear can watch it. Run every
step, and on any error read it, fix the code/config, and re-run. **Do not stop until the DONE
criterion holds. Absolute paths only.**

## Pipeline
1. Stage the clips into `public/clips/` (Remotion only serves files under `public/`):
   `python3 $PROJECT/scripts/mp4_prep.py $PROJECT/beats/soul-tuzi.beats.json`
2. Voice the beats (ElevenLabs, NBB voice — key from `../../vox/.env`):
   `python3 $PROJECT/scripts/riff_audio.py $PROJECT/beats/soul-tuzi.beats.json`
3. Conform to measured audio (writes `beats/soul-tuzi.conformed.json`, overwriting the placeholder):
   `python3 $PROJECT/scripts/riff_conform.py $PROJECT/beats/soul-tuzi.beats.json`
4. Lint (warnings OK; fix only errors — captions here are longer than the Onda ones, so L3 warns are expected):
   `python3 $PROJECT/scripts/riff_gate.py $PROJECT/beats/soul-tuzi.conformed.json`
5. Render:
   `$PROJECT/node_modules/.bin/remotion render $PROJECT/src/index.ts riff-soul-tuzi $PROJECT/out/riff-soul-tuzi.mp4`

## How it's built (so you can fix it, not rebuild it)
- Composition `riff-soul-tuzi` = `src/riff/RiffMp4.tsx`. Body segments have a `clip` field and render `<OffthreadVideo src={staticFile('clips/<name>')} loop muted objectFit=cover>`; the two `outro-*` segments render a Remotion brutalist `Card`. Captions + audio are the same `<BeatCaption>` / `<Audio>` machinery as the Onda tour.
- `RiffMp4.tsx` statically imports `beats/soul-tuzi.conformed.json`. A placeholder (empty `segments`) is committed so the project bundles before the first conform; step 3 overwrites it with real frames. If you edit the beat sheet, re-run steps 2–3 before rendering.
- The narration is authored in `beats/soul-tuzi.beats.json` (do not auto-generate it). Facts are sourced from Higgsfield's Soul ID blog; the consistency read is honest (casting-consistent, forensically drifting).

## Known-good facts — do NOT re-litigate
- `remotion.config.ts` pins the project root **absolute** — keep it.
- The zod "3.25.76 vs 4.3.6" banner is **non-fatal**.
- If a scene is `<undefined/>` (React #130), an import name is wrong — fix it, don't guess props.
- `OffthreadVideo` must be `muted` (the riff audio is the ElevenLabs track, not the clip's).

## DONE when
`$PROJECT/out/riff-soul-tuzi.mp4` exists, is non-empty, and rendered with **zero frame errors**.
Then print the output path (and the runtime) so Bear can watch it.

## Optional — publish
`python3 $PROJECT/scripts/riff_publish.py --video $PROJECT/out/riff-soul-tuzi.mp4 --sheet $PROJECT/beats/soul-tuzi.conformed.json --playlist Brutalist --run`
(The `--sheet` is REQUIRED — riff_publish defaults to the Onda sheet, which would put the wrong title/description on this video. Title + description come from this sheet.)
(`publish-workspace/*.json` are real OAuth secrets — never print, commit, or move them.)
