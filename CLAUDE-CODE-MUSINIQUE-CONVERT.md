# Claude Code Prompt — Unattended Musinique Conversion

Converts every base reel in the Musinique catalog into the Musinique ai-explainer /
Claude-skin cut: Claude skin + Baldwin register, the two-host 50/50 Liam+Puck
voice split, the greeting, and the Musinique "why it matters" tangent beat. Writes each
result to `beat_sheet.musinique.json` (base `beat_sheet.json` is never touched). No approval
pauses. Free pipeline only — no ElevenLabs, no publishing, no git. Does NOT regenerate
audio or render.

Run three of these in parallel — one per channel; each touches a different catalog, so
they don't conflict.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books`

Paste the whole block below — nothing to edit.

```text
Convert EVERY reel in the Musinique catalog to its ai-explainer / Claude-skin cut.
Unattended batch: no approval pauses, process reels independently, never let one
reel's failure stop the batch. Free pipeline only: no ElevenLabs, no
generate_audio.py, NO publishing, NO uploading, NO git commit or push. This job
edits BEAT SHEETS only — it does not regenerate audio or render.

CHANNEL: musinique
CATALOG: books/musinique/youtube   (reels nest at youtube/<topic>/<reel>/)
AI VOICE: Liam am_onyx     ORG VOICE: Puck  am_puck     (each reel is ONE voice; ~50/50 split)
REGISTER: Baldwin
GREETING: Liam reel -> "This is Liam for Musinique."   ·   org reel -> "This is Musinique."
TANGENT BEAT THEME: the relevance to indie artists

READ ONCE BEFORE THE BATCH
- SCRIPTS/hai_convert.py                               (the mechanical pass you call)
- brutalist-art/skills/make/channel-convert/SKILL.md   (this conversion, full rules)
- brutalist-art/skills/make/ai-explainer/SKILL.md      (the Claude skin + channel laws)
- brutalist-art/MUSINIQUE.md (the Baldwin charter — fights for the indie musician)

ONE-TIME SETUP
Work list = every directory under books/musinique/youtube that contains a beat_sheet.json.
Log the count.

PER-REEL LOOP (for each reel folder)
1. IDEMPOTENT SKIP. If beat_sheet.musinique.json exists AND has both a greeting line and a
   tangent beat (a beat with "tangent": true), log SKIPPED(done) and continue.
2. SOURCE. Read the reel's base beat_sheet.json. If missing/empty, log SKIPPED(no-base).
3. CLAUDE-SKIN + REGISTER REWRITE. Produce the ai-explainer / Claude-skin cut for
   claude-musinique: rewrite each beat's narration_text in the Baldwin register (per its
   VOICE.md / charter). Keep the Claude bookends ai-explainer defines (greeting first;
   "Your Turn" second-to-last; brand card last). Preserve real facts and equations —
   NO fabrication; label hypotheticals.
4. GREETING. Ensure an opening greeting beat exists, started as "This is Musinique." (the
   mechanical pass rewrites it to the correct Liam/org form once the voice is assigned).
5. TANGENT BEAT (only if missing). Insert ONE beat immediately after the first content
   beat. Narration in the Baldwin register, 2-4 sentences on: the relevance to indie artists. Give it:
   - beat_id = a NON-colliding id like "B01B" (NEVER renumber existing beats — their
     rendered manim/ and media/ clips are named by beat_id),
   - "act" naming the theme, and "tangent": true (idempotency marker),
   - a "shot" that will render — reuse a card/Remotion pattern already in this reel.
   Place it in the beats array right after the first content beat.
6. WRITE the result to beat_sheet.musinique.json (NOT beat_sheet.json).
7. MECHANICAL PASS. Run:
   python3 SCRIPTS/hai_convert.py --channel musinique <reel-folder>
   (assigns the 50/50 voice, sets every beat engine=kokoro + that voice, rewrites the
   greeting to the correct Liam/org form, sets metadata.register — edits the variant.)
8. LOG one line: reel, voice assigned, rewritten?, tangent added?.

GUARDRAILS
- Idempotent. Free voices only (never engine "elevenlabs", never generate_audio.py).
- No renumber (suffixed ids like B01B). Base beat_sheet.json NEVER modified. No fabrication.

FINISH
Write CONVERSION-LOG-musinique.md at books/musinique/youtube: total, converted, skipped(done),
skipped(no-base), failed (reasons), Liam/Puck voice counts. Then STOP — no audio,
no render, no publish.

AFTER (separate, human-run, free):
  generate_audio_kokoro.py <reel>   then   morning_render.py --channel musinique
```
