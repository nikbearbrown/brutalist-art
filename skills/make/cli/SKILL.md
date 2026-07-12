---
name: cli
description: >
  Build a "CLI video" — a Teardown-voice reel that shows code being typed into a
  terminal (the Onda terminal skin, a simulated Claude session) and shows the
  OUTPUT as a moving vox-explainer beat: a Manim / Remotion / d3 animation, or a
  slate you fill later. Generalizes the `simulation` aspect — the terminal drives
  the story; the output is always motion, never a still. Use when the user types
  `cli <concept|chapter|idea>` or asks for a CLI video / Onda video / "show what's
  typed into a CLI with the output as a vox beat". Register: Teardown (NikBearBrown).
  Output: beat_sheet.json for vox_run.sh.
---

# cli — the CLI-video style (Onda terminal in, animated output out)

A **CLI video** shows two things in alternation: **a simulated terminal session**
(the Onda skin — someone typing `claude "…"` and reading what it makes) and **what
the command produced** (an output beat — a *moving* visualization). Two differences
from the `simulation` aspect: the output is not Manim-only (it is any animation or a
slate), and every CLI video carries a **fixed narrative spine** so it teaches, not
just demonstrates.

`vox_compile.py` already resolves an output slot by precedence
`media/<BID>.mp4 > manim/<BID>.(mp4|mov) > media/<BID>.png > slate` — so the output
beat plays whatever motion you drop in, and un-filled beats ship as labeled slates.

## Trigger
`cli <concept | chapter | idea> [--out <dir>]`
Also: "make a CLI video", "Onda video of building X", "show the CLI then the output".

## The required beat spine (EVERY CLI video — not optional)
```
B00  INTRO        brand open (Remotion: NikBearBrownOpen).
     PROBLEM      what is the problem, why are we solving it, the context, why the
                  viewer should care — the stakes, stated BEFORE any terminal opens.
                  No CLI yet: this is the "why" that earns the build.
     ─── the CLI loop (must contain ≥1 revision) ───
     ASK          terminal: the command/prompt typed into the CLI (Onda).
     CODE         terminal: read the generated code before running (optional per cycle).
     OUTPUT       the run's result — a MOVING visualization (Manim/Remotion/d3) or a slate.
     CHANGE       terminal: check the output, decide it needs a change, type the revision.
     OUTPUT       the revised result — the change made visible.
                  (repeat ASK→CODE→OUTPUT→CHANGE for more cycles if the story needs;
                   AT LEAST ONE revision cycle is REQUIRED — a CLI video without a
                   check-and-change is incomplete.)
     ─── close ───
     SUMMARY      what we built and what the output showed — the lesson, in one beat.
     NEXT STEPS   what to do next / what to try / where it goes from here.
     OUTRO        brand outro (Remotion: NikBearBrownOutro) — the LAST beat.
```
Mandatory, every time: (1) the **PROBLEM** beat after the intro and before the CLI;
(2) **at least one revision** inside the CLI loop (an output, a check, a change, a
re-run); (3) the **SUMMARY** and **NEXT STEPS** beats before the outro. A CLI video
missing any of these three is not done.

The through-line is *problem → build → run → check → change → what it means → what's
next* — Teardown-voiced and output-agnostic.

## Input beats — the Onda terminal skin
Reuse the terminal Remotion scenes (dark terminal window on the teardown ground:
`#111111` body, `#1C1C1C` bar, `#E8E8EC` text, CRIMSON prompt, PT Mono, typewriter):
- **ASK** → `NikBearBrownTerminalAsk` · props: `command`, `topic`, `segment`, `runningText`.
- **CODE** → `NikBearBrownCodeBlock` · props: `filename`, `topic`, `segment`, `code`.
- **CHANGE** → `NikBearBrownTerminalAsk` with the revision command + `runningText: "updating…"`.

**Onda restyle (optional):** mac traffic-light dots, a workspace color-accent, an
`onda` tab, a Claude-Code prompt marker → `OndaTerminalAsk` / `OndaCodeBlock` (new
scenes in `aspects/remotion-pass/remotion/src/scenes/`, registered in `Root.tsx`).
Until they exist, the NikBearBrown terminal scenes are the skin; when they do, just
swap `shot.remotion.pattern`.

## Output beats — a MOVING slot (never a still)
The output beat is a **video**, never a static image. Set `shot.source` to null and
fill it ONE of these ways:
1. **Manim** → `shot.source:"manim"`, add the scene to `vox_scenes.py` → `manim/<BID>.mp4`.
   Best for a parametric/data animation (a curve drawing, a value snapping onto a grid).
2. **Remotion** → `shot.remotion.pattern` → `media/<BID>.mp4`. Typographic/UI motion.
3. **d3 (animated)** → render a d3 animation to mp4, drop as `media/<BID>.mp4`.
4. **screen-recording mp4** → `media/<BID>.mp4` — a capture of the real run.
5. **nothing → slate** → `vox_run.sh` emits a labeled slate for you to fill with one
   of the above. Every output beat is a slate until the motion is dropped in.
**No static png.** If one frame seems to be the artifact, animate its reveal/transform
or make it a slate. Record the intended motion in the beat's `visual_intent`.

## Voice — Teardown (NikBearBrown)
Narration reads the session like a teardown: the problem and stakes (PROBLEM beat),
what the command does, what to *verify* in the output, the design choice the run
exposes, then the lesson and the next move. Strip jargon; explain the machinery; NO
FABRICATION. Forbidden phrases per `voices/teardown/VOICE.md`.

## Build & render (reuses the vox pipeline unchanged)
1. Emit `beat_sheet.json` in the required spine above — INTRO, PROBLEM, the CLI loop
   with ≥1 revision, SUMMARY, NEXT STEPS, OUTRO. Add `vox_scenes.py` for Manim outputs.
2. `python3 scripts/generate_audio.py <reel>` — Teardown-voice narration (spends).
3. `bash scripts/vox_run.sh <reel>` — renders terminal/brand beats, renders Manim
   outputs, leaves un-filled output beats as slates, compiles the review cut.
4. Fill each output slate with a Manim/Remotion/d3/mp4 as it's ready; re-run `vox_run.sh`.

## Reference
`reference/example-cli-beat_sheet.json` — a worked CLI video in the full required
spine (INTRO → PROBLEM → ASK → CODE → OUTPUT → CHANGE → OUTPUT → SUMMARY → NEXT STEPS
→ OUTRO), output beats as animated slots.
