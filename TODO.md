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
- **RESOLVED (live-verified):** the three gate scripts were located at `vox/tmp/qc-tooling/` and are now vendored to `runtime/qc/` (`static_scene_check.py`, `wcag_margin_check.py`, `manim_layout_audit.py`); `run.sh` `$QC` repointed to `runtime/qc`. Remaining: confirm Gates A/W/B pass on a real reel end-to-end.
- **Effort:** M (mostly done)

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
- **CORRECTION (live-verified):** the outro asset `vox/bearbrown/` is MEDIA (mp4 brand cards, 16x9 + 9x16) — the brief forbids committing large binaries, so it can't be vendored into git. Treat it like pantry media: `run.sh` should look for `$ART_BEARBROWN` (or `./bearbrown/`) and, if absent, print a visible 'outro skipped — set ART_BEARBROWN to your brand cards' warning instead of silently skipping. Refusal message repoint still applies.
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

### [P1] Standardize env loading on ONE repo-root `.env` (live reconciliation)
- **Repo:** brutalist-art
- **Evidence:** a live check (`.env` reconciliation, 2026-07-12) confirmed the toolkit's `.env.example` variable set is COMPLETE — nothing used by the live pipelines is missing. But env *loading* is inconsistent: the live pipelines variously (a) use `os.getenv` only (shell must be pre-sourced — `runtime/scripts/generate_audio.py:104`), (b) hard-fall-back to a parent `.env` (the live `cancer-*/…/make_audio.py` reads `unreal-reels/.env` by absolute path), and (c) the vendored `component-showcase/…/riff_audio.py` fell back to `../../vox/.env`. The Phase-3 path sweep caught `books/vox` and `../vox/scripts` but MISSED `vox/.env` — five references survived (riff_audio.py, AUTORUN-soul-tuzi.md, code-walkthrough HOWTO + preflight.sh, script-writer/schema.md).
- **Why:** without one convention a user who put keys in the repo-root `.env` finds some scripts don't see them (they only read the shell env or a stale parent file), so audio silently fails or uses the wrong key.
- **Status:** the `vox/.env` reach-outs are now FIXED (repointed to the repo-root `.env`), and `./art` + `run.sh` now auto-load the repo-root `.env`. Remaining: make the standalone Python scripts (`generate_audio.py`, `silent_run.py`, the lecture `make_audio.py` when vendored) load the repo-root `.env` too via a shared helper, so direct invocation matches `./art`.
- **Acceptance:** every audio/render script resolves keys as: shell env → repo-root `.env`; no script references `vox/.env`/`unreal-reels/.env`; running with keys only in `brutalist-art/.env` (no shell export) produces audio.
- **Effort:** S

### [P1] Fix the `.env.example` key drift
- **Repo:** brutalist-art
- **Evidence:** **Dead in the toolkit** (no vendored consumer): `FAL_KEY`; `ELEVENLABS_MODEL_ID` is dead *here* but live in `ai1-cli/remotion` (not vendored) — keep it commented, not removed. **Checked-but-not-consumed**: `HIGGSFIELD_API_KEY`/`MINIMAX_API_KEY` (only `setup:59`; scripts use the `higgsfield` CLI). **Used but undocumented**: `ART_QC`, `ART_FACTS` (`run.sh`), `BB_PUBLISH_WORKSPACE` (`math-explainer/scripts/silent_publish.py:29`, legacy `bb-` namespace), `RIFF_PROJECT` (`component-showcase/remotion/remotion.config.ts:23`).
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

### [P1] Add a silent-audio guard after narration (live failure mode)
- **Repo:** brutalist-art
- **Evidence:** live-verified failure — a revoked/wrong `ELEVENLABS_API_KEY` produces valid-SIZE mp3s at ~-91 dB (silent), not an error. The live fix was ad-hoc (`/tmp/regen_silent.py`) detecting via `ffmpeg -i <f> -af volumedetect` (mean_volume < -80 dB = silent). `runtime/scripts/generate_audio.py` has no such check.
- **Why:** a whole reel can render with silent audio and look 'done'; the failure is invisible until playback.
- **Acceptance:** `generate_audio.py` measures each mp3's mean volume and re-tries (or flags) any beat below -80 dB; a `--regen-silent` mode re-does only the silent ones.
- **Effort:** S

