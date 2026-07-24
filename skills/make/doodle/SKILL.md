---
name: doodle
description: >
  SVG-library doodle animation — rough.js hand-drawn icons from the
  organized-svg library (524 icons, 10 categories), rendered as Remotion
  beats. Two modes: build a FULL doodle explainer reel, or fill individual
  doodle beats inside any other explainer's beat sheet (explainer,
  ai-explainer, cli-explainer, …). Use when the user types `doodle`,
  `doodle beat`, `doodle reel`, `doodle chart`, asks for a hand-drawn /
  sketchy / roughViz-style icon or chart beat, or wants the organized-svg
  library animated. Sketchy bar/line/pie charts included (DoodleChart).
  Audio-first, phase-gated, Kokoro default. Never publishes.
---

# doodle — the organized-svg doodle grammar

You are animating **Bear's doodle icon library** — `doodles/svg/`
(bugs · business · everyday · food · medical · nostalgia · school · shapes ·
social-media · space) — into hand-drawn Remotion beats. rough.js re-draws each
potrace icon as sketchy outline + pencil hachure; @remotion/paths reveals it
stroke by stroke; captions are hand-lettered (Shadows Into Light). A sketchy
chart type (bar / line / pie) covers quantitative doodle beats.

**How this differs from `sketch-explainer`:** that skill's master is Manim
line-art (MinutePhysics register) with icons as optional overlays. Here the
**doodle beats ARE the master visual** — rendered by the standard Remotion
slate path (`remotion_scenes.py` → `media/<BID>.mp4` → `compile.py`), so a
doodle beat drops into ANY reel without schema changes. Use sketch-explainer
when the concept needs precise math drawn in Manim; use doodle when the
teaching rides on icon vocabulary, everyday objects, or a sketchy chart.

## The two modes

**Mode 1 — full doodle reel.** A complete explainer where every beat is a
DoodleScene/DoodleChart (bookend title/outro cards included — they are
DoodleScenes with caption only). Flow below.

**Mode 2 — doodle beats in another reel.** Any beat sheet, any skill: author a
`doodle` block on the beats that want the look, run `doodle_fill.py`, render
via `remotion_scenes.py` as usual. The host reel's compile picks up
`media/<BID>.mp4` like any other filled slot. Nothing else in the host
pipeline changes.

## Read before acting

- `reference/style.md` — the doodle visual constitution (tuning values, the
  fixed-seed law, accent grammar, chart grammar). **Read first, every time.**
- `runtime/schema/beat_sheet.schema.json` — the beat-sheet contract.
- Component prop schemas (standing rule #4 — props must match the zod
  schema exactly): `runtime/remotion/src/scenes/DoodleScene.tsx`,
  `runtime/remotion/src/scenes/DoodleChart.tsx`.

## The non-negotiables

1. **Audio first.** Generate narration (Kokoro default — free; ElevenLabs
   only via explicit gate) and measure it BEFORE `doodle_fill.py` — the fill
   step copies `actual_duration_s` into each beat's `props.durationS`.
2. **Fixed seed.** Never randomize rough.js seeds per render; the seed is a
   beat-sheet value (default 42). Re-roughening per frame = flicker.
3. **One accent.** Teardown grammar: at most ONE red element per beat (the
   thing under scrutiny). `doodle_fill.py` enforces it; don't fight it.
4. **Never force a match — the three-tier rule.** Each icon request
   resolves in order: (1) the SVG library `doodles/svg/` (preferred —
   roughened + draw-on); (2) the PNG tier (pasted-in look: multiply blend,
   slight tilt, popin — no draw-on) — the fallback library `doodles/png/`
   AND the generated-still stock at `<library>/images/` (~1,500 PNGs,
   indexed by `build_index.py` alongside the icons); (3) neither → the
   beat stays a slate, a `MISSING:` line prints, and a request card is
   appended to the reel's `SHOPPING.md` ("doodle needed for X", with the
   target filename for both tiers). Drop the asset in, re-run
   `build_index.py` + `doodle_fill.py --only <BID>`. No "close enough"
   icons, ever — a token hit on an `images/` still is a LEAD: LOOK at the
   png before letting it stand; if it's wrong, delete the block and card it.
