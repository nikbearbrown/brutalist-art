# Deck Redesign — TODO / Handoff (for tomorrow)

The animated deck now RENDERS with motion (build_deck_anim.py was created and works),
but the DESIGN is wrong. This is a redesign of the lecture-deck format, not a tweak.
Do not start coding — read this, then work the task list in order.

## The core problem with what exists now

- The animation is **words and boxes moving** — it "makes no sense." Motion for its
  own sake, not motion that explains.
- **Karaoke is word-level; it should be IDEA-level.** What the voice is saying must
  match the idea being highlighted — highlight a *phrase/idea chunk*, timed to when the
  voice says it, not one word at a time.
- **The slides are far too wordy.** The VOICEOVER is the verbose channel; the SLIDE is
  not. Slides should be spare — concepts drawn, not paragraphs printed.

## The target format (16:9, and we are NOT converting to 9:16)

Split the frame left/right (for 9:16 later it would be top/bottom instead — note it,
don't build it):

```
┌─────────────────────────────────┬──────────────┐
│  LEFT 2/3                        │  RIGHT 1/3   │
│                                  │              │
│  the CONCEPT, DRAWN:             │  the NARRATION│
│  - the pattern vocabulary        │  text, as    │
│    (chips / flows / stat rows)   │  IDEA-LEVEL  │
│    WHEN it fits, OR              │  KARAOKE —   │
│  - a whiteboard drawing of the   │  the idea    │
│    concept: simple shapes,       │  being spoken│
│    figures, hand-drawn feel      │  is the one  │
│                                  │  highlighted │
└─────────────────────────────────┴──────────────┘
```

- **Left 2/3 — concept drawn.** Use the existing pattern components (chips, flows,
  stat rows, grids) WHEN the concept fits them. When it doesn't, a **whiteboard-style
  drawing**: the concept sketched with simple shapes and figures (a vessel, a rim, a
  gradient, an arrow) — not text in boxes. This is the part that should carry meaning.
- **Right 1/3 — idea-level karaoke text.** The narration, chunked into IDEAS, with the
  currently-spoken idea highlighted. Highlight = what the voice is saying right now.

## Task list (ordered)

1. **Idea segmentation + alignment (`idea_align.py` — currently MISSING).** Split each
   beat's narration into idea chunks (clause/phrase level, not words). Align each chunk
   to its time span in the audio (forced alignment if available; even-spacing fallback).
   Write per-beat idea timings. This is the spine of idea-karaoke — build it first.
2. **New two-column slide layout** in the deck CSS / build_deck_anim.py: left 2/3
   concept plane, right 1/3 idea-karaoke text column. Retire the full-width wordy
   `.ccap p` paragraph as the main text.
3. **Idea-karaoke in `__deckAnim.seek`.** Highlight the idea chunk whose time span
   contains p (map p→time via the beat duration + idea_align timings), in the right
   1/3. Not word-by-word.
4. **Whiteboard concept drawings for the left 2/3.** When a beat has no clean pattern
   mapping, generate a simple-shape/figure sketch of the concept (SVG line-art,
   hand-drawn feel) instead of text boxes. Keep the pattern components as the first
   choice when they fit.
5. **Trim on-slide text.** The slide carries the drawing + the idea chunks only; the
   verbosity lives in the voiceover. Cut the long caption paragraphs.

## Carried over from the earlier diagnosis (still true, fold in)

- **HUD chrome is baked into the render** (progress bar, nav dots, page counter, corner
  mark). Add a render/bare mode that hides them before screenshot. (render_deck_video.py)
- **Timing:** ~50s/slide is too long, and the reveal is stretched across ~45% of the
  slide so content sits faded for too long. Front-load reveals; tie pacing to the idea
  timings from task 1.
- **Math:** no on-slide KaTeX yet (physics decks show raw LaTeX). Narration LaTeX is
  already spoken (latex_to_speech). Add KaTeX for the left-plane visuals if a formula
  is the concept.

## Keep — do NOT change

- The pattern vocabulary (chips, flows, stat rows, grids) is good — keep it as the
  first-choice left-plane treatment.
- Orange-accent discipline, typography, the count-up on stats.
- Sentences over bullets (already true).
- build_deck_anim.py exists and wires into build_lectures.py correctly — extend it,
  don't rebuild from scratch.

## Files in play

- `books/skills/animated-deck/assets/build_deck_anim.py` — the deck+animation builder
  (created this session; extend for the two-column layout + idea-karaoke).
- `books/skills/animated-deck/assets/idea_align.py` — MISSING; build it (task 1).
- `books/render_deck_video.py` — the seek-stepping renderer (add bare/render mode; HUD off).
- `books/build_lectures.py` — routes to build_deck_anim.py; already has latex_to_speech
  + exercises-skip base rule.
- Reference render reviewed: `books/TMP/cancer-nanomedicine-ch02-transport-barriers.mp4`
  (598s, 12 slides — animation works, design wrong).

## Resume prompt for tomorrow

"Read books/brutalist-art/DECK-REDESIGN-TODO.md and work the task list in order. Start
with idea_align.py (idea-level segmentation + timing), then the two-column layout
(left 2/3 concept drawn, right 1/3 idea-karaoke). Slides spare, voice verbose. Show me
one rebuilt chapter before batching."
