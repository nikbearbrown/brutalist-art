---
name: simulation
description: >
  Build a Medhavy-register "Build it with Claude Code + Manim" reel for a physics or
  math concept — the workflow video, NOT the physics explainer. Subject is the
  prompt→read→run→check→change loop; the chapter concept is the running example.
  Use when the user types `simulation <book>` or `simulation <chapter>` or asks to
  make a Claude Code + Manim sim reel. Register: Medhavy (Wonder). Output: a
  beat_sheet.json + vox_scenes.py ready for `vox_run.sh`.
---

# simulation — the Claude Code + Manim workflow reel

A Medhavy-register video that teaches **how to build your own physics simulation
with a CLI (Claude Code) and Manim** — not the physics itself. The chapter concept
is the *excuse* to run the loop; every riff is about the workflow.

## What it is and is not

**IS:** A demonstration of the prompt → read → run → check → change loop. The
learner leaves knowing how to write a generation prompt, how to read the generated
script, what to verify in a running sim, and how to issue a follow-up change.

**IS NOT:** A physics explainer. The physics facts must be correct (gate below),
but they are not the lesson. Never lecture about the concept; the sim shows it.

## Register

**Medhavy** — Wonder register, Okabe-Ito palette, Medhavy voice.
All `MEDHAVY.md` rules apply:
- FIRST beat = Medhavy intro (MedhavyOpen). LAST beat = Medhavy outro (MedhavyOutro).
- Pronunciation split: tts says `med dahvy`; screen shows `Medhavy`.
- Always run visual + fact gate. 9:16 Short = ONE example, strictly < 3:00.

See `MEDHAVY.md § Video register rules` and `REGISTERS.md`.

## Front-end: scouting simulatable concepts

Before building, scan the chapter for concepts that are:
1. **Simulatable** — a mathematical rule that produces a visible curve, trajectory,
   spectrum, or geometry. "Something happens" when you change a parameter.
2. **Verifiable** — the sim output has at least TWO concrete testable predictions
   (boundary cases, known limits, published values).
3. **Surprising** — the classical/intuitive answer fails, or the result is
   counterintuitive. Drama motivates the loop.

Good candidates: UV catastrophe, photoelectric threshold, Compton shift, orbital
mechanics, wave interference, radioactive decay. Bad candidates: abstract
formalism (no curve), concepts that require animation the sim can't produce.

### Modes
- **One deep sim** — one concept, four beats (PROMPT→SCRIPT→RUN→CHANGE), more
  riff time per beat. Best for complex or dramatic concepts.
- **Reel of 3–4 sims** — three concepts, four beats each, quick pace. Best for
  a chapter survey or when all three are equally strong.

---

## Beat structure

### Bookends (always)
- **B00** — Medhavy intro (MedhavyOpen, Onda terminal). See `MEDHAVY.md`.
- **B_last** — Medhavy outro (MedhavyOutro). See `MEDHAVY.md`.

### Per simulation segment: four acts

#### Act 1 — PROMPT (Onda Terminal beat, `MedhavyTerminalAsk`)
Show the **real** `claude "..."` terminal command that generates the scene.

The `command` prop is the literal prompt — copy-pasteable, not pseudocode.
Every generation prompt must specify:
1. The physical rule (the equation or law the sim encodes).
2. The numbers (concrete parameter values — wavelength, mass, work function, etc.).
3. What to render (curve / arrow / orbit / histogram — the visual artifact).

**Riff (narration):** talk about prompting, not physics. What three things every
generation prompt must include. Why under-specifying leads to a re-do. The prompt
is a specification, not a question.

#### Act 2 — SCRIPT (Onda CodeBlock beat, `MedhavyCodeBlock`)
Show the **actual generated Python/Manim file** that runs in Act 3. Not a
cleaned-up version — the real output.

Highlight the ONE line (or function) that encodes the physics. Everything else is
scaffolding; that line is where an error hides.

**Riff (narration):** talk about reading generated code. Find the key line. Check
it against a reference before running. The read step costs 30 seconds and catches
errors before a wasted render. This is not optional.

#### Act 3 — RUN (Manim scene, `vox_scenes.py`)
The running simulation. Show it for real; no placeholder.

The Manim scene is in `vox_scenes.py` (class `B{N}_<ConceptRun>`). It must:
- Encode the physics correctly (gate below).
- Follow `VISUAL-RULES.md`: short tags only, spectral colors for light, safe-area
  margins, no sentence-length labels.
- Follow Gate W: INK for all `Text()`, palette fills only for TEAL/CRIMSON.

Name exactly **two concrete things to verify** in the narration — boundary cases
or published values. "Does the curve peak where the formula predicts?" is a check.
"It looks right" is not.

