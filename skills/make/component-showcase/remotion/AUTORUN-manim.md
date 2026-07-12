# AUTORUN — one Brutalist riff per Manim library (the ManimCE five)

You are Claude Code on Bear's Mac, working directory
`$ART_HOME/skills/make/component-showcase/remotion` (= `$PROJECT`).
The Manim libraries live under `$ART_HOME/runtime/manim`.

**Goal:** render **one catalog riff per ManimCE library** — render a sample of each library's
scenes to mp4, then ride the mp4-riff pipeline (`RiffManim` composition) to a finished video.
Run each step; on any error read it, fix it, and continue. **Do not stop until every library
below has an output (or is logged as unrenderable). Absolute paths only.**

## Prerequisites (check once)
- ManimCE installed: `manim --version` (else `pip install manim --break-system-packages`).
- Each library may need its own deps. If a render fails with `ModuleNotFoundError`, `pip install`
  the missing package (e.g. `manim-physics`) and retry that scene.

## The ManimCE libraries (GL-only repos are OUT OF SCOPE — see bottom)
| name | --lib path | --link | scenes found |
|---|---|---|---|
| manim-fourier-series | `../manim/manim-fourier-series` | github.com/taibeled/manim-fourier-series | 13 |
| manim-physics | `../manim/manim-physics` | github.com/Matheart/manim-physics | 2 (examples) |
| PsiAnimator-MCP | `../manim/PsiAnimator-MCP` | github.com/manasp21/PsiAnimator-MCP | 7 |
| Quantum-Memories-and-Repeaters-Visualised | `../manim/Quantum-Memories-and-Repeaters-Visualised` | github.com/VishuVish/Quantum-Memories-and-Repeaters-Visualised | 16 |
| Math-To-Manim | `../manim/Math-To-Manim` | github.com/HarleyCoops/Math-To-Manim | 160 (cap at 8) |

## Per-library procedure
The beat sheet + audio use one shared filename (`beats/manim.*`), so **finish one library's
render before starting the next.** For each row (`NAME`, `LIB`, `LINK`):
1. Discover + render + stage clips + write the beat sheet:
   `python3 $PROJECT/scripts/manim_catalog.py --lib $PROJECT/<LIB> --name "<NAME>" --link <LINK> --max 8`
   (First try `--discover-only` to see the scene list. Scenes that fail to render are skipped and logged — that's fine, catalog what renders.)
2. `python3 $PROJECT/scripts/riff_audio.py $PROJECT/beats/manim.beats.json`
3. `python3 $PROJECT/scripts/riff_conform.py $PROJECT/beats/manim.beats.json`
4. `python3 $PROJECT/scripts/riff_gate.py $PROJECT/beats/manim.conformed.json`  (warnings OK)
5. Render: `$PROJECT/node_modules/.bin/remotion render $PROJECT/src/index.ts riff-manim $PROJECT/out/riff-manim-<NAME>.mp4`
6. Optional publish: `python3 $PROJECT/scripts/riff_publish.py --video $PROJECT/out/riff-manim-<NAME>.mp4 --sheet $PROJECT/beats/manim.conformed.json --playlist Brutalist --run`  (the `--sheet` is REQUIRED — riff_publish defaults to the Onda sheet; title/description must come from the manim sheet)

## How it's built (fix, don't rebuild)
- `manim_catalog.py` finds ManimCE `Scene` subclasses (AST, skips `manimlib` GL files), renders each with `manim -ql`, copies the mp4 into `public/clips/manim/`, and writes `beats/manim.beats.json` (intro + one clip segment per rendered scene + credit + brutalist/@NikBearBrown outro). The per-scene description is the class docstring where present, else factual — do not fabricate.
- `RiffManim` (composition `riff-manim`) plays each clip via `<OffthreadVideo ... objectFit=contain>` (contain, not cover — don't crop the math) under the same captions/audio as the mp4 riff. It statically imports `beats/manim.conformed.json`; a placeholder is committed so it bundles, and step 3 overwrites it.

## Known-good facts — do NOT re-litigate
- `remotion.config.ts` pins the project root **absolute** — keep it. zod banner is **non-fatal**.
- `OffthreadVideo` must be `muted`.

## DONE when
Each ManimCE library above has either `$PROJECT/out/riff-manim-<NAME>.mp4` (non-empty, zero
frame errors) OR a one-line note in your final summary saying why it couldn't render (e.g. all
scenes errored, missing deps you couldn't install). Print the output paths.

## OUT OF SCOPE (ManimGL — needs porting or a separate ManimGL render pass, do NOT attempt here)
`openblochsphere`, `Quantum-Animation`, `quantum-animation-toolbox` (GL parts), `videos` (3b1b, 5,276 scenes).
