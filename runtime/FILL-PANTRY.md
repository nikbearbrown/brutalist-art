# Filling the Pantry with Midjourney

How to fill a reel's vox beats with Midjourney art, end to end. Built and run against the `computational-skepticism-for-ai` reels (dashboard-that-lied, fluency-trap, computational-epistemology). Tool lives at `books/brutalist-art/runtime/scripts/fill_pantry.py`, exposed as `art fill-pantry`.

---

## The loop, in one picture

```
1. art fill-pantry <reel> --backend midjourney   → composes id-prefixed prompts
2. fire the reel's whole queue into MJ            → one short burst, spaced ~4s
3. YOU animate the keepers in MJ                  → the ones you like become motion
4. YOU "download all" as a zip, drop in PANTRY/   → inside the connected folder
5. art fill-pantry <reel> --ingest <zip>          → matches by id → pantry/<bid>.mp4
```

Nobody waits: you fire a reel, stop; you animate + download whenever; you cue the next reel at some later time. MJ only ever sees a small burst (**a reel has ≤7 vox beats**), never hours of continual fire.

---

## 1. The prompt is subject + style, split

The single biggest lesson: **the style modifier dominates a thin subject.** "the empty floor, 3D sculpture --profile …" produces a random image, because the profile carries all the signal and "the empty floor" carries none. Every generated image comes out wildly different.

So each beat's prompt has two independent parts:

- **Subject** — a *detailed* description of the scene, grounded in what the video is actually saying at that beat. This is the part you write. Concrete, ~30–45 words, no style words.
- **Style modifier** — a short tag + a Midjourney `--profile`. The profile is the trained style lock; the tag stays tiny.

Composed prompt (non-human beat):

```
<bid> <detailed subject>, 3D sculpture --ar 16:9 --profile ytob5vr 7dkile2 5l34wh8 x9o4m9g
```

Write the subject from the beat's **narration**, not the terse slate note. "the conference room glow" → *"a modern glass conference room at dawn, a data team around a long table facing a wall screen showing one green line rising steeply, faces lit by the green glow…"*. Persist it into the beat sheet's `shot.suggested_prompt` so it's durable and the tool reuses it.

---

## 2. Style modifiers — a named library

In `runtime/style/vox-plates/claude/style.json`, `style_modifiers` maps a **style type** to a suffix + `--profile`. Pick per beat with `shot.style_type` (default `artsy`):

| style_type | suffix | profile |
|---|---|---|
| `artsy` | `3D sculpture` (Tove Jansson / Mary Blair look) | `ytob5vr 7dkile2 5l34wh8 x9o4m9g` |
| `photo` | `1980s aesthetic, iPhone photography in the style of William Eggleston` | `9vpvb2l 44qs9jw` |

The **profile is the style** — you don't need the verbose "in the style of …" text, the profile carries it. Add more style types (whiteboard, pixel, …) by editing the JSON; no code change.

> **`photo` makes photoreal people.** The tier re-check keeps subjects generic (no named real person/place), every photo fill gets an explicit AI-disclosure sidecar, and it's illustrative only — never passed off as a real photograph.

---

## 3. The recurring character (human beats)

When a beat's subject has a person, the tool auto-prepends **both** an image reference and a text description, so the *same man* appears across every beat:

```
<image-url> <bid> <char_desc>, <detailed subject>, 3D sculpture --ar 16:9 --profile …
```

- **`char_ref_url`** — `https://s.mj.run/U-VwEe7xSPo` (a Midjourney image reference; it *must* lead the prompt).
- **`char_desc`** — `39-year-old athletic man with a blond, buzz cut hairstyle, striking blue eyes`.

Both live in `style.json`. The tool decides "has a person" from keywords (man, woman, figure, philosopher, scholar, hands, portrait, …). Result: a consistent protagonist plays every human role — the philosopher, the scholar at the ledger, the cloaked doubter — same face, different costume/scene. Write the subject describing the *scene and costume*; let the char-ref carry the face.

---

## 4. Safety fences (the tool enforces these)

