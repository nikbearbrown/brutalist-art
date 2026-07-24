---
name: line-art-vectorizer
description: >
  Turn simple black-and-white line art into clean, gate-passing SVGs — and
  generate line art that converts well in the first place. Two halves: a
  Midjourney prompt-set for SVG-friendly art, and a tracer that tries each
  image and TOSSES anything too complex (or under-traced) rather than ship a
  messy vector. Use when asked to vectorize icons/line art, make an SVG icon
  set, convert PNGs to SVG, or generate clean b+w line art for
  figures/Remotion.
metadata:
  tags: svg, vectorize, line-art, icons, midjourney, trace, vtracer, assets
---

# Dürer

Named for Albrecht Dürer — the master engraver whose whole craft was clean black line on
white. This skill does two things, and you can use either half alone:

1. **Generate** SVG-friendly line art (a Midjourney prompt-set) — `references/midjourney-prompts.md`.
2. **Convert** that art (or any simple b+w line art) into clean, validated SVGs —
   `scripts/linework-to-svg.py`.

The governing rule, in AI1 terms: **it tries, and tosses what it can't do cleanly.** A bad
vector is worse than none. Simple art comes out clean; complex art is rejected with a reason,
not faked.

## The loop

```
Midjourney prompt-set  →  b+w line-art PNG  →  linework-to-svg.py  →  svg-format-audit  →  keep / toss
   (SVG-friendly art)         (your input)          (trace)            (the gate)        (toss-if-bad)
```

## Convert — `scripts/linework-to-svg.py`

```bash
pip install vtracer pillow      # once; no system libs needed
python scripts/linework-to-svg.py [png-dir-or-file] -o [out-dir]
```

What it does per image: flattens the art onto white (handles black-on-transparent exports —
otherwise the tracer sees "all black"), downscales, traces with vtracer (binary, spline,
`path_precision=2` so you don't get 15-decimal float bloat), injects a `viewBox`, then judges:

- **KEEP** — a clean trace in range.
- **toss · too complex** — output `> 40 KB` (a busy illustration, not an icon).
- **toss · under-traced** — output `< 800 B` (thin outlines that the tracer lost; thicken the
  source or recreate by hand).
- **toss · degenerate/empty** — the trace collapsed (e.g. just the canvas frame).

Every kept file passes `svg-format-audit.mjs` (viewBox, no raster, real paths). Run that gate
as the hard check after converting.

## Simplify (when a trace is too complex)

`--simplify auto` (the default) escalates: if a trace busts the size cap, durer retries with
progressively more blur + downscale + threshold (levels 1-3) and keeps the first that fits,
tagging the level used (e.g. `[simplify L2]`). Use `--simplify 0` to disable.

**Honest limit — simplify reduces detail, it does not redraw.** A genuinely artistic or colored
illustration (sketch/construction lines, shading, several colors, a detailed character) will not
become a clean icon: it either stays busy or collapses into blobs. durer is also **monochrome** —
colors are flattened to black/white. If the source isn't flat, thick, solid-black line art, fix it
**upstream** (the Midjourney prompt-set) or **recreate** the icon from primitives. Don't expect
simplify to manufacture simplicity that was never generated.

## What traces well vs not

- **Best:** solid/thick black shapes and bold filled icons (an atom, a bar chart, a silhouette).
- **OK:** clean medium-weight line drawings.
- **Tossed:** thin-outline doodles (under-trace), photos, gradients, fine detail, multi-tone art.

## The premium path: recreate from primitives

For *geometric* icons, recreating the SVG by hand beats tracing — by a lot. The atom is just
ellipses + circles; a bar chart is rects + axis lines. Hand-authored: **937 bytes, grouped,
animatable.** Traced: ~29 KB, one blob path. So: if the agent recognizes a simple geometric
subject, author it from `[ellipse]/[circle]/[rect]/[line]` (group logical parts in `[g]`,
ASCII-safe, with `[title]`); fall back to the tracer for organic line art; toss the rest.

## Output contract

Report: how many tried · kept · tossed (with the per-image reason); where the kept SVGs landed;
and whether each passed `svg-format-audit`. Never embed a raster inside an `[svg]` (the Madison
cover mistake) — that's a fake vector and the gate fails it.
