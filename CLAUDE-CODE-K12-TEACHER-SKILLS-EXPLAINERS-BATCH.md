# Claude Code Prompt — K-12 Teacher Skills Explainers (batch, claude-liam)

Builds a claude-explainer video (Liam voice) for EVERY candidate in the
k12-teacher-skills scout list, one after another, until all are done.

Source card list (4 candidates today, but the prompt loops over whatever the
file contains):
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/k12-teacher-skills/youtube/video-ideas.md`

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. It is a LOOP: it works
through every card, resumable, and does not stop until each one has a finished
mp4 or a logged failure. Per the ownership rule, videos build INTO the source
book's own folder, not the toolkit's. Free pipeline only — Kokoro voice, no
ElevenLabs, no higgsfield, no publishing, no git commit or push.

```text
Build one claude-explainer video (16:9, claude-liam) for EVERY candidate in
../anthropics/k12-teacher-skills/youtube/video-ideas.md, and keep going until
all of them are built. This is a batch LOOP, not a single video. Free pipeline
only: Kokoro voice, no ElevenLabs, no higgsfield, no publishing, no git commit
or push. Run start-to-finish without approval pauses (no paid spend is
possible under these constraints).

READ COMPLETELY BEFORE ACTING (once, then apply to every card)

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md
- skills/make/explainer/SKILL.md (and the MOTION.md / REMOTION.md it points to)
- skills/make/your-turn/SKILL.md (closing block contract)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts
- ../anthropics/k12-teacher-skills/youtube/video-ideas.md (the card list)
- ../anthropics/k12-teacher-skills/README.md (what the skill actually is —
  the k12-lesson-differentiation plugin; the videos teach ITS pedagogy)

SHARED RULES (every video in the batch)

- Channel claude-liam: persona Liam (in for Bear), folder chip @NikBearBrown,
  voice Kokoro am_onyx, register Teardown. Do not use ElevenLabs.
- Format 1920x1080 (16:9), 30 fps. Audio-first: narration generated and
  measured per beat FIRST; every beat conforms to its audio. Length follows
  the card's "Length band" (these are 2–3 min each) — derived from beats,
  not padded to a clock.
- AUDIENCE = K-12 TEACHERS. Even in Liam's Teardown voice, every "why" serves
  a teacher deciding how to differentiate a real lesson. Never teach evading
  standards or lowering rigor — the through-line of this skill is preserving
  grade-level cognitive demand while changing the scaffold. Land that.
- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. EB Garamond segment titles, Title Case.
  Claude UI (composer) appears only in the bookends (ILLUSTRATE LAW); the
  middle is concept-illustrated Remotion/Manim, never the app.
- Every number, example, and case shown must come from that card (and its
  cited reference file under ../anthropics/k12-teacher-skills/plugin/skills/
  if you need to confirm a detail). Invent no data. Cite once, small:
  "Source: Agent Skills for K-12 Teachers (Anthropic)".

CARD → VIDEO CONTRACT (apply to each candidate)

Read the card's fields and turn them into the reel:
- Slug: kebab-case from the card's topic (e.g. candidate 01 →
  "preserve-cognitive-demand-differentiation"). Keep it short and stable.
- Beat 0 — ClaudeComposerAsk cold open: Liam speaks the card's HOOK, tightened.
- The turn: pose the card's "The Question" as the mystery the video answers.
- The teach: the card's "Core idea," built as motion using the card's
  "Manim move" as the governing animation verb —
    scan = a reading eye/laser sweeping one structure across representations;
    accumulate = pieces adding up into the whole;
    split = one thing dividing into scaffolded vs unscaffolded halves;
    slosh = a conserved quantity (e.g. a working-memory bar) redistributing.
- The centerpiece figure: build the card's "Visual object" natively and
  animate it — e.g. candidate 01/02 stack the SAME problem in three
  representations (concrete → visual → symbolic) and show all tiers meeting at
  the same hard case; candidate 03 shows the identical passage scaffolded vs
  clean, side by side; candidate 04 shows a working-memory bar consumed by
  decoding vs freed by fluency. Walk the card's "Example seed" through it.
- Honesty beat (Teardown move): name the card's "Exclusions" as the edge of
  the claim — what this video is NOT saying (e.g. 04: this is not about
  dyslexia or phonics method; the fix is separate fluency work, read-aloud is
  only the bridge).
- Closing per your-turn: VERDICT recap card → Your Turn composer beat →
  title re-read on the @NikBearBrown brand card. The Your Turn prompt is a
  real thing a teacher can paste into Claude — write it specific to that
  card's lesson and have Liam read it in full. Suggested pattern:
  "Here's a [grade] [subject] standard I'm teaching: [___]. Give me the same
  grade-level hard case at three scaffold tiers — below, at, above — without
  lowering the cognitive demand for any tier."

THE LOOP (do this until the card list is exhausted)

1. Parse video-ideas.md into an ordered list of candidates (01..N). Write a
   batch ledger at ../anthropics/k12-teacher-skills/youtube/BATCH-LOG.md with
   one row per card: slug | status (pending/built/failed) | mp4 path | notes.
2. For each candidate in order, SKIP if its youtube/<slug>/<slug>.mp4 already
   exists and probes as valid (idempotent/resumable — safe to re-run). Else
   build it end to end per the CARD → VIDEO CONTRACT into:
   ../anthropics/k12-teacher-skills/youtube/<slug>/
     - beat_sheet.json
     - <slug>.mp4 (1920x1080)
     - SOURCES.md — every on-screen claim mapped to the card / reference file.
3. Verify each mp4 exists and plays (probe duration and frame count) before
   marking it built. Then update BATCH-LOG.md and MOVE ON to the next card.
4. If a beat's animation fails to render after two attempts, replace THAT beat
   with a slate card naming it and log it — never silently drop a beat, and
   never let one bad beat stop the video.
5. If a whole video fails after a genuine attempt, mark it "failed" with the
   reason in BATCH-LOG.md and CONTINUE to the next card — one failure must not
   halt the batch.
6. Stop only when every card is either "built" or "failed." Then print the
   final BATCH-LOG table and, per built video, its beat → timestamp table.

Begin now with candidate 01 and work down. Do not ask for confirmation
between videos — run the whole list.
```
