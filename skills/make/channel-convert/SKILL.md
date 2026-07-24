---
name: channel-convert
description: Convert base reel scripts to a Claude-skin channel — HAI, Medhavy, or Musinique. Extends the ai-explainer skill: it applies the Claude skin + channel register, then adds the two-host 50/50 Liam+org voice split, the greeting, and a channel-specific tangent beat. Writes a beat_sheet.[channel].json variant (base untouched). Use when the user types `hai convert`, `medhavy convert`, `musinique convert`, or points the converter at humanitarians_html / medhavy / musinique. Idempotent, free voices only (Kokoro) — never spends ElevenLabs.
---

# channel-convert — HAI / Medhavy / Musinique

Converts base scripts into the **ai-explainer style with the Claude skin**, per
channel. It is an **extension of `ai-explainer`** — that skill owns the Claude
skin, schema, register rewrite, and render path (`brand_variant.py [input]
claude-[channel]`). This skill adds three channel deltas on top and writes them to
a **`beat_sheet.[channel].json` variant** (the base `beat_sheet.json` is never
touched):

1. **Two-host 50/50 voice split.** Liam `am_onyx` is the shared AI voice; each
   channel has an org voice. Each whole reel is ONE voice; ~50/50 across the
   catalog (stable by slug hash).
2. **Greeting.** Liam reel → **"This is Liam for [AI name]."**  ·  org reel → **"This is [org]."**
3. **Tangent beat** right after the first content beat — the channel's "why this
   matters" angle.

| Channel | Catalog | Org voice | Register | Tangent theme |
|---|---|---|---|---|
| **hai** | `humanitarians_html/youtube` | **Kore** `af_kore` | **Pragmatist** | why a smart general audience should care |
| **medhavy** | `medhavy/youtube` | **Bella** `af_bella` | **Wonder** | the pedagogy — how to teach/learn it |
| **musinique** | `musinique/youtube` | **Puck** `am_puck` | **Baldwin** (charter `MUSINIQUE.md`) | the relevance to indie artists |

Greetings: hai → "This is Liam for Humanitarians AI." / "This is Humanitarians."
· medhavy → "This is Liam for Medhavy." / "This is Medhavy." · musinique → "This is
Liam for Musinique." / "This is Musinique." Registers live in
`brutalist-art/runtime/voices/[register]/VOICE.md` (Baldwin = `MUSINIQUE.md` +
this project's Baldwin voice).

## The pass, per reel (audit-and-fix, idempotent)
1. **Audit** `beat_sheet.[channel].json` (or bootstrap from `beat_sheet.json`): is it
   ai-explainer/Claude-skin styled in the channel register? Does it have the greeting
   and the tangent beat?
2. **Claude-skin + register (only if needed).** Apply the ai-explainer conversion for
   `claude-[channel]` (Claude skin, register rewrite). Reuse `ai-explainer` /
   `brand_variant.py`; don't reinvent it.
3. **Add the tangent beat (only if missing).** Insert ONE beat after the first content
   beat (`B01`), narration in the channel register, 2–4 sentences on the channel's
   tangent theme. Non-colliding `beat_id` (`B01B` — never renumber), `act` naming the
   theme, `tangent: true`, a `shot` that renders (reuse a card pattern in the reel).
4. **Mechanical pass** — assign the reel voice, greeting, register metadata:
   `python3 SCRIPTS/hai_convert.py --channel [hai|medhavy|musinique] [reel]`
   (writes `beat_sheet.[channel].json`).
5. **Report** what changed.

## After converting (free, on the user's Mac)
```
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py [reel]   # regenerate mp3s (uses the variant's voices)
python3 SCRIPTS/morning_render.py --channel [channel]                   # render -> TMP/[channel]/
```
> Render must read `beat_sheet.[channel].json`. If `compile.py`/`run.sh` don't yet
> accept a beat-sheet filename, that's the one remaining pipeline hook to add
> (a `--variant`/filename flag), OR the channel makes the variant the active sheet.

## Guardrails
- Idempotent; free voices only (never `engine: elevenlabs`, never `generate_audio.py`);
  no renumber (suffixed ids); base `beat_sheet.json` untouched; no fabrication.

## Mechanical-only (voices + greeting + tangent audit, no rewrites)
```
python3 SCRIPTS/hai_convert.py --channel [channel] --dry-run   # audit, change nothing
python3 SCRIPTS/hai_convert.py --channel [channel]             # apply to the variant
```
