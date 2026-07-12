# TODO — the Brutalist family, promised vs. built

*Generated 2026-07-12 by a cross-repo gap scan (per `TODO-SCAN-BRIEF.md`). Every item cites the
file that evidences it. Priorities: **P0** = something documented as working is broken/missing;
**P1** = described-but-unbuilt or a real usability gap; **P2** = polish / long-horizon. Effort S/M/L.*

## Repos scanned

| Repo | Type | Role |
|---|---|---|
| `brutalist/` | ENGINE | The spec (`BRUTALIST.md`) + a large draft/prompt/style corpus. Documentation, not runnable. |
| `brutalist-art/` | TOOLKIT | This repo — the refactored video toolkit (skills/, runtime/, examples/, setup). |
| `brutalist-d3-x-claude/` | BOOK | D3×Claude charts (81 chapters). |
| `brutalist-figma-claude/` | BOOK | Figma×Claude design-systems engineering (18 chapters). |
| `brutalist-using-d3-and-html-to-make-slide-decks/` | BOOK | Slide-design critique + D3 figures (15 chapters). |
| stray root files | — | `AUTORUN-brutalist-one.md`, root `BRUTALIST.md`, and the refactor docs. |

**State of the family.** The refactor gave the *video* toolkit a clean skeleton — an alias-aware
`art` dispatcher, a de-vox'd `runtime/` spine, a working beat ledger (`todo.py`), and a per-feature
`setup` doctor. But three classes of gap remain: (1) **the refactor's own vendoring left dangling
paths** — the shipped examples and ~55 skill command blocks still point at the pre-refactor
`aspects/…` layout, so `./art run` crashes on the very examples the docs advertise; (2) **the
Brutalist governance architecture that gives the project its name** — the intent/schema/PROJECT
files, the enforced phase gate, the refusal behavior in `BRUTALIST.md` — is essentially
unimplemented in the toolkit; and (3) **the three books teach a sibling "Brutalist for static
design" product** (D3, slides, Figma) that shares only the governance spine and is out of scope
for the video toolkit. Per-repo ledgers are in `TODO-APPENDIX.md`.

Note: many P0/P1 path items below are **regressions introduced by the Phase 3 vendoring in this
refactor** — they are cheap to fix and should land before Phase 5 examples are built on top of them.

**Scope correction (Gate-4 review):** the **lecture pipeline** (chapter → HTML deck → narrated
lecture video) was deferred as D4 but has **34 finished videos shipped** — it is a core video
type, not an optional extra. See the lead P0 in Theme 3; this reverses D4.

---

## Theme 1 — Toolkit: make `./art run` actually run (Phase-3 regressions)

### [P0] Repoint every `examples/*/scenes.py` at `runtime/manim`
- **Repo:** brutalist-art
- **Evidence:** `examples/slate-cut--base-rate/scenes.py:22` `sys.path.insert(0, …parents[2] / "aspects/explainer/vox-explainer/manim")` then `from animated_graphics import *`. That path does not exist; the lib is `runtime/manim/animated_graphics.py`. Same dead import in `examples/terminal-screencast--compression-journey/scenes.py` and `examples/explainer--size-paradox/scenes.py`.
- **Why:** `./art run <reel>` renders `scenes.py`; all three shipped examples crash at Manim import — the headline "it just runs" claim is false out of the box.
- **Acceptance:** `./art run examples/slate-cut--base-rate` reaches render; every `examples/*/scenes.py` resolves the graphics lib via `runtime/manim` (or `$ART_HOME`).
- **Effort:** S

### [P0] Add `PROMPTS.md` to `slate-cut--base-rate` (or exempt zero-open reels) so it passes GATE F
- **Repo:** brutalist-art
- **Evidence:** `runtime/scripts/run.sh` GATE F requires `FACTCHECK.md SHOTLIST.md PROMPTS.md`; `examples/slate-cut--base-rate/` has the first two, not `PROMPTS.md`.
- **Why:** CAPABILITIES sells this as the zero-key teaching example; it fails its own paperwork gate before rendering.
- **Acceptance:** `./art run examples/slate-cut--base-rate` passes GATE F.
- **Effort:** S

