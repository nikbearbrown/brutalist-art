---
name: remotion-pass
description: Fill vox slate beats (beats with no mp4) with vox-palette Remotion motion graphics, template-first. Use when the user types `remotion pass`, `fill slates`, `remotion <reel>`, asks to turn slate beats into motion graphics, to render a Remotion scene for a beat, or to build/promote a Remotion scene pattern. Template-first, create-on-gap, human-gated promotion. Renders to media/<BID>.mp4; the vox compiler conforms duration.
---

# remotion-pass — fill slate beats with vox Remotion motion graphics

A vox aspect that fills **slate beats** (beats that resolve to a grey slate because
they have no `media/<BID>.mp4` and no `manim/<BID>.mp4`) with a **vox-palette
Remotion scene**, rendered to `media/<BID>.mp4`. The existing `vox_compile.py` slot
contract does the rest: `media/<BID>.mp4` is the top slot, audio is stripped, and the
clip is **retimed to the beat's `actual_duration_s`** — so a Remotion scene fills any
beat length.

This does **not** replace the Manim `own` lane or the photographic-still lane. It is a
fourth vector lane beside `geo` / `c2v` / `raster`, chosen per beat.

## The operating contract (read this — it is the whole design)

### The loop, per slate beat
1. **Motion-graphic, or leave it a photo?** Some slates are genuinely photographic
   plates (a face, an archival photo) where a motion graphic is the wrong answer.
   The matcher's first decision is allowed to be *"leave it a slate."* Keep the media
   economy honest — do not turn every plate into generic kinetic filler.
2. **What is the beat teaching (`scene_type`)?** Derive the pedagogical move from the
   beat's `narration_text` + `new_visual_element` using the decision tree in
   `../../remotion/_bench/SCENE-SELECTION.md`. Record it as `shot.scene_type`.
3. **Do any candidates fit — without forcing?** Look up `scene_type` in
   `../../remotion/_bench/index.json` → ranked candidate patterns. A candidate *fits*
   if its form matches the scene_type AND the beat's content drops into its props
   cleanly. It does **not** fit the moment you would be fighting it (hacking internals,
   overriding its motion, forcing content it was not built to hold).
4. **Reuse if it fits; build if it doesn't.**
   - **Fits** → adapt lightly: inject the beat's content into the pattern's props,
     confirm it is palette-locked to the vox tokens, set nothing about duration (the
     compiler conforms it). Render.
   - **Doesn't fit** → author a new scene, **specific** (fastest path to a working
     reel — do not pay the generalization tax yet). Render. It ships reel-local.
5. **Render → `media/<BID>.mp4`**, and **stamp provenance** on the beat (below).

### The two gates (shipping ≠ promoting)
- **Machine gate ("check it")** — does it render, pass Gate A/B layout QC, fill the
  beat. Decides whether it goes in *this* video. Same gates the Manim scenes run.
- **Human gate ("vet it") — Bear only.** Is this pattern general and on-brand enough
  to earn a permanent slot in the bench. A scene can pass the machine gate (ships) and
  fail the human gate (too specific → stays reel-local, never promoted). Most bespoke
  concept-carriers die reel-local; only the recurring ones are worth promoting. **The
  library only ever changes — add, rewrite, retire — through Bear's gate.**

### Promotion discipline: promote patterns, not instances
A scene built for beat B04 of one video is *specific*. Before it enters the bench it
must be **generalized**: pull the specifics into props, lock to the palette tokens, tag
it with a `scene_type`. Generalize **at promotion time, not build time**. Promotion
arrives as a **review card**: the generalized component rendered at 2–3 different prop
values (proof it is really parameterized, not a disguised one-off) + proposed
`scene_type`. Bear vets the card in a ten-second look. On approval it moves into the
vox-remotion project's `src/scenes/` and gets an `index.json` row.

### Review → triage (the `change <reel>: …` conversation)
The review cut burns the **beat id + status + timecode** on every beat (`--review`),
so a screenshot names the beat directly (timecode → beat via cumulative durations is
the fallback). From the beat, the **provenance stamp** names the pattern. Then triage
by **blast radius**, asking one question: *would this bug show up in every use of the
pattern, or only this one?*
- **Injected content** (wrong number/label/color mapping/timing for this beat) →
  **instance fix**: edit `shot.remotion.props`, re-render only that beat.
