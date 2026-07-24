# SHOPPING.md — claude-liam-context-dreaming
## Gate D2 — written 2026-07-22 after audio lock

Six plates for eight VOX beats. All **Tier 1** (generic/illustrative — generate
or stock, no real-world referents, no real people). Every motion asset requests
MORE than the locked window so conform trims, never stretches.

---

### ACT II — "The Archive"

```
├─ pantry/R1.png                                    [VOX · kenburns run · B09+B10]
│    tier: 1 (generic — library / data-archive / filing aesthetic)
│    need: ≥1800px wide (kenburns headroom; planned push-in to 1.5×; focus
│          [0.5, 0.45] for B09, [0.52, 0.5] for B10)
│    description: rows of organised documents, data stacks, or card-catalog
│          aesthetic. Calm, institutional tone. No real-world institution,
│          no signage, no people.
│    sourcing: AI-generate (suggested prompt below) or stock
│    suggested prompt: "Rows of filing drawers or stacked data cards,
│          top-down or slight 3/4 angle, clean institutional lighting,
│          desaturated palette (will be further desaturated in treatment),
│          no text, no people, photorealistic"
│    beat window: B09 locked 13.55s, B10 locked 12.57s
│          → request as ONE plate; vox run shares a single image
│
├─ pantry/B12.png                                   [VOX · hold · single]
│    tier: 1 (generic — two isolated data nodes with clear space between)
│    need: ≥1600px wide. Two clearly separate objects/nodes in an abstract
│          plane with obvious negative space between them (the 'gap'). No
│          connecting lines. Clean margin on both sides.
│    description: abstract: two spheres, points, or node-shapes separated
│          by open space. Will have terracotta question mark drawn on by
│          annotation layer.
│    sourcing: AI-generate
│    suggested prompt: "Two small spheres or circles on a light neutral
│          background, wide apart, no connections between them, deep focus,
│          clean, minimal, photorealistic"
│    beat window: B12 locked 14.61s (hold motion — still image)
│
├─ pantry/B16.png                                   [VOX · kenburns · single]
│    tier: 1 (generic — two-sided imagery: organised/declarative vs
│          enacted/procedural)
│    need: ≥1800px wide; kenburns ease-in toward centre. Clear visual split
│          between left and right halves (or top/bottom). One side neat and
│          tabular; other side gestural or fluid.
│    description: diptych feel: on the left, organised cards/documents; on
│          the right, hands working, flowing movement, or enacted process.
│          No text, no people's faces.
│    sourcing: AI-generate
│    suggested prompt: "Split composition: left side neat stacked papers
│          or indexed cards; right side fluid abstract brush strokes or
│          flowing water. No text. Clean neutral tones. Photorealistic."
│    beat window: B16 locked 13.78s
```

---

### ACT IV — "The Mechanism"

```
├─ pantry/B28.png                                   [VOX · kenburns · single]
│    tier: 1 (generic — dual-axis scatter or 2×2 plane)
│    need: ≥1800px wide; kenburns from edges inward. Visible axis structure
│          with points that clearly differ on two dimensions. Enough margin
│          space for terracotta P and C labels at the axis edges.
│    description: scatter plot or 2×2 matrix aesthetic — abstract data
│          points distributed across a plane. Some cluster in a 'passing'
│          zone, others outside it. No real data, no labels pre-existing on
│          the image.
│    sourcing: AI-generate
│    suggested prompt: "Abstract scatter plot on a light background, data
│          points distributed across two axes, some clustered in one
│          quadrant, minimal style, no labels, photorealistic"
│    beat window: B28 locked 13.95s
│
├─ pantry/R2.png                                    [VOX · kenburns run · B30+B31]
│    tier: 1 (generic — layered/tiered storage, hot/warm/cold depth)
│    need: ≥1800px wide; kenburns ease-in for B30, continue for B31 to
│          1.5×. Vertical layering clearly readable: distinct bands from
│          warm/bright at top to cool/dark at bottom. Enough vertical
│          resolution for two different focus crops.
│    description: layered geological or data-stack cross-section — warm
│          orange tones at top (hot), neutral midtone in middle (warm),
│          cool blue-grey at bottom (cold). Abstract, no hardware, no UI.
│          No text.
│    sourcing: AI-generate
│    suggested prompt: "Cross-section of layered geological strata or
│          abstract data layers: top layer warm amber/ochre, middle layer
│          neutral grey, bottom layer cool slate-blue. Clean transitions.
│          Photorealistic, no text, no people."
│    beat window: B30 locked 14.36s, B31 locked 16.30s
│          → request as ONE plate; vox run shares a single image
│
└─ pantry/B33.png                                   [VOX · annotate/draw-on · single]
     tier: 1 (generic — two-column abstract representation)
     *** CRITICAL: clean margin space on BOTH sides for draw-on brackets ***
     need: ≥1800px wide. Left half: abstract numerical / vector pattern
           (rows of small numbers, dots, matrix cells). Right half: abstract
           text-label pattern (word-sized blocks, lines of readable-weight
           text placeholders). Columns must be visually distinct and
           separated by clear vertical space — enough for a terracotta
           bracket annotation on each column without overlapping content.
           NO pre-existing column labels ("RAD", "DEG", or any text) on the
           plate — the annotation layer writes those.
     description: split two-column data representation — numerical/vector
           on the left, language/label on the right. Think: a spreadsheet
           or notebook open to two distinct column types.
     sourcing: AI-generate
     suggested prompt: "Two-column view: left column shows rows of small
           numbers and decimal values (vector/matrix style); right column
           shows short text word-tokens or label rows. Columns separated
           by clear white space. Clean, minimal, top-down view, no labels
           or headers, photorealistic."
     beat window: B33 locked 13.87s (hold then draw-on)
```

---

## Sourcing checklist

- [ ] R1.png — drop to `pantry/R1.png`
- [ ] B12.png — drop to `pantry/B12.png`
- [ ] B16.png — drop to `pantry/B16.png`
- [ ] B28.png — drop to `pantry/B28.png`
- [ ] R2.png — drop to `pantry/R2.png`
- [ ] B33.png — drop to `pantry/B33.png` ← critical margins

Once all six files are in `pantry/`, rerun `./art run youtube/claude-liam-context-dreaming`.
Only changed slots recompile.

To ship the review cut before all plates arrive, Bear explicitly approves
"ship with slates" in BUILD-LOG.md — the pipeline will hold VOX beats as
labelled slates.
