---
name: riff
description: Render a visual unit — a few frames of an mp4, a Remotion scene, or a Manim scene — with a made-up themed-educational example, and riff on it in the NikBearBrown / Teardown voice — what it does, pros and cons, and above all its usefulness for education. Batches into one compilation reel per functional category. Use when the user types `riff [target]`, asks to review/showcase/critique scenes or components, or to see the vox Remotion bench rendered with examples. The inform step of bench promotion — riff surfaces trade-offs; the human decides what to promote. Lives in brutalist/remotion/; renders on the user's machine.
---

# riff — render-and-critique a visual unit in the NikBearBrown voice

`riff` shows a scene and judges it. It renders a visual unit with a made-up **themed-
educational** example, then riffs in the **NikBearBrown / Teardown** register: what it does,
where it's useful, its pros and cons, and — the point — **its usefulness for education**.

**Brutalist role (read `brutalist/BRUTALIST.md`):** riff is the *inform* arm of bench
promotion. It renders and critiques so the human can *see* each scene and hear its trade-offs.
**Riff never decides what to keep or promote** — it surfaces pros/cons and stops. That refusal
is the point (principles 4 + 5 + 6). Project state + the audited contract: `PROJECT.md`.

## Inputs (three adapters, one riff format)
- **mp4** → ffmpeg frame-grab (a couple of representative frames), then riff.
- **Remotion scene** → render with fixture props via the harness, then riff. *(v1 target.)*
- **Manim scene** → render via `vox_graphics.py` with an example, then riff. *(later.)*

## Phases (audio-first, phase-gated — the vox spine)
1. **Select** — resolve the target list: a functional-category batch, one scene, or a path.
2. **Fixture** — supply each scene a themed-educational example (override content props only;
   onda schemas default the rest). Fixtures: `src/fixtures/[category].ts`.
3. **Render (user's Mac)** — one short clip per scene in the **teardown** palette. The harness
   renders what renders and **logs every failure** (slug + reason); it never silent-drops.
4. **Riff** — author the NBB Teardown script per scene (*what it does · pros/cons · educational
   use*), seeded from the scene's `meta.json` (`description`, `pickWhen`). Then ElevenLabs NBB
   voice + faster-whisper captions (reused from vox).
5. **Assemble** — stitch `[scene clip + NBB VO + caption]` per functional category into one
   reel (DATA, TEXT, SHAPE, TITLE, TRANSITION, BACKGROUND, EFFECT, AUDIO). Cold-open → per-
   scene riff → next.

## Commands
- `riff onda` — pilot: render + riff onda's components, one reel per category present.
- `riff [collection]` — a bench collection (once the pilot proves the harness).
- `riff [path-to.mp4]` / `riff [path-to-scene]` — a single unit.

## Refusal (Brutalist teeth)
- Asked to **decide which scenes are good / to promote** → declines; riff informs, the human
  promotes. It renders the evidence and lays out pros/cons instead.
- Asked to **skip the render gate** and mass-produce all category reels before the pilot
  renders → declines; one lane verified before the next (BRUTALIST.md phase gate).
- **Rendering and ElevenLabs spend happen on the user's machine**, after the human verifies the
  scripts. Riff authors; it does not spend.

## Reuse (do not reinvent)
NBB voice + `vox` `generate_audio.py` · faster-whisper caption pipeline · Remotion assembly ·
the `teardown` tokens · the category inventory (`vox-remotion-bench-inventory.md`) as the
batching plan. New machinery: the scene-render harness + the themed-fixture library only.
