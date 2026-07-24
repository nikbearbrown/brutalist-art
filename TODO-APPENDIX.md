# TODO-APPENDIX — per-repo capability ledger

Auditable claimed-vs-built tables backing `TODO.md`. Every `*brutalist*` directory under
`bear-textbooks/books/` appears here.

## `brutalist/` — ENGINE (the spec + a doc/prompt corpus)

A text snapshot: `BRUTALIST.md` (the six-principle spec) plus a large `MD/` corpus of draft
prompts, D3/chart docs, and style guides. Documentation, not runnable code — it is the *promised*
column for the whole family.

| Spec claim (`BRUTALIST.md`) | Built in the toolkit? | Evidence |
|---|---|---|
| Intent Layer via interrogation script | **No** | no interview/intent script anywhere in `brutalist-art/` |
| `CLAUDE.md` per stack (coding constitution) | **No** | zero `CLAUDE.md` files in the toolkit |
| `PROJECT.md` two-layer + audit/dump script | **No** | only a stray reel `PROJECT.md`; no populator |
| Phase Gate *enforced* (Audit→Schema→Generate→Verify→Handoff) | **Partial/soft** | prose "phase-gated" in skills; only `run.sh` GATE F + (absent) QC gates are mechanical |
| Labor Separation / request-card handoff | **Yes** | CAPABILITIES "human must supply" column; `todo.py` beat ledger works |
| Refusal Behavior at persona level | **No** | no implementation; `run.sh` REFUSED guards are the closest analog |
| Current-Knowledge-Deferred-Action ("mother may I") | **No** | `brutalist_update.py` exists but not a permission-gated flow |
| Governing files: **2** (`CLAUDE.md`+`PROJECT.md`) | **Contradicted by books (3)** | books require `CLAUDE.md`+`DESIGN.md`+`PROJECT.md` |

## `brutalist-art/` — TOOLKIT (this repo)

| Claimed (docs / `--list`) | Reality | Item |
|---|---|---|
| `art` dispatcher + GLOSSARY alias resolution | **Works** — `--list` maps 34 skills incl. old names (cosmetic mangle on one multi-source name) | #18 |
| `./art todo <reel>` beat ledger | **Works** — `todo.py --help` runs | — |
| `./art run <reel>` end-to-end compile | **Broken on shipped examples** — dead `aspects/` import in every `scenes.py`; GATE F missing PROMPTS.md; QC + outro no-op | Theme 1 |
| `./setup` readiness table | **Present, sound** — degrades optional gracefully; missing rows for cli-explainer/remotion-explainer/collage-ads | Theme 2 |
| 34 media skills (SKILL.md each) | **Present as docs; ~55 command paths stale** (`aspects/…`) | Theme 1 |
| `runtime/manim/animated_graphics.py` | **Present** (~728 lines); skill-local copy diverges (VOX_PALETTE, books/vox) | Theme 1 |
| `runtime/remotion/` scenes | **Present** (NikBearBrown/Medhavy/Brutalist); some stale strings | Theme 5 |
| Flagship `explainer` full pipeline | **Capped** — assembly plane + karaoke unbuilt | Theme 3 |
| `story-film` Phase 1–3 "built" | **No scripts vendored** | Theme 3 |
| `figure-planner` skill | **No SKILL.md** (library only) | Theme 1 |
| **Lecture pipeline** (chapter→deck→video) | **Absent** — but 34 videos shipped; source in `unreal-reels/` | Theme 3 (D4 reversal) |
| Worked example per skill | **5 of 19** exist | Theme 7 |
| LICENSE / CONTRIBUTING / CI | **None** (MIT decided, not filed) | Theme 2 |
| beat_sheet schema as a contract | **Present but unenforced** (no validator) | Theme 2 |

## `brutalist-d3-x-claude/` — BOOK (D3×Claude, 81 ch)

Teaches honest D3 v7 single-file HTML charts by prompting Claude against the three-file Brutalist
system, with Cleveland–McGill marks/channels pedagogy and a 61-chart reference. **Buildable
today** with Claude + D3 CDN; needs no engine. Toolkit overlap: `figure-planner/graphs.sh` is the
same "D3-with-Claude" idea but renders placeholders only, and the book never routes readers to it.
Uses **no** old video house names. Frictions: "hai palette" vs teardown (Theme 5), 3-vs-2 governing
files (Theme 4), duplication (Theme 6).

## `brutalist-figma-claude/` — BOOK (Figma×Claude, 18 ch)

A design-systems-engineering handbook: Figma API as a document graph, naming-as-API-contract,
audit/remediate, five extraction pipelines, Figma MCP + a `FIGMA.md` governing file. A faithful
application of the Brutalist philosophy to a **new stack**. Names a CLI suite (`figma-ping.js`,
`figma-audit.js`, `extract-tokens.mjs`, `npm run figma:audit`) with **no implementation anywhere**
— and it shouldn't live in the video toolkit. A **separate product** (Theme 6). No old video jargon.

## `brutalist-using-d3-and-html-to-make-slide-decks/` — BOOK (15 ch)

Despite the title, a slide-**design-critique** book (the slideument problem, assertion headlines,
Mayer multimedia theory, a diagnostic checklist) whose exercises generate **individual** D3 HTML
figures — **not decks**. The titular deck-assembly capability is taught nowhere and implemented
nowhere (no deck grammar/format in the book; no deck generator in the toolkit). Retitle or add a
deck chapter (Theme 6). Shares the palette split and the 3-file governance question; ch11 ships
with unfilled template cells (Theme 5).

## Stray root files

- `AUTORUN-brutalist-one.md` — the "Brutalist standard" video-build recipe; written against the
  pre-refactor `$BOOKS/vox/…` layout and a 2-bookend flow, now stale (Theme 5, item G1/G2).
- root `BRUTALIST.md`, `README.md`, and the refactor docs (`REFACTOR-BRIEF.md`, `REFRACTOR-PLAN.md`,
  `GLOSSARY.md`, `MANIFEST.md`, `CAPABILITIES.md`, `INSTALL.md`, `TODO-SCAN-BRIEF.md`) — current.

## Refactor deferrals — status

| Deferral | Status |
|---|---|
| D4 deck/lecture skills "out of scope" | **REVERSED** — 34 lecture videos shipped; now a P0 (Theme 3) |
| D5 promote figure-planner to a real skill | **Incomplete** — library vendored, no SKILL.md (Theme 1) |
| D6 park product-photos/listing-cards | **Done except enforcement** — still shown by `--list` (Theme 2) |
