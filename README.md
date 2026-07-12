# brutalist-art — consolidated video toolkit (refactor, step 1: GATHER + ANNOTATE)

This repo is the new single home for **every video-making and video-uploading skill** that
was previously scattered across `bear-textbooks/books/vox/`, `books/unreal-reels/`,
`books/brutalist/remotion/`, `books/ai1-cli/remotion/`, `books/higgsfield/`, and the
top-level `skills/` and `figure-harvest/` folders.

**This is step 1 of a refactor: a COPY, not a rewrite.** Nothing here has been merged,
deduplicated, or rewired yet. Each skill was copied verbatim (minus rendered media) so we
can see the whole surface in one place and decide what to keep, merge, and delete next.

## Layout

```
skills/
  make/     32 skills — scouts, builders, previz/routing, ops (the reel factory)
  upload/    2 skills — audit (YouTube status) + notebooklm-youtube (publish)
  assets/    6 skills — Higgsfield generation, durer (SVG), figure-harvest
  figures/   cajal/figures/graphs/tables — gathered from ai1-cli (script + prompt libs); see POINTER.md
examples/    one mp4-stripped "render this" starter per video type
MANIFEST.md  annotated inventory: every skill, where it came from, what it does, its deps
```

## How to read it
Start with **`MANIFEST.md`** — it annotates all 40 copied skills with their original path in
`bear-textbooks/`, a one-line description, and any dependency/duplicate flags. The `examples/`
folder holds a runnable-shaped sample of each major reel type (beat sheets, scene code, and
scripts — the mp4/wav/png renders were stripped) so someone can try "render this" before
authoring their own.

## ⚠️ The one thing to know before running anything
These are the **skill/command definitions plus each skill's own files** — they are **not yet
self-contained**. The vox skills still call the *shared* vox runtime that was NOT copied here
(it is infrastructure, not a per-skill file):

- `vox/scripts/` — `vox_run.sh`, `generate_audio.py`, `vox_compile.py`
- `vox/manim/animated_graphics.py`, `vox/DESIGN.md`, `vox/voices/`, `vox/reference/pedagogy.md`, `vox/.env`
- the unreal-reels shared scripts, `bearbrown/`, and Remotion projects

The unreal-reels and ai1-cli skills likewise depend on their toolkits' shared scripts and
`node_modules` (excluded). **Wiring that shared runtime in (or vendoring/deduping it) is refactor
step 2.** For now, treat this repo as the annotated map, and run skills from their original
locations until the runtime is consolidated.

## Deliberately NOT copied (flagged for a later decision)
- **Decks & lectures** (`brutalist-slides`, `slide-deck`, `lecture-assets`, `deck-lecture`,
  `animated-deck`) — the chapter→deck→narrated-video pipeline. Left out per scope choice; add if wanted.
- **`dataviz`** — a Cowork session skill, not a repo file (the other figure/data tools WERE
  gathered from `ai1-cli` into `skills/figures/`; see `skills/figures/POINTER.md`).
- All **rendered media** (`*.mp4/.mov/.wav/.mp3`), `node_modules`, `.git`, caches, `out/`.
