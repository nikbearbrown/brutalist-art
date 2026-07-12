---
name: hai
description: Convert a built reel into the HAI (Humanitarians AI) audience variant — beat_sheet.hai.json, the same reel rewritten in the Pragmatist register, in the HUMANITARIANS voice + muted-editorial palette, with a Humanitarians AI outro. Use when the user types `hai <reel>`, asks to make the Humanitarians / practitioner cut of a reel, or to rewrite a beat sheet in Pragmatist for HAI. Never touches beat_sheet.json.
---

# hai — the HAI (Humanitarians AI) audience variant

Forks a reel into `beat_sheet.hai.json`: the same video rewritten for **HAI** (busy,
mid-career practitioners applying AI in social-impact work — get productive fast). See
the charter `HAI.md` and register `voices/pragmatist/VOICE.md`. **The canonical
`beat_sheet.json` is never modified** — the variant is a sibling file.

## Flow (per reel)
1. **Scaffold (deterministic, no spend):**
   ```bash
   python3 scripts/vox_variant.py <REEL> hai
   ```
   Creates `beat_sheet.hai.json` — a copy of the canonical with metadata set:
   `audience: HAI`, `voice_id` = `ELEVENLABS_VOICE_HUMANITARIANS`, `palette: humanitarians`,
   `register: Pragmatist`, and a `_variant_todo` checklist. Stale durations are dropped.
2. **Rewrite the register (Claude Code — the real work).** Open `beat_sheet.hai.json`
   and rewrite **every beat's `narration_text` into the Pragmatist register** — method,
   when to use it, and (the main event for AI) **when NOT to and where it fails**;
   efficient, no personality tax. Preserve beat ids, the act structure, the visuals, and
   each card's on-screen copy where it still fits. **Change the voice, not the facts** —
   no fabrication.
3. **Irreducibly-Human tangent (0–1, iff a clear opportunity).** If — and only if — a
   clean line appears, add ONE bounded aside with a re-entry cue: *"this the AI does
   well; this is the human's, and can't be handed off."* A decision boundary, not a
   sermon. Most reels get none.
4. **Outro → Humanitarians AI.** Replace the outro with the HAI outro, content from the
   **Humanitarians AI** section of the book's `AUTHOR.MD` (not the default channel).
   Renders via the Remotion `OutroSeries` / `OutroCTA` once those exist.
5. **Build (audience-namespaced).** Generate audio in the HUMANITARIANS voice, render
   scenes in the muted-editorial palette, compile → the HAI slate cut. Only the variant's
   audio bills; GATE P still applies (a fresh `PEDAGOGY.md` pass before spend).
6. **Handoff — the HAI Fellows.** HAI Fellows take the slate cut and further use Claude
   Code to update and revise scenes by their own judgment. The variant is a strong,
   on-doctrine starting point they refine — not a locked master.

## Pending wiring (shared with `medhavy`)
The build step needs `generate_audio.py` / `vox_compile.py` to accept an `--audience`
so outputs namespace (`mp3.hai/`, `media.hai/`, `<slug>.hai-review.mp4`) and the render
selects the audience palette tokens (`tokens/humanitarians.ts`; a Manim parallel for
`vox_graphics.py`), plus the Remotion outro compositions. Until that lands, steps 1–4
(the variant beat sheet) are fully usable; step 5 is manual.
