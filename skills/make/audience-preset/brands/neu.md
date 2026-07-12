---
name: neu
description: Convert a built reel into the NEU (Northeastern) audience variant — beat_sheet.neu.json, the same reel rewritten in the Lecture register, on the NEU brand palette (NU red / black / white / gold, Lato), with a Northeastern outro. Use when the user types `neu <reel>`, asks to make the Northeastern / class / professor cut of a reel, or to rewrite a beat sheet in Lecture for NEU. Never touches beat_sheet.json.
---

# neu — the NEU (Northeastern) audience variant

Forks a reel into `beat_sheet.neu.json`: the same video rewritten for **NEU** — a
Northeastern student inside a specific course, watching a reel their professor
assigned. See the charter `NEU.md` and register `voices/lecture/VOICE.md`. **The
canonical `beat_sheet.json` is never modified** — the variant is a sibling file.

NEU is **brand-governed** (Northeastern brand law: `brutalist/… NEU-DESIGN.md`), which
makes it stricter than the other audience variants: red is brand, never state; type is
Lato; good/bad cannot be color-coded.

## Flow (per reel)
1. **Scaffold (deterministic, no spend):**
   ```bash
   python3 scripts/vox_variant.py <REEL> neu
   ```
   Creates `beat_sheet.neu.json` — a copy of the canonical with metadata set:
   `audience: NEU`, `voice_id` = `ELEVENLABS_VOICE_NEU` **if set, else falls back to
   `ELEVENLABS_VOICE_NIKBEARBROWN`** (Bear's voice — the default), `palette: neu`,
   `register: Lecture`, and a `_variant_todo` checklist. Stale durations are dropped.
2. **Rewrite the register (Claude Code — the real work).** Open `beat_sheet.neu.json`
   and rewrite **every beat's `narration_text` into the Lecture register** — the voice
   of a good instructor inside a course: define terms precisely on first use, tie the
   concept to the course's learning objective, cite the assigned reading where one
   exists, keep it rigorous and assessable. Sentence case, no hype. **You are changing
   the voice, not the facts** — numbers and claims unchanged. Preserve beat ids, act
   structure, and scene intent.
3. **Coursework tangent (0–1, iff a clear hook).** If — and only if — a clear moment
   appears to connect the concept to the course itself (an assigned reading, a problem
   set, what the assessment tests), add ONE bounded aside with a re-entry cue: *"this is
   the reading by X"; "you'll use this on the midterm."* Most reels get none.
4. **Outro → Northeastern.** Replace the outro with the NEU outro, content from the
   **Northeastern** section of the book's `AUTHOR.MD` (the course / professor, not the
   default channel). Renders via the Remotion `OutroSeries` / `OutroCTA` once they exist.
5. **Build (audience-namespaced).** Generate audio in the NEU voice (Bear's by default),
   render scenes on the **NEU brand palette** (`VOX_PALETTE=neu` for Manim, `tokens/neu.ts`
   for Remotion — NU red / black / white / gold, **Lato**), compile → the NEU slate cut.
   Only the variant's audio bills; GATE P still applies (a fresh `PEDAGOGY.md` pass before
   spend). **Brand check before render:** every asset contains NU Red as brand only (never
   for a negative value); good/bad reads from KEPT/LOST label + position, not color; gold
   is rare + large-area only; white ground; Lato throughout, regular-weight headings.
6. **Handoff.** The NEU professor takes the slate cut and revises scenes with Claude Code
   by their own judgment — the variant is a strong starting point, not a locked master.

## NEU voice — other professors
Bear's voice ships as the NEU default because he uses NEU mode for his own class slides.
It is distinctive enough that it *dominates* a lecture — which is the intended nudge:
another professor should create or choose their own voice, set `ELEVENLABS_VOICE_NEU` in
`.env`, and their class will sound like them, not like Bear.

## Pending wiring (shared with `medhavy` / `hai`)
The build step needs `generate_audio.py` / `vox_compile.py` to accept an `--audience`
so outputs namespace (`mp3.neu/`, `media.neu/`, `<slug>.neu-review.mp4`) and the render
selects the NEU tokens (`tokens/neu.ts`; Manim reads `VOX_PALETTE=neu` in `vox_graphics.py`),
plus the Remotion outro compositions. NEU additionally needs **Lato bundled in
`fonts/Lato/`** and registered with fontconfig. Until that lands, steps 1–4 (the variant
beat sheet) are fully usable; step 5 is manual.