#### Act 4 — CHANGE (Onda Terminal beat, `MedhavyTerminalAsk`)
Show a **follow-up `claude "update ..."` command** that modifies the sim.

The change should be one parameter or one visual tweak — not a redesign. The point
is that the loop closes: you ran it, you checked, you issued a precise change, you
re-ran.

**Riff (narration):** closing the loop IS the skill. The physics was the vehicle.
The learner should feel they could open their own terminal right now and run the
same loop on a concept from their own work.

---

## Physics gate

Physics correctness is a headline requirement even though physics is not the lesson.
FACTCHECK.md must exist and be correct before audio spend. Entries:

- Every formula cited or shown must be verified against a primary source.
- Every number (wavelength, work function, Compton wavelength, etc.) must match
  the textbook value to the displayed precision.
- The sim's two testable predictions must be stated explicitly in FACTCHECK.md
  and verified against expected values.

Gate F (FACTCHECK.md present) + Gate P (PEDAGOGY.md `VERDICT: PASS`) gate the
audio step. Gate A / W / B gate the Manim render. All must pass.

---

## Visual gate (summary)

From `VISUAL-RULES.md` — apply to every `vox_scenes.py` scene:

- **LESS TEXT:** labels are short tags (`Na`, `E = 1.77 eV`, `e⁻`). No sentences.
- **SPECTRAL COLORS:** light objects use wavelength → RGB (700 nm=red, 546 nm=green,
  ~400 nm=violet). Palette colors (TEAL/CRIMSON) are for abstract quantities only.
- **SAFE AREA:** 16:9 safe ±6.3 x / ±3.4 y; 9:16 safe ±1.95 x / ±3.4 y.
- **GATES:** run Gate A + W + B; fix all errors; warnings acceptable only if
  physics demands them.

---

## Reuses from the vox toolkit

| Asset | Location | Use |
|---|---|---|
| `beat_sheet.json` | reel folder | single source of truth: durations, tts, props |
| `generate_audio.py` | `scripts/` | Gate P → ElevenLabs TTS → `mp3/` |
| `vox_run.sh` | `scripts/` | Gate A/W/B → Manim renders → compile → review mp4 |
| `vox_compile.py` | `scripts/` | assembles per-beat video + audio |
| `static_scene_check.py` | `tmp/qc-tooling/` | Gate A |
| `wcag_margin_check.py` | `tmp/qc-tooling/` | Gate W |
| `manim_layout_audit.py` | `tmp/qc-tooling/` | Gate B |
| `vox_graphics.py` | `aspects/explainer/vox-explainer/manim/` | Manim palette + components |
| Onda terminal/code-block | `aspects/remotion-pass/remotion/` | MedhavyTerminalAsk, MedhavyCodeBlock |
| `REGISTERS.md` | `vox/` | outro lookup + tts substitution table |
| `PRONUNCIATION.md` | `vox/` | pronunciation dictionary |

Cross-reference `RIFFING.md` in `books/brutalist/remotion/` for riff doctrine
(how to write the narration that rides over the visual beats).

---

## Commands

### `simulation <book-folder>` — scout + plan
1. Read `MEDHAVY.md`, `VISUAL-RULES.md`, `REGISTERS.md`.
2. Scan the book's chapters for simulatable concepts (see Front-end above).
3. Propose: one deep sim or reel of 3–4. State which concepts and why.
4. Wait for approval before writing anything.

### `simulation <chapter file>` — build from a specific chapter
Same as above, restricted to that chapter.

### `simulation build <slug>` — execute the build
After the plan is approved:
1. Write `FACTCHECK.md`, `SHOTLIST.md`, `PEDAGOGY.md` (with `VERDICT: PASS`).
2. Write `beat_sheet.json` (B00 Medhavy intro → content beats → B_last Medhavy outro).
3. Write `vox_scenes.py` (one class per Manim beat, named `B{N}_<ConceptRun>`).
4. Run Gate A + W (pre-flight): `VOX_FACTS=0 bash vox/scripts/vox_run.sh <reel>`.
5. Fix gate failures. Cap at 3 attempts; stop and report if still failing.
6. Generate audio: `python3 vox/scripts/generate_audio.py <reel>`.
7. Run full build: `bash vox/scripts/vox_run.sh <reel>`.
8. Deliver: `<reel>/<slug>-review.mp4`.

For the 9:16 Short: run `python3 vox/scripts/vox_short.py <reel> --only <segment-beats> --handle @MedhavyAI --no-endcard`, write `short/vox_scenes.py` for portrait Manim beats, re-run gates on `short/`.