- **The pattern itself** (reads wrong, collides at any input, off-brand as built,
  teaches poorly) → **pattern issue**. Before touching a shared pattern, surface its
  **consumers** (`_bench/consumers.json`): "used by N beats across M videos; changing
  it re-renders all of them." Then choose four-way: local adjustment · **fork a
  variant** (the pattern isn't wrong, it just doesn't fit this case — make a sibling,
  don't mutate the shared one) · rewrite the pattern · retire it. A rewrite/retire is a
  gated event — it re-enters Bear's vet and re-renders the named consumers.

## Beat-sheet schema additions

Two new pieces on a beat's `shot`:

```jsonc
"shot": {
  "type": "GRAPHIC", "source": "own", "motion": "…",
  "scene_type": "data-chart",          // NEW: the pedagogical move (index.json key)
  "remotion": {                         // NEW: present when this beat is a remotion lane
    "pattern": "BarChart",             // Composition id in the vox-remotion project
    "provenance": "onda/BarChart",     // where the pattern came from, or "reel-local"
    "version": "1",
    "props": { "title": "…", "data": [ … ], "accentIndex": 3 },  // injected content
    "rendered": {                       // stamped by the driver after a successful render
      "out": "media/B04.mp4", "frames": 180, "at": "<iso8601 passed in>"
    }
  }
}
```

`_bench/consumers.json` — the reverse index the triage reads/writes:
```jsonc
{ "BarChart": [ { "video": "vox-comma-orphan", "beat": "B04" }, … ] }
```

## Commands (driver: `scripts/vox_remotion.py`)

```bash
# what would be filled? (slate beats that carry a shot.remotion.pattern)
python3 scripts/vox_remotion.py <REEL> --list
# render all remotion slate beats → media/<BID>.mp4, stamp provenance + consumers
python3 scripts/vox_remotion.py <REEL>
# just one beat (instance fix after a change)
python3 scripts/vox_remotion.py <REEL> --only B04
# then the normal machine pass picks the mp4s up:
bash scripts/vox_run.sh <REEL>
```

The driver renders each beat's `shot.remotion.pattern` composition from the vox-remotion
project (`aspects/remotion-pass/remotion/`), passing `shot.remotion.props` as
`--props`. Browser: on the Mac, Remotion's default works. In a constrained/allowlisted
environment set `VOX_CHROME` (a chrome/headless-shell binary) and
`VOX_CHROME_MODE=chrome-for-testing` — the proven container invocation.

## The vox-remotion project (`aspects/remotion-pass/remotion/`)

A standard Remotion project. `src/tokens/vox.ts` is the single palette/motion token
source (cream/ink/teal/crimson/slate/gold + the house `SPRING_SMOOTH`) — the one place
the whole bench retints. Every scene is a `Composition` in `src/Root.tsx` with a Zod
`schema` and `defaultProps`, and reads its timing off `useCurrentFrame()` /
`durationInFrames` so it fills any beat length. `src/scenes/BarChart.tsx` is the first
proven, palette-locked scene — copy its shape.

Setup (once, on the Mac): `cd aspects/remotion-pass/remotion && npm install`. Load the
bundled Montserrat / EB Garamond / PT Mono so the family names in `tokens/vox.ts`
resolve (else Remotion substitutes system faces).

The 367-keeper bench under `../../remotion/_bench/` is the **quarry**; a scene is a
trusted starter only once it renders here at the vox palette. The project's
`src/scenes/` is the **proven core** — it grows by promotion, never by bulk import.

## Next phase — Remotion-only outros (spec)

Outros move from the green-screen mascot clips (`vox_outro.py`) to **two Remotion
compositions**, each picking an "interesting" template (this is where the polished-but-
decorative bench keepers — kinetic type, particles, reveals — earn their place; a
rotating pool per book keeps it fresh):
- **`OutroSeries`** — a bear description of the series. Content from the book's
  `ABOUT.MD` (`books/<book>/ABOUT.MD`, two levels up from the reel).
- **`OutroCTA`** — the like/comment/subscribe blurb. Content from the book's
  `AUTHOR.MD`.
`ABOUT.MD` + `AUTHOR.MD` exist for all 96 book folders with a `chapters/`. The driver
gains `--outro`: read the book's two files, assemble props, render `OutroSeries` +
`OutroCTA` to the reel's outro slots. Implement after the core body-slate loop is in
use.