### [P0] Fix or honestly disable the `run.sh` QC gates (missing `tmp/qc-tooling`)
- **Repo:** brutalist-art
- **Evidence:** `runtime/scripts/run.sh:15-18` calls Gates A/W/B from `$QC="$ROOT/tmp/qc-tooling"` (`static_scene_check.py`, `wcag_margin_check.py`, `manim_layout_audit.py`); `repo/tmp/` does not exist, so all QC silently skips. `manim_layout_audit.py` actually lives at `skills/make/sketch-explainer/scripts/`.
- **Why:** Docs promise pre-flight/pixel QC on every render; nothing is checked. A user believes broken layouts are gated when they aren't.
- **Acceptance:** either vendor the three QC scripts into `runtime/` and repoint `$QC`, or `run.sh` + docs state QC is unavailable and fail loudly if `ART_QC=1` but tooling is absent.
- **Effort:** M

### [P0] Author `skills/figures/figure-planner/SKILL.md` (D5 half-done)
- **Repo:** brutalist-art
- **Evidence:** `skills/figures/figure-planner/` has only library files; `./art figure-planner --help` → no SKILL.md. `REFRACTOR-PLAN.md` D5: "promote ai1-cli copies to a real `figure-planner` skill." Listed as ready in CAPABILITIES + doctor + `--list`.
- **Why:** Documented-as-shipped, actually bodyless — `--help` errors.
- **Acceptance:** `./art figure-planner --help` prints a real SKILL.md; `POINTER.md`'s source-of-truth question is resolved.
- **Effort:** M

### [P1] Rewrite the ~55 stale `aspects/…` command paths in SKILL.md files
- **Repo:** brutalist-art
- **Evidence:** `grep -rn "aspects/" skills` → 55 hits in runnable command blocks, e.g. `script-writer/SKILL.md:93` `python3 aspects/teardown-script/scripts/td_script_gate.py` (actual: `skills/make/script-writer/scripts/`); `kids-video/SKILL.md:80`; `lyric-resync/SKILL.md:103-105`; and `component-showcase/remotion/scripts/riff_publish.py:26` `UPLOADER = "../../unreal-reels/aspects/…/youtube_publish.py"` (fails at runtime, not just docs).
- **Why:** Every pasted command hits a nonexistent path after the vendoring.
- **Acceptance:** `grep -rn "aspects/" skills` returns 0 runnable-path hits.
- **Effort:** M

### [P1] Reconcile or delete the `explainer` skill-local `animated_graphics.py`
- **Repo:** brutalist-art
- **Evidence:** `skills/make/explainer/manim/animated_graphics.py:43` `_PAL = os.environ.get("VOX_PALETTE","teardown")`, `:45` `books/vox/DESIGN.md`, `:53` `books/vox/fonts/`. The reconciled copy `runtime/manim/animated_graphics.py:43` uses `ART_PALETTE`/`runtime/design`. `run.sh:30` uses the runtime copy; `explainer/SKILL.md:74` points users at the skill-local legacy copy.
- **Why:** The skill's own manim file ignores `ART_PALETTE` and reaches for nonexistent `books/vox/` paths — the GLOSSARY-promised reconciliation is half-done.
- **Acceptance:** the two are identical (or the skill copy is deleted and SKILL.md points at `runtime/manim/`); no `VOX_PALETTE`/`books/vox/` remain in the skill copy.
- **Effort:** M

### [P1] Give `./art run` a `--help`
- **Repo:** brutalist-art
- **Evidence:** `runtime/scripts/run.sh` has no arg parsing; `run.sh --help` → `[run] no such reel dir: --help`.
- **Why:** The advertised `./art run <reel>` entry point can't be introspected and misreads `--help` as a reel path.
- **Acceptance:** `./art run --help` prints usage, exits 0.
- **Effort:** S

