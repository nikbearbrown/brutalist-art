# REFRACTOR-PLAN — brutalist-art → clone-and-go video toolkit

*Phase 1 deliverable (Audit & Plan) per `REFACTOR-BRIEF.md`. Filename spelling kept as the brief specifies.*
*Status: **AWAITING HUMAN SIGN-OFF (Gate 1)** — nothing below has been executed yet.*
*Audit method: every claim in this plan was verified against the code — the full skill tree in this repo plus code snapshots of the five parent toolkits (`vox/`, `unreal-reels/`, `ai1-cli/`, `brutalist/`, `higgsfield/`). Diffs by `md5sum`/`diff`; env vars by grepping `os.environ` / `process.env` / API hosts.*

---

## 1. What the audit found (state of the repo)

- **40 gathered skills** under `skills/{make,upload,assets,figures}`, copied faithfully: every copy checked against its parent original is **byte-identical (zero drift since gather)**, except one stray junk set (`vox-explainer-unreal/manim/layout_audit*` QC artifacts).
- **The repo has no git history yet.** Branch `main`, zero commits, remote `github.com/nikbearbrown/brutalist-art` (empty). "Preserve history via `git mv`" therefore starts from a clean slate: Phase 1 makes the **baseline commit** of the gathered state, so every later rename diffs against it.
- **The skills are not runnable in isolation**, exactly as the brief warns. The dominant gap is the **vox script spine** (`vox_run.sh` + 15 `vox_*.py` scripts) — referenced by at least 12 skills, present in this repo **zero** times, and existing in **two divergent parallel copies** in the parents (`vox/scripts/` and `unreal-reels/scripts/`).
- **Hardcoded machine paths will break any clone**: `/Users/nik/...` (brownblue publish, greybox fonts, voxbio HANDOFF), `/Users/bear/...` (remotion-pass README), `~/ai` venv assumptions (bears-doodles, greybox, brownblue), and `books/vox` / `books/unreal-reels` repo-relative reach-outs (notebooklm-youtube `pipeline.py`, simulation docs).
- **The brief's key list was wrong in three important ways** (verified from code — see §4): there is no `HIGGSFIELD_API_KEY` or `MINIMAX_API_KEY` anywhere (AI image/video goes through the external `higgsfield` CLI's own login); YouTube auth is file-based OAuth (`client_secret.json` + `youtube_token.json`), not an env var; and no skill in this repo calls the Anthropic API at all — the driving CLI *is* the LLM runtime.
- **⚠️ Real secrets are committed in the parent toolkits** (not in this repo): live `ELEVENLABS_API_KEY` and `FAL_KEY` values in `vox/.env`, `unreal-reels/.env`, and `ai1-cli/remotion/.env`. See §8, decision D7 — those keys should be rotated, and vendoring must never copy a `.env`.
- **Examples cover only ~5 of ~20 video types**, and none has a rebuild README. The no-key ladder start (previz / silent sketch) has no example at all yet.

---

## 2. Final proposed name map (Gate 1 approval item)

Rules applied: plain video-production jargon, no house codenames as identity, vendor names allowed in help text only. Old names survive as **aliases** (Phase 2 alias table in `GLOSSARY.md`).

### Scouts → one skill
| Old | New | What it makes |
|---|---|---|
| `vox-scout`, `bears-doodles-scout`, `cli-scout` | **`idea-scout`** with `--style collage\|sketch\|terminal` | Mines a book/text for video candidates → review cards. |

Evidence: `vox-scout` and `bears-doodles-scout` are near-twins — same 4-file skeleton, same command grammar, `scan_book.py` differs **only in the output directory** (3 lines). Their card formats and selection doctrine become per-style data files. `cli-scout` is a cousin (SKILL.md-only, different card schema, BUILD/RESEARCH lanes); it merges cleanly **only if** its card schema is templated out to a reference file like the others. **Recommended: merge all three**; fallback option is to merge two and keep a separate `terminal-scout`. *(D1a)*

