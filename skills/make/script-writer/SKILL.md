---
name: script-writer
description: >
  Turn any text — a chapter, lecture notes, a paper, a tweet, a YouTube
  transcript, a pasted block — into the script for an explainer video:
  narration in the Sardonic voice by default (override to Teardown via
  metadata.register), sequenced by the Brown Blue pedagogical constitution.
  Output is style-agnostic — a script document plus a vox beat_sheet.json
  whose beats carry role + narration + visual intent but leave shot.source
  open, so the same script can later be dressed as pure Manim, the
  @NikBearBrown house style, a Remotion cut, or a doodle. Default engine
  Kokoro am_onyx (free); ElevenLabs only as explicit override. Writes and
  audits the script only — never renders, generates audio, or spends. Use
  when the user types `script [input]`, asks to make an explainer script
  from this text, a teardown script, or to turn a chapter/lecture/transcript
  into a video script.
---

# script-writer (formerly `teardown-script`) — `script`

Turn **any text** — a chapter, lecture notes, a paper, a tweet, a YouTube transcript, a pasted
block — into the *script* for an explainer video: narration in the
**Sardonic voice** (`voices/sardonic/VOICE.md`) by default, sequenced by the **Brown Blue
pedagogical constitution** (`reference/pedagogy.md`). The output is
**style-agnostic** — a script document plus a vox `beat_sheet.json` whose beats
carry role + narration + visual *intent* but leave `shot.source` open, so the
same script can later be dressed as pure Manim, the @NikBearBrown house style, a
Remotion cut, or a doodle. **The script is the substance; the style is applied
downstream.**

> **Default engine: Kokoro (free, local). Default voice: am_onyx.** Override with
> `metadata.engine` / `metadata.voice_kokoro` (per sheet) or `beat.engine` /
> `beat.voice` (per beat). To use ElevenLabs set `metadata.voice_id`. To use the
> Teardown narration register instead, set `metadata.register:"Teardown"`.
> All other engines and voices remain fully available as explicit overrides.

This command writes and audits a script. It does **not** render, generate audio,
or spend anything. Hand the finished folder to `slate cut` / `remotion pass` /
`generate_audio.py` when you want to build it.

## Trigger
`script [text | file.md | chapter | lecture-notes | tweet | transcript | pasted block]  [--out [dir]]  [silent]`

Also fires on: "make an explainer script from this", "teardown script for …",
"turn this into a video script in the teardown voice."

## The two constitutions it fuses
1. **Voice — Sardonic** (`../../voices/sardonic/VOICE.md`): dry, spare, capable-adult.
   Economy and rigor; dry wit in footnotes; trusts the viewer to follow without
   hand-holding. **NO FABRICATION.** Forbidden phrases are hard-banned (see below).
   *(Override to Teardown by setting `metadata.register:"Teardown"` — the full
   Feynman × MKBHD design-critic register in `voices/teardown/VOICE.md`.)*
2. **Pedagogy — Brown Blue** (`reference/pedagogy.md`, a self-contained copy of
   the constitution): concrete-before-abstract, mystery-framed open, discovery
   narration, the HOOK→…→BOUNDARY arc, derived length, the boundary beat.

When the two ever seem to conflict, **pedagogy owns structure, voice owns
sentences.** The arc is Brown Blue; the words inside each beat are Sardonic.

## The build loop (phases — never skip a gate)

**Phase 0 · Intake** (skipped by `silent`). Read the input text. Say back, in the
Teardown voice, the **one insight** this video delivers and the **key case** that
motivates it. If the text carries more than one insight, push back — *"this is
two videos; which insight do you want, or split it?"* — don't quietly cram it.

**Phase 1 · Gate-1 sequencing** (`reference/pedagogy.md` §1–§2, §5–§6).
- Name the **key exercise / key case** in one line (this lives in the script
  draft and metadata, never spoken as a preamble).
- Find the **mystery gap**: the fact that *should* predict an outcome, and the
  case where it doesn't. Utility framing ("understanding X is critical for Y")
  is banned as the opener.
- **Derive the length** — count the arc, ~5–9 s/beat, add HOLD time — and report
  the tier (Single-insight 2–4 / Standard 4–8 / Multi-act 8–15, the last needs
  explicit approval). Never pad, never rush.
- List **deferrals**: anything cut for scope goes under "deferred" (→ BOUNDARY).

**Phase 2 · Write the narration** in the Sardonic voice, beat by beat.
- Explain the machinery; reveal what the design optimized for; name one trade-off.
- **Discovery voice** (§3): "notice what just happened", "so we're stuck —
  unless—". Never "it can be shown that" — if it can be shown, the beat shows it.