### [P2] `run.sh` refusal + outro point at missing assets
- **Repo:** brutalist-art
- **Evidence:** `run.sh` REFUSED branch cites `reels/_example-comma-orphan/scenes.py` (no `reels/` dir); the outro branch guards on `$ROOT/bearbrown` which doesn't exist, so the "outro law" brand card never fires.
- **Why:** The one actionable hint in the refusal path dead-ends; every reel ships without the mandated brand outro.
- **Acceptance:** refusal points at `examples/slate-cut--base-rate/scenes.py`; `bearbrown/` vendored or the skip warns visibly.
- **Effort:** S

---

## Theme 2 — Toolkit: setup, keys, discoverability

### [P1] Add `LICENSE` (MIT — decision already closed)
- **Repo:** brutalist-art
- **Evidence:** `REFRACTOR-PLAN.md` Gate-1 final call "MIT license"; no `LICENSE` at root.
- **Why:** Blocks publishing the (empty) GitHub remote.
- **Acceptance:** `LICENSE` (MIT) at root, referenced from README.
- **Effort:** S

### [P1] Give `terminal-screencast`, `remotion-explainer`, `collage-ads` CAPABILITIES + doctor rows
- **Repo:** brutalist-art
- **Evidence:** all three have real SKILL.md + appear in `./art --list`; none has a `CAPABILITIES.md` row, and `setup`'s `FEATURES` array has no `terminal-screencast`/`remotion-explainer`/`collage-ads` entry.
- **Why:** shipped video-producing skills are invisible on the two at-a-glance surfaces users are told to consult.
- **Acceptance:** each gets a CAPABILITIES row + `./setup <name>` readiness row (or an explicit "helper, not a standalone type" note).
- **Effort:** M

### [P1] Fix the `.env.example` key drift
- **Repo:** brutalist-art
- **Evidence:** **Dead keys** (no consumer): `FAL_KEY`, `ELEVENLABS_MODEL_ID`. **Checked-but-not-consumed**: `HIGGSFIELD_API_KEY`/`MINIMAX_API_KEY` (only `setup:59`; scripts use the `higgsfield` CLI). **Used but undocumented**: `ART_QC`, `ART_FACTS` (`run.sh`), `BB_PUBLISH_WORKSPACE` (`math-explainer/scripts/silent_publish.py:29`, legacy `bb-` namespace), `RIFF_PROJECT` (`component-showcase/remotion/remotion.config.ts:23`).
- **Why:** users set keys that do nothing, and can't discover real toggles; `BB_` breaks the `ART_` convention.
- **Acceptance:** dead keys removed or marked "reserved"; `ART_QC`/`ART_FACTS`/`RIFF_PROJECT` documented; `BB_PUBLISH_WORKSPACE`→`ART_PUBLISH_WORKSPACE`; the `k_ai` doctor check reflects actual `higgsfield` login state.
- **Effort:** M

### [P1] Enforce the shared `beat_sheet.schema.json` at compile/run preflight
- **Repo:** brutalist-art
- **Evidence:** `runtime/schema/beat_sheet.schema.json` is cited as the contract by `runtime/README.md` and two SKILL.md files, but no code imports `jsonschema`; every producer writes `beat_sheet.json` unvalidated.
- **Why:** the "shared schema contract" is claimed but unenforced; malformed sheets fail deep in the pipeline.
- **Acceptance:** `run`/`compile` validates the sheet against the schema and errors clearly.
- **Effort:** M

### [P2] Enforce "unlisted" for parked skills; fix their stale cross-refs; fix `--list` cosmetics
- **Repo:** brutalist-art
- **Evidence:** `GLOSSARY.md` marks `product-photos`/`listing-cards` "(parked, unlisted)" yet `./art --list` prints them; their SKILL.md bodies still say "use higgsfield-product-photoshoot / higgsfield-generate". `./art --list` also renders `figure-planner (was from-ai1-cli/(cajaletal.))` — the awk alias strip mangles "cajal et al.".
- **Acceptance:** `--list` hides parked skills (or `--all` reveals them); parked cross-refs use `ai-asset-gen`/`ai-character-id`; former-name renders readably.
- **Effort:** S

