---
name: medhavy
description: >
  MEDHAVY (Medhavy.com) brand spec — Wonder register, Kokoro af_kore (default) or the
  MEDHAVY ElevenLabs clone (override), medhavy palette (Okabe-Ito, colorblind-safe),
  Medhavy.com outro, and NO exercise beat. For the first-class `medhavy` command (which
  creates a medhavy- directory and adds the outro beat), see skills/make/medhavy/SKILL.md.
  Never touches the canonical beat_sheet.json.
---

# medhavy — the MEDHAVY (Medhavy.com) brand

Audience: advanced undergrad / master's students doing research; the videos are helpers.

The **first-class `medhavy` command** (directory convention, Wonder rewrite, Medhavy.com
outro) is documented in `skills/make/medhavy/SKILL.md`. This file is the brand spec.

## Register — Wonder

First principles, genuine wonder, intellectual honesty, no drills. The discovery cut:
build the idea up, name what's surprising and what's uncertain, no problem sets in the body.
Voice reference: `voices/wonder/VOICE.md`.

## Voice / engine

| Engine | Default | Override |
|---|---|---|
| Kokoro | `af_kore` | — |
| ElevenLabs | — | `ELEVENLABS_VOICE_MEDHAVY` env var; set `engine:"elevenlabs"` to activate |

## Palette — `medhavy` (Okabe-Ito)

Colorblind-safe, warm eggshell ground. Tokens: `runtime/remotion/src/tokens/medhavy.ts`.
CREAM `#F0EAD6` · INK `#000000` · TEAL `#009E73` · CRIMSON `#D55E00` · SLATE `#4D4D4D` · GOLD `#F0E442`.
Typography: the house type (**EB Garamond** / **Montserrat**) — MEDHAVY reuses the house FONT.

## Ending — no exercise beat

Unlike `hai` (CLI worked exercise) and `nbb` (LLM exercise), the MEDHAVY cut has **no
exercise beat**. It keeps only the optional experiment tangent (0–1) and ends on the outro.

## Outro

Medhavy.com outro — content from the `Medhavy.com` section of the book's `AUTHOR.MD`
(not the default channel). Renders via Remotion `OutroSeries` / `OutroCTA` in the medhavy palette.

## Directory convention

`medhavy <input>` writes into a new `medhavy-` directory (the source is never modified):
`<book>/youtube/<slug>/` → `<book>/youtube/medhavy-<slug>/`;
`<book>/lectures/<chapter>-lecture/` → `<book>/medhavy-lectures/<chapter>-lecture/`;
the beat sheet inside is `beat_sheet.medhavy.json`. See `skills/make/medhavy/SKILL.md`.
