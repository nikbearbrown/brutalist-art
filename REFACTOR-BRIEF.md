# REFACTOR BRIEF — brutalist-art → a clone-and-go video toolkit

**You are a senior refactoring agent (Fable 5).** You have full autonomy over the
`brutalist-art/` repository. Your job is to turn the pile of gathered skills in this repo into
a clean, self-documenting, **clone-and-go** toolkit that a newcomer can use from a CLI (Claude
Code, Codex, or similar) with the AI doing the technical work and the human supplying only
context and creative decisions.

Work in **phases with human sign-off gates** (see PHASES). Do not do the whole thing in one
shot. Never invent facts about the code — read it. Preserve git history where you can (`git mv`,
not delete-and-recreate).

---

## 0. Read first (the current state)

This repo was assembled by a "gather + annotate" pass. Read these before touching anything:
- `README.md` — what's here and the known caveats.
- `MANIFEST.md` — the annotated inventory of all ~40 gathered skills, their **original source
  paths** in the parent `bear-textbooks/` repo, and dependency/duplicate flags.
- `skills/make/`, `skills/upload/`, `skills/assets/`, `skills/figures/` — the skills themselves.
- `examples/` — mp4-stripped sample projects.

**Critical fact:** the gathered skills are command definitions plus each skill's own files, but
they are **NOT yet runnable in isolation**. The vox skills call a shared runtime that was NOT
copied here. The source toolkits live in the parent repo — you will pull the shared runtime in:
- `../vox/` → `scripts/` (`vox_run.sh`, `generate_audio.py`, `vox_compile.py`), `manim/vox_graphics.py`,
  `DESIGN.md`, `voices/`, `reference/pedagogy.md`, `.env`
- `../unreal-reels/` → shared scripts, `bearbrown/`, Remotion projects
- `../ai1-cli/`, `../brutalist/`, `../higgsfield/` → the satellite runtimes

If the parent repo is not available at refactor time, STOP and ask the human to add it —
document exactly which paths you need.

---

## 1. The product vision (what "done" feels like)

A new person clones this repo, opens the folder in a CLI, and within 15 minutes can render an
existing example end-to-end. Concretely:

1. **`git clone` → open in CLI → read one page.** The root `README.md` tells them the whole
   story: what this makes, the one command to check their setup, and the learning path.
2. **`./setup` (or `make setup` / `npm run setup`) is a doctor.** It checks every dependency and
   every API key, and prints a per-feature readiness table: "✅ sketch-explainer ready — ❌ AI-video
   needs HIGGSFIELD_API_KEY and Node ≥ 20." Nobody has to reverse-engineer what they need.
3. **Keys are explained by what they unlock, not by vendor trivia.** `.env.example` lists every
   key with a comment: which features need it, whether it costs money, and where to get it. A user
   who only wants silent sketch explainers should never be asked for an AI-video key.
4. **Names are plain jargon.** No insider brand names. A newcomer reads the skill list and knows
   what each one makes without a decoder ring (see NAMING).
5. **The learning path is example-first.** Each video type ships one complete example. The
   documented path is: *rebuild this example from its source inputs → confirm your setup produces
   the same result → then point the same skill at your own material.*