### [P2] Add `CONTRIBUTING.md` + minimal CI
- **Repo:** brutalist-art
- **Evidence:** no `CONTRIBUTING.md`, no `.github/`, no tests. (Node lockfiles ARE committed for all three Remotion projects — no gap there.)
- **Why:** needed before opening the public remote; CI would catch exactly the drift found in this scan (missing SKILL.md, doctor rows, env drift).
- **Acceptance:** `CONTRIBUTING.md` covers the skill-folder + SKILL.md + GLOSSARY-alias contract; a CI workflow runs `./setup`, `./art --list`, and asserts every listed skill has a SKILL.md.
- **Effort:** M

---

## Theme 3 — Toolkit: unbuilt features documented as present

### [P0] Build `./art fill-in <reel>` — auto-render every pipeline-makeable beat
- **Repo:** brutalist-art
- **Evidence:** today `todo.py` *reports* which beats are `needs-fill` with method `manim`/`remotion` (pipeline) vs. `ai-video-prompt`/`historical-image`/`user-capture` (human), and `compile.py` renders a slate/request card for anything unfilled — but nothing *acts* on the pipeline-makeable ones. A beat Claude could animate can sit unfilled and surface to the human as a request card (see `beat_plan.py` `fill_plan` + `compile.py` slate path).
- **Why:** the labor split must be honest — the human should only ever be asked for beats the machine genuinely can't make. A request card on a Manim/Remotion beat is a defect. Fill-in is the enforcement: audit the ledger, render every `who=pipeline` beat, and leave cards *only* for `who=human` beats.
- **Acceptance:** `./art fill-in <reel>` iterates the beat ledger, renders each `needs-fill` beat whose method is `manim` or `remotion` (via `animated_graphics.py` / the Remotion scene path), re-runs `todo.py`, and reports "N pipeline beats filled, M human beats remain (with prompts)"; after it runs, no request card exists for a pipeline-makeable beat. **Render contract:** per scene, retry up to 5× fixing errors between attempts; if it still fails, leave the beat unrendered (slate + `needs-fill`) and continue to the next — never stall the reel. A completed pass may contain a few flagged beats on purpose; the human reviews the cut and redoes those. Works unattended (`claude --dangerously-skip-permissions`).
- **Effort:** M

### [P0] Bring the lecture pipeline into the toolkit (reverses deferral D4)
- **Repo:** brutalist-art (missing) ← source in `unreal-reels/`
- **Evidence:** the chapter → HTML deck → narrated lecture-video pipeline exists as two mature skills — `unreal-reels/skills/deck-lecture/` (13 scripts: `build_sections.py`, `extract_slides.py`, `align_captions.py`, `scaffold_remotion.py`, `prerender_deck.py`, … + a full Remotion template `src/Lecture.tsx`, `Doodle.tsx`, `EquationTangent.tsx`) and `unreal-reels/skills/lecture-assets/` + `unreal-reels/scripts/silent_run.py`. **34 finished lecture videos are shipped**: `cancer-nanomedicine/ch{01..12}-lecture` (12), `cancer-medicine/ch{01..11}-lecture` (11), `cancer-research/ch{01..11}-lecture` (11) — each folder carries `deck.html`, `beat_sheet.json`, `build_deck.py`, `make_audio.py`, `render.py`, `slides/`, and the rendered `.mp4`. `REFRACTOR-PLAN.md` D4 marked this "out of scope."
- **Why:** this is the single most-produced video type in the family (34 outputs vs. a handful of others), it generates its own deliverable class (HTML lecture deck **and** narrated lecture video with idea-karaoke timing), and it is entirely absent from `./art --list`, CAPABILITIES, and the doctor. D4 was a scope error.
- **Acceptance:** two first-class skills in the toolkit — a chapter→lecture-video pipeline and a deck→video pipeline (names TBD, e.g. `lecture-video` + `deck-video`) — vendored with their scripts + Remotion template under the de-vox'd runtime; a CAPABILITIES row + doctor row each; at least one of the 34 existing lectures restored as the example.
- **Effort:** L (largest single addition; the code exists and works, so mostly vendoring + renaming + wiring)


