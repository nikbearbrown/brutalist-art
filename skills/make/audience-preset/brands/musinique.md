---
name: musinique
description: Convert a built reel into the MUSINIQUE audience variant — beat_sheet.musinique.json, the same reel rewritten in the Teardown register, Kokoro voice am_puck (default) or MUSINIQUE ElevenLabs clone (override) + monochrome/SaaS-clean palette (musinique), with a Musinique outro. Use when the user types `musinique <reel>`, asks to make the Musinique-branded cut of a reel, or to build a reel for the Musinique web properties. Never touches beat_sheet.json.
---

# musinique — the MUSINIQUE audience variant

Forks a reel into `beat_sheet.musinique.json`: the same video rewritten for the
**Musinique** properties (musinique.com + artist subdomains). See the register
`voices/teardown/VOICE.md` and the palette in `runtime/design/musinique-palette.md`.
**The canonical `beat_sheet.json` is never modified** — the variant is a sibling file.

## Design identity

**Musinique is the opposite pole from Brutalist**: where Brutalist is a hard-edged
terminal aesthetic (orange, JetBrains Mono, no radius, Solari), Musinique is monochrome
— all-greys editorial SaaS: white → greys → black, black/white high-contrast CTAs,
rounded corners, soft shadows, **Inter** humanist sans, generous whitespace, lucide line
icons. Contrast IS the accent; the one non-neutral color is the link blue (`#2563eb`).

## Flow (per reel)
1. **Scaffold (deterministic, no spend):**
   ```bash
   python3 runtime/scripts/brand_variant.py <REEL> musinique
   ```
   Creates `beat_sheet.musinique.json` — a copy of the canonical with metadata set:
   `audience: MUSINIQUE`, `engine: "kokoro"`, `voice_kokoro: "am_puck"` (default TTS),
   `voice_id` = `ELEVENLABS_VOICE_MUSINIQUE` (ElevenLabs override — change `engine` to
   `"elevenlabs"` to activate it), `palette: musinique`, `register: Teardown`, and a
   `_variant_todo` checklist. Stale durations are dropped.
2. **Rewrite the register (Claude Code — the real work).** Open
   `beat_sheet.musinique.json` and rewrite **every beat's `narration_text` in the
   Teardown register** (`voices/teardown/VOICE.md`) — explain the machinery, reveal the
   design philosophy, name the trade-offs. Preserve beat ids, the act structure, the
   visuals / scene intent, and on-screen copy where it still fits. **Voice only, not
   facts** — no fabrication, numbers and claims unchanged.
3. **Optional tangent (0–1).** If a clear moment appears to connect to the Musinique
   world (record-label / artist / music-production angle), add ONE bounded aside with a
   re-entry cue. Most reels get none.
4. **Outro → Musinique.** Replace the outro with the Musinique outro from
   `AUTHOR.MD :: Musinique`. References musinique.com / the artist pages.
5. **Build (audience-namespaced).** Generate audio in the Kokoro am_puck voice (default)
   or the Musinique ElevenLabs clone (set `engine: "elevenlabs"` to switch), render
   scenes in the **musinique palette** (monochrome greys, blue accent, Inter
   humanist-sans), compile → the MUSINIQUE slate cut. Only the variant's audio bills;
   GATE P still applies (a fresh `PEDAGOGY.md` pass before spend).
6. **Handoff.** The Musinique team takes the slate cut and revises scenes with Claude
   Code by their own judgment.

## Palette notes (musinique)
The musinique palette lives in `runtime/design/musinique-palette.md` and
`runtime/remotion/src/tokens/musinique.ts`. Monochrome:
- **Ground** `#FFFFFF` → **INK** `#111827` (near-black)
- **Good/kept** uses the blue accent `#2563eb` (the one non-neutral mark)
- **Bad/lost** uses gray-700 `#374151` (monochrome; label + position carry meaning)
- **Type** Inter (humanist sans) throughout — NOT Montserrat/JetBrains Mono
- Rounded shapes (radius, soft shadows) are a deck/web trait; Manim/Remotion renders
  the color layer only.

> **shadcn `:root` tokens not yet confirmed** — values inferred from the shadcn
> "neutral" preset. To lock them exactly: drop the site's `globals.css` `:root`/`.dark`
> block into the palette doc and the token file will update. See
> `runtime/design/musinique-palette.md` § TODO.

## Pending wiring (shared with other variants)
The build step needs `generate_audio.py` / compile pipeline to accept `--audience
musinique` so outputs namespace under `mp3.musinique/` / `<slug>.musinique-review.mp4`
and the render selects `tokens/musinique.ts` / `ART_PALETTE=musinique`. Until that
lands, steps 1–4 (the variant beat sheet) are fully usable; step 5 is manual.