### [P2] Document the shell-key-overrides-.env footgun
- **Repo:** brutalist-art
- **Evidence:** live-verified — because scripts resolve `os.getenv` first (shell wins), a stale/revoked `ELEVENLABS_API_KEY` exported in the shell silently overrides the good value in `.env`; the live workaround was `unset ELEVENLABS_API_KEY` before running. Our `./art`/`run.sh` `.env` auto-load is also 'shell wins'.
- **Why:** a user with an old key in their shell profile gets silent failures despite a correct `.env`.
- **Acceptance:** the doctor warns when a key is set in BOTH the shell and `.env` with different values; INSTALL/README note the `unset` fix.
- **Effort:** S

### [P2] Coverage gap: only 2 of N pipelines are live-verified
- **Repo:** all
- **Evidence:** a live Claude Code session could describe only two pipelines end-to-end — `ch-lecture` (animated-deck) and `vox/youtube` (the vendored vox spine). The other video types (music-video, sketch-explainer, dance-video, lyric-*, story-film, etc.) were produced by **now-terminated sessions**; their process is only recoverable from the vendored source-skill scripts, not a live account.
- **Why:** reconciliation is complete for 2 pipelines; the rest rest on the vendored artifacts being faithful (the gather was byte-identical, so likely fine, but unverified against a live run).
- **Acceptance:** as each remaining type gets its Phase-5 example built + run once, mark it live-verified; note any script that doesn't actually run.
- **Effort:** M

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
- **CORRECTION (live-verified 2026-07-12):** the pipeline that actually made the 34 lecture videos is **`skills/animated-deck/`**, NOT the Remotion `unreal-reels/skills/deck-lecture`. Real stack: per-chapter `make_audio.py` (stdlib urllib → ElevenLabs) → `skills/animated-deck/assets/build_deck_anim.py` (D3 + `d3.min.js` + `deck_anim.js`, emits self-contained `deck.html`) → `idea_align.py` (faster-whisper → `align.json` idea-karaoke timing) → `render_deck_video.py` (Playwright headless Chromium → per-slide clips → ffmpeg concat → mp4). Batch driver `books/batch_idea_highlight.py`. Artifacts: `anim.json` (D3 config), `align.json`, slides `S01..Snn` (a DIFFERENT schema than the vox `beat_sheet` B01..Bnn). `deck-lecture` (Remotion) is a separate/older variant — vendor `animated-deck`, the proven one.
- **New deps this brings:** Playwright + headless Chromium, faster-whisper (already have), D3 (bundled `d3.min.js`). The `setup` doctor needs a `playwright` check + a lecture-video feature row.
- **Name (RESOLVED at gate):** the skill is **`deck-lecture`** (conveys it makes an HTML deck AND a lecture). One skill, chapter → deck → narrated lecture video, enter-at-deck supported.
- **Renderer note:** two deck→video renderers exist — `skills/animated-deck/` (Playwright/D3, the PROVEN one behind the 34 videos) and the session `deck-lecture` (Remotion). Phase 5 vendors animated-deck as canonical; whether to also carry the Remotion path is a Phase-5 impl decision.
- **Acceptance:** vendor `skills/animated-deck/` (assets + the three scripts + batch driver) as the `deck-lecture` skill under the de-vox'd runtime; document the slide-schema deck `beat_sheet`; add a CAPABILITIES + doctor row (incl. Playwright); restore one of the 34 lectures as the example.
- **Effort:** L


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