### [P1] `story-film` claims "built" scripts that were never vendored
- **Repo:** brutalist-art
- **Evidence:** `skills/make/story-film/` has only `SKILL.md` + `README.md` (no `scripts/`), yet SKILL.md says Phase 3 storyboard `generate_storyboard.sh (built)`; that script exists nowhere in the tree.
- **Why:** a user following the "built" phases hits a missing script immediately.
- **Acceptance:** vendor `generate_storyboard.sh` (fix the reuse-map paths) or downgrade "built" claims to "reuses `<vendored path>`".
- **Effort:** M

### [P1] `explainer` assembly/annotation plane + karaoke are spec-only (flagship cap)
- **Repo:** brutalist-art
- **Evidence:** `skills/make/explainer/REMOTION.md:1` "the Remotion assembly plane — spec (v1, not yet built)"; `explainer/SKILL.md:276` karaoke "(Not yet built — until it lands, DOCUMENT/COMPOSITE annotation beats degrade to clean plates)".
- **Why:** the flagship's final step (word-keyed overlays, auto-credits, karaoke) doesn't exist; two shot types silently drop to static plates.
- **Acceptance:** the assembly plane renders DOCUMENT/COMPOSITE overlays keyed to word timestamps, or CAPABILITIES/SKILL explicitly caps the flagship at "clean plates only" until built.
- **Effort:** L

### [P2] Stale "not yet built" / stale-path docs in built skills
- **Repo:** brutalist-art
- **Evidence:** `component-showcase/remotion/PROJECT.md:85` says the harness is "not yet built" but `src/harness/OndaScene.tsx`+`registry.ts`+`fixtures/data.ts` now exist (reverse gap). `terminal-screencast/SKILL.md:67-69` and `slate-filler/SKILL.md:114-128` and `code-walkthrough/preflight.sh:49-56` all point at the moved `aspects/remotion-pass/remotion/` (now `runtime/remotion/`); the Onda restyle scenes are unbuilt but have a working fallback.
- **Acceptance:** built-harness doc updated; remotion project references repointed to `runtime/remotion/`; `preflight.sh` can reach "Ready".
- **Effort:** S

---

## Theme 4 — The Brutalist governance layer (the thesis)

### [P1] Build the Brutalist governance layer the spec sells
- **Repo:** brutalist/ (spec) + brutalist-art (impl)
- **Evidence:** `brutalist/BRUTALIST.md` mandates a per-stack `CLAUDE.md`, a two-layer `PROJECT.md` "populated by the Brutalist interrogation script" + "the project audit/dump script", an enforced Phase Gate (Audit→Schema→Generate→Verify→Handoff), and Refusal Behavior. In `brutalist-art`: zero `CLAUDE.md`; the only `PROJECT.md` is a stray reel doc; no interrogation script; phase-gating is prose, not mechanism (only `run.sh` GATE F + the absent QC gates are mechanical).
- **Why:** "maximally informed, minimally autonomous" — intent interrogation, per-stack constitution, enforced gate, refusal — is the project's whole thesis and its name; it's undelivered. The toolkit is currently a well-organized media-skill library.
- **Acceptance:** a `PROJECT.md` interrogation script (populates both layers), at least one per-stack `CLAUDE.md`, and a documented phase-gate/refusal mechanism the skills reference.
- **Effort:** L

