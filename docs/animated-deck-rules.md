# Animated Lecture Deck — the REAL rules: VISUALIZE · SYNC · FOCUS

> Supersedes `lecture-deck-rules.md`, which documented the STRIPPED static renderer
> (`build_deck.py`). This file documents the system that actually animates, syncs to
> audio, and moves focus with the voice — reverse-engineered from a working deck.

## Where the truth lives (NOT in build_deck.py)
- **Working decks (the engine):** `brutalist_art/public/talks/library/Living-Models/lectures/*/deck.html`
  — self-contained, minified. Canvas/SVG `draw()` + `requestAnimationFrame`, audio
  `currentTime` sync, `.ih` / `.idea-active` focus.
- **The per-slide source spec + timing sidecars:** in a lecture folder —
  `anim.json`, `align.json`, `resolved-anchors.json` (see `cancer-nanomedicine/lectures/ch01-lecture/`).
- **build_deck.py (all 33 forks):** renders ONLY the static component slides, and even
  drops the idea anchors. No pattern library, no alignment, no resolve, no focus. This
  is the stripped copy. It is why "medhavy" was just a recolored dead deck.

## The system = 3 layers on the same component vocabulary (wire / stat / flow / grid / pan / thesis)

### Layer 1 — VISUALIZE  (`anim.json`, keyed per slide S03, S04, …)
A slide that should animate carries:
```
"S03": {
  "version": 2,
  "pattern": "scaleComparison",          // a NAMED animation from the library
  "meta": "// SLIDE 03 — WHAT A NANOPARTICLE IS",
  "data": { axis:{min,max,unit}, band:{from,to,label}, items:[ … ] },  // the slide's REAL numbers
  "anchors": { axis_done:{phrase:"…"}, items_start:{phrase:"…"}, items_end:{phrase:"…"} },
  "signals": { axis_draw:{ramp:…}, band_in:{ramp:…}, items_go:{ramp:…} }
}
```
- **pattern** = one of a fixed LIBRARY. The FULL set, by real usage across every
  `anim.json` in the repo:
  - `calloutTour`   — **1101 uses (the workhorse)** — annotate a figure/diagram and
    TOUR its callouts in sync with the narration. This is the image-with-synced-
    annotations pattern the stripped renderer dropped; it is what figure-heavy science
    decks need. Nail this one and you have ~90% of the value.
  - `binaryBranch` (43), `divergentFates` (27), `scaleComparison` (14),
    `attritionChain` (11), `threshold` (8).
  - BUG: a few slides use `DivergentFates` / `BinaryBranch` (capitalized). The engine
    dispatches on lowercase names, so those render DEAD — fix casing during codify/QC.
- **data** = the concrete numbers/labels the animation draws (e.g. attritionChain:
  `total:1000, stages:[…], endClaim:"~0.7% at tumor"`).
- Renders as a **full-bleed animated SVG** (`.canim .asvg`, `position:absolute; inset:0`)
  that REPLACES the text body for that slide.
- **anchors** = named moments defined as a PHRASE from the narration.
- **signals** = how each element ramps in when its anchor fires.

A text-only (non-drawn) slide uses instead:
```
"S04": { "version":2, "type":"idea",
         "anchors": { b0:{phrase:"…"}, b1:{phrase:"…"}, b2:{phrase:"…"}, b3:{phrase:"…"} } }
```
— no drawing, just idea-by-idea focus (Layer 3).

### Layer 2 — SYNC  (`align.json` → `resolved-anchors.json`)
1. Generate per-slide audio.
2. Forced-align (whisper) → **align.json**, per slide:
   `{ "words": [[word, t_seconds], …], "starts": [sentence_start_times] }`.
3. Resolve every anchor PHRASE against the word timings → **resolved-anchors.json**,
   per slide: `{ anchorName: fractionOfSlide }` — e.g.
   `"S03": { axis_done:0.1877, items_start:0.2368, items_end:0.4154 }`.
4. The deck reads the slide audio's `currentTime`; when it crosses a resolved anchor,
   that anchor's signal fires. **Visuals land ON the words.**

### Layer 3 — FOCUS  (`.ih` / `.idea-active`)
- The slide container gets class `.ih` (idea-highlight) → **every component dims to
  muted** by default (`.ih .wire b`, `.ih .stat .big`, `.ih .flow .chip`,
  `.ih .cell-part`, `.ih .pan`, `.ih .lead`, `.ih .thesis b` … all muted).
- As `currentTime` crosses each idea's resolved anchor (`b0, b1, …`, or a pattern's
  `items_go`), that component gets `.idea-active` → snaps to full `--fg` color while
  its siblings stay dim.
- Net effect: the on-screen element being spoken is LIT; the rest recede. Focus
  tracks the voice, phrase by phrase.

## The actual build pipeline (what a real deck run does)
1. **Author** each slide: component `body_html` (build_deck vocabulary) **+** an
   `anim.json` entry — a `pattern`+`data` for concept slides, or `type:"idea"` with
   idea anchors for text slides. Anchors are written as NARRATION PHRASES.
2. **Audio**: generate per-slide mp3 (Kokoro af_kore = Medhavy, or ElevenLabs).
3. **Align**: whisper forced-alignment → `align.json` (word → time).
4. **Resolve**: match each anchor phrase to its word time → `resolved-anchors.json`
   (anchor → fraction of slide).
5. **Emit**: the deck with the animation ENGINE (a `draw()` per pattern, a
   `requestAnimationFrame` + `currentTime` loop that fires signals and toggles
   `.idea-active`) and audio inlined.

## Why the current pipeline is broken
`build_deck.py` performs a stripped Step 1 render and NONE of Steps 2–5. So every
deck it makes is static colored boxes that neither move nor track the voice. The
palette (medhavy/brutalist/…) only recolors that dead output. Consolidating the 33
forks fixes drift but still leaves you with the wrong engine.

## The fix (this should be ONE skill, and isn't)
Capture this as a canonical builder in brutalist-art — e.g. `skills/make/animated-deck`
(or fold into `lecture`):
1. **Extract the full pattern library** from the working deck engine (JS) into a
   documented set of named patterns, each with its `data` schema + `draw()` + `signals`.
2. **Ship the align + resolve steps** (whisper → align.json → resolved-anchors.json).
3. **Ship the engine template** (draw dispatch + currentTime loop + `.ih`/`.idea-active`).
4. Point every lecture folder at it; retire `build_deck.py` (the stripped renderer) or
   demote it to "static preview only."
Until that exists, any "deck" build that goes through `build_deck.py` is the corpse,
not the system.
