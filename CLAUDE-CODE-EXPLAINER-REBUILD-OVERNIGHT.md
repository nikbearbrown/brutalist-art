# Claude Code Prompt — Overnight Rebuild of claude-explainer Reels to Current House Laws

Rebuilds already-built claude-explainer reels so they obey the CURRENT House
laws in `skills/make/ai-explainer/SKILL.md` (LOGO, REBUILD,
SHOW-DON'T-TELL, FILL-THE-CANVAS, DOUBLE-CHECK, VISUAL QC, HANDOFF read-aloud).
Free pipeline, unattended, reviewable in the morning. Nothing published.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace.

```text
Overnight batch: REBUILD each claude-explainer reel in the WORK LIST so it
complies with the CURRENT House laws in skills/make/ai-explainer/SKILL.md.
These reels were built under the OLD rules and predate the new laws. This is a
rebuild in place of the visuals (and the few beats whose narration must
change) — NOT a re-scripting from scratch and NOT a reflow. Unattended: no
approval pauses, reels processed independently, one reel's failure never stops
the batch. Free pipeline only: Kokoro am_onyx, NO ElevenLabs, no higgsfield,
no publishing, NO git commit or push. Back up each original before
overwriting; leave every new cut in its folder for review.

READ COMPLETELY BEFORE ACTING
- AGENTS.md
- skills/make/ai-explainer/SKILL.md   (the House laws are the SPEC to
  rebuild toward — read the whole Hard-rules section)
- CLAUDE-CODE-VISUAL-QC-CHECK.md
- runtime/remotion/src/tokens/claude.ts and tokens/layout.ts (SAFE)
- skills/upload/youtube-publisher/SKILL.md (only to resolve id -> folder via
  the publish ledger)

STEP 0 — RESOLVE + CLASSIFY (skip what isn't a claude-explainer reel)
For each WORK LIST id: resolve it to its local reel folder (the publish
ledger youtube_publish_ledger.json maps id -> folder; else match by title).
Open the folder's beat_sheet.json and classify:
- REBUILD it ONLY if it is a claude-explainer reel: metadata palette "claude",
  register "Teardown", channel claude / claude-liam (a Liam/Bear Teardown
  teardown-of-a-paper/profile reel).
- SKIP + log (not-an-explainer) if it is a technique showcase ("Every Remotion
  Move…", "One Wordmark…" — component-showcase format), a pure brand/logo
  reel, or any non-explainer brand. Do not touch these.
- If a folder can't be resolved, log SKIPPED(no-folder) and continue.
Print the resolved REBUILD list and the SKIP list before building.

STEP 1 — AUDIT EACH REBUILD REEL against the House laws
Read the beat_sheet + sample a few frames of the existing mp4. For every beat,
record which laws it violates:
- SHOW-DON'T-TELL: a beat whose narration describes something that can move but
  renders as a static card / title / bullet list. → must become animation.
- REBUILD: any screenshot or lifted static figure standing in for a rebuilt
  graphic. → rebuild as native animation.
- FILL-THE-CANVAS / TYPESIZE: undersized type or content clustered in the top
  third over dead space. → scale up, fill SAFE.
- LOGO: missing NBB corner bug on any beat, or no full-size NBB on the outro.
- HANDOFF: the "Your turn." prompt only appears on screen (not read aloud and
  discussed), or is a bland "learn more" rather than an interesting,
  episode-extending prompt.
- OUTRO / COLD OPEN / SPARK-LINE / one-terracotta: any drift from the laws.
Write the audit to <folder>/_rebuild/AUDIT.md: beat | law(s) violated | fix.

STEP 2 — REBUILD TO COMPLIANCE (audio-preserving where it can be)
- Animate the telling beats: replace each static/telling beat with a native
  animated Remotion beat (C2 rhetorical pattern, C3 concept illustration, or
  Manim) that ENACTS the narration, reveals landing on the spoken words
  (SHOW-DON'T-TELL). Rebuild any screenshot as animation (REBUILD LAW), only
  source-verifiable numbers on screen.
- FILL-THE-CANVAS: size type and content to occupy SAFE (from layout.ts) — no
  timid fonts, no dead lower half. Position from SAFE; maxWidth + wrap on
  variable text; the ~24px floor is a floor, not a target.
- LOGO: add the low-opacity NBB corner bug (lower-right, inside SAFE) to EVERY
  beat, and the full-size NBB on the outro card. Source from the nbb skill /
  runtime assets; fallback @NikBearBrown wordmark.
- HANDOFF: make the "Your turn." prompt an interesting, episode-extending
  prompt, and rewrite that beat's narration so Liam READS it aloud and
  DISCUSSES why to run it.
- AUDIO RULE (free pipeline): keep every unchanged beat's existing audio as-is.
  Regenerate audio ONLY for beats whose narration text changed (the handoff
  read-aloud; any DOUBLE-CHECK de-sensationalizing correction) — and ONLY on
  reels already voiced by Kokoro/claude-liam (free). If a reel is voiced by
  Bear/ElevenLabs (paid), do the VISUAL rebuild only, DO NOT spend on audio,
  and flag in AUDIT.md that the handoff-read-aloud + any narration fix needs a
  later gated ElevenLabs pass. Never change timing of unchanged beats.
- DOUBLE-CHECK: where a number or claim on screen isn't supported by the reel's
  own SOURCES.md / source chapter, fix it (correct or drop) and log it — never
  invent. Keep the Teardown voice.

STEP 3 — RENDER + VISUAL QC
Back up the current mp4 to <folder>/<slug>-pre-rebuild.mp4 first. Re-render the
changed beats and recompile. Then run the VISUAL QC LAW pass: sample frames
(>=2 fps + per-beat 15/50/85%), Read the PNGs, run the 9-point rubric (edge
bleed, title-safe, overflow, collision, legibility, brand bug, aspect, CANVAS
FILL). Log to <folder>/_qc/REPORT.md. Fix root causes and re-render until zero
BLOCKER/MAJOR. Runtime should stay ~unchanged (audio is mostly preserved).

STEP 4 — LOG + REPORT
- Per reel, append to youtube/_explainer-rebuild/BUILD-LOG.md: slug | laws
  fixed | beats animated | audio-regenerated? (yes/visual-only-flagged) | QC
  verdict | done/failed/skipped.
- On failure after two attempts, restore the -pre-rebuild.mp4, write FAILED.md,
  and continue — never ship a broken reel.
- When finished, write youtube/_explainer-rebuild/SUMMARY.md and end with:
  counts (rebuilt / visual-only-flagged / skipped-not-explainer / failed), and
  a REVIEW LIST of the new mp4 paths (and their -pre-rebuild.mp4 twins) so I can
  compare before/after in the morning. Nothing is published; re-upload is a
  separate human step.

WORK LIST (id — title)
iUXC69MZl8E — Persisting Progress Across Context Windows
oPI3c6pf1N4 — The Hard Case
mvCN15H91Ko — The Engineer Who Stayed (profile)
m4tv4cL1l7Y — The Fluency Ceiling
kes_0sIS-k8 — Same Text, Better Scaffold
c0jDRjBpnQI — The CRA Ladder
HcQlKBkA9tM — Caching Pixels You've Already Seen
F-3csy0YmMs — Claude, Seeded
_NBPIIa4fVQ — Claude, Peer-Reviewed
P1RfhJJ6hS0 — Claude on the Clock
QENWK9l8J9s — When Safety Training Fails
Dm8-lZ-Y0ZE — The Sycophancy Gradient
1yCYkISIMDQ — An Off Switch for Dangerous Knowledge
okgNY7sHYmE — What 81,000 People Want from AI
fR9GCsYtjYs — Claude's Values Across Models and Languages
-WCwbxmraIA — Claude, For Teachers
4HoBA5otwMU — Claude, On Average
eX_jbpfwmI0 — Claude, Taught
PK8o4CU_2m8 — The Photoelectric Effect
(Plus any other claude-explainer reel folders you find alongside these — audit
them too. The "Every Remotion Move…" / "One Wordmark…" technique showcases are
NOT explainers: skip and log them.)
```
