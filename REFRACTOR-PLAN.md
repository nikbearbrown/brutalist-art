# REFRACTOR-PLAN — brutalist-art → clone-and-go video toolkit

*Phase 1 deliverable (Audit & Plan) per `REFACTOR-BRIEF.md`. Filename spelling kept as the brief specifies.*
*Status: **GATE 1 CLOSED — all decisions D1–D10 resolved by the human.** Final calls: `scout` + `cli-scout`; one `bio` skill with `--length` (default 3:00); `vox-explainer` → **`explainer`**; `muybridge` → `remotion-explainer`; MIT license; entry command `art`; greybox **deleted**; all three audience presets kept as data; deck/lecture out of scope; figures library promoted to `figure-planner`; product-photo skills parked unlisted; keys rotated, all keys live in `.env`.*
*Rev 2 — amended with Gate-1 feedback: (a) all keys live in `.env`, including blank `HIGGSFIELD_API_KEY` / `MINIMAX_API_KEY` placeholders, docs note the passthrough; (b) `vox/` is the more recent toolkit (derived from `unreal-reels/`) → canonical for all spine reconciliation; (c) the previz story is the slate-placeholder + pantry contract, not "greybox paper" (retired — see D10).*
*Audit method: every claim in this plan was verified against the code — the full skill tree in this repo plus code snapshots of the five parent toolkits (`vox/`, `unreal-reels/`, `ai1-cli/`, `brutalist/`, `higgsfield/`). Diffs by `md5sum`/`diff`; env vars by grepping `os.environ` / `process.env` / API hosts.*

---

## 1. What the audit found (state of the repo)

- **40 gathered skills** under `skills/{make,upload,assets,figures}`, copied faithfully: every copy checked against its parent original is **byte-identical (zero drift since gather)**, except one stray junk set (`vox-explainer-unreal/manim/layout_audit*` QC artifacts).
- **The repo has no git history yet.** Branch `main`, zero commits, remote `github.com/nikbearbrown/brutalist-art` (empty). "Preserve history via `git mv`" therefore starts from a clean slate: Phase 1 makes the **baseline commit** of the gathered state, so every later rename diffs against it.
- **The skills are not runnable in isolation**, exactly as the brief warns. The dominant gap is the **vox script spine** (`vox_run.sh` + 15 `vox_*.py` scripts) — referenced by at least 12 skills, present in this repo **zero** times, and existing in **two divergent parallel copies** in the parents (`vox/scripts/` and `unreal-reels/scripts/`).
- **Hardcoded machine paths will break any clone**: `/Users/nik/...` (brownblue publish, greybox fonts, voxbio HANDOFF), `/Users/bear/...` (remotion-pass README), `~/ai` venv assumptions (bears-doodles, greybox, brownblue), and `books/vox` / `books/unreal-reels` repo-relative reach-outs (notebooklm-youtube `pipeline.py`, simulation docs).
- **The brief's key list differed from the code in three ways** (verified — see §4): no *script* reads `HIGGSFIELD_API_KEY` or `MINIMAX_API_KEY` (AI image/video goes through the external `higgsfield` CLI's own auth); YouTube auth is file-based OAuth (`client_secret.json` + `youtube_token.json`), not an env var; and no skill in this repo calls the Anthropic API at all — the driving CLI *is* the LLM runtime. **Policy (per Gate-1 feedback): `.env` is still the single home for all keys** — `.env.example` ships blank `HIGGSFIELD_API_KEY` and `MINIMAX_API_KEY` placeholders and the docs explain how to supply them via the environment; the doctor treats the higgsfield CLI login OR the env var as "ready."
- **⚠️ Real secrets are committed in the parent toolkits** (not in this repo): live `ELEVENLABS_API_KEY` and `FAL_KEY` values in `vox/.env`, `unreal-reels/.env`, and `ai1-cli/remotion/.env`. See §8, decision D7 — those keys should be rotated, and vendoring must never copy a `.env`.
- **Examples cover only ~5 of ~20 video types**, and none has a rebuild README. The no-key ladder start (previz / silent sketch) has no example at all yet.