- **NO FABRICATION.** Use only facts present in the input text (or common, load-
  bearing knowledge you are certain of). If a needed number/fact is missing, write
  `[VERIFY: …]` inline — never invent people, quotes, data, or history. Label
  hypotheticals ("Suppose…", "Imagine…").

**Phase 3 · Assign roles + visual intent** (§4). Every beat gets a role from
`HOOK · INSTANCE · TRANSFORM · ABSTRACTION · TANGENT · PAYOFF · BOUNDARY`, in that
partial order. Hard rules the gate enforces:
- Opens on **HOOK**, unsolved, zero vocabulary/notation.
- **≥2 INSTANCE beats shown *moving* before each ABSTRACTION.**
- Definitions arrive as **endpoints**, not openers.
- Any ABSTRACTION that **lands an equation** → set `lands_equation:true` and
  follow it immediately with a **TANGENT** beat that *explains* the symbols
  (never re-derives).
- **PAYOFF** puts the HOOK's object back on screen (`references_hook:true`).
- **BOUNDARY** (fused outro): one line of what was *not* taught + one concrete
  `viewer_exercise`.
Give each beat a `visual_intent` — what the viewer should SEE — but do **not**
pick a renderer. Leave `shot.source` null.

**Phase 4 · Emit** into `[out]/` (default `reels/[slug]/`; for a book, pass
`--out ../[book]/youtube/[slug]/`):
- `script.md` — the human read: title, the key-case line, derived length + tier,
  each beat (`ROLE · narration · [visual]`), the filled **Gate-1 audit table**,
  and a **Deferred** list. Clean markdown.
- `beat_sheet.json` — the style-agnostic vox sheet (schema in
  `reference/schema.md`).

**Single-file mode.** When the input is exactly one text file (a transcript, a
note dump), name the outputs **`[topic]-[title].md`** and `[topic]-[title].json`
instead of `script.md` / `beat_sheet.json` — both slugified (lowercase; every run
of non-alphanumerics → a single hyphen; trimmed). `topic` and `title` are the ones
you derive in Phase 1 (topic = the field/area in 1–3 words; title = the on-screen
answer). Write them beside the source unless `--out` says otherwise; the source
file is never renamed or modified. Example: `graph-theory-why-v-minus-e-plus-f-equals-2.md`.

**Phase 5 · Gate** — run the linter; it must PASS before you hand off:
```bash
python3 aspects/teardown-script/scripts/td_script_gate.py [out]
```
Fix every FAIL and re-run. Warnings are advisory (forbidden-phrase hits, off-pace
beats) — clear them unless you can defend keeping them.

## Output contract (style-agnostic beat_sheet)
`metadata`: `title · slug · register:"Sardonic" · engine:"kokoro" ·
voice_kokoro:"am_onyx" · voice_id:"${ELEVENLABS_VOICE_NIKBEARBROWN}" ·
palette:"teardown" · style_preset:"nikbearbrown" · pedagogy:"brownblue" ·
key_case · tier · source · total_estimated_duration_seconds · deferred[]`.
*(`voice_id` is the ElevenLabs override — unused when engine is kokoro but kept
so switching engines requires no schema change. Set `register:"Teardown"` to
override the narration style. Set `engine:"elevenlabs"` + remove `voice_kokoro`
to route audio to generate_audio.py instead.)*
`beats[]`: `beat_id · role · narration_text · visual_intent · on_screen_text? ·
estimated_duration_s · lands_equation? · references_hook? · viewer_exercise? ·
shot:{ type:"GRAPHIC", source:null, motion:"fade" }`.
`palette`/`voice`/`style_preset` are **defaults, not commitments** — the sheet is
the basis for any style. To dress it: `slate cut [dir]` (house/Manim),
`remotion pass [dir]` (Remotion), or hand the roles to any other builder.

## Forbidden phrases (Sardonic — the gate warns on these)
Never: "one could argue", "it seems as though", "it can be shown", "obviously",
"clearly", "isn't this amazing", "isn't it fascinating", "innovative"/"revolutionary"
without saying what changed, "premium"/"sleek"/"seamless" without a functional
definition, specs without context. The Sardonic voice is spare and dry — never
gushing, never warm, never padding. Instead: state the fact and move on; let the
reader work through the gap; put the wit in a footnote, not the main line.

## Silent modifier
`script [text] silent` → skip intake and pushback, execute immediately. All
pedagogy gates, the arc, the forbidden-phrase ban, and NO FABRICATION still hold.
Clean output only.

## Worked example
`reference/example/` — a complete pass (zero-point energy) with its `script.md`
and `beat_sheet.json`; run the gate on it to see a green board.
