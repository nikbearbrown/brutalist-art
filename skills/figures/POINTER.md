# figure / data-viz skills — gathered from ai1-cli (the repo-native form)

`cajal`, `figures`, `graphs`, and `tables` do NOT exist as `SKILL.md` skills anywhere in
`bear-textbooks/`. In this repo they live inside **`books/ai1-cli/`** as a script plus
prompt-library / appendix docs. Those source files are copied here under `from-ai1-cli/`:

| File | Original (`books/ai1-cli/`) | What it is |
|---|---|---|
| `graphs.sh` | `graphs.sh` | Graphs+tables renderer: processes `<!-- [TYPE: description] -->` placeholders in `chapters/*.md`, makes placeholder images and renders tables for local iteration (Cowork does the real D3/SVG). The `graphs`/`tables` skill in script form. |
| `_lib_design-figure-architect-prompt.md` | `pantry/_lib_design-figure-architect-prompt.md` | The **Figure Architect** paste-in prompt system (high-assertion zone detection MC/VG/PQ → publication-quality image prompts). The `figures` skill in prompt form. |
| `_lib_design-figure-architect.md` | `pantry/_lib_design-figure-architect.md` | Companion design doc for the Figure Architect. |
| `88-appendix-cajal.md` | `pantry/88-appendix-cajal.md` | The **CAJAL command set + SVG Style Guide** reproduced for copying (SCOPE framework, figure-type library, phase gates, house SVG spec). The `cajal` skill. |
| `11-creating-figures.md` | `pantry/11-creating-figures.md` | Chapter 11 craft essay — deciding what to leave out. |
| `86-appendix-finishing-figures.md` | `pantry/86-appendix-finishing-figures.md` | Finishing-pass figure appendix. |
| `09-finishing-pass-and-figures.md` | `pantry/09-finishing-pass-and-figures.md` | Production pipeline: finishing pass → CAJAL Image Suggest → SVG-to-PNG build. |
| `svg-to-png.mjs` | `SCRIPTS/svg-to-png.mjs` | Renderer CAJAL depends on (Node 18+, `sharp`): SVG → 300-DPI PNG. |

## Note on the Cowork session skills
There are ALSO Cowork/Claude session skills named `cajal`, `figures`, `graphs`, `tables`, and
`dataviz` that load at runtime and may be more current than these ai1-cli copies. When
refactoring, decide the source of truth: promote these ai1-cli files into real `SKILL.md`
skills, or keep depending on the session-loaded versions and treat these as the library.