- **Spend gate.** `--backend midjourney` is dry-run by default: it composes and prints prompts, spends nothing. (The MJ posting itself is agent-driven in Chrome — MJ has no API.)
- **Tier re-check.** Any subject naming a real person, place, or dated event is refused — regardless of the shopping-list tag. *This is why you write generic figures:* "Descartes" → refused; "a 17th-century philosopher in a dark cloak" → passes, and dodges any likeness concern. All-caps words (SALE, TRUE) are fine — only Title-Case proper nouns trip it.
- **Matte fence.** `cutout` / `parallax` beats need an alpha MJ can't provide, so they're flagged **human-tier** — MJ can hand you a still, you extract the matte.
- **Provisional + provenance.** Every fill lands with a `.auto` marker (unreviewed) and a `.source.txt` sidecar (model, prompt, provenance: ai). Nothing is treated as final until you sign off.

Roughly: a reel has **≤7 auto-fillable vox beats** (deep-explainers 3–7, short reels 0–1). The rest is Manim/Remotion, which is code, never gen-AI.

---

## 5. Firing the burst

Compose and review first:

```
books/brutalist-art/art fill-pantry <reel> --backend midjourney
```

Then post the whole reel's queue into Midjourney in one burst — **space each submit ~4 seconds.** A rapid no-gap burst races the MJ page and silently drops posts (this bit us: B05/B23 vanished until re-fired with a gap). Each prompt carries its `B##` id, so it self-labels in the eventual download.

---

## 6. Animate, download, ingest

1. In MJ, **animate the ones you like** — the ingest prefers the `.mp4` per beat, so an animated beat becomes the pantry clip; an un-animated one would be the still.
2. **Download all** as a zip (or drop the loose files) into **`books/PANTRY/`** (or anywhere in the connected folder).
3. Ingest into the right reel:

```
books/brutalist-art/art fill-pantry <reel> --ingest books/PANTRY/<zip-or-folder>
```

The ingest unzips, matches each file to its beat — **primarily by the `B##` id in the filename**, subject text as fallback (robust to MJ truncating long prompts) — prefers the animation, and renames into `pantry/<bid>.mp4|png` with the sidecar + `.auto`. It only fills what's in the zip; it never touches beats already done.

### The one real gotcha: beat-id collisions

`B02` and `B27` exist in *many* reels. The ingest matches ids **within the reel you point it at**, so **keep each reel's download in its own zip** — animate + download one reel at a time, and ingest it against that reel. Don't let two reels share a zip.

---

## 7. Gotchas & fixes baked in

- **Slates faking "filled."** Pass-1 placeholder slates are small (~400 KB) mp4s in `media/`. The tool now ignores media under ~1.2 MB (and ignores sidecars), so a slate no longer reports a slot as filled.
- **`VOX:` label prefix** on `new_visual_element` is stripped from the subject automatically.
- **Where compile reads media.** `resolve_slot` reads `media/<bid>` (+ manim). The pantry drop is the source; the local `art run` intake moves/overrides pantry → media during the render.

---

## 8. Config quick reference

`books/brutalist-art/runtime/style/vox-plates/claude/style.json`:

```jsonc
{
  "style_modifiers": {
    "artsy": { "suffix": "3D sculpture",
               "params": "--ar 16:9 --profile ytob5vr 7dkile2 5l34wh8 x9o4m9g" },
    "photo": { "suffix": "1980s aesthetic, iPhone photography in the style of William Eggleston",
               "params": "--ar 16:9 --profile 9vpvb2l 44qs9jw" }
  },
  "default_style_type": "artsy",
  "char_ref_url": "https://s.mj.run/U-VwEe7xSPo",
  "char_desc": "39-year-old athletic man with a blond, buzz cut hairstyle, striking blue eyes",
  "mj_interval_sec": 240
}
```

Plate/config resolution is most-specific-wins: `<reel>/style/` → `<book>/youtube/_style/` → this channel default.

## 9. Commands cheat-sheet

```bash
# compose + review (spends nothing)
books/brutalist-art/art fill-pantry <reel> --backend midjourney

# ingest a downloaded zip/folder into the reel's pantry
books/brutalist-art/art fill-pantry <reel> --ingest books/PANTRY/<zip>

# render the reel locally (runs the QC gates; ~4K, multi-minute)
books/brutalist-art/art run <reel>
```

`<reel>` = e.g. `books/computational-skepticism-for-ai/youtube/claude-liam-dashboard-that-lied`.
