---
name: audience-preset
description: >
  Produce an audience-branded variant of a finished reel — fork the canonical
  beat_sheet.json into a namespaced brand copy (beat_sheet.<brand>.json), rewrite
  the narration register, optionally add one brand-flavored tangent beat, swap the
  outro, and rebuild under the brand's palette and voice. Never touches the
  canonical beat_sheet.json. Brands are data files in brands/ — currently hai
  (Humanitarians AI, Pragmatist register), medhavy (Medhavy, Wonder register,
  Okabe-Ito palette), and neu (Northeastern, Lecture register, NU brand laws).
  Use when the user types `hai <reel>`, `medhavy <reel>`, `neu <reel>`,
  `audience-preset <reel> <brand>`, or asks for a brand/audience variant of a
  built video. (Formerly three skills: hai, medhavy, neu.)
---

# audience-preset — brand variants of a finished reel

One skill, one flow, N brands. The per-brand facts (register, ElevenLabs voice
env var, `VOX_PALETTE` key, outro, tangent flavor, extra brand laws) live in
`brands/<brand>.md` — those files are the originals of the three former skills
and remain the authoritative spec for each brand.

## The flow (identical for every brand)

1. **Fork the sheet** — `python3 runtime/scripts/brand_variant.py <REEL> <brand>`
   scaffolds `beat_sheet.<brand>.json` from the canonical sheet. The canonical
   `beat_sheet.json` is NEVER modified.
2. **Rewrite the register** — narration rewritten in the brand's register
   (see `brands/<brand>.md`), same beats, same facts.
3. **Optional tangent** — at most one brand-flavored tangent beat, if the brand
   file calls for it.
4. **Swap the outro** — the brand's outro replaces the default.
5. **Build namespaced** — audio, renders, and the composite build under the
   brand namespace; palette comes from the brand's `VOX_PALETTE` key; voice from
   the brand's `ELEVENLABS_VOICE_*` env var (fallbacks per brand file).
6. **Hand off** — same publish path as any reel.

## Brands

| brand | register | voice env | palette | outro |
|---|---|---|---|---|
| `hai` | Pragmatist | `ELEVENLABS_VOICE_HUMANITARIANS` | humanitarians | Humanitarians AI |
| `medhavy` | Wonder | `ELEVENLABS_VOICE_MEDHAVY` | medhavy (Okabe-Ito) | Medhavy.com |
| `neu` | Lecture | `ELEVENLABS_VOICE_NEU` → NIKBEARBROWN fallback | neu (NU red/black/white/gold, Lato) | Northeastern |

**NEU brand laws:** the `neu` brand carries extra guardrails (red is brand, never
state; Lato only; no color-coded good/bad; gold rare; pre-render brand check).
They apply only when `<brand> = neu` and are specified in `brands/neu.md`.

## Adding a brand

Add `brands/<name>.md` with the same fields (register, voice env, palette key,
outro, tangent flavor, any brand laws). No code changes — `brand_variant.py`
takes the brand name as an argument.
