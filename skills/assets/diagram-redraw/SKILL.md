---
name: diagram-redraw
description: >-
  Mine a facts/<topic> Wikipedia knowledge slice for figures worth redrawing, and
  render them in the book's house style into an images subfolder. Use when the user
  types `figure-harvest`, asks to harvest/redraw diagrams from the facts data, to find
  "doable and useful images" for a book, or to turn a topic's Wikipedia media into
  house-style figures. The usefulness signal is editorial: a Wikipedia editor chose to
  include the image. Keeps redrawable concept figures (diagrams, charts, schematics);
  drops logos (trademark) and photographs (not redrawable as diagrams). Never copies a
  source image — redraws fresh. Pairs with the cajal SVG style guide.
---

# Figure Harvest

Turn a topic's Wikipedia media references into a curated set of **house-style figures**.

## The idea

Every image on a Wikipedia page is there because a human editor decided it earned its place.
That editorial judgment is a usefulness signal we can harvest. But the *expression* (the
specific drawing or photo) is copyrighted or trademarked — only the **idea** is free. So:

- **Concept diagrams / charts / schematics** → redraw fresh in the book's house style. (A Bohr-model diagram, a free-body diagram, a supply–demand curve — the idea is standard; the drawing is ours.)
- **Logos / wordmarks / seals** → skip. Trademarked; the mark *is* the protected thing.
- **Photographs** → skip. You can't redraw a photo as a diagram, and the photo is copyrighted.

Why it matters: the doable fraction flips entirely by subject. Mathematics ≈ 40% doable
diagrams; physics, chemistry, biology are diagram-rich; branding and marketing are mostly
logos and product photos (≈ 8%). The skill finds the signal wherever it lives.

## Inputs

- `facts/<topic>/terms.json` — media references: `{file, type, strategy, commons_url}` per term.
- `facts/<topic>/graph.json` — concept link graph; `in_degree` = how foundational a concept is.
- Optional target book: `books/<slug>/` with `chapters/` (for relevance filtering) and a house
  style authority (`brutalist/DESIGN.md` + the cajal `svg-style.md`).

## Output

- `figure-harvest/out/<topic>-figures.{json,md}` — ranked, classified candidate plan.
- `books/<slug>/images/harvested/` — redrawn SVG + PNG figures in house style, one per selected concept.
- A short log of what was drawn and what each figure references.

---

## Pipeline

### Stage 1 — Classify & rank (deterministic, no AI)

```
node figure-harvest/harvest.mjs --topic <topic> [--book books/<slug>] [--top 60]
```

Classifies every media ref into doable / logo / photo / other, dedupes, and ranks the doable
set by foundational-ness (graph `in_degree`) — with `--book`, concepts that appear in the book
float to the top. Writes the candidate plan. Read the `.md` to curate.

### Stage 2 — Select (human or book-scoped)

Pick the figures to draw. Two modes:
- **Book-scoped (preferred):** keep candidates relevant to the target book's chapters/terms — these are the *useful* ones for *this* book.
- **Top-N foundational:** the most-linked concepts in the topic, for a book still being outlined.

Drop anything already covered by an existing figure. Aim for figures the chapter actually needs — the greyscale-first discipline applies: a figure with no job doesn't get drawn.

### Stage 3 — Redraw in house style (AI, parallelizable)

For each selected concept, draw a **fresh** figure that teaches the same idea, conforming to
the book's `brutalist/DESIGN.md` + cajal `svg-style.md`:
- White canvas, `#F5F5F5` plot region, ink `#121212`, hairlines `#D4D4D4`, neutral grays.
- **Greyscale-first:** structure in greyscale; add the red `#C8102E` accent only on the one
  element the reader must look at first; most figures use no red.
- EB Garamond titles / Inter labels / JetBrains Mono numerics; `role="img"` + `<title>`/`<desc>`.
- Use the Commons image **only as a reference** for what the concept looks like. Never trace,
  embed, or copy it. Redraw from the idea.
- Save to `books/<slug>/images/harvested/<concept-slug>.svg`, then convert to PNG (sharp).

---

## Rules

- **Never copy a source image.** Redraw the idea in house style. Don't download/embed the Commons file.
- **Skip logos and photos** — always. They are the protected expression, not a teachable diagram.
- **Useful = the book needs it.** The editorial signal gets a concept onto the candidate list;
  relevance to the target book decides whether it's drawn.
- **Cite the concept, not the picture.** If a figure restates a sourced fact, cite the fact;
  never imply the figure is the Wikipedia image.

## Caveats (observed)

- The book-relevance matcher is literal (concept term must appear in chapter text); it under-counts
  paraphrased concepts. Treat a 0 as "check by hand," not "nothing relevant."
- A few edge cases leak through classification (journal marks, montage figures). Stage 2 curation catches them.
- High `in_degree` ranks general concepts (e.g. "Quantum mechanics") above specific drawable ones;
  when picking, prefer concepts that map to a single clean diagram.
