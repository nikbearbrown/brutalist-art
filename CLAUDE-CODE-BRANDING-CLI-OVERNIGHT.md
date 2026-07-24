# Claude Code Prompt — Overnight claude-cli Explainers (branding-and-ai cli-ideas)

Builds one **claude-cli** explainer for every card in
`branding-and-ai/youtube/cli-ideas.md`, unattended, on the free pipeline.
Leaves reviewable cuts — nothing published.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace.

```text
Overnight batch: build a claude-cli explainer video for EVERY card in
../branding-and-ai/youtube/cli-ideas.md (12 cards). Unattended — no approval
pauses, process cards independently, one card's failure never stops the
batch. Free pipeline only: Kokoro am_onyx, NO ElevenLabs, no higgsfield, no
publishing, NO git commit or push. Leave every cut in its folder for review.

READ COMPLETELY BEFORE ACTING
- AGENTS.md
- skills/make/cli-explainer/SKILL.md   (the claude-cli builder: the
  required beat spine, THE REVISION LAW, the cli-vs-claude-cli Skins split,
  and the House-laws block — obey all of it)
- skills/make/ai-explainer/SKILL.md       (House laws canonical: LOGO,
  REBUILD, SHOW-DON'T-TELL, FILL-THE-CANVAS, DOUBLE-CHECK, VISUAL QC, HANDOFF)
- skills/make/cli-explainer/reference/example-cli-beat_sheet.json
- runtime/remotion/src/tokens/claude.ts and tokens/layout.ts (SAFE)
- docs/remotion-best-practices/SKILL.md
- ../branding-and-ai/youtube/cli-ideas.md      (the 12 cards = the work list)
- ../branding-and-ai/chapters/                 (the SOURCE OF TRUTH for every
  number and claim — DOUBLE-CHECK against these, never the card alone)

CHANNEL / FORMAT (every video)
- claude-cli skin: the CLAUDE interface (ClaudeComposerAsk / ClaudeCodeBeat,
  Claude fidelity palette). NOT the generic cli terminal skin.
- Channel claude-liam: persona Liam in for Bear, Kokoro am_onyx, register
  TEARDOWN. "This is Liam, in for Bear" in B00 and the outro (IN-FOR-BEAR
  LAW). Folder chip @NikBearBrown. NBB logo bug on every beat, full-size on
  the outro (LOGO LAW).
- 1920x1080 (16:9), 30fps. Audio-first: Kokoro narration measured per beat
  FIRST; beats conform to audio. Expect ~3–5 min each. (Free pipeline, so no
  GATE P — the seatbelt is met: git-tracked, regenerable, zero paid spend.)

THE SPINE (per cli-explainer — every video, 16:9)
INTRO (cold open, ClaudeComposerAsk, ask lands answered) → PROBLEM (the card's
Hook = the why/stakes, before any prompt) →
  cycle 1:  CLI (show + discuss the prompt) → CODE (the generated code — the
            CRITICAL OUTPUT; show and discuss it) → OUTPUT (the run's result) →
  cycle 2 = the revision:  CLI (revised prompt, "updating…") → CODE (the diff
            that matters) → OUTPUT (the BETTER result) →
SUMMARY (the verdict / teardown angle, one beat) → NEXT STEPS (HANDOFF —
"Your turn." with an INTERESTING prompt that extends the build into the
viewer's own work; Liam READS it aloud and DISCUSSES why to run it) → OUTRO
(ClaudeTitleOutro, title restate). THE REVISION LAW: the 16:9 ALWAYS has the
revision cycle — do not ship a single-cycle 16:9.

OUTPUT BEATS — REBUILD AS ANIMATION, never a screenshot or a real screen-grab
The cards say "Screen-rec mp4", but this is an unattended build with no live
capture — so REBUILD each card's output artifact as a native ANIMATED Remotion
beat in the Claude palette: the ASCII table, the scorecard, the health matrix,
the dual-track plan, the dependency table — animate it building in (rows
drawing on, the score bar growing, the flagged cell lighting terracotta),
synced to the narration (SHOW-DON'T-TELL). The CODE beat shows real, plausible
source (ACTUAL-CODE LAW) that could generate that output. A beat with no
buildable animation ships as a labeled slate — never a static png, never a
faked capture.

HONESTY (DOUBLE-CHECK LAW — these cards cite hard numbers)
Every on-screen number (e.g. "82% of developers", "$206,000 average",
"30–50% above") must be verified against ../branding-and-ai/chapters/ before
it appears. If a card's figure isn't supported in the book, teach the claim
without the number — never invent or guess a statistic. Log each on-screen
number and its chapter source in the video's SOURCES.md. Rewrite the card's
framing in the Teardown voice; do not parrot the card.

PER-CARD LOOP  (output folder: ../branding-and-ai/youtube/claude-cli-<slug>/)
1. Parse the card: title, lane (BUILD/RESEARCH), hook, the concept, the
   artifact it builds, and the revision the story turns on. Derive a
   kebab-case slug.
2. If ../branding-and-ai/youtube/claude-cli-<slug>/ already has a finished
   mp4, log SKIPPED(exists) and continue (idempotent).
3. Author beat_sheet.json in the spine above (Claude-skin input beats,
   animated output beats, scenes.py for any Manim). RESEARCH-lane cards still
   use the same spine — the "CLI" is the research prompt, the "CODE"/critical
   output is the synthesized brief/table, the revision refines the synthesis.
4. Generate Kokoro am_onyx narration per beat; conform beats to audio.
5. Render (vox_run.sh / the CLI d3 lane as appropriate); fill output slates
   with the animated rebuilds.
6. VISUAL QC LAW: sample frames (>=2 fps + per-beat 15/50/85%), Read the PNGs,
   run the 9-point rubric (edge bleed, title-safe, overflow, collision,
   legibility, brand bug, aspect, CANVAS FILL — type sized to fill SAFE, not
   timid in the top third). Log to <folder>/_qc/REPORT.md. Fix root causes and
   re-render until zero BLOCKER/MAJOR.
7. Outputs per card: beat_sheet.json, claude-cli-<slug>.mp4 (1920x1080),
   SOURCES.md (every number → chapter). Verify the mp4 exists and plays.

BATCH DISCIPLINE
- One card's failure never stops the batch. If a video fails to render after
  two attempts, write FAILED.md in its folder explaining why and continue.
- Append one line per card to
  ../branding-and-ai/youtube/CLAUDE-CLI-BUILD-LOG.md: slug | lane | duration |
  QC verdict | done/failed/skipped | notes.
- When finished, write
  ../branding-and-ai/youtube/CLAUDE-CLI-SERIES-INDEX.md: every built video with
  title, lane, duration, folder, and a suggested playlist order.
- End the run with counts (built / failed / skipped), total runtime, the path
  to the series index, and a short REVIEW LIST of the finished mp4 paths so I
  can open and check them in the morning. Nothing is published.
```