### [P1] Reconcile the governing-file count: spec says 2 files, books say 3
- **Repo:** brutalist/ + all three books
- **Evidence:** `BRUTALIST.md` §Governing Files lists only `CLAUDE.md` + `PROJECT.md`; every book requires three, e.g. `brutalist-d3-x-claude/chapters/18-brutalist-claude-project.md:12` "refuses to generate output before `CLAUDE.md`, `DESIGN.md`, and `PROJECT.md` are in place". `DESIGN.md` (the visual constitution) is first-class in practice, absent from the spec.
- **Why:** spec and teaching material disagree on the core artifact set.
- **Acceptance:** `BRUTALIST.md` adds `DESIGN.md` to §Governing Files + the phase-gate precondition (or the books drop to two). File set matches across spec + all books.
- **Effort:** S

---

## Theme 5 — Book ↔ tool coherence

### [P1] Rewrite `AUTORUN-brutalist-one.md` for the post-refactor layout + 3-bookend flow
- **Repo:** brutalist-art (root doc)
- **Evidence:** `AUTORUN-brutalist-one.md:23,27,33` use `$BOOKS/vox/scripts/brutalist_update.py`, `$BOOKS/vox/aspects/remotion-pass/remotion`, and the Onda `_bench` components — all gone after vendoring (now `runtime/scripts/brutalist_update.py`, `runtime/remotion/`). It documents only B00+B99, but `runtime/scripts/brutalist_update.py:6,172` now also inserts **B00B / `BrutalistAdaptCLI`**. Its QC-gate step (`:46-48`) cites `wcag_margin_check.py` (un-vendored) and scripts scattered under different skills.
- **Why:** run verbatim against the toolkit, the recipe fails at step 1; its "build the two Remotion patterns" step is dead work (the three Brutalist scenes are pre-built in `runtime/remotion/src/scenes/`).
- **Acceptance:** every AUTORUN command resolves inside the repo (`./art run …` / `runtime/scripts/*.py`); documents B00+B00B+B99; the build-from-Onda step is removed/marked done.
- **Effort:** M

### [P1] De-vox the vendored `runtime/design/DESIGN.md` and two Remotion files
- **Repo:** brutalist-art
- **Evidence:** `runtime/design/DESIGN.md:1` "# DESIGN.md — the Vox-explainer design constitution", body cites `vox_graphics.py`/`vox_compile.py`/`books/vox/fonts/`. `runtime/remotion/src/scenes/BrutalistTerminalOpen.tsx:11` comments "vox_compile.py conforms…"; `runtime/remotion/src/Root.tsx:73-74` hard-codes the old 2-item B00/B99 checklist (no B00B). `runtime/scripts/generate_audio.py:15` "in the ~/ai venv". (These survived the Phase-3 sweep.)
- **Why:** vendored runtime files still carry the trademarked name and dead paths/names the sweep was meant to remove.
- **Acceptance:** title + body use `animated_graphics.py`/`compile.py`/`runtime/…`; `grep -rn "vox" runtime/` returns only a labeled lineage note; Root.tsx checklist matches the 3-bookend flow.
- **Effort:** S

### [P2] Reconcile palette fragmentation into one registry
- **Repo:** all
- **Evidence:** D3 book uses "hai palette" (parchment `#F5EBE0`/espresso `#3B1A07`, `brutalist-d3-x-claude/chapters/49-ohlc-chart.md:30`); slides book uses NEU red `#C8102E`; toolkit default `teardown` = `#FFFFFF/#2A1A0E/#C8102E` (`runtime/design/DESIGN.md:26`). Three surfaces, three palettes, three token vocabularies, no shared source.
- **Why:** a reader moving between books/tool gets a different "Brutalist look" each time.
- **Acceptance:** the toolkit's palette registry names `hai`/`neu`/`teardown` as entries (it already models "palette is a registry keyed by metadata"), or each book states its palette explicitly.
- **Effort:** M

### [P2] Editorial defects in book intros/tables (not toolkit)
- **Repo:** brutalist-d3-x-claude, slide-decks book
- **Evidence:** identical boilerplate intros (`brutalist-d3-x-claude/chapters/00-introduction.md:1` and slide-decks `00-introduction.md:1`); `slide-decks/chapters/11-owning-your-design-md.md` has unfilled template cells + an unclosed paren "accent color (#C8102E"; the D3 appendix `18-brutalist-claude-project.md:1` is headed "Chapter 16" but listed as 19.
- **Acceptance:** intros customized, table filled, headings reconciled. (Editorial — separate from the toolkit.)
- **Effort:** S

