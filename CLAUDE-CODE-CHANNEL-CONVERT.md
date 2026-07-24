# Claude Code Prompt — Unattended Channel Conversion (HAI / Medhavy / Musinique)

Converts every base reel in a channel's catalog into the ai-explainer / Claude-skin
cut for that channel — Claude skin + channel register, the two-host 50/50 Liam+org
voice split, the greeting, and the channel's "why it matters" tangent beat. Writes
each result to `beat_sheet.<channel>.json` (the base `beat_sheet.json` is never
touched). No approval pauses. Free pipeline only — no ElevenLabs, no publishing, no
git. It does NOT regenerate audio or render; those are separate steps after.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books`

Set the channel on the first line of the prompt (`CHANNEL: hai` | `medhavy` |
`musinique`), then paste the whole block. Nothing else to replace.

```text
CHANNEL: hai

Convert EVERY reel in the CHANNEL's catalog to that channel's ai-explainer /
Claude-skin cut. Unattended batch: no approval pauses, process reels
independently, never let one reel's failure stop the batch. Free pipeline only:
no ElevenLabs, no generate_audio.py, NO publishing, NO uploading, NO git commit
or push. This job edits BEAT SHEETS only — it does not regenerate audio or render.

CHANNEL SPECS (use the row for CHANNEL above):
| channel   | catalog (under books/)          | org voice        | register   | greeting (Liam / org)                                   | tangent beat theme                                  |
| hai       | humanitarians_html/youtube      | Kore  af_kore    | Pragmatist | "This is Liam for Humanitarians AI." / "This is Humanitarians." | why a smart general audience should care about it   |
| medhavy   | medhavy/youtube                 | Bella af_bella   | Wonder     | "This is Liam for Medhavy." / "This is Medhavy."        | the pedagogy — how to teach and learn this topic    |
| musinique | musinique/youtube               | Puck  am_puck    | Baldwin    | "This is Liam for Musinique." / "This is Musinique."    | the relevance to indie artists                      |
Liam = am_onyx (the shared AI voice). Each reel is ONE voice; the split is ~50/50
across the catalog. The mechanical script assigns the voice + finalizes the greeting.

READ ONCE BEFORE THE BATCH
- SCRIPTS/hai_convert.py                                  (the mechanical pass you will call)
- brutalist-art/skills/make/channel-convert/SKILL.md      (this conversion, full rules)
- brutalist-art/skills/make/ai-explainer/SKILL.md         (the Claude skin + channel laws)
- brutalist-art/runtime/voices/<register>/VOICE.md        (the channel's register — pragmatist/wonder)
- For musinique register (Baldwin): brutalist-art/MUSINIQUE.md (the charter)

ONE-TIME SETUP
Resolve the CHANNEL's catalog root from the table. Build the work list = every
directory under it that contains a beat_sheet.json (reels nest at
youtube/<topic>/<reel>/). Log the count.

PER-REEL LOOP (for each reel folder)
1. IDEMPOTENT SKIP. If beat_sheet.<channel>.json already exists AND has both a
   greeting line and a tangent beat (a beat with "tangent": true), log
   SKIPPED(done) and continue.
2. SOURCE. Read the reel's base beat_sheet.json. If missing/empty, log
   SKIPPED(no-base) and continue.
3. CLAUDE-SKIN + REGISTER REWRITE. Produce the ai-explainer / Claude-skin cut for
   claude-<channel>: rewrite each beat's narration_text in the channel's register
   (per its VOICE.md). Keep the Claude bookends the ai-explainer skill defines
   (greeting beat first; "Your Turn" second-to-last; channel brand card last).
   Preserve real facts and equations — NO fabrication; label hypotheticals.
4. GREETING. Ensure the opening greeting beat exists (start it as "This is
   <channel org name>." — the mechanical pass rewrites it to the correct
   Liam/org form once the voice is assigned).
5. TANGENT BEAT (only if missing). Insert ONE beat immediately after the first
   content beat (the beat after the greeting). Narration in the channel register,
   2–4 sentences on the channel's tangent theme (see the table). Give it:
   - beat_id = a NON-colliding id like "B01B" (NEVER renumber existing beats —
     their rendered manim/ and media/ clips are named by beat_id),
   - "act" naming the theme, and "tangent": true (idempotency marker),
   - a "shot" that will render — reuse a card/Remotion pattern already used in
     this reel (a stakes/CARD beat), matching its visual convention.
   Place it in the beats array right after the first content beat.
6. WRITE the result to beat_sheet.<channel>.json (NOT beat_sheet.json).
7. MECHANICAL PASS. Run:
   python3 SCRIPTS/hai_convert.py --channel <channel> <reel-folder>
   This assigns the reel's 50/50 voice, sets every beat engine=kokoro + that
   voice, rewrites the greeting to the correct Liam/org form, and sets
   metadata.register. It edits beat_sheet.<channel>.json in place.
8. LOG one line: reel, voice assigned, rewritten?, tangent added?.

GUARDRAILS
- Idempotent — re-running changes nothing already complete.
- Free voices only — never set engine "elevenlabs"; never call generate_audio.py.
- No renumber — new beats get suffixed ids (B01B).
- Base beat_sheet.json is NEVER modified.
- No fabrication.

FINISH
Write a CONVERSION-LOG-<channel>.md at the catalog root: total reels, converted,
skipped(done), skipped(no-base), failed (with reasons), and the Liam/org voice
counts. Then STOP — do not regenerate audio, render, or publish.

AFTER (separate, human-run, free):
  generate_audio_kokoro.py <reel>   then   morning_render.py --channel <channel>
```
