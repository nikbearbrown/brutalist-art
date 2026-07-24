# Claude Code Prompt — CLI-Explainer SPINE Fix (structural conformance batch)

Successor to CLAUDE-CODE-CLI-EXPLAINER-FIX.md. That pass fixed the three
surface defects (Liam / terminal title / your-turn outro). THIS pass brings
every CLI reel up to the FULL `cli-explainer` spine
(`brutalist-art/skills/make/cli-explainer/SKILL.md` — the renamed
`terminal-screencast`). Unattended, FREE only — Kokoro audio, never
ElevenLabs, never publishes, no git.

STATE AS OF 2026-07-19 (see TMP/CLI-SPINE-AUDIT-2026-07-19.md)
- 1,741 CLI reels audited; the MECHANICAL fixes are already applied
  (spark-line greetings, composer segment titles, empty outro titles —
  1,116 sheets patched, originals in beat_sheet.json.spinefix-bak).
- What remains is STRUCTURAL, by flag (a reel can carry several):
  B00-NOT-COMPOSER 1552 · NO-CODE 524 · NO-YOURTURN 432 · NO-SUMMARY 338 ·
  BAD-OUTRO 313 · NO-PROBLEM 294 · SCHEMA-LEGACY 90 · B00-UNANSWERED 71 ·
  NO-REVISION 62
- The worklist with per-reel flags: TMP/CLI-SPINE-WORKLIST-2026-07-19.json
  (re-generate any time: `python3 SCRIPTS/cli_explainer_audit.py [book]`).

Run Claude Code from `/Users/bear/Documents/CoWork/bear-textbooks/books`.
Scope ONE BOOK per run (CLI explainers span many books; folder-by-folder is
the clean shape). Paste the block.

```text
SCOPE: <book folder, e.g. computational-skepticism-for-ai>

Bring every CLI reel in SCOPE up to the full cli-explainer spine. Unattended
batch: no approval pauses, reels independent, one failure never stops the
batch. FREE ONLY — Kokoro via generate_audio_kokoro.py; NEVER ElevenLabs,
NEVER generate_audio.py, NO publish, NO git.

READ ONCE BEFORE THE BATCH
- brutalist-art/skills/make/cli-explainer/SKILL.md   (the spine + all laws)
- brutalist-art/skills/make/ai-explainer/SKILL.md    (house laws, persona)
- brutalist-art/skills/upload/your-turn/SKILL.md OR skills/make/*/your-turn
- SCRIPTS/cli_explainer_audit.py                     (the conformance checker)
- TMP/CLI-SPINE-WORKLIST-2026-07-19.json             (per-reel flags — your work list)

WORK LIST
Reels in SCOPE listed in the worklist. Trust the flags but re-verify per reel
(sheets may have moved since the audit). Back up beat_sheet.json to
beat_sheet.json.spinefix-bak if no backup exists yet. Never renumber existing
beat_ids — rendered clips are named by id; new beats get non-colliding ids.

PER-REEL FIX (idempotent — fix only the flags present)
1. B00-NOT-COMPOSER — the reel opens on NikBearBrownOpen, a SLATE, or any
   non-composer. Convert/insert B00 as the composer cold open per COLD OPEN
   LAW: ClaudeComposerAsk, world-language hello + persona greeting, segment =
   episode title, command = the reel's real first ask (borrow the first ASK
   beat's command if one exists, else derive from the title), output = 2-4
   result lines so the ask lands ANSWERED. Liam narration ("This is Liam, in
   for Bear" only if B00 narration is being rewritten anyway — IN-FOR-BEAR
   LAW). Books whose subject is another tool keep their own skin: codex-*
   books use CodexComposerAsk/CodexCodeBeat/CodexTitleOutro (real components,
   registered under Codex-Templates); tools with no skin yet (e.g. copilot)
   use the claude default.
2. B00-UNANSWERED — composer opener with no output lines: add 2-4 plausible,
   non-fabricated result lines consistent with the reel's actual output beats.
3. NO-PROBLEM — insert a PROBLEM beat after B00, before the first ask: the
   stakes, why the viewer should care, no prompt yet. New narration, Teardown
   voice, NO FABRICATION.
4. NO-CODE — every ask cycle needs its CODE beat (ClaudeCodeBeat or skin
   equivalent) showing the ACTUAL source (ACTUAL-CODE LAW): pull real lines
   from the reel's scenes.py / sim JS / generated script, trimmed to what
   teaches, with a sparkLine. Never pseudocode.
5. NO-REVISION (16:9 only) — add the second cycle: CHANGE composer beat
   (runningText "updating…", greeting "The change,") -> revised CODE ->
   better OUTPUT. Reuse existing output media where the reel already has a
   second output; otherwise the new OUTPUT beat ships as a labeled slate.
6. NO-SUMMARY — insert the SUMMARY beat (the lesson in one beat) before the
   closing block.
7. NO-YOURTURN / BAD-OUTRO — apply the your-turn skill: VERDICT recap
   (ClaudeVerdictArtifact) -> "Your turn." composer with a prompt RELEVANT to
   this video, read in full -> ClaudeTitleOutro title re-read. All Liam.
8. SCHEMA-LEGACY — the sheet is the old label/narration/shots[] schema:
   rebuild it in the shared beat_sheet schema first (map label->act,
   narration->narration_text, shots[0]->shot), THEN apply steps 1-7.
9. Spark-line, segment-title, outro-title fixes are already applied
   catalog-wide; re-check anyway (SPARK-LINE LAW: no empty greeting on inner
   composer beats).

AFTER FIXING A REEL (only if narration changed)
10. python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py <reel>
11. ART_FACTS=0 ART_QC=0 bash brutalist-art/runtime/scripts/run.sh <reel>
12. VERIFY: master has audio, 3840x2160; then
    python3 SCRIPTS/cli_explainer_audit.py <SCOPE> — the reel must come back
    clean or its remaining flags logged with a reason.

GUARDRAILS
- FREE ONLY. No publish, no git. Idempotent. No renumbering. No fabrication.
- Props-only changes (no narration touched) need re-render but NOT audio regen.

FINISH
Write CLI-SPINE-FIX-LOG.md at the SCOPE root: totals, per-reel flags fixed,
skipped(clean), failed(reasons). Re-run the auditor for the scope and paste
its summary line into the log. Then STOP.
```

After a scope completes, stage the corrected videos for review:

```bash
python3 /Users/bear/Documents/CoWork/bear-textbooks/books/SCRIPTS/morning_render.py <book> --rendered-only --shorts 0 --count 999
```
