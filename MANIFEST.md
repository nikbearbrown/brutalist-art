# MANIFEST — brutalist-art skills (provenance record)

40 skills were copied from `bear-textbooks/` on the gather pass (baseline commit `8cccb4e`);
Phase 2 renamed them to plain names, merged duplicates, and removed dead weight — every change
listed in the **Phase 2 change log** below and in `GLOSSARY.md` (old → new alias table).
Each row: the folder here, its original source path (relative to `bear-textbooks/`), what it
does, and flags. Media, `node_modules`, and `.git` were excluded at gather time.

## Phase 2 change log (renames applied; nothing else changed behavior)

- **Renamed** every skill to its plain name — full table in `GLOSSARY.md`.
- **Merged:** `vox-scout` + `bears-doodles-scout` → `scout` (bears card format kept in
  `scout/reference-sketch/`; its 3-line-divergent `scan_book.py` duplicate dropped);
  `hai` + `medhavy` + `neu` → `audience-preset` (originals now `audience-preset/brands/*.md`);
  `mini-bio` + `voxbio` → `bio` (voxbio's SKILL.md kept as `bio/reference/collage-style.md`).
- **Deleted:** `vox-explainer-unreal` (older duplicate of `explainer`: pre-palette-registry
  `animated_graphics.py`, plus stray `layout_audit*` QC artifacts), `greybox` (scrapbook previz,
  superseded by the slate+pantry flow — REFRACTOR-PLAN §6a), `voxbio/HANDOFF.md` (stray
  working file). Nothing deleted from git history; removed trees were moved to
  `CoWork/_to_delete/phase2-removed/` on disk.
- **Moved:** `remotion-best-practices` → `docs/remotion-best-practices/` (reference, not a command).
- **Examples renamed** to match (see GLOSSARY).

## skills/make — the reel factory (scouts → builders → helpers → ops)

### Scouts (mine a book → review cards, never videos)
| Skill | Source | What it does | Flags |
|---|---|---|---|
| `scout` | `books/vox/aspects/scout` (+ merged `books/unreal-reels/aspects/explainer/scout`) | Mines a book for video candidates → `<book>/youtube/video-ideas.md`. Sketch-style card format in `reference-sketch/`. | Merge of vox-scout + bears-doodles-scout. |
| `cli-scout` | `books/vox/aspects/cli-scout` | Mines a book for "X with Claude" CLI-video candidates → `<book>/youtube/cli-ideas.md`. BUILD vs RESEARCH lane. | Name kept. |

### Builders (approved concept → beat sheet → reel)
| Skill | Source | What it does | Flags |
|---|---|---|---|
| `script-writer` | `books/vox/aspects/teardown-script` | Turns any text into a style-agnostic script + `beat_sheet.json` (shot.source left open). Upstream of the builders. | Ships `reference/example/beat_sheet.json`. |
| `terminal-screencast` | `books/vox/aspects/cli` | CLI video — terminal in, moving output out; fixed spine (INTRO→PROBLEM→ASK→CODE→OUTPUT→…→OUTRO). | Ships `reference/example-cli-beat_sheet.json`. |
| `code-walkthrough` | `books/vox/aspects/simulation` | "Build it with Claude Code + Manim" workflow reel. | Emits `beat_sheet.json` + `scenes.py`. |
| `explainer` | `books/vox/aspects/explainer/vox-explainer` | The flagship: per-beat best-tool mp4 (Manim + Ken Burns + AI video + Remotion annotation plane), composited at the end. Two-axis shot system, slot contract. | Absorbed `vox-explainer-unreal` (deleted; older `animated_graphics.py` without the palette registry). |
| `sketch-explainer` | `books/unreal-reels/aspects/explainer/bears-doodles` | ~1-min-style MinutePhysics progressive-disclosure sketch explainer. | |
| `math-explainer` | `books/unreal-reels/aspects/explainer/brownblue` | 3–8 min pure-Manim 3Blue1Brown-style explainer. | Reuses sketch-explainer scripts. |
| `explainer-deepen` | `books/unreal-reels/aspects/explainer/brownblue-convert` | Audits a sketch vs math-explainer depth; rewrites into a deeper version. | Ships `scripts/audit.py`. |
| `recitation-film` | `books/unreal-reels/aspects/explainer/voxlit` | Film of a spoken-word literary recitation (performance = clock). | |
| `bio` | `books/unreal-reels/aspects/bios/mini-bio` (+ merged `aspects/bios/voxbio`) | Narrated biography, `--length` default 3:00. Editorial-collage treatment in `reference/collage-style.md`. | Ships `templates/fonts/`. Merge of mini-bio + voxbio. |
| `music-video` | `books/unreal-reels/aspects/songbird/muzak` | Beat-synced music video from WAV + lyrics (librosa). | |
| `lyric-overlay` | `books/unreal-reels/aspects/songbird/muzak-overlay` | Karaoke lyrics + audiogram over an existing finished video. | |
| `lyric-resync` | `books/unreal-reels/skills/lyric-match` | Re-cuts an existing video so each beat's clip is image-to-video from the matching frame, cut to the lyric. | |
| `dance-video` | `books/unreal-reels/skills/songbird-dance` | Beat-synced dance reel — a character dances ON the beat. | |
| `kids-video` | `books/vox/aspects/kids` | Early-childhood (ages 1–5) concept films with dev-psych gates (Gate K). | |
| `story-film` | `books/unreal-reels/SKILL.md` (+ README) | Story-to-film orchestrator: one beat = one scene = one narrated line over one clip. | SKILL.md + README only. |
| `remotion-explainer` | `books/ai1-cli/remotion/.agents/skills/muybridge` | Remotion explainer, scope-before-spectacle; silent/captioned by default. | Supersedes session skill `cajal-video-tutorial`. |
| `collage-ads` | `books/unreal-reels/arcads-collage-motion` | Halftone paper-collage / stop-motion-graphic ads (Arcads MCP). | |

### Decision helpers (routing / pacing)
| Skill | Source | What it does | Flags |
|---|---|---|---|
| `shot-planner` | `books/unreal-reels/skills/shared/media-router` | Recommends Manim/Remotion/T2I/T2V per beat to maximize learning (CTML + CLT). | |
| `duration-planner` | `books/unreal-reels/skills/shared/pacing` | Sizes a video to its content, not a clock; consolidation floor, rejects padding. | |

### Audience presets (brand variants)
| Skill | Source | What it does | Flags |
|---|---|---|---|
| `hai` | `books/vox/aspects/hai` (promoted from `audience-preset/brands/hai.md`) | Creates a HAI (Humanitarians AI) cut — Pragmatist register, Kokoro af_heart, humanitarians palette. Writes into a **new `hai-` directory**; adds CLI worked exercise (second-to-last) + Humanitarians AI outro (last). Brand spec: `audience-preset/brands/hai.md`. Runtime: `brand_variant.py hai`. | First-class skill; former `hai` re-promoted with directory convention + CLI exercise + outro beats. |
| `nbb` | `books/vox/aspects/nbb` (new first-class skill) | Creates a NikBearBrown cut — Teardown register (Feynman × MKBHD), ElevenLabs NIKBEARBROWN voice (paid, no Kokoro), teardown palette. Writes into a **new `nbb-` directory**; adds LLM exercise + dig-deeper (second-to-last) + NikBearBrown outro (last). Brand spec: `audience-preset/brands/nbb.md`. Runtime: `brand_variant.py nbb`. GATE P before audio spend. | First-class skill; nbb was the undocumented default brand — now explicit with directory convention + LLM exercise beat. |
| `audience-preset` | `books/vox/aspects/{hai,medhavy,neu}` | Brand variant for medhavy/neu/musinique → `beat_sheet.<brand>.json` sibling; hai/nbb/medhavy → `<brand>-` directory. Never touches the canonical sheet. Brands: `brands/{hai,medhavy,neu,nbb}.md`. | Merge of three skills; runtime is `brand_variant.py`. `hai` + `nbb` delegate to their own SKILL.md. |

### Ops / maintenance
| Skill | Source | What it does | Flags |
|---|---|---|---|
| `slate-filler` | `books/vox/aspects/remotion-pass` | Fills slate beats (no mp4) with palette-matched Remotion motion graphics. | Ships a Remotion project. |
| `reel-updater` | `books/vox/aspects/update` | Brings built reels up to latest specs (migrate outro, regen stale audio). Dry-run by default. | |
| `component-showcase` | `books/brutalist/remotion/SKILL.md` | Renders a visual unit with a themed example and critiques it; compilation bench. | **SKILL.md only** — runtime (`brutalist/remotion/`) vendored in Phase 3. |

## skills/upload — status + publish
| Skill | Source | What it does | Flags |
|---|---|---|---|
| `video-inventory` | `books/vox/aspects/audit` | Audits every published video across books; writes the status report. Deterministic, idempotent. | |
| `youtube-publisher` | `skills/notebooklm-youtube` | Publishes videos to YouTube in chapter order: transcript + timestamped description + Remotion bookends. | File-based OAuth (`client_secret.json` + `youtube_token.json`). |

## skills/assets — generation engines the reels pull from
| Skill | Source | What it does | Flags |
|---|---|---|---|
| `ai-asset-gen` | `books/higgsfield/.agents/skills/higgsfield-generate` | Images/videos/3D/audio via the Higgsfield CLI (Seedance, Nano Banana, Soul, Kling). | Core AI engine; external CLI auth. |
| `ai-character-id` | `books/higgsfield/.agents/skills/higgsfield-soul-id` | Trains an identity-faithful character; returns a `reference_id`. | |
| `product-photos` | `books/higgsfield/.agents/skills/higgsfield-product-photoshoot` | Brand/product/lifestyle/ad images. | **Parked, unlisted** (not video). |
| `listing-cards` | `books/higgsfield/.agents/skills/higgsfield-marketplace-cards` | Marketplace listing image sets. | **Parked, unlisted** (not video). |
| `line-art-vectorizer` | `books/higgsfield/.agents/skills/durer` | Clean gate-passing SVGs from b+w line art (vtracer). | Feeds figures/Remotion. |
| `diagram-redraw` | `figure-harvest` | Redraws reference diagrams from `facts/<topic>` into house-style figures. | Ships demo PNGs. |

## skills/figures — the figure/data library (from ai1-cli)
`figure-planner` (formerly `from-ai1-cli/`): `graphs.sh` (graphs+tables renderer),
`_lib_design-figure-architect-prompt.md` (the figures prompt system), `88-appendix-cajal.md`
(CAJAL command set + SVG Style Guide), the figure-craft chapter docs, and `svg-to-png.mjs`
(SVG → 300-DPI PNG, Node + sharp). Full table in `POINTER.md`. Promoted to a real skill
(SKILL.md authored in Phase 3) per Gate-1 decision D5.

## docs
| Doc | Source | What it is |
|---|---|---|
| `docs/remotion-best-practices/` | `books/ai1-cli/remotion/.agents/skills/remotion-best-practices` | Remotion video-creation best practices in React. Reference, not a command. |

## examples — one mp4-stripped "render this" starter per type
| Folder | Source | Type it demonstrates |
|---|---|---|
| `00-story-film-demos/` | `books/unreal-reels/examples` | `bios-demo`, `explainer-demo`, `songbird-demo` (text seeds). |
| `terminal-screencast--compression-journey/` | `books/embedded-ai/youtube/cli-compression-journey` | `terminal-screencast`. |
| `explainer--size-paradox/` | `books/cancer-nanomedicine/youtube/vox-size-paradox` | `explainer`. |
| `slate-cut--base-rate/` | `books/unreal-reels/reels/vox-base-rate` | The no-key slate cut (the previz — every ungeneratable beat renders as a named slate). |
| `music-video--c-is-for-cookie/` | `books/unreal-reels/music/c-is-for-cookie` | `music-video`. |

Each keeps its `beat_sheet.json`, scene code, and scripts; rendered media was stripped so the
folder is a clean "author + render" starting point. Phase 5 adds one example per remaining type
plus rebuild READMEs.

## Next (Phase 3, per REFRACTOR-PLAN)
1. Vendor the shared runtime (`vox/scripts/` spine — vox is canonical, it is the newer toolkit
   derived from unreal-reels; `animated_graphics.py`; DESIGN.md; voices/; fonts/; Medhavy bookends
   Remotion project; the component-showcase runtime from `brutalist/remotion/`).
2. Path-hygiene sweep (no `/Users/...`, `~/ai`, or `books/...` reach-outs).
3. The `art` dispatcher + shared `--help` + shared `beat_sheet.json` schema.
4. Author SKILL.md for `figure-planner`.
