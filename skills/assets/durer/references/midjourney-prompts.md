# Midjourney prompt-set — SVG-friendly line art

Goal: generate art that **traces cleanly** (or is easy to recreate from primitives). The tracer
and the gate do the judging; these prompts just stack the odds. The single biggest lever:
**solid, thick, flat black on pure white — no shading, no gradient, no color, no texture.**

## Universal modifiers (append to any subject)

```
flat vector icon, solid black on pure white background, thick uniform outline,
bold filled shapes, high contrast, centered, single subject, no shading, no gradient,
no texture, no color, no background detail --style raw --s 50 --no color gray shadow gradient texture photo
```

## Templates

**Solid icon (traces best)**
```
minimalist flat icon of [SUBJECT], solid black silhouette with thick outline,
pure white background, no shading, no gradient, centered, vector style
--style raw --s 50 --ar 1:1 --no color gray shadow gradient texture
```

**Clean line drawing**
```
simple bold black line drawing of [SUBJECT], thick even stroke, coloring-book style,
white background, no shading, minimal detail, centered
--style raw --s 50 --ar 1:1 --no fill color gradient shadow texture
```

**Doodle / sticker**
```
hand-drawn doodle of [SUBJECT], thick black marker line, flat, sticker style,
white background, no shading, no color
--style raw --s 50 --ar 1:1 --no color gradient shadow
```

## Rules that decide whether it converts

- **Thick beats thin.** A thin single-pixel outline under-traces and gets tossed. Ask for
  "thick", "bold", "solid". When in doubt, prefer a filled silhouette over an outline.
- **One subject, isolated, centered, white background.** Busy scenes blow past the complexity
  cap and get tossed.
- **No shading/gradient/color/texture.** Those become noisy multi-path traces.
- **Generate a few, upscale, then convert.** If `linework-to-svg.py` tosses it as "too complex",
  regenerate simpler; if "under-traced", regenerate thicker/filled.
- **Geometric subjects (charts, atoms, arrows, shapes)** → consider recreating from SVG
  primitives instead of MJ at all; it's cleaner and tiny.

## Licensing note

MJ output license depends on your plan/terms; and if you're recreating a *purchased* pack's
icon, simple symbols (atom, bar chart) generally aren't copyrightable but detailed designs can
be — check before shipping a derived set.
