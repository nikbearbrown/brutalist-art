# Agent Instructions

## HARD STOP — money rule (overrides everything)

**If any MCP server, tool, or command is about to spend money, purchase, pay, buy, subscribe,
renew, or otherwise incur a real-world charge — STOP. Do not do it. Ask the human first and wait
for an explicit yes.** This is a hard stop, not a confirmation you can auto-approve. It applies
even when the tool is official, sanctioned, and working perfectly, even under
`--dangerously-skip-permissions`, and even mid-batch or in an unattended run — a payment action
pauses the run and asks, every time. Named examples today: Vercel MCP's `buy_domain` and any
domain/deploy purchase, and any paid generation credit (ElevenLabs, Higgsfield, and the like).
When in doubt about whether something costs money, treat it as if it does and ask. Prefer the free
pipeline (Kokoro voice, read-only tools) for everything that doesn't require spend.

## Read this first

This repository contains a local production toolkit for educational videos and visual assets.
The toolkit is organized as agent skills. Do not infer a workflow from a skill's folder name:
open and read the relevant `SKILL.md` completely before using it.

The local skills live here:

```text
skills/
├── assets/   # image, diagram, vector, character, and product-visual workflows
├── figures/  # reference library only — contains no SKILL.md and is not invokable (see below)
├── make/     # video discovery, planning, production, adaptation, and repair
└── upload/   # inventory and publishing workflows
```

Find every local skill with:

```bash
find skills -type f -name SKILL.md -print | sort
```

Each skill's `SKILL.md` is authoritative for its triggers, inputs, phase gates, tools, output
locations, and stopping conditions. If a skill links to scripts, brand specifications, templates,
or references, resolve relative paths from that skill's directory and read only the material needed
for the current task.

## How agents use the skills

When the user names a skill, or their request clearly matches a skill's description:

1. Announce which skill is being used and why.
2. Read that skill's entire `SKILL.md` before modifying files or spending money.
3. Follow its phase gates and human-approval boundaries exactly.
4. Reuse its scripts, templates, palettes, voices, and output conventions.
5. Never claim that an artifact was rendered, generated, uploaded, or published unless it was
   actually produced and verified.

When several skills could apply, use the smallest set that covers the request. Builder skills make
artifacts; scout skills only propose candidates. A scout result still requires human selection
before a builder begins. Skills that say “never publishes” do not authorize publishing.

## Skill map

### Asset skills — `skills/assets/`

- `ai-asset-gen` — Higgsfield image, video, 3D, sound, music, advertising, and related generation.
- `ai-character-id` — train a reusable Soul Character identity model.
- `diagram-redraw` — identify useful source diagrams and redraw them in house style.
- `line-art-vectorizer` — generate or trace simple line art into quality-gated SVGs.
- `listing-cards` — create marketplace listing and A+-style product cards.
- `product-photos` — create brand-quality product photographs and campaign visuals.

### Discovery and planning — `skills/make/`

- `scout` — find Vox-style explainer candidates in a book.
- `claude-scout` — find Claude-branded explainer candidates.
- `cli-scout` — find “build/research X with Claude” candidates.
- `sim-scout` — find Manim and interactive D3/dataviz simulation candidates.
- `duration-planner` — derive runtime and pacing from content rather than a fixed clock.
- `shot-planner` — select Manim, Remotion, generated imagery, or generated video per beat.
- `script-writer` — local script-writing material; its manifest currently lacks normal frontmatter,
  so inspect it directly before relying on it as an invokable skill.

Scout skills produce review files, not finished media. The human chooses what gets built.

### Educational-video builders — `skills/make/`

- `explainer` — audio-first Vox-style mixed-media production pipeline.
- `math-explainer` — pure-Manim, concrete-before-abstract mathematical explanation.
- `sketch-explainer` — MinutePhysics-style progressive sketch explanation.
- `remotion-explainer` — textbook concept to short Remotion explainer.
- `claude-explainer` — Claude-desktop visual language with Bear's ElevenLabs voice.
- `deep-explainer` — 5–10 min documentary cut on the ai-explainer chassis; ~20–25% of body
  beats are vox beats animated from static pantry stills, the rest Manim and Remotion;
  vox-run continuity, slate previz, and a tier-tagged shopping-list gate.
- `cli-explainer` — Claude prompt, actual code, and animated output walkthrough.
- `code-walkthrough` — Medhavy “build it with Claude Code + Manim” workflow film.
- `kids-video` — developmentally constrained early-childhood concept film.
- `recitation-film` — visual marginalia around a public-domain spoken performance.
- `bio` — narrated cinematic mini-biography.
- `story-film` — narrated AI film from a story, lyric, or scene list.

### Music and performance — `skills/make/`

- `music-video` — beat-reactive Remotion music and lyric video.
- `dance-video` — long, downbeat-aligned Seedance choreography clips.
- `lyric-overlay` — synchronized lyrics and waveform over an existing finished video.
- `lyric-resync` — rebuild drifting visuals around forced-aligned lyric beats.
- `songbird` — prompt sequencing and musical-session direction.
- `session` — performance direction and Suno-ready session notes.

### Brand and audience adaptations — `skills/make/`