### [P1] Reconcile the palette registry to the 6 canonical design palettes (live-verified)
- **Repo:** brutalist-art
- **Evidence:** the current design system has SIX palettes — `brutalist, hai, medhavy, musinique, neu, nikbearbrown`. **`musinique`** is a NEW, not-yet-in-toolkit palette (the record-label/artist web properties): essentially **monochrome greys** (white→greys→black, black/white CTAs, humanist sans, rounded/soft-shadow shadcn look), documented in `runtime/design/musinique-palette.md` (exact `:root` HSL pending its external CSS). The other five — but the toolkit stores them under inconsistent, stale keys across two surfaces. Manim `runtime/manim/animated_graphics.py:35` `_PALETTES` has keys `teardown, newsprint, neu, medhavy, humanitarians` (5) — it uses `teardown` for nikbearbrown and `humanitarians` for hai, and **has no `brutalist` key at all**. Remotion `runtime/remotion/src/tokens/` has `brutalist, humanitarians, medhavy, neu, newsprint, teardown, vox` (7). `teardown.ts` re-exports `vox` and comments "the NikBearBrown default palette"; `brutalist.ts` is a SEPARATE terminal/dark palette (`#ea580c` orange, `#080808` bg) — Remotion-only.
- **Why:** (1) a Manim scene cannot render in the `brutalist` palette (missing from the registry); (2) three names for one palette (nikbearbrown = teardown = vox) and hai = humanitarians make `metadata.palette` ambiguous; (3) Manim (5) and Remotion (7) disagree on the set, so the same reel can look different in its Manim vs Remotion beats.
- **Third surface (live-verified):** `brutalist` also lives in **HTML deck CSS** (`:root` custom properties — the `.dc.html` deck program: `--accent:#ea580c`, JetBrains Mono, Solari sub-palette `#080808`/`#F5A623`), used by the cancer-* book videos and the animated-deck lecture pipeline. Authoritative tokens captured in `runtime/design/brutalist-palette.md`. So reconciliation spans **three** surfaces: Manim `_PALETTES`, Remotion `tokens/`, and the deck CSS.
- **Acceptance:** canonical keys `brutalist, hai, medhavy, musinique, neu, nikbearbrown` resolve identically across all three surfaces; **add `brutalist` AND `musinique` entries to the Manim registry** (musinique = monochrome greys + humanist-sans type law; exact values once its CSS lands) (map per `runtime/design/brutalist-palette.md`: CRIMSON=#ea580c, TEAL=#16a34a, JetBrains-Mono type law like neu→Lato); keep `teardown`→nikbearbrown, `humanitarians`→hai, `vox`→nikbearbrown, `newsprint` as back-compat aliases; DESIGN.md uses the canonical five. `ART_PALETTE=brutalist` renders a Manim beat, a Remotion beat, and a deck in the same look.
- **Effort:** M

### [P2] (superseded) Reconcile palette fragmentation into one registry
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

## Theme 8 — QC & format coverage (live-verified 2026-07-12)

### [P1] Add a general Remotion visual gate (parity with the Manim gates)
- **Repo:** brutalist-art
- **Evidence:** the visual gates in `runtime/qc/` (`static_scene_check`, `wcag_margin_check`, `manim_layout_audit`) parse `scenes.py` — they check **Manim** beats only. The only Remotion-side gate is `skills/make/component-showcase/remotion/scripts/riff_gate.py`, which is bench-specific, not a reel-beat check. So Remotion-rendered beats (terminal scenes, slate-filler, bookends) bypass contrast/overflow/layout QC that Manim beats get.
- **Why:** a Remotion beat can ship with clipped text or off-palette color and nothing catches it, while the equivalent Manim beat would fail Gate W/B.
- **Acceptance:** a Remotion visual gate — screenshot a rendered `media/<B>.mp4` (or the Remotion still) and run the same WCAG contrast + margin/overflow checks `wcag_margin_check.py` applies to Manim; wire it into `run.sh` for beats with `shot.type` REMOTION.
- **Effort:** M

### [P2] Surface the 16:9→9:16 converter through `./art`
- **Repo:** brutalist-art
- **Evidence:** the reformatter exists and is captured — `runtime/scripts/shorts.py` ("THE REFORMAT RULE (16:9 → 9:16)", crops to 1080×1920, only reformats slots that earn vertical time) — but `./art` has no `shorts` subcommand and CAPABILITIES/`setup` don't mention it, so a user can't discover it.
- **Acceptance:** `./art shorts <reel>` runs `shorts.py`; a one-line CAPABILITIES note ("derive a 9:16 Shorts cut from any finished 16:9 reel").
- **Effort:** S

### [note] Script fact-checking is a GATE, not a tool (by design)
- **Evidence:** `FACTCHECK.md` is a required, human-authored claims file that `run.sh` GATE F enforces (must exist alongside `SHOTLIST.md`/`PROMPTS.md`); there is no automated fact-checker script, and there shouldn't be — fact-checking is the human's accountability in the labor split. This is captured as-is; documented here so it isn't mistaken for a missing tool.

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
