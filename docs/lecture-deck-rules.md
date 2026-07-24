# Lecture Decks — Visualization & Focus Rules

The rules `build_deck.py` enforces when it turns a `beat_sheet.json` into a
self-contained talking `deck.html`. These rules previously lived only in code;
this file is the written spec.

## Which build_deck.py is canonical
- **Current:** `cancer-medicine/*/ch01-lecture/build_deck.py` (2026-07-13, ~14 KB) —
  palette-aware, componentized, focus-disciplined. This is the one to copy forward.
- **Superseded:** the ~10 KB copies under `cancer-research/`, `cancer-nanomedicine/`,
  and `lecture_pipeline/` (2026-07-12/13).
- **Prior lineage (different look entirely):** bullet-and-figure decks — `ul.bul`
  bullet lists, `.body.split`, `.fig` image+caption, a `cover` slide. More text per
  slide, no accent-claim titles. If a deck looks like this, it predates the focus rules.

## What build_deck.py does
`beat_sheet.json → deck.html` (self-contained; audio inlined as base64). It reads
`segments`; each segment carries: `id`, `num`, `section`, `title` (accented parts),
`body_html`, and `beats[0].text` (the ONE narration line). `metadata.palette` and
`metadata.typography` select the CSS tokens and font.

---

## Visualization rules

1. **One accent hue, always.** Four palettes — `brutalist` (orange), `teardown`
   (VOX: white ground, warm ink, red), `humanitarians` (editorial), `medhavy`
   (Okabe-Ito) — each emits `:root` tokens (bg / fg / accent / muted / card /
   green / warn / font). Exactly one accent carries every highlight: the title's
   key term, the meta dot, the progress bar, `chip.on`, `callout`, the `thesis`
   rule. In `teardown`, green ≡ ink and warn ≡ accent — literally one hue. Never
   introduce a second highlight color.

2. **A fixed component vocabulary for slide bodies — NOT bullet walls.** `body_html`
   is built from these semantic components, each matched to an idea shape:
   - `lead` — one muted framing sentence.
   - `flow` / `chip` (+ `.arw` arrows; `chip.on` / `.dim` / `.warn`) — a process or sequence.
   - `phase` — labeled stages.
   - `stat-row` / `big` / `cap` / `eq` — magnitudes and numbers.
   - `grid2` / `grid3` + `cell-part` (`.hot` = emphasized) — parts, taxonomy, comparison.
   - `stack` / `wire` — labeled points on an accent left-rule.
   - `balance` (`.pan.surv` / `.pan.die` + `.fulcrum`) — a trade-off / two outcomes.
   - `callout` — one framed assertion.
   - `thesis` — the big claim, accent left-border.
   - `close` / `close-tags` / `sig` — the outro.

3. **Title carries the claim; body is centered.** `.stitle` is large (clamp
   26–46px, weight 800); its single most important word is wrapped in the accent
   span (`.o`). `.cbody` vertically centers a SMALL number of elements — never a
   scroll of text.

4. **Chrome + texture (fixed):** 5%-opacity dot-grid background, top progress bar,
   bottom nav dots, a `// SLIDE NN — SECTION` meta label, section footer + chapter
   number, sound toggle, per-slide inlined audio, `.sdark` dark-slide variant.
   16:9, 1280-wide viewport.

---

## Focus rules (what separates the current decks from the old bullet decks)

1. **One slide = one idea.** If a slide needs two ideas, split it.
2. **The title is a CLAIM, not a topic** — and its single key term is the accent.
   (Old decks titled "DNA Replication Process"; new decks assert.)
3. **One visual component per slide,** chosen to match the idea's *shape* — not bullets.
4. **Minimal on-slide words.** The component + the accented term carry the point;
   the prose lives in the narration, not on the slide.
5. **Exactly one narration beat per slide** (`beats[0].text`), held in the hidden
   NARRATION band (`.ccap { display:none }`) for the pipeline's audio + captions.
   The slide SHOWS; the voice EXPLAINS. Never read the slide aloud.
6. **Locate every slide** with the meta label + section footer + chapter number.

---

## The component-choice heuristic (idea shape → component)

| The idea is…                          | Use              |
|---------------------------------------|------------------|
| a sequence / process / pipeline       | `flow` + `chip`  |
| ordered stages                        | `phase`          |
| a number, rate, or magnitude          | `stat` / `big`   |
| parts of a whole / a taxonomy         | `grid2` / `grid3`|
| a comparison of a few items           | `grid` + `cell-part` |
| a labeled list of related points      | `wire` stack     |
| a trade-off / two outcomes            | `balance` pans   |
| the single load-bearing claim         | `thesis`         |
| one point that must not be missed     | `callout`        |
| the opening frame                     | `lead`           |
| the close                             | `close`          |

If an idea doesn't fit any component, that's usually a sign the slide is carrying
two ideas — split it (focus rule 1), don't invent a bullet list.

---

## Where these rules apply in the pipeline
`build_deck.py` is the **deck stage** of the lecture pipeline
(beat_sheet → deck.html → audio → captions → render). The visualization + focus
rules are actually *applied* when the beat sheet's `body_html` is authored — the
renderer only styles what the beat sheet already committed to. So a deck is only
as focused as its beat sheet: author `body_html` from the component vocabulary
above, keep one idea per slide, and let the accent + the component do the work.