- `audience-preset` — non-destructive branded variant using a brand data file.
- `nbb` — NikBearBrown Teardown-register version; ElevenLabs Bear voice.
- `medhavy` — Wonder-register research-student version; Kokoro `af_kore`.
- `hai` — Humanitarians AI Pragmatist version; Kokoro `am_onyx`.
- `brutalist-medhavy` — learning-first laws layered over another builder; it changes pedagogical
  judgment, not the underlying rendering machinery.

These adaptations write new namespaced outputs and must not overwrite their source artifact.

### Production maintenance — `skills/make/`

- `slate-filler` — replace empty Vox beats with template-first Remotion motion graphics.
- `reel-updater` — migrate existing reels to current specifications; dry-run by default.
- `explainer-deepen` — audit a short doodle explainer and optionally produce a deeper Brown Blue cut.
- `claude-refactor` — retrofit existing videos to Claude openings, handoffs, and outros.
- `component-showcase` — render and critique reusable visual components for education.
- `collage-ads` — decode and produce halftone editorial-collage advertising assets.

`skills/make/component-showcase/remotion/SKILL.md` is a nested `riff` entry describing essentially
the same showcase workflow; treat the top-level component-showcase skill as the primary entry.

### Inventory and publishing — `skills/upload/`

- `video-inventory` — audit Vox video state across books and write the inventory report.
- `youtube-publisher` — prepare NotebookLM video episodes and publish them to the Medhavy channel.

Publishing is an external state change. Follow the skill's review and authorization requirements;
never infer permission merely because a finished file exists.

### Figure library — `skills/figures/`

`skills/figures/` is a reference library, not an invokable skill: it has no `SKILL.md`, so the
`find` command above will not list it. `POINTER.md` explains the situation — the `cajal`,
`figures`, `graphs`, and `tables` workflows exist in this workspace only as copies from
`books/ai1-cli/` (paste-in prompt systems, `graphs.sh`, `svg-to-png.mjs`), gathered under
`figure-planner/`. Session-loaded Cowork skills with the same names may be more current than
these copies. Read `POINTER.md` before treating this material as the source of truth.

## Remotion reference

Remotion implementation guidance is separate from the invokable skills:

```text
docs/remotion-best-practices/SKILL.md
```

Read it when implementing or reviewing Remotion code, in addition to the selected production
skill. It is a technical reference, not a substitute for the builder's editorial workflow.

The rest of `docs/` holds written companions to the Brutalist video series and reference
material; `docs/README.md` is the index. The repository root also contains ready-to-paste
Claude Code prompt documents (`CLAUDE-CODE-*.md`) that encode specific one-off workflows —
they are prompts to run, not skills, and are not listed in the skill map above.

## HTML decks are a separate pipeline

The skills in this repository are predominantly video and asset workflows. They are not the source
of the narrated HTML lecture decks found throughout the wider `books/` workspace.

The written specs for that pipeline now live locally in `docs/`:

- `docs/how-to-create-a-lecture-deck.md` — the two paths: the batch per-book pipeline
  (`books/build_lectures.py`, which drives the animated-deck engine) and the premium
  single-lecture path with a cloned voice.
- `docs/lecture-deck-rules.md` — the rules `build_deck.py` enforces, including which copy of
  `build_deck.py` is canonical.
- `docs/animated-deck-rules.md` — the animated-deck format rules.

Those decks usually live in a structure such as:

```text
<book>/lectures/chNN-lecture/
├── build_deck.py
├── deck.html
├── make_audio.py
├── narration/
└── beat_sheet.json
```

Some older books use `<book>/chNN-lecture/` without the `lectures/` level. Inspect a nearby original
lecture folder and its generator before changing a copied deck. Do not tell the user that
`explainer`, `remotion-explainer`, or another video skill is the HTML-deck generator.

The HTML portion is produced by the lecture/deck pipeline and its local `build_deck.py` pattern.
Narration is produced separately. When repairing a deck, preserve the original pedagogical
sequence, Brutalist palette, slide controls, narration mapping, and asset paths; then regenerate
audio only when the narration changed or audio is missing.

## Core production principles

- Audio-first means measured narration or music is the master clock.
- Preserve phase gates, especially approval before paid generation or audio spend.
- Use the slot and filename conventions defined by the selected skill.
- Prefer existing verified assets and templates over regeneration.
- Keep canonical sources intact when producing brand, audience, or deeper variants.
- Design educational media for learning: prediction before reveal, concrete before abstract,
  useful friction, readable pacing, and a clear handoff to practice.
- Never publish without explicit authorization and the publishing skill's required checks.
- **Never spend money without a human yes — see the HARD STOP money rule at the top of this file.
  Any MCP/tool payment action stops the run and asks, every time.**

## Connected MCP servers

- **Vercel MCP** — installed via `npx add-mcp https://mcp.vercel.com` (official first-party
  server, OAuth). Gives agents access to Vercel projects, deployments, build/runtime logs, and
  domain/deploy actions. To (re)install: run `npx add-mcp https://mcp.vercel.com`, or in Claude
  Code `claude mcp add --transport http vercel https://mcp.vercel.com` then `/mcp` to authorize.
  The OAuth grant is **account-equivalent** — it can reach write tools including `deploy_to_vercel`
  and `buy_domain` (an irreversible real-money purchase with no protocol-level confirmation).
  Keep human confirmation on for every tool call, and prefer read tools (logs, project/deployment
  inspection) for routine work.