### Builders
| Old | New | Notes |
|---|---|---|
| `bears-doodles` | **`sketch-explainer`** | MinutePhysics-style sketch animation. |
| `brownblue` | **`math-explainer`** | 3Blue1Brown-style pure-Manim. |
| `brownblue-convert` | **`explainer-deepen`** | Audit + rewrite a sketch into a deeper math-explainer. |
| `vox-explainer` (+ `vox-explainer-unreal` **merged in, deleted**) | **`collage-explainer`** | Editorial newsprint mixed-media. See dedup §3.1. |
| `voxlit` | **`recitation-film`** | Literary recitation as the master clock. |
| `mini-bio` + `voxbio` | **`bio-documentary`** with `--style photoreal\|collage` | See dedup §3.4; option to keep two skills. *(D1b)* |
| `cli` | **`terminal-screencast`** | Fixed-spine CLI video. |
| `simulation` | **`code-walkthrough`** | "Build it with Claude Code + Manim" reel. |
| `teardown-script` | **`script-writer`** | Any text → script + `beat_sheet.json`. |
| `muzak` | **`music-video`** | Beat-synced from WAV + lyrics. |
| `muzak-overlay` | **`lyric-overlay`** | Karaoke lyrics + audiogram over finished video. |
| `lyric-match` | **`lyric-resync`** | Re-cut existing video to the words (Hailuo image-to-video). |
| `songbird-dance` | **`dance-video`** | Character dances on the beat (Seedance). |
| `cubs` | **`kids-video`** | Ages 1–5, dev-psych gated. |
| `unreal-reels` (orchestrator) | **`story-film`** | Story → narrated AI film. *(new — not in brief's table)* |
| `muybridge` | **`code-animated-explainer`** *(brief proposed `remotion-explainer`; "Remotion" is a vendor name — pick one)* *(D1c)* | Scope-before-spectacle Remotion explainer. |
| `arcads-collage-motion` | **`collage-ads`** | Halftone paper-collage ads. *(new)* |

### Decision helpers & ops
| Old | New | Notes |
|---|---|---|
| `greybox` | **`previz`** | Already jargon — keep (brief-approved direction). |
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

---

## 3. Dedup list (Gate 1 approval item)

**3.1 `vox-explainer` vs `vox-explainer-unreal` → keep `vox-explainer`, delete the other.** Evidence: `MOTION.md`/`REMOTION.md` byte-identical; `SKILL.md` differs by one path reference; the real divergence is `manim/vox_graphics.py` — the vox-explainer copy (728 lines) is the **descendant** with the 5-palette registry (`VOX_PALETTE=teardown|newsprint|neu|medhavy|humanitarians`) that the audience presets depend on; the unreal copy (689 lines) is the hardcoded-palette ancestor. The unreal folder also carries stray QC artifacts (`layout_audit*` + 3 PNGs) that get deleted regardless. Nothing worth salvaging from the unreal copy.

**3.2 Three scouts → one `idea-scout`.** See §2. The scan script is parameterized by output dir; card formats and selection doctrine become per-style reference files.

**3.3 `hai`/`medhavy`/`neu` → one `audience-preset` skill.** All three are SKILL.md-only wrappers around the *same* shared script (`vox_variant.py <REEL> {hai|medhavy|neu}`), same 6-step flow, differing only in data (register, voice env var, palette, outro, tangent flavor). `neu` additionally carries ~15 lines of Northeastern brand-law guardrails — these become conditional rules attached to the `neu` brand entry. Runtime is already single-source.

**3.4 `mini-bio` vs `voxbio`.** Not duplicates — deliberate siblings (photoreal Higgsfield vs editorial-collage on the previz chassis) sharing a byte-identical `bn_layout.py`. Recommended: one `bio-documentary` skill with `--style`, since they share the story law and layout lib; acceptable alternative: two skills. voxbio's stray `HANDOFF.md` working file is removed either way. *(D1b)*

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
| **Higgsfield / Minimax-Hailuo / Seedance / Kling** | **NOT an env var.** External `higgsfield` CLI binary with its own `higgsfield auth login`; scripts gate on `higgsfield account status` and parse with `jq` | AI image/video: lyric-resync, dance-video, bio photoreal, collage stills, ai-asset-gen | paid |
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

1. **The vox spine → `runtime/scripts/`** — from `vox/scripts/`: `vox_run.sh`, `vox_compile.py`, `generate_audio.py`, `vox_align.py`, `vox_outro.py`, `vox_pantry.py`, `vox_short.py`, `vox_emit.py`, `vox_convert.py`, `vox_fill_slates.py`, `vox_remotion.py`, `vox_variant.py`, `vox_update.py`, `vox_audit.py` (+ `brutalist_update.py`, teardown rerender pair). **Must be reconciled with the parallel divergent copy in `unreal-reels/scripts/`** — Phase 3 diffs each pair and keeps the superset, documenting each choice.
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

---

## 7. Examples & learning path (Phase 5 preview)

Existing: `cli--compression-journey`, `vox-explainer--size-paradox`, `vox-slate--base-rate`, `muzak--c-is-for-cookie`, `00-unreal-reels-demos` (text seeds only). None has a rebuild README. Missing entirely: examples for previz **(the zero-key ladder start)**, sketch-explainer, math-explainer, lyric-resync, dance-video, kids-video, recitation-film, bios, code-animated-explainer, youtube-publisher. Phase 5 restores source inputs for one example per type from the parents' project folders and orders `LEARN.md`: previz (no keys) → silent sketch (no keys) → narrated sketch (ElevenLabs) → collage-explainer → AI-video types (higgsfield CLI) → publisher (OAuth).

---

## 8. Decisions needed at this gate (D1–D9)

| # | Decision | Recommendation |
|---|---|---|
| D1a | Scouts: merge all three into `idea-scout`, or keep `terminal-scout` separate? | Merge all three |
| D1b | Bios: one `bio-documentary --style` or two skills? | One skill, style flag |
| D1c | `muybridge` → `remotion-explainer` (brief) or `code-animated-explainer` (no vendor name)? | `code-animated-explainer` |
| D2 | License for the repo (brief says ask). Also: the vendored fonts (Montserrat OFL — fine; verify `vox/fonts/`). | MIT for code; keep font OFL notices |
| D3 | Which audience presets survive as brand data files: `hai`, `medhavy`, `neu` — all three? | Keep all three (they're now just data) |
| D4 | Deck/lecture skills (`deck-lecture`, `lecture`, `animated-deck`, …) — still out of scope? | Keep out; revisit after Phase 6 |
| D5 | Figures source of truth: promote ai1-cli copies to a real `figure-planner` skill, or treat Cowork session skills as truth and keep these as `docs/figures/` library? | Promote to skill; session skills stay upstream inspiration |
| D6 | `product-photos` / `listing-cards` (non-video Higgsfield skills): keep, drop, or park in `skills/assets/` unlisted? | Park (keep folders, exclude from the front-door skill list) |
| D7 | **Rotate the live `ELEVENLABS_API_KEY` + `FAL_KEY` committed in `vox/.env`, `unreal-reels/.env`, `ai1-cli/remotion/.env`** (parent repos — outside my write scope, flagged per brief) | Rotate now |
| D8 | Entry-point command name: `art`? (alternatives: `reel`, `studio`) | `art` |
| D9 | Approve Phase 1 baseline commit as described in §9 (repo currently has zero commits) | Approve |

---

## 9. Phase schedule (gates preserved from the brief)

| Phase | Work | Commit | Gate asks the human |
|---|---|---|---|
| **1 (this)** | Audit; this plan | **Baseline commit** of gathered state + this plan + minimal `.gitignore` (`.DS_Store`, `.env`, `node_modules/`, `out/`) | D1–D9 above |
| **2** | Apply approved name map via `git mv`; delete `vox-explainer-unreal` + junk (§3.7); merge scouts/presets/bios per D1; write `GLOSSARY.md` with alias table; update `MANIFEST.md` names. **No behavior changes.** | "Phase 2: rename + dedup + aliases" | Spot-check names/aliases; confirm nothing lost (MANIFEST accounts for every merge/delete) |
| **3** | Vendor runtime per §5 (reconciling the two vox-spine copies, documented per file); path-hygiene sweep (§5.9); shared-lib dedup (§3.5); `art` dispatcher + shared `--help` + shared schema. Skills run in isolation. | "Phase 3: vendored runtime + unified grammar" | Run one skill end-to-end from a fresh clone (no `../` reach-outs) |
| **4** | `.env.example` (from §4, grouped by feature), `INSTALL.md` (pinned deps per OS), `setup` doctor with per-feature readiness table, `CAPABILITIES.md` | "Phase 4: setup + capability matrix" | `./setup` output reviewed on the human's machine |
| **5** | One example per type with source inputs restored; per-example rebuild READMEs; `LEARN.md` ladder (§7); verify no-key examples rebuild | "Phase 5: examples-first learning path" | Human rebuilds the no-key + ElevenLabs examples |
| **6** | Rewrite `README.md` front door; `CONTRIBUTING.md` (skill folder contract: `SKILL.md` + `README.md` + scripts, one shape); `LICENSE` per D2; run the brief's §6 acceptance test in a clean container; fix gaps | "Phase 6: front door + acceptance" | Final acceptance sign-off |

**Git logistics note:** commits are made from the repo on your machine. The session's mounted view of the folder cannot *delete* files (git lock cleanup leaves stale `index.lock`-type crumbs that I move into a junk folder rather than delete); `git add`/`git commit` complete correctly via git's rename path — verified live. If any git step wedges, the fallback is: I stage exact file changes + hand you the exact `git` commands to run locally. Nothing is pushed to the empty GitHub remote unless you ask.

---

*Gate 1 is open: reply with approvals/edits to D1–D9 (or "approve all as recommended") and Phase 2 begins.*