---

## 2. Final proposed name map (Gate 1 approval item)

Rules applied: plain video-production jargon, no house codenames as identity, vendor names allowed in help text only. Old names survive as **aliases** (Phase 2 alias table in `GLOSSARY.md`).

### Scouts → two skills *(D1a — RESOLVED at gate)*
| Old | New | What it makes |
|---|---|---|
| `vox-scout` + `bears-doodles-scout` (merged twins) | **`scout`** | Mines a book/text for video candidates → `video-ideas.md`. |
| `cli-scout` | **`cli-scout`** (name kept) | Mines for CLI-video candidates → `cli-ideas.md` (BUILD/RESEARCH lanes). |

Evidence for the twin merge: same 4-file skeleton, same command grammar, `scan_book.py` differs **only in the output directory** (3 lines); card formats and selection doctrine become reference data inside the one `scout` skill.

### Builders
| Old | New | Notes |
|---|---|---|
| `bears-doodles` | **`sketch-explainer`** | MinutePhysics-style sketch animation. |
| `brownblue` | **`math-explainer`** | 3Blue1Brown-style pure-Manim. |
| `brownblue-convert` | **`explainer-deepen`** | Audit + rewrite a sketch into a deeper math-explainer. |
| `vox-explainer` (+ `vox-explainer-unreal` **merged in, deleted**) | **`explainer`** *(RESOLVED at gate — not "collage-"; the whole point is that each beat's mp4 is generated by whatever tool is best for that beat — Manim, Remotion, AI video, stills — and composited together at the end)* | The flagship per-beat best-tool explainer. See dedup §3.1. |
| `voxlit` | **`recitation-film`** | Literary recitation as the master clock. |
| `mini-bio` + `voxbio` | **`bio`** with `--length` (default 3:00; shorter/longer on request — "mini-bio" = asking for a short one) *(D1b — RESOLVED at gate)* | See dedup §3.4. |
| `cli` | **`terminal-screencast`** | Fixed-spine CLI video. |
| `simulation` | **`code-walkthrough`** | "Build it with Claude Code + Manim" reel. |
| `teardown-script` | **`script-writer`** | Any text → script + `beat_sheet.json`. |
| `muzak` | **`music-video`** | Beat-synced from WAV + lyrics. |
| `muzak-overlay` | **`lyric-overlay`** | Karaoke lyrics + audiogram over finished video. |
| `lyric-match` | **`lyric-resync`** | Re-cut existing video to the words (Hailuo image-to-video). |
| `songbird-dance` | **`dance-video`** | Character dances on the beat (Seedance). |
| `cubs` | **`kids-video`** | Ages 1–5, dev-psych gated. |
| `unreal-reels` (orchestrator) | **`story-film`** | Story → narrated AI film. *(new — not in brief's table)* |
| `muybridge` | **`remotion-explainer`** *(D1c — last open name; alternative `code-animated-explainer` if vendor-free naming matters here)* | Scope-before-spectacle Remotion explainer. |
| `arcads-collage-motion` | **`collage-ads`** | Halftone paper-collage ads. *(new)* |

### Decision helpers & ops
| Old | New | Notes |
|---|---|---|
| `greybox` | **deleted** *(D10 resolved)* | The "greybox paper" scrapbook look is superseded: previz is now the pipeline's own slate-placeholder + pantry flow (§6a). Deletion accounted in MANIFEST. |
| `media-router` | **`shot-planner`** | Manim/Remotion/T2I/T2V per beat. |
| `pacing` | **`duration-planner`** | Sizes video to content. |
| `hai`, `medhavy`, `neu` | **`audience-preset`** (one skill + per-brand data files) | See dedup §3.3. Which brands survive → *(D3)*. |
| `remotion-pass` | **`slate-filler`** | Fills slate beats with motion graphics. *(new)* |
| `update` | **`reel-updater`** | Migrate built reels to latest specs. *(new)* |
| `riff` | **`component-showcase`** | Render + critique visual units. Runtime must be vendored (§5). |
| `remotion-best-practices` | → **`docs/remotion-best-practices.md`** | Reference doc, not a command — demote out of `skills/`. |

### Upload & assets
| Old | New | Notes |
|---|---|---|
| `audit` | **`video-inventory`** | YouTube status across books. |
| `notebooklm-youtube` | **`youtube-publisher`** | Publish + bookends + transcript description. |
| `higgsfield-generate` | **`ai-asset-gen`** | Vendor name in help text only. |
| `higgsfield-soul-id` | **`ai-character-id`** | Trains an identity for consistent generation. |
| `higgsfield-product-photoshoot` | **`product-photos`** — or **drop** | Borderline (product, not video). *(D6)* |
| `higgsfield-marketplace-cards` | **`listing-cards`** — or **drop** | Borderline. *(D6)* |
| `durer` | **`line-art-vectorizer`** | B/W line art → clean SVG. |
| `figure-harvest` | **`diagram-redraw`** | Redraw reference diagrams house-style. |
| `skills/figures/from-ai1-cli/` (cajal et al.) | **`figure-planner`** (+ keep library as `docs/figures/`) | Source-of-truth decision needed. *(D5)* |

Alias policy: `GLOSSARY.md` gets one row per rename (old → new → one-liner); the Phase 3 dispatcher resolves every old name; SKILL.md frontmatter keeps old names in the trigger text so muscle memory and external references still work.

### 2b. Runtime-file name map (Gate-2 addition — "vox" is a trademark, remove it everywhere)

Applied to files already in this repo at Gate 2; applied to the rest as they are vendored in
Phase 3 (each vendor copy is renamed on arrival, all references swept in the same commit).

| Old runtime name | New name |
|---|---|
| `vox_graphics.py` | **`animated_graphics.py`** (see spec below) |
| `vox_scenes.py` (per-reel scene file) | `scenes.py` |
| `vox-preflight.sh` | `preflight.sh` |
| `vox_run.sh` | `run.sh` (wrapped by `art run`) |
| `vox_compile.py` | `compile.py` |
| `vox_align.py` | `align.py` |
| `vox_outro.py` | `outro.py` |
| `vox_pantry.py` | `pantry.py` |
| `vox_short.py` | `shorts.py` |
| `vox_emit.py` | `stage_publish.py` |
| `vox_convert.py` | `convert.py` |
| `vox_fill_slates.py` | `fill_slates.py` |
| `vox_remotion.py` | `remotion_scenes.py` |
| `vox_variant.py` | `brand_variant.py` |
| `vox_update.py` | `update_reels.py` |
| `vox_audit.py` | `inventory.py` |
| `VOX_PALETTE`, `VOX_NO_DRAWTEXT`, `VOX_CHROME(_MODE)` | `ART_PALETTE`, `ART_NO_DRAWTEXT`, `ART_CHROME(_MODE)` — old names accepted as fallback during the Phase 3 transition |
| "vox slate", "vox reel" (terminology in docs and slate-card text) | "slate", "reel" |

**`animated_graphics.py` spec (Phase 3 behavior upgrade, per Gate-2 feedback):** for each beat
it looks at the concept and decides whether **Remotion or Manim** can animate it; if one can,
it renders. If neither tool fits, it does not emit a bare pipeline slate — it replaces the
placeholder with a **request card addressed to the human**: "generate 5–10 seconds of video
with a generative-AI tool," **plus a suggested prompt** written for that beat. The slate text
("PIPELINE → render vox_graphics.py scene B06_*") becomes that human-readable request; the
pantry contract (§6a) then conforms whatever the human drops in.

---

## 3. Dedup list (Gate 1 approval item)

**3.1 `vox-explainer` vs `vox-explainer-unreal` → keep `vox-explainer`, delete the other.** Evidence: `MOTION.md`/`REMOTION.md` byte-identical; `SKILL.md` differs by one path reference; the real divergence is `manim/vox_graphics.py` — the vox-explainer copy (728 lines) is the **descendant** with the 5-palette registry (`VOX_PALETTE=teardown|newsprint|neu|medhavy|humanitarians`) that the audience presets depend on; the unreal copy (689 lines) is the hardcoded-palette ancestor. The unreal folder also carries stray QC artifacts (`layout_audit*` + 3 PNGs) that get deleted regardless. Nothing worth salvaging from the unreal copy.

**3.2 Twin scouts → one `scout`; `cli-scout` stays separate.** See §2. The scan script is parameterized by output dir; card formats and selection doctrine become reference files. `scout` writes `video-ideas.md`, `cli-scout` writes `cli-ideas.md`.

**3.3 `hai`/`medhavy`/`neu` → one `audience-preset` skill.** All three are SKILL.md-only wrappers around the *same* shared script (`vox_variant.py <REEL> {hai|medhavy|neu}`), same 6-step flow, differing only in data (register, voice env var, palette, outro, tangent flavor). `neu` additionally carries ~15 lines of Northeastern brand-law guardrails — these become conditional rules attached to the `neu` brand entry. Runtime is already single-source.

**3.4 `mini-bio` + `voxbio` → one `bio` skill** *(D1b resolved)* — they share the story law and a byte-identical `bn_layout.py`; visual treatment is chosen per beat like any other reel (§6a), and `--length` (default 3:00) replaces the mini/long split. voxbio's stray `HANDOFF.md` working file is removed. |

**3.5 Shared-file dedup (move to one shared lib in Phase 3).** Byte-identical today: `bn_layout.py` (mini-bio ↔ bears-doodles), `useBeatData.ts`, `LyricLayer.tsx`, `AudioVisualizer.tsx` (muzak ↔ muzak-overlay). Divergent, reconcile to the named superset: `theme.ts` and `MusicVideo.tsx` (muzak copy is the superset), `vox_graphics.py` (vox-explainer 728-line palette-registry copy is canonical; `brutalist/PY/` 689-line copy used by riff gets reconciled when riff's runtime is vendored). Genuinely different despite shared names (keep separate): `Root.tsx`/`index.ts`/`package.json` per Remotion project, `new_video.py` (doodle vs music scaffolders), per-skill `style.md`/`pedagogy.md`.

**3.6 `muybridge` supersedes the session skill `cajal-video-tutorial`** (same skill, muybridge is the newer superset) — muybridge becomes the source of truth under its new name.

**3.7 Junk to remove (accounted here per the no-silent-deletes rule):** `vox-explainer-unreal/manim/layout_audit.{json,md}` + `layout_audit_frames/` (3 PNGs), `voxbio/HANDOFF.md`, stray `.DS_Store` files.

---

## 4. Verified keys & installs (corrections to the brief)

What the code actually consumes — this drives `.env.example`, the `setup` doctor, and `CAPABILITIES.md` in Phase 4.

| Credential | Reality (verified) | Unlocks | Cost |
|---|---|---|---|
| `ELEVENLABS_API_KEY` | env var, POST `api.elevenlabs.io` | ALL narration: sketch/math/collage explainers, bios, kids, story-film, publisher audio | paid |
| `ELEVENLABS_VOICE_*` (`NIKBEARBROWN`, `MEDHAVY`, `HUMANITARIANS`, `VOICE_ID`) | env vars (IDs, semi-sensitive) | which cloned voice speaks; audience presets | free (IDs) |
| `HIGGSFIELD_API_KEY`, `MINIMAX_API_KEY` | Blank placeholders in `.env.example` (kept per Gate-1 feedback — the user's environment carries them and docs explain the passthrough). The scripts themselves shell out to the external `higgsfield` CLI (`higgsfield auth login`, gated on `account status`, parsed with `jq`); the doctor accepts either a CLI login or the env vars as "ready" | AI image/video: lyric-resync, dance-video, bio photoreal, collage stills, ai-asset-gen | paid |
| **YouTube Data API** | **NOT an env var.** Desktop-app OAuth: `client_secret.json` (from GCP) + cached `youtube_token.json` | youtube-publisher, video-inventory publish path | free quota |
| `ANTHROPIC_API_KEY` | **Not used by any skill in this repo** (the driving CLI is the LLM). Only ai1-cli batch scripts call `api.anthropic.com` | nothing in this toolkit directly | — |
| `FAL_KEY` | fal.ai, optional style-LoRA path | optional image styling | paid, optional |
| `VOX_PALETTE`, `VOX_NO_DRAWTEXT`, `VOX_CHROME(_MODE)`, `BB_PUBLISH_WORKSPACE`, `RIFF_PROJECT` | local behavior toggles, no cost | palette/caption/render/publish config | free |
| `REMOTION_MAPBOX_TOKEN` | referenced in a best-practices doc only; no active skill wires it | (doc only) | — |

**Local, no-key capabilities** (the free ladder): ffmpeg/ffprobe (nearly every skill), Manim + LaTeX (`MathTex`) + dvisvgm, faster-whisper (captions/alignment), librosa + soundfile (beat grids), Pillow (previz, stills), vtracer (SVG tracing), Node ≥ 18 + Remotion 4.x + React 18.3.1 (+ `sharp` for SVG→PNG), `jq`/`curl`.

**Install reality:** the two parent `requirements.txt` files are identical and fully **unpinned** (`requests, mutagen, fal-client, librosa, soundfile, numpy, faster-whisper`); `manim`, `Pillow`, `vtracer`, `manimpango`, and the Google API trio are imported but listed nowhere. Node projects consistently use Remotion `^4.0.0` / React `18.3.1`; only `ai1-cli/remotion` pins exact versions (Remotion `4.0.448`). Phase 4 writes one pinned `requirements.txt` + per-Remotion-project lockfiles.

---

## 5. Runtime-vendor list (Gate 1 approval item)

Everything below is **read-only copied from the parents into this repo** (never modifying the parents), landing in a new top-level `runtime/` unless noted. Order = priority.

1. **The vox spine → `runtime/scripts/`** — from `vox/scripts/`: `vox_run.sh`, `vox_compile.py`, `generate_audio.py`, `vox_align.py`, `vox_outro.py`, `vox_pantry.py`, `vox_short.py`, `vox_emit.py`, `vox_convert.py`, `vox_fill_slates.py`, `vox_remotion.py`, `vox_variant.py`, `vox_update.py`, `vox_audit.py` (+ `brutalist_update.py`, teardown rerender pair). **Reconciliation rule (per Gate-1 feedback): `vox/` is the more recent toolkit, derived from `unreal-reels/` — `vox/scripts/` is canonical wherever both carry a script**; the `unreal-reels/scripts/` copy is consulted only for scripts vox lacks (e.g. the songbird/dance generators), and each choice is still diff-verified and documented.
2. **`runtime/manim/vox_graphics.py`** — single canonical copy (the 728-line palette-registry version); all skills import from here.
3. **Design constitution → `runtime/design/`** — `vox/DESIGN.md`, `vox/voices/` (7 register dirs), `vox/fonts/` (96K TTFs — license check at D2). Note: the brief's expected `vox/reference/pedagogy.md` **does not exist** as one file; pedagogy lives per-aspect (`kids/`, `teardown-script/`) and is already vendored with those skills.
4. **Medhavy bookends Remotion project → `runtime/remotion-bookends/`** — `vox/aspects/remotion-pass/remotion/` (280K, no node_modules); hard requirement of `youtube-publisher` and the upstream of `slate-filler`'s scenes.
5. **Sketch-explainer canonical scripts** — already vendored byte-identical in `bears-doodles/scripts/` (16 files); `math-explainer`'s `../bears-doodles/` reach-outs get repointed, not re-vendored.
6. **`component-showcase` (riff) runtime → vendored under the skill** — `brutalist/remotion/` (2.1M source tree: `src/{riff,harness,fixtures}`, `slate_run.sh`, configs) + reconcile `brutalist/PY/vox_graphics.py` to the canonical copy.
7. **Figures satellite** — `graphs.sh` and `svg-to-png.mjs` already vendored (parents are the confirmed source of truth, currently identical); vendor `ai1-cli/remotion/` scaffold **only if** `code-animated-explainer` keeps its studio-scaffold flow (it references that project's structure) — proposed: yes, into the skill's `templates/`.
8. **Higgsfield satellite — nothing to vendor.** The runtime is the external `higgsfield` CLI (binary + login), documented in INSTALL.md; the `references/*.md` prompt libraries are already vendored with the assets skills.
9. **Path hygiene sweep (Phase 3, after vendoring):** replace every `/Users/nik/...`, `/Users/bear/...`, `~/ai`, `books/vox`, `books/unreal-reels`, and `../vox/` reference with repo-relative paths or env-var defaults (`BB_PUBLISH_WORKSPACE` pattern). Known sites: `brownblue/scripts/silent_publish.py`, `brownblue/SKILL.md`, `greybox/scripts/greybox.py` (font dir), `notebooklm-youtube/scripts/pipeline.py`, `remotion-pass/remotion/README.md`, `simulation/HOWTO-FELLOWS.md`, `bears-doodles` scripts (`~/ai` venv).
10. **Never vendor:** any `.env` (parents' contain live keys), `node_modules`, rendered media, `vox/remotion/_bench` (4.3M, riff's real runtime is item 6), parents' output folders (`reels/`, `music/`, `physics/`, `lectures/`).

---

## 6. Unified command grammar (Phase 3 target)

Single entry point at repo root — proposed name **`art`** *(D8)*: `./art <skill> <target> [--flags]`, with `./art --list`, `./art <skill> --help` in one shared format, alias resolution from `GLOSSARY.md`, and a shared `beat_sheet.json` schema (published as `runtime/schema/beat_sheet.schema.json` — the bears-doodles template schema is the seed; muzak/songbird beat variants become documented extensions). The audio-first, phase-gated discipline stays; gates become explicit named stops (`--gate` prints what the human must approve).

### 6a. The slate-placeholder + pantry contract (the human/AI division, verbatim into every skill README)

This is how the pipeline actually divides the work (per Gate-1 feedback; implemented today by `vox_compile.py` + `vox_pantry.py`):

1. The tool **generates every piece of media it can** — Manim, Remotion, or any other local tool — and composites it per beat.
2. For media it **cannot fake** (real captures, archival footage, a screen recording, a performance), it does not improvise a stand-in: it emits a **slate placeholder** for that beat, named for its slot.
3. The human drops the real media into **`pantry/`**.
4. The tool **checks the intake**, usually strips its sound, **cuts or extends it to fit the beat**, gives it the proper slot name, and copies it into place for the composite.

So the human never touches timelines or naming — they supply context, approvals, and the captures the CLI can't produce; the tool does all conforming. This paragraph (adapted per skill) satisfies the brief's §1.6 "human/AI division is explicit" requirement, and it replaces the retired "greybox paper" previz: a first pass of any reel *is* the previz — slates standing in for exactly the media the human owes.

---

## 7. Examples & learning path (Phase 5 preview)

Existing: `cli--compression-journey`, `vox-explainer--size-paradox`, `vox-slate--base-rate`, `muzak--c-is-for-cookie`, `00-unreal-reels-demos` (text seeds only). None has a rebuild README. Missing entirely: examples for sketch-explainer, math-explainer, lyric-resync, dance-video, kids-video, recitation-film, bios, code-animated-explainer, youtube-publisher. Phase 5 restores source inputs for one example per type from the parents' project folders and orders `LEARN.md`. The zero-key ladder start is the **slate cut**: run a reel through the compiler with no keys and no pantry media — every ungeneratable beat renders as a named slate (`vox-slate--base-rate` is already this shape), teaching the pantry contract (§6a) before any key is bought. Ladder: slate cut (no keys) → silent sketch (no keys) → narrated sketch (ElevenLabs) → collage-explainer → AI-video types (higgsfield CLI / keys) → publisher (OAuth).

---

## 8. Decisions needed at this gate (D1–D9)

| # | Decision | Recommendation |
|---|---|---|
| D1a | ~~Scouts~~ — **RESOLVED**: `scout` (twins merged, → `video-ideas.md`) + `cli-scout` kept (→ `cli-ideas.md`) | — |
| D1b | ~~Bios~~ — **RESOLVED**: one `bio` skill, `--length` default 3:00 | — |
| D1c | ~~muybridge name~~ — **RESOLVED**: `remotion-explainer` | — |
| D2 | ~~License~~ — **RESOLVED**: MIT for code; bundled fonts keep their OFL notices | — |
| D3 | ~~Presets~~ — **RESOLVED**: keep all three (`hai`, `medhavy`, `neu`) as brand data files | — |
| D4 | ~~Deck/lecture~~ — **RESOLVED**: stays out of scope; revisit after Phase 6 | — |
| D5 | ~~Figures~~ — **RESOLVED**: promote ai1-cli copies to a real `figure-planner` skill | — |
| D6 | ~~Product skills~~ — **RESOLVED**: park `product-photos` / `listing-cards` unlisted | — |
| D7 | ~~Key rotation~~ — **RESOLVED**: old keys deleted, new keys issued; they live only in the user's environment / untracked `.env` | — |
| D8 | ~~Entry point~~ — **RESOLVED**: `art` | — |
| D9 | ~~Baseline commit~~ — **done** (root commit `8cccb4e`, local only, nothing pushed) | — |
| D10 | ~~greybox~~ — **RESOLVED**: delete (removal documented in MANIFEST; the no-key slate cut replaces it in the learning ladder) | — |

**Resolved at Gate 1 (from your feedback):** all keys live in `.env` with blank `HIGGSFIELD_API_KEY`/`MINIMAX_API_KEY` placeholders and a documented env-var passthrough; `vox/scripts/` is canonical over `unreal-reels/scripts/` (vox is the newer, derived toolkit); the human/AI division is the slate-placeholder + pantry contract (§6a).

---

## 9. Phase schedule (gates preserved from the brief)

| Phase | Work | Commit | Gate asks the human |
|---|---|---|---|
| **1 (this)** | Audit; this plan | **Baseline commit** of gathered state + this plan + minimal `.gitignore` (`.DS_Store`, `.env`, `node_modules/`, `out/`) | D1–D9 above |
| **2** | Apply approved name map via `git mv`; delete `vox-explainer-unreal` + junk (§3.7) + `greybox` per D10; merge scouts/presets/bios per D1; write `GLOSSARY.md` with alias table; update `MANIFEST.md` names. **No behavior changes.** | "Phase 2: rename + dedup + aliases" | Spot-check names/aliases; confirm nothing lost (MANIFEST accounts for every merge/delete) |
| **3** | Vendor runtime per §5 (reconciling the two vox-spine copies, documented per file); path-hygiene sweep (§5.9); shared-lib dedup (§3.5); `art` dispatcher + shared `--help` + shared schema. Skills run in isolation. | "Phase 3: vendored runtime + unified grammar" | Run one skill end-to-end from a fresh clone (no `../` reach-outs) |
| **4** | `.env.example` (from §4, grouped by feature), `INSTALL.md` (pinned deps per OS), `setup` doctor with per-feature readiness table, `CAPABILITIES.md` | "Phase 4: setup + capability matrix" | `./setup` output reviewed on the human's machine |
| **5** | One example per type with source inputs restored; per-example rebuild READMEs; `LEARN.md` ladder (§7); verify no-key examples rebuild | "Phase 5: examples-first learning path" | Human rebuilds the no-key + ElevenLabs examples |
| **6** | Rewrite `README.md` front door; `CONTRIBUTING.md` (skill folder contract: `SKILL.md` + `README.md` + scripts, one shape); `LICENSE` per D2; run the brief's §6 acceptance test in a clean container; fix gaps | "Phase 6: front door + acceptance" | Final acceptance sign-off |

**Git logistics note:** commits are made from the repo on your machine. The session's mounted view of the folder cannot *delete* files (git lock cleanup leaves stale `index.lock`-type crumbs that I move into a junk folder rather than delete); `git add`/`git commit` complete correctly via git's rename path — verified live. If any git step wedges, the fallback is: I stage exact file changes + hand you the exact `git` commands to run locally. Nothing is pushed to the empty GitHub remote unless you ask.

---

*Gate 1 closed with all decisions resolved — Phase 2 (rename + dedup + aliases) authorized.*
