---
name: medhavy
description: >
  Create a MEDHAVY beat sheet from any input — a reel folder, a lecture folder,
  or a book (batch: every reel/lecture it contains). Writes into a new medhavy-
  directory; the source is never modified. Rewrites narration in the Wonder
  register (first principles, genuine wonder, intellectual honesty, no drills),
  keeps an optional experiment tangent (0–1), and ends with the Medhavy.com outro.
  No CLI/LLM exercise beat. Voice: Kokoro af_kore. Palette: medhavy (Okabe-Ito,
  colorblind-safe). Use when the user types `medhavy <input>`, or asks for the
  research-student / MEDHAVY cut. Brand spec: brands/medhavy.md.
---

# medhavy — the MEDHAVY (research-student) cut

Creates a **new `medhavy-` directory** from any source input and writes the MEDHAVY
beat sheet as `beat_sheet.medhavy.json` inside it. The canonical source
(`beat_sheet.json`, build scripts, media) is **never modified**.

## Trigger

```
medhavy <input>
```

`<input>` is one of:
- **Reel folder** — `<book>/youtube/<slug>/` (has `beat_sheet.json`)
- **Lecture folder** — `<book>/lectures/<chapter>-lecture/` (has `beat_sheet.json`)
- **Book folder** — `<book>/` → batch: convert every reel + lecture it contains

## Output directory convention

| Source path | medhavy- output directory | Beat sheet filename |
|---|---|---|
| `<book>/youtube/<slug>/` | `<book>/youtube/medhavy-<slug>/` | `beat_sheet.medhavy.json` |
| `<book>/lectures/<chapter>-lecture/` | `<book>/medhavy-lectures/<chapter>-lecture/` | `beat_sheet.medhavy.json` |

Inside that `medhavy-` directory:
- `beat_sheet.medhavy.json` — the MEDHAVY cut
- Lecture build scripts copied from source: `build_deck.py`, `make_audio*.py`, `render.py`

---

## Flow (per reel or lecture)

### Step 1 — Scaffold (deterministic, no spend)

```bash
python3 runtime/scripts/brand_variant.py <INPUT_PATH> medhavy
```

Creates the `medhavy-` directory and writes `beat_sheet.medhavy.json` with audience
metadata pre-set and a `_variant_todo` checklist. For lectures, copies build scripts
from the source dir. No API calls, no spend.

**What the script sets:**
```json
{
  "audience": "MEDHAVY",
  "engine": "kokoro",
  "voice_kokoro": "af_kore",
  "palette": "medhavy",
  "typography": { "serif": "EB Garamond", "sans": "Montserrat" },
  "register": "Wonder",
  "outro_source": "AUTHOR.MD :: Medhavy.com",
  "derived_from": "beat_sheet.json"
}
```

ElevenLabs override: set `metadata.engine: "elevenlabs"` — `voice_id` from
`ELEVENLABS_VOICE_MEDHAVY` is already written into the sheet.

### Step 2 — Rewrite the register (Wonder)

Open the new `medhavy-<…>/beat_sheet.medhavy.json` and **rewrite every beat's
narration** in the Wonder register (`voices/wonder/VOICE.md`, `brands/medhavy.md`):

- First principles — build the idea up from what the viewer already knows.
- Genuine **wonder** — the "why is this surprising / beautiful" a researcher feels.
- Intellectual honesty — name what's uncertain, what's assumed, what's open.
- **No drills, no exercises in the body.** This is the discovery cut, not a problem set.
- **Change the voice, not the facts.** No fabrication; numbers and claims unchanged.

For **reel** format: rewrite `beats[*].narration_text`.
For **lecture** format: rewrite `segments[*].beats[*].text`.

Preserve beat/segment IDs, act structure, visuals, and on-screen card copy where it
still fits the new register.

### Step 3 — Experiment tangent (0–1 per video)

If — and **only** if — the material obviously invites a small experiment, add **one**
bounded aside with a re-entry cue:

> *"Want to see this yourself? Try this."* — a paste-ready LLM prompt on a prompt card.

A single invitation, not a lecture. **Most reels get none.** Do not force it.

**No CLI worked exercise and no LLM exercise beat** — those are hai / nbb only.
MEDHAVY ends on the outro.

### Step 4 — Outro (LAST beat)

Add/replace the final beat with the **Medhavy.com outro**. Content from the
`Medhavy.com` section of the book's `AUTHOR.MD` (not the default channel). Renders via
Remotion `OutroSeries` / `OutroCTA` in the medhavy palette.

### Step 5 — Verify ending order

Confirm the beat sequence closes as:

```
… Wonder body beats …
[optional experiment tangent]
[Medhavy.com outro]            ← last (no exercise beat)
```

---

## Batch mode (book input)

When `<input>` is a book folder, run the scaffold for every source:

```bash
# Reels
find <book>/youtube/ -maxdepth 1 -mindepth 1 -type d ! -name 'medhavy-*' | \
  while read d; do python3 runtime/scripts/brand_variant.py "$d" medhavy; done

# Lectures
find <book>/lectures/ -maxdepth 1 -mindepth 1 -type d -name '*-lecture' | \
  while read d; do python3 runtime/scripts/brand_variant.py "$d" medhavy; done
```

Then perform Steps 2–5 for each resulting `medhavy-` directory.

---

## Build (only when the user also asks to build)

From the `medhavy-` directory:

```bash
# Audio (Kokoro default)
python3 runtime/scripts/generate_audio_kokoro.py <medhavy-dir>/beat_sheet.medhavy.json

# Audio (ElevenLabs override — set engine:"elevenlabs" first)
python3 runtime/scripts/generate_audio.py <medhavy-dir>/beat_sheet.medhavy.json

# Lectures: deck + render from the copied build scripts (point them at beat_sheet.medhavy.json)
python3 <medhavy-dir>/build_deck.py
python3 <medhavy-dir>/render.py

# Compile (reels)
python3 runtime/scripts/compile.py <medhavy-dir> --height 1080
```

GATE P applies: a `PEDAGOGY.md` pass before any spend.

---

## The medhavy palette

Okabe-Ito (colorblind-safe, the gold standard) on a warm eggshell ground:

| Role | Hex | When |
|---|---|---|
| CREAM | `#F0EAD6` | ground |
| INK | `#000000` | text / marks |
| TEAL | `#009E73` | good / kept / true (Okabe-Ito bluish green) |
| CRIMSON | `#D55E00` | bad / lost / broken (Okabe-Ito vermillion) |
| SLATE | `#4D4D4D` | structure / entity cards |
| GOLD | `#F0E442` | highlighter fill only — never text |

Categorical: `#0072B2` `#E69F00` `#56B4E9` `#009E73` `#D55E00` `#CC79A7`.

Typography — house type: **EB Garamond** (serif body) + **Montserrat** (sans headers);
MEDHAVY reuses the house FONT. Tokens: `runtime/remotion/src/tokens/medhavy.ts`.

---

## Standing rules

- Source files (`beat_sheet.json`, build scripts, media) are **never modified**.
- GATE P applies before any audio spend.
- NO exercise beat — MEDHAVY is the Wonder discovery cut; it ends on the outro.
- MEDHAVY users refine the slate cut further with Claude Code — a strong starting
  point, not a locked master.