6. **The human/AI division is explicit.** Every skill's doc states what the AI/CLI does
   (the technical build) and what the human must supply (the context, the approvals, the
   real captures the CLI can't fake).

---

## 2. Deliverables (the concrete artifacts to produce)

### 2.1 Naming — retire the house jargon
Rename every skill and user-facing command to a **plain, self-descriptive name** using
well-known video/production jargon. Produce `GLOSSARY.md` mapping every OLD house name → NEW name
→ one-line description, and keep the old names as **aliases** (a command alias table) so existing
muscle memory and any external references still resolve. Proposed direction (you refine, human
approves the final map in Phase 1):

| Old (house) | New (plain jargon) — proposed |
|---|---|
| bears-doodles | `sketch-explainer` |
| brownblue | `math-explainer` (3b1b-style) |
| brownblue-convert | `explainer-deepen` |
| vox-explainer / vox | `collage-explainer` |
| voxlit | `recitation-film` |
| voxbio / mini-bio | `bio-documentary` |
| cli (skill) | `terminal-screencast` |
| simulation | `code-walkthrough` |
| teardown-script | `script-writer` |
| cli-scout / vox-scout / bears-doodles-scout | `idea-scout` (one skill, `--style` flag) |
| muzak | `music-video` |
| muzak-overlay | `lyric-overlay` |
| lyric-match | `lyric-resync` |
| songbird-dance | `dance-video` |
| cubs | `kids-video` |
| greybox | `previz` (already jargon — keep) |
| media-router | `shot-planner` |
| pacing | `duration-planner` |
| hai / medhavy / neu | `audience-preset` (brand presets, data-driven) |
| riff | `component-showcase` |
| muybridge | `remotion-explainer` |
| cajal | `figure-planner` |
| durer | `line-art-vectorizer` |
| figure-harvest | `diagram-redraw` |
| notebooklm-youtube | `youtube-publisher` |
| audit | `video-inventory` |
| higgsfield-* | `ai-asset-gen` namespace (keep vendor name in help text only) |

Also collapse obvious **duplicates**: `vox-explainer` and `vox-explainer-unreal` are the same
skill — merge to one. The three scouts are one skill with a style flag. Document every merge.

### 2.2 Setup & dependency documentation
- **`.env.example`** — every environment variable, grouped by the feature it unlocks, each with:
  purpose, which skills use it, cost (free / paid), and where to obtain it. At minimum, verify
  against the code (grep the skills for `os.environ`, `process.env`, API calls) — do not trust
  this list, confirm it: `ANTHROPIC_API_KEY` (the driving CLI), `ELEVENLABS_API_KEY` (narration +
  voice clone), `HIGGSFIELD_API_KEY` (AI image/video/3D/audio), `MINIMAX_API_KEY` (Hailuo
  image-to-video for lyric-resync), YouTube Data API OAuth (youtube-publisher), Arcads MCP creds
  (collage ads). Note which tools are **local, no key** (faster-whisper captions, librosa beat
  analysis, Manim, ffmpeg, Pillow previz).
- **`INSTALL.md`** — every install, per OS where it differs: Python + the pip deps (manim,
  librosa, pillow, faster-whisper, sharp via node…), Node ≥ 20 + Remotion + headless Chromium,
  ffmpeg, LaTeX (for Manim math). Pin versions. Provide a single `requirements.txt` /
  `package.json` / lockfiles so `./setup` can install everything.
- **`setup` script (the doctor)** — checks binaries (`ffmpeg`, `node`, `python`, LaTeX), Python/
  Node deps, and each API key; prints the per-feature readiness table from §1.2; exits non-zero if
  a *core* dep is missing but degrades gracefully for optional (paid) features.

### 2.3 The capability / feature matrix
`CAPABILITIES.md` — one row per video type: what it makes (1 line) · required keys · required
installs · cost per run (free / ~$ narration / ~$$ AI-video) · the example that teaches it · the
one human-supplied input it cannot generate. This is the "what do I need for this or that" table.

### 2.4 Examples-first learning path
- Every video type has exactly one complete example under `examples/<type>/` with its **source
  inputs kept** (the chapter/text/song/lyrics, the beat sheet, the scene code) and a short
  `README.md` that says: *"Run `<command>` here to rebuild this from scratch; you should get
  `<result>`. Then copy this folder, swap in your own inputs, and run again."*
- Add a top-level `LEARN.md` that orders the examples from simplest (silent previz, no keys) to
  most involved (AI-video with paid keys), so a newcomer climbs the ladder.
- Examples must be runnable after `./setup` with the minimum keys for that type; the no-key types
  (previz, sketch without narration) must run with zero API keys.

### 2.5 Unified command grammar & runtime
- Give every skill the **same command shape** (e.g. `art <skill> <target> [--flags]`) with a
  shared `--help`, a shared `beat_sheet.json` schema, and a single entry point that dispatches.
- **Vendor the shared runtime** from the parent toolkits into this repo so skills run in
  isolation (no `../vox/...` reach-outs). Deduplicate the shared scripts. If two skills ship
  divergent copies of the same script, reconcile to one and note it.
- Keep the **audio-first, phase-gated** discipline the skills already use; make the gates explicit
  and human-signable.

### 2.6 Top-level docs
Rewrite `README.md` as the front door (story, quickstart, learning path, human/AI split). Keep
`MANIFEST.md` as the provenance record (update names). Add `CONTRIBUTING.md` describing the
skill folder contract so new skills fit the same mold. Add a `LICENSE` (ask the human which).

---

## 3. Naming & doc rules
- Plain names a stranger understands; no personal/brand codenames in commands. Vendor/brand names
  (Higgsfield, ElevenLabs, Remotion, Manim) are fine in help text and capability rows — they ARE
  the jargon there — but not as the skill's identity.
- Every skill folder must contain: `SKILL.md` (the command spec), a `README.md` (human-facing:
  what it makes, keys, the human's job vs the CLI's job), and its scripts. One shape for all.
- Write for a newcomer who is strong on subject-matter context but not on this toolchain. The
  toolchain does the technical lift; the docs teach the *decisions*, not the plumbing.

## 4. Constraints
- Operate ONLY inside `brutalist-art/`. Do not modify the parent `bear-textbooks/` sources; you
  may READ them to vendor the runtime.
- Reversible, reviewable steps. Commit per phase with clear messages. No force-deletes of
  anything you haven't first accounted for in `MANIFEST.md`.
- Strip/keep media as-is (this repo is already media-free); never commit large binaries,
  `node_modules`, or secrets. `.env` stays git-ignored; only `.env.example` is committed.
- If a decision is genuinely the human's (final name map, license, which brand presets survive,
  whether to include the deck/lecture skills that were left out), STOP at the gate and ask.

