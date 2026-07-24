# doodle — visual constitution

The doodle look is **ink on white paper**: the teardown palette
(`runtime/design/DESIGN.md`) drawn by hand. White ground (`#FFFFFF`), warm
near-black ink (`#2A1A0E`), structure gray (`#545454`), and ONE red
(`#C8102E`) for the single element under scrutiny. Paper grain sits on top
(procedural feTurbulence, static — paper does not boil).

## Type

Everything hand-lettered: **Shadows Into Light** for titles, captions,
labels, and chart numbers. This is a deliberate, documented exception to the
four-font law — inside a doodle beat the hand IS the brand; Montserrat/PT
Mono would break the fiction. The moment a beat needs typeset text (a quote
card, a code block), it is not a doodle beat — route it to the host reel's
normal patterns.

Fallback chain (until the font is installed / loaded): Bradley Hand → Comic
Sans MS → cursive. The scenes load the bundled woff2 via FontFace, so
renders are correct even on a machine with no fonts installed.

## The fixed-seed law

rough.js randomness is seeded **per shape, from the beat sheet** (default
42; `doodle.seed` to taste). The seed is part of the artwork: re-rolling it
per frame or per render produces wobble-flicker ("boiling"), which reads as
broken, not hand-made. Geometry is roughened ONCE per shape per render
process and cached (`doodle/roughen.ts`); ~100–200ms per 2000-unit potrace
icon, measured.

## Icon tuning (2000×2000 potrace library)

Values in `DOODLE_DEFAULTS` (`doodle/roughen.ts`), tuned visually on
medical-heart / medical-virus / space icons:

| knob | value | why |
|---|---|---|
| roughness | 4 | visible wobble at 2000-unit scale (1–2 reads as clean vector) |
| bowing | 2 | slight line sag, like fast marker strokes |
| strokeWidth | 14 | ≈3px at typical on-screen icon size |
| hachureGap | 55 | open pencil shading, not a solid fill |
| fillWeight | 7 | hachure strokes at half the outline weight |
| simplification | 0.6 | potrace paths carry far more nodes than a hand needs |

The library's shapes are potrace FILLS (the drawn linework is itself the
filled region), so hachure-shading those regions + a sketchy outline reads
as pencil-over-ink. Don't switch to `fillStyle: solid` — that's just the
original icon with wobble.

## Motion

- `drawon` (default, the beat's subject): contours reveal sequentially via
  evolvePath — one line at a time, ~1.4s, ease-out; hachure shading fades in
  as the contour finishes (a hand shades after it outlines).
- `popin` (secondary icons): the house `SPRING_SMOOTH` — no overshoot
  circus; one focal moment per beat.
- Auto-stagger when `delayS` is unset: item i starts at i × ~1.3s.
- Captions fade at 0.4s; the red rough underline draws on after.

## PNG items (tier 2)

A PNG from `doodles/png/` renders **pasted into the sketchbook**: multiply
blend (white backgrounds melt into the paper), `grayscale(0.85)` so it sits
with the ink, a deterministic ±2° tilt (from the item index — a hand never
pastes straight), spring pop-in. No draw-on — a PNG has no paths to trace,
and `doodle_fill.py` demotes `drawon` to `popin` automatically. Best source
material: scanned hand doodles, stamps, single-subject images on white.
Busy photographs will read as collage, not doodle — prefer commissioning the
SVG (the SHOPPING.md card asks for exactly that first).

## Accent grammar (teardown, enforced)

At most ONE red element per beat: `accent: true` on one icon, or
`accentIndex` on one datum. Red = the thing under scrutiny. Everything else
is ink. `doodle_fill.py` demotes extra accents and says so.

## Chart grammar

- Series/slices are separated by **hachure angle** (24–32° steps), never by
  hue — every chart must survive grayscale (squint test: can you still find
  the accent and tell slices apart? The labels must carry it).
- Red follows the accent law: `accentIndex` marks the datum the narration
  is scrutinizing; -1 when the beat makes no such claim.
- 3+ genuinely categorical series that each need their own color = not a
  doodle chart; route to the host reel's Manim/Okabe-Ito data-viz patterns
  (`DESIGN.md` data-viz laws).
- Axes are SLATE, drawn on first (0.6s), before any data appears —
  the paper is ruled before the hand plots.
- yMax auto-rounds to a "nice" ceiling; set `yMax` explicitly when two
  chart beats in one reel must share a scale (never let the axis re-scale
  between consecutive beats making the same comparison).

## Layout defaults

16:9 (1920×1080) is the authored frame. Single icon: 50/44 @ 22–26% width
(caption zone reserves the bottom ~18%). Two: xPct 32/68. Three: 22/50/78 @
~16%. Labels ≤3 words, else they wrap into the icon. Eyebrow top-left in
SLATE for act/section context — sparingly; a doodle page with three text
zones is a poster, not a doodle.

## What this skill refuses

- Multi-color icon fills (the library is monochrome by design; accent is
  state, not decoration).
- Per-frame re-roughening ("make it wiggle like it's alive") — that's the
  boil effect; if a future variant wants it, it must be a NEW quantized-time
  mode (re-seed at 4fps max), gated behind its own reference note, never the
  default.
- Forcing an icon match. `MISSING:` + a slate beats a wrong doodle.
