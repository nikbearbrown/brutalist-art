# CLAUDE.md — brutalist-art

@AGENTS.md

The imported `AGENTS.md` is the operating manual: the skill map, phase gates,
approval boundaries, and publishing rules. It governs every session. This file
adds only what is Claude-specific or needed to get a session productive fast.

## What this repository is

A local production toolkit for educational videos and visual assets, organized
as agent skills under `skills/`. The philosophy — "maximally informed,
minimally autonomous" — is in `README.md`: Claude does the technical build;
the human keeps every creative and spend decision.

## Claude-specific material

- `CLAUDE-BRAND.md` — brand charter for the `claude` audience: the Claude
  desktop app's own visual language (cream page, terracotta accent, one orange
  moment per beat). Token source of truth:
  `runtime/remotion/src/tokens/claude.ts`. Never retint the palette.
- Claude-branded skills: `skills/make/ai-explainer/` (builder, extends
  `explainer`), `skills/make/claude-scout/` and `skills/make/cli-scout/`
  (scouts), `skills/make/claude-refactor/` (retrofit existing videos to Claude
  openings, handoffs, and outros).
- `CLAUDE-CODE-*.md` at the repo root are ready-to-paste Claude Code prompts
  for specific one-off workflows (e.g. `nbb <video path>` wraps an existing
  body video; the Medhavy+HAI conversion prompt). They are prompts to run, not
  skills — read the named doc completely before executing one.

## Setup, keys, and spend

- Credentials live in `.env` (gitignored); `.env.example` documents every key
  and what leaving it blank disables. `./setup` is the live doctor.
- `CAPABILITIES.md` is the at-a-glance table: per video type, the keys,
  installs, rough cost, worked example, and what the human must supply.
- Cost tiers: Kokoro narration is free/local (the default for most brands);
  ElevenLabs narration and higgsfield image/video are PAID. Per AGENTS.md,
  never trigger paid generation or audio spend without explicit approval at
  the skill's phase gate.

## Provenance and working state

- `MANIFEST.md` — where every skill was gathered from and what Phase 2
  renamed, merged, or deleted; `GLOSSARY.md` — old → new skill-name table.
  Useful when older docs or books reference a skill by its former name.
- `HANDOFF.md` and `TODO.md` — current project state and open work; check
  them before starting anything that might already be in flight.