## 5. Phases (gate = human sign-off before proceeding)
1. **Audit & plan.** Read everything; verify the real env-var/install inventory from the code;
   produce `REFRACTOR-PLAN.md` with the final proposed name map, the dedup list, the runtime-vendor
   list, and the phase schedule. **GATE.**
2. **Rename + dedup + aliases.** Apply the approved name map with `git mv`; merge duplicates;
   write `GLOSSARY.md` with the alias table. Nothing else changes behavior yet. **GATE.**
3. **Vendor runtime + unified command grammar.** Pull in and dedupe the shared scripts; add the
   single dispatch entry point and shared schema. Skills now run in isolation. **GATE.**
4. **Setup, keys, installs.** Write `.env.example`, `INSTALL.md`, the `setup` doctor,
   `CAPABILITIES.md`. `./setup` prints an accurate readiness table on a clean machine. **GATE.**
5. **Examples-first.** Restore source inputs to one example per type, add per-example rebuild
   READMEs and `LEARN.md`, verify each rebuilds after `./setup`. **GATE.**
6. **Front-door docs + acceptance test.** Rewrite `README.md`; run the acceptance test below;
   fix gaps. **GATE (final).**

## 6. Definition of done (acceptance test)
On a **fresh clone in a clean container**:
1. `README.md` alone tells a newcomer what to do next.
2. `./setup` runs, installs core deps, and prints a per-feature readiness table naming exactly
   which key/install each unlocks.
3. With **zero API keys**, the newcomer rebuilds the no-key example (previz or silent sketch) to
   completion.
4. With only `ELEVENLABS_API_KEY`, they rebuild the narrated `sketch-explainer` example.
5. Every skill answers `--help` in the same grammar; every old house name still resolves via alias.
6. No secret, no large binary, no `node_modules` in git. `MANIFEST.md`/`GLOSSARY.md` are accurate.

Begin with Phase 1. Produce `REFRACTOR-PLAN.md` and stop at the first gate.
