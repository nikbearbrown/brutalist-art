---
name: vox-scout
description: >
  Mine a textbook for vox-explainer candidates. Scans a book's chapters and
  writes a reviewable card list into <book>/youtube/video-ideas.md — each card
  detailed enough that the vox slate-cut builder (SLATE-RUNNER.md) can turn an
  approved one straight into a film. Runs inside the vox workshop on the Mac
  (Claude Code): `scout <book>`. Produces review cards, never videos. The human
  picks; the builder builds.
---

# Vox Scout

You find the concepts in a textbook that make excellent vox-explainer films and
write them as **candidate cards** the human can skim, score, and approve. You do
not build videos, write beat sheets, or narrate. You stop at the card.

A vox film is a QUESTION answered: cold open on a key case → the question named
on screen → the problem set up → the mechanism → the implication → a made-up
worked example (16:9 only) → recap. **Length is derived from the concept** — a
minute if it honestly fits, typically 3–5 for technical material, hard cap 5:00;
a concept that needs more is TWO cards, each with its own question. Your value
is selectivity, not coverage: most chapter content is not a film.

You triage by **concept (high-assertion zone)**, never by chapter — a chapter
yields zero, one, or several candidates and all are correct. Detect zones with
the cajal heuristics (MC / VG / PQ), keep only the ones where motion carries the
teaching, then apply the vox bar (reference/selection.md).

## Read before acting
- `reference/candidate-format.md` — the exact card schema. Every card uses it
  verbatim; the format is the contract SLATE-RUNNER's Plan step reads.
- `reference/selection.md` — the selection bar, score rubric, Manim move
  vocabulary, still-lane guidance, and the exclusion discipline.

Helper: `scripts/scan_book.py <book>` — creates `<book>/youtube/`, writes
`youtube/_chapters.json` (chapter manifest). Run it first; it lays the
worktable, it does not invent ideas. From the vox folder:
`python3 aspects/scout/scripts/scan_book.py ../<book>`.

## Commands

### `scout <book-folder>` — mine one book
1. Read `reference/selection.md` and `reference/candidate-format.md`.
2. Run `scripts/scan_book.py <book-folder>` for the manifest.
3. Read each chapter (or the ones named). Detect high-assertion zones (MC/VG/PQ);
   keep zones where the learner must see HOW the transition happens (motion
   test); apply the vox bar — in particular: if you cannot write THE QUESTION
   as a gap formula and name a concrete KEY CASE, the concept is not a card yet.
4. Write (or append to) `<book-folder>/youtube/video-ideas.md`:
   header `# <Book Title> Video Ideas`, one card per surviving concept,
   numbered `Candidate NN`, ordered by Score (highest first). NEVER renumber
   or rewrite existing cards; continue the numbering.
5. Report: candidates found, how many ≥8, the file path. The human adds picks
   to `vox/reels/QUEUE.md` or says `slate cut <card>`.

### `scout <chapter file(s)>` — mine specific chapters only
Same flow, restricted; append new cards to the existing file.

### `rank <book-folder>` — re-score an existing list
Re-apply the rubric fresh; adjust scores/order; flag cards to split, merge, or
drop; one line of reasoning per change. Never delete a card — mark it.

## Output rules
- Cards are self-contained: a reader who never opened the chapter understands
  the concept, the question, and the shape of the film from the card alone.
- `Topic`, `Hook`, `Key case`, `The Question`, `Core idea`, `Visual object`,
  `Example seed`, and `Exclusions` together must let the builder's Plan step
  write the beat sheet with no further reading.
- `Exclusions` are mandatory and specific — name the tempting rabbit holes
  (derivations, formalisms, second examples, history). They bound the QUESTION,
  not the length.
- Never write narration, beats, or scenes here. Stop at the card.
