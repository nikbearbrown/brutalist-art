---
name: medhavy
description: Convert a built reel into the MEDHAVY audience variant — beat_sheet.medhavy.json, the same reel rewritten in the Wonder register, in the MEDHAVY voice + Okabe-Ito palette, with a Medhavy.com outro. Use when the user types `medhavy <reel>`, asks to make the research-student / MEDHAVY cut of a reel, or to rewrite a beat sheet in Wonder for MEDHAVY. Never touches beat_sheet.json.
---

# medhavy — the MEDHAVY audience variant

Forks a reel into `beat_sheet.medhavy.json`: the same video rewritten for **MEDHAVY**
(advanced undergrad / master's, doing research; videos are helpers). See the charter
`MEDHAVY.md` and register `voices/wonder/VOICE.md`. **The canonical `beat_sheet.json` is
never modified** — the variant is a sibling file.

## Flow (per reel)
1. **Scaffold (deterministic, no spend):**
   ```bash
   python3 scripts/vox_variant.py <REEL> medhavy
   ```
   Creates `beat_sheet.medhavy.json` — a copy of the canonical with metadata set:
   `audience: MEDHAVY`, `voice_id` = `ELEVENLABS_VOICE_MEDHAVY`, `palette: medhavy`,
   `register: Wonder`, and a `_variant_todo` checklist. Stale durations are dropped.
2. **Rewrite the register (Claude Code — the real work).** Open
   `beat_sheet.medhavy.json` and rewrite **every beat's `narration_text` into the Wonder
   register** — first principles, wonder, intellectual honesty, no drills. Preserve beat
   ids, the act structure, the visuals / scene intent, and each card's on-screen copy
   where it still fits. **You are changing the voice, not the facts** — no fabrication,
   numbers and claims unchanged.
3. **Experiment tangent (0–1, iff a clear opportunity).** If — and only if — the
   material obviously invites a little experiment, add ONE bounded aside with a re-entry
   cue: *"want to see this yourself? try this"* or a **paste-ready LLM prompt** on a
   prompt card. Most reels get none.
4. **Outro → Medhavy.com.** Replace the outro with the MEDHAVY outro, content from the
   **Medhavy.com** section of the book's `AUTHOR.MD` (not the default channel). Renders
   via the Remotion `OutroSeries` / `OutroCTA` once those exist.
5. **Build (audience-namespaced).** Generate audio in the MEDHAVY voice, render scenes in
   the Okabe-Ito palette, compile → the MEDHAVY slate cut. Only the variant's audio bills;
   GATE P still applies (a fresh `PEDAGOGY.md` pass on the rewritten sheet before spend).
6. **Handoff.** MEDHAVY users / HAI Fellows take the slate cut and revise scenes with
   Claude Code by their own judgment — the variant is a strong starting point, not a
   locked master.

## Pending wiring (shared with `hai`)
The build step needs `generate_audio.py` / `vox_compile.py` to accept an `--audience`
so outputs namespace (`mp3.medhavy/`, `media.medhavy/`, `<slug>.medhavy-review.mp4`) and
the render selects the audience palette tokens (`tokens/medhavy.ts`; a Manim parallel of
the Okabe-Ito set for `vox_graphics.py`), plus the Remotion outro compositions. Until
that lands, steps 1–4 (the variant beat sheet) are fully usable; step 5 is manual.