---

## Theme 6 — Scope & product boundaries

### [P2] Record the product boundary: brutalist-art = video; the books = a sibling "Brutalist design" line
- **Repo:** all
- **Evidence:** `CAPABILITIES.md` enumerates 19 video types; none is "D3 chart", "slide deck", or "Figma extraction". The three books define a static-design product (D3/slides/Figma) sharing only `BRUTALIST.md`. The only bridge is `skills/figures/figure-planner` (chapter figures).
- **Why:** the refactor brief asked whether decks/slides belong in the video toolkit — answer: no.
- **Acceptance:** a one-line product-boundary note in the refactor docs; no deck/Figma code added to the toolkit.
- **Effort:** S

### [P2] Slide-decks book teaches no deck assembly; Figma book's CLI suite is unimplemented
- **Repo:** slide-decks book, figma book
- **Evidence:** `…slide-decks/chapters/01-the-slideument-problem.md:188` exercises emit "a standalone HTML file" (single figure); no deck grammar/navigation anywhere, and no deck generator in the toolkit. `brutalist-figma-claude/chapters/00-introduction.md` names `figma-ping.js`/`figma-audit.js`/`extract-tokens.mjs`/`npm run figma:audit`/`FIGMA.md` — none implemented anywhere.
- **Why:** the slide-decks book's titular capability is taught nowhere; the Figma book presents a "composable CLI suite" with no home.
- **Acceptance:** slide-decks book adds a deck-assembly chapter + format or is retitled to its true scope; the Figma CLI's home repo is cited or its artifacts labeled reader-built.
- **Effort:** M

### [P2] Consolidate "D3 chart with Claude" (book ↔ figure-planner ↔ session `graphs` skill)
- **Repo:** brutalist-d3-x-claude, brutalist-art
- **Evidence:** the D3 book teaches per-chart Claude prompts; `skills/figures/figure-planner/graphs.sh:4-6` says it renders *placeholders* only ("Cowork enrichment handles generation"); the same idea also exists as the session `graphs` skill. Three homes; the "official" tool doesn't actually render the chart.
- **Acceptance:** decide `figure-planner` is the canonical home (and the D3 book references it) or de-scope it; document that `graphs.sh` is placeholder-only.
- **Effort:** M

---

## Theme 7 — Examples & publishing

### [P1] Ship the 14 missing examples (this is Phase 5)
- **Repo:** brutalist-art
- **Evidence:** `CAPABILITIES.md` marks `*(to add)*` / `—` for sketch-explainer, math-explainer, bio, code-walkthrough, recitation-film, kids-video, lyric-overlay, lyric-resync, dance-video, ai-asset-gen, line-art-vectorizer, figure-planner, youtube-publisher. Only 5 of 19 typed rows have an example.
- **Why:** the examples are the teaching artifact each type points to; 14 have nothing to copy from.
- **Acceptance:** each CAPABILITIES row links a real `examples/<type>--*` folder or is honestly reclassified. (Planned as the meta-video Phase 5 — see `REFRACTOR-PLAN.md`.)
- **Effort:** L

### [P2] Publish the toolkit to its remote once P0/P1 land
- **Repo:** brutalist-art
- **Evidence:** remote `github.com/nikbearbrown/brutalist-art` reported empty; nothing pushed. (Verify before asserting.)
- **Acceptance:** after the LICENSE + P0 path fixes, push the refactored toolkit.
- **Effort:** S

---

*Top of the stack for a human picking up work: the four **P0**s in Theme 1 (they make `./art run`
real on the shipped examples) and the `LICENSE` in Theme 2. All are S/M and mostly clean up
Phase-3 vendoring residue. Per-repo capability ledgers: `TODO-APPENDIX.md`.*