5. **Render only via `runtime/scripts/remotion_scenes.py <reel>`**
   (standing rule #3 — foreground, `--concurrency=1`). Verify by LOOKING at
   a frame + `qc-sheet.png` (standing rule #2).

## Commands

### `doodle index` — (re)build the library manifest
```bash
python3 skills/make/doodle/scripts/build_index.py
```
Writes `doodles/svg/icons.json` (id, category, tokens per icon) covering the
SVG categories, `doodles/png/`, and the `<library>/images/` still stock.
Re-run after adding or renaming icons or images. Deterministic.

### `doodle reel [concept | chapter path]` — Mode 1, full explainer
1. Hand the source to **script-writer** for the narration script +
   `beat_sheet.json` skeleton (one sentence = one beat). Gate: script
   approval. The reel folder lives in `<book>/youtube/<slug>/` per the
   ownership rule.
2. On each beat, author the `doodle` block (see below): icon terms from the
   beat's one new visual element; caption = the beat's key phrase, not the
   whole narration. Bookends: caption-only DoodleScenes.
3. Gate: beat-sheet approval. Then audio:
   `python3 runtime/scripts/generate_audio_kokoro.py <reel>` (or the reel's
   configured engine) — measured durations land in the sheet.
4. `python3 skills/make/doodle/scripts/doodle_fill.py <reel>`
5. `python3 runtime/scripts/remotion_scenes.py <reel>`
6. `./art run <reel>` → review cut + `qc-sheet.png`; LOOK at it. Fix, then
   `./art final <reel>`.

### `doodle beats <reel> [B04 ...]` — Mode 2, beats in a host reel
Author `doodle` blocks on just those beats, then steps 4–6 above (audio for
the host reel is presumed already generated — if not, audio first, always).

### `doodle chart` — a single quantitative doodle beat
Same as Mode 2 with a `chart` block instead of `icons`. Chart grammar in
`reference/style.md`: red marks the datum under scrutiny (`accentIndex`),
hachure ANGLE (never hue) separates series, grayscale-safe by construction.

### `doodle status <reel>`
`python3 skills/make/doodle/scripts/doodle_fill.py <reel> --list`

## The `doodle` block (authored per beat in beat_sheet.json)

```json
{
  "beat_id": "B04",
  "narration_text": "…",
  "shot": {"type": "REMOTION", "source": "own"},
  "doodle": {
    "icons": [
      {"terms": "anatomical heart", "label": "the heart", "accent": true,
       "xPct": 50, "yPct": 44, "widthPct": 24, "mode": "drawon"}
    ],
    "caption": "your heart is a pump",
    "eyebrow": "",
    "title": ""
  }
}
```

Caption/title-only pages (act cards, outros) are valid: omit `icons` and set
`title` (big center headline) and/or `caption`.

Chart beat: replace `icons` with
`"chart": {"kind": "bar", "title": "…", "unit": "%", "accentIndex": 2,
"data": [{"label": "A", "value": 12}]}`.

Layout guidance: 1 icon → center (50/44, width 22–26). 2 icons → 32/68.
3 icons → 22/50/78, width ~16. Keep labels ≤3 words. `mode: "popin"` for
quick secondary icons; `drawon` for the beat's subject.

## Costs

Kokoro narration is free/local (the default). rough.js/Remotion rendering is
free/local. ElevenLabs narration is PAID — only via the explicit spend gate
(`./art keys` first, approval before generation). No Higgsfield/gen-AI in
this skill at all.

## Provenance

Vendored: `runtime/remotion/src/vendor/rough.esm.js` (roughjs 4.6.6, MIT —
LICENSE alongside). Handwriting face: Shadows Into Light (OFL) —
`runtime/remotion/public/fonts/` (woff2, loaded by the scenes) +
`runtime/fonts/Shadows_Into_Light/` (TTF, install like the other bundled
families for Manim parity). roughViz was evaluated and deliberately NOT
used: D3-v5-locked, charts-only, unmaintained; its scale+rough wiring is
reimplemented dependency-free in DoodleChart.
