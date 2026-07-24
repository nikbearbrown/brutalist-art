# Claude Code Prompt — Audit & Fix the CLI Explainers (Liam / terminal / outro)

Audits every claude-cli explainer and fixes three recurring defects, then
regenerates audio (free Kokoro) and re-renders at 4K so the fixes show. Unattended,
FREE only — never ElevenLabs, never publishes. Uses the existing `your-turn` skill
for the closing block.

THE THREE DEFECTS
1. **Liam says "Bear."** The claude-cli persona is **Liam (in for Bear)** — Liam is
   the speaker. Narration where Liam introduces or refers to himself as Bear is wrong.
   (The CHANNEL name "Nik Bear Brown / nikbearbrown.com" and the @NikBearBrown handle
   are branding and stay — only the *speaker identity* must be Liam, never "this is Bear.")
2. **Claude terminal missing its title.** The opening Claude terminal composer should
   read **"Claude ✳ [SEGMENT TITLE]"** — greeting + persona + the beat's title. Many
   show just "Claude ✳" with no title, or open on a GRAPHIC with no terminal beat at all.
3. **The new outro is missing.** The standardized close is the `your-turn` three-beat
   block: VERDICT recap → "Your Turn" prompt → TITLE re-read (all Liam). Many still have
   the old outro ("Nik Bear Brown. Build it with a CLI…").

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books`

Optionally scope to one book by setting SCOPE below (folder-by-folder). Paste the block.

```text
SCOPE: (blank = whole catalog; or a book folder like computational-skepticism-for-ai)

Audit and fix every CLI explainer. Unattended batch: no approval pauses, reels
independent, one failure never stops the batch. FREE ONLY — Kokoro audio via
generate_audio_kokoro.py; NEVER ElevenLabs, NEVER generate_audio.py, NO publish,
NO git commit or push.

READ ONCE BEFORE THE BATCH
- brutalist-art/skills/make/ai-explainer/SKILL.md        (the Claude terminal beat, persona, bookends)
- brutalist-art/skills/upload/your-turn/SKILL.md OR skills/make/*/your-turn  (the closing block spec)
- brutalist-art/runtime/scripts/generate_audio_kokoro.py (free voice)
- brutalist-art/runtime/scripts/run.sh                   (art run: render + composite audio)

WORK LIST
Every reel under books/(SCOPE or all) whose slug marks it a claude-cli explainer:
slug contains "-cli-" or starts with "claude-liam-cli". Reels nest at
youtube/<topic>/<reel>/ in some books. Back up each beat_sheet.json to
beat_sheet.json.clifix-bak before editing (once).

PER-REEL AUDIT + FIX (idempotent — fix only what's wrong)
1. LIAM NOT BEAR. Read every beat's narration_text. The speaker is Liam. Fix any
   line where Liam self-identifies as Bear (e.g. "This is Bear" -> "This is Liam,
   in for Bear"; a "Thanks Bear" handoff on a beat whose own voice is Liam ->
   "Let's recap"). DO NOT touch the channel name "Nik Bear Brown" / "nikbearbrown.com"
   / "@NikBearBrown" — that is branding, not a speaker claim.
2. CLAUDE TERMINAL + TITLE. Ensure beat 0 is the Claude terminal composer
   (ClaudeComposerAsk) per ai-explainer: world-language hello + persona + the segment
   TITLE, so it reads "Claude ✳ [TITLE]" not a bare "Claude ✳". If the opener is a
   GRAPHIC with no terminal beat, add/convert it to the terminal composer. Anywhere a
   segment/terminal card shows "Claude ✳" with no title, set its title prop to the
   beat's segment title (Title Case).
3. OUTRO. Ensure the last three beats are the `your-turn` block: VERDICT recap
   (ClaudeVerdictArtifact) -> "Your turn." (ClaudeComposerAsk, a prompt relevant to
   THIS video, Liam reads it in full) -> TITLE re-read (ClaudeTitleOutro), all Liam
   (kokoro am_onyx). If the reel has the old outro or is missing the block, apply the
   your-turn skill's rules to replace the closing beats. Use non-colliding beat_ids if
   adding beats (never renumber existing ones — their rendered clips are named by id).
4. If nothing was wrong, log SKIPPED(clean) and continue.

AFTER FIXING A REEL (only if it changed)
5. REGENERATE AUDIO (free — narration changed):
   python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py <reel>
6. RE-RENDER at 4K (skip authoring gates — re-render of shipped content):
   ART_FACTS=0 ART_QC=0 bash brutalist-art/runtime/scripts/run.sh <reel>
7. VERIFY the new master has audio and reads 3840x2160.
8. LOG one line: reel, fixes applied (liam / terminal / outro), rendered?.

GUARDRAILS
- FREE ONLY (never engine "elevenlabs", never generate_audio.py). No publish, no git.
- Idempotent — a clean reel is left untouched.
- No renumber; back up beat_sheet.json to .clifix-bak first.
- No fabrication in any rewritten narration.

FINISH
Write CLI-FIX-LOG.md at the SCOPE root (or books/): totals, reels fixed by defect
(liam / terminal / outro), skipped(clean), failed(reasons). Then STOP — no publish.
```
