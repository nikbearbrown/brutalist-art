# MANIFEST — brutalist-art gathered skills (annotated inventory)

40 skills copied from `bear-textbooks/` on the first refactor pass. Each row: the folder here,
its original source path, what it does, and dependency/duplicate flags. Media, `node_modules`,
and `.git` were excluded. Paths in "Source" are relative to `bear-textbooks/`.

## skills/make — the reel factory (scouts → builders → helpers → ops)

### Scouts (mine a book → review cards, never videos)
| Skill | Source | What it does | Flags |
|---|---|---|---|
| `cli-scout` | `books/vox/aspects/cli-scout` | Mines a book for "X with Claude" CLI-video candidates → writes `<book>/youtube/cli-ideas.md`. BUILD vs RESEARCH lane by subject. | Produced the current `cli-ideas.md` files. |
| `vox-scout` | `books/vox/aspects/scout` | Mines a book for vox-explainer candidates → `<book>/youtube/video-ideas.md`. | frontmatter name = `vox-scout`. |
| `bears-doodles-scout` | `books/unreal-reels/aspects/explainer/scout` | Mines a book for Bear's Doodles candidates → `<book>/vids/`. | frontmatter name = `bears-doodles-scout`. Different lane from vox-scout. |

### Builders (approved concept → beat sheet → reel)
| Skill | Source | What it does | Flags |
|---|---|---|---|
| `teardown-script` | `books/vox/aspects/teardown-script` | Turns any text into a style-agnostic Teardown-voice script + `beat_sheet.json` (shot.source left open). Upstream of the vox builders. | Ships `reference/example/beat_sheet.json`. |
| `cli` | `books/vox/aspects/cli` | "CLI video" — Onda terminal in, moving output out; fixed spine (INTRO→PROBLEM→ASK→CODE→OUTPUT→CHANGE→…→SUMMARY→NEXT→OUTRO). | Ships `reference/example-cli-beat_sheet.json`. |
| `simulation` | `books/vox/aspects/simulation` | Medhavy-register "Build it with Claude Code + Manim" workflow reel. | Emits `beat_sheet.json` + `vox_scenes.py`. |
| `vox-explainer` | `books/vox/aspects/explainer/vox-explainer` | Editorial newsprint mixed-media compositing pipeline (Manim + Ken Burns + AI video + Remotion annotation plane). | **DUPLICATE** of `vox-explainer-unreal` — reconcile. |
| `vox-explainer-unreal` | `books/unreal-reels/aspects/explainer/vox-explainer` | Same skill, unreal-reels copy (isotype/paper-collage framing). | **DUPLICATE** of `vox-explainer`. |
| `bears-doodles` | `books/unreal-reels/aspects/explainer/bears-doodles` | ~1-min MinutePhysics progressive-disclosure sketch explainer. | |
| `brownblue` | `books/unreal-reels/aspects/explainer/brownblue` | 3–8 min pure-Manim 3Blue1Brown-style explainer. | Reuses bears-doodles scripts. |
| `brownblue-convert` | `books/unreal-reels/aspects/explainer/brownblue-convert` | Audits a doodle vs Brown Blue depth; rewrites into a deeper `-bb` version. | Ships `scripts/audit.py`. |
| `voxlit` | `books/unreal-reels/aspects/explainer/voxlit` | Vox-style film of a spoken-word literary recitation (performance = clock). | |
| `mini-bio` | `books/unreal-reels/aspects/bios/mini-bio` | Narrated mini-biography; photoreal Higgsfield footage alternating with Manim cards. | Ships `templates/fonts/`. |
| `voxbio` | `books/unreal-reels/aspects/bios/voxbio` | 3–5 min Vox editorial-collage biography on the greybox chassis. | |
| `muzak` | `books/unreal-reels/aspects/songbird/muzak` | Beat-synced music video from WAV + lyrics, mostly Remotion motion graphics (librosa beat analysis). | |
| `muzak-overlay` | `books/unreal-reels/aspects/songbird/muzak-overlay` | Adds karaoke lyrics + audiogram over an existing finished music video. | |
| `lyric-match` | `books/unreal-reels/skills/lyric-match` | Re-cuts an existing music video so each beat's clip is image-to-video (Hailuo) from the matching frame, cut to the lyric. | |
| `songbird-dance` | `books/unreal-reels/skills/songbird-dance` | Beat-synced dance reel — a character dances ON the beat via Higgsfield Seedance 2.0. | |
| `cubs` | `books/vox/aspects/kids` | Bear's Cubs — early-childhood (ages 1–5) concept films on the vox chassis with dev-psych gates (Gate K). | frontmatter name = `cubs`. |
| `unreal-reels` | `books/unreal-reels/SKILL.md` (+ README) | Top-level story-to-film orchestrator: one beat = one scene = one narrated line over one clip. | SKILL.md + README only. |
| `muybridge` | `books/ai1-cli/remotion/.agents/skills/muybridge` | Remotion explainer, scope-before-spectacle; silent/captioned by default. | ≈ session skill `cajal-video-tutorial`. |
| `arcads-collage-motion` | `books/unreal-reels/arcads-collage-motion` | Halftone paper-collage / stop-motion-graphic ads on the Arcads MCP (nano-banana-2 + Seedance). | |

### Decision helpers (previz / routing / pacing)
| Skill | Source | What it does | Flags |
|---|---|---|---|
| `greybox` | `books/unreal-reels/aspects/explainer/greybox` | Zero-cost deterministic scrapbook-collage previz from any `beat_sheet.json` (Pillow + ffmpeg). | Ships `scripts/greybox.py`. |
| `media-router` | `books/unreal-reels/skills/shared/media-router` | Recommends Manim/Remotion/T2I/T2V per beat to maximize learning (CTML + CLT). | |
| `pacing` | `books/unreal-reels/skills/shared/pacing` | Sizes a video to its content, not a clock; consolidation floor, rejects padding. | |

### Ops / maintenance
| Skill | Source | What it does | Flags |
|---|---|---|---|
| `remotion-pass` | `books/vox/aspects/remotion-pass` | Fills vox slate beats (no mp4) with vox-palette Remotion motion graphics. | Ships a Remotion project. |
| `update` | `books/vox/aspects/update` | Brings built reels up to latest specs (migrate outro, regen stale audio). Dry-run by default. | |
| `hai` | `books/vox/aspects/hai` | Audience variant → `beat_sheet.hai.json` (Humanitarians AI, Pragmatist register). | Never touches `beat_sheet.json`. |
| `medhavy` | `books/vox/aspects/medhavy` | Audience variant → `beat_sheet.medhavy.json` (Medhavy, Wonder register, Okabe-Ito). | Never touches `beat_sheet.json`. |
| `neu` | `books/vox/aspects/neu` | Audience variant → `beat_sheet.neu.json` (Northeastern, Lecture register, NU palette). | Never touches `beat_sheet.json`. |
| `riff` | `books/brutalist/remotion/SKILL.md` | Renders a visual unit with a made-up example and riffs on it in Teardown voice; compilation bench. | **SKILL.md only** (remotion tree not copied). |
| `remotion-best-practices` | `books/ai1-cli/remotion/.agents/skills/remotion-best-practices` | Reference: Remotion video-creation best practices in React. | Reference doc. |

## skills/upload — status + publish
| Skill | Source | What it does | Flags |
|---|---|---|---|
| `audit` | `books/vox/aspects/audit` | Audits every vox video across books; writes `vox/YOUTUBE.MD`. Deterministic, idempotent. | |
| `notebooklm-youtube` | `skills/notebooklm-youtube` | Turns NotebookLM `.mp4` downloads into chapter-ordered @MedhavyAI YouTube episodes (transcript + timestamped description + Remotion bookends). | The actual upload skill. |

## skills/assets — generation engines the reels pull from
| Skill | Source | What it does | Flags |
|---|---|---|---|
| `higgsfield-generate` | `books/higgsfield/.agents/skills/higgsfield-generate` | Images/videos/3D/audio via Higgsfield (Seedance, Nano Banana, Soul, Kling, Marketing Studio). | Core AI video/still engine. |
| `higgsfield-soul-id` | `books/higgsfield/.agents/skills/higgsfield-soul-id` | Trains a Soul Character (identity-faithful generation); returns a `reference_id`. | |
| `higgsfield-product-photoshoot` | `books/higgsfield/.agents/skills/higgsfield-product-photoshoot` | Brand/product/lifestyle/ad images. | Borderline (product, not video). |
| `higgsfield-marketplace-cards` | `books/higgsfield/.agents/skills/higgsfield-marketplace-cards` | Compliant marketplace listing image sets. | Borderline (product, not video). |
| `durer` | `books/higgsfield/.agents/skills/durer` | Clean gate-passing SVGs from b+w line art (Midjourney + vtracer). | Feeds figures/Remotion. |
| `figure-harvest` | `figure-harvest` | Redraws Wikipedia diagrams from `facts/<topic>` into house-style figures. | Ships demo PNGs. |

## skills/figures — gathered from ai1-cli (repo-native form)
`cajal`, `figures`, `graphs`, `tables` don't exist as `SKILL.md` skills anywhere; in the repo
they live in `books/ai1-cli/` as a script + prompt libraries. Copied here under
`skills/figures/from-ai1-cli/`: `graphs.sh` (graphs/tables renderer), `_lib_design-figure-architect-prompt.md`
(the `figures` skill in prompt form), `88-appendix-cajal.md` (the CAJAL command set + SVG Style
Guide), the figure-craft chapter/appendix docs, and `svg-to-png.mjs` (the renderer). Full table
in `skills/figures/POINTER.md`. Note: `dataviz` and up-to-date `cajal/figures/graphs/tables` also
exist as Cowork session skills — pick a source of truth in refactor step 2.

## examples — one mp4-stripped "render this" starter per type
| Folder | Source | Type it demonstrates |
|---|---|---|
| `00-unreal-reels-demos/` | `books/unreal-reels/examples` | Purpose-built `bios-demo`, `explainer-demo`, `songbird-demo`. |
| `cli--compression-journey/` | `books/embedded-ai/youtube/cli-compression-journey` | `cli` video (Onda terminal + animated output). |
| `vox-explainer--size-paradox/` | `books/cancer-nanomedicine/youtube/vox-size-paradox` | `vox-explainer` compositing reel. |
| `vox-slate--base-rate/` | `books/unreal-reels/reels/vox-base-rate` | vox slate cut. |
| `muzak--c-is-for-cookie/` | `books/unreal-reels/music/c-is-for-cookie` | `muzak` music video. |

Each keeps its `beat_sheet.json`, scene code (`vox_scenes.py`/manim), and scripts; the rendered
`*.mp4/.wav/.mp3/.png` were stripped so the folder is a clean "author + render" starting point.

## Refactor step 2 (next, not done here)
1. Reconcile the two `vox-explainer` copies into one.
2. Vendor or wire in the shared vox runtime (`vox/scripts/`, `vox_graphics.py`, `DESIGN.md`,
   `voices/`, `.env`) so `skills/make/*` are runnable from this repo.
3. Decide on the deck/lecture group and the figure/data session skills.
4. Normalize each skill to a single command grammar and a shared `beat_sheet.json` schema.
