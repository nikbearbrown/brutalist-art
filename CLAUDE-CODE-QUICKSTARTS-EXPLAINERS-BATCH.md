# Claude Code Prompt — Claude Quickstarts Explainers (batch, claude-liam)

Builds a claude-explainer video (Liam voice) for EVERY candidate in the
claude-quickstarts scout list, one after another, until all are done — each
carried by native animated visualizations and infographics.

Source card list (5 candidates):
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-quickstarts/youtube/video-ideas.md`

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. It is a resumable LOOP:
it works through every card and does not stop until each has a finished mp4 or
a logged failure. Per the ownership rule, videos build INTO the source book's
own folder, not the toolkit's. Free pipeline only — Kokoro voice, no
ElevenLabs, no higgsfield, no publishing, no git commit or push.

```text
Build one claude-explainer video (16:9, claude-liam) for EVERY candidate in
../anthropics/claude-quickstarts/youtube/video-ideas.md, and keep going until
all of them are built. This is a batch LOOP, not a single video. Free pipeline
only: Kokoro voice, no ElevenLabs, no higgsfield, no publishing, no git commit
or push. Run start-to-finish without approval pauses (no paid spend is
possible under these constraints) — the human reviews the finished mp4s at the
end, not between videos.

READ COMPLETELY BEFORE ACTING (once, then apply to every card)

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md
- skills/make/explainer/SKILL.md (and the MOTION.md / REMOTION.md it points to)
- skills/make/your-turn/SKILL.md (closing block contract)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts
- ../anthropics/claude-quickstarts/youtube/video-ideas.md (the card list)
- ../anthropics/claude-quickstarts/README.md and, per card, its Source path
  under ../anthropics/claude-quickstarts/<source> (confirm any figure/number
  the card cites before you animate it)

SHARED RULES (every video in the batch)

- Channel claude-liam: persona Liam (in for Bear), folder chip @NikBearBrown,
  voice Kokoro am_onyx, register Teardown. Do not use ElevenLabs.
- Format 1920x1080 (16:9), 30 fps. Audio-first: narration generated and
  measured per beat FIRST; every beat conforms to its audio. Length follows
  the card's "Length band" — derived from beats, not padded to a clock.
- AUDIENCE = developers building with Claude (computer use, browser
  automation, autonomous coding agents). Teardown register.
- VISUALIZE EVERYTHING YOU CAN. This is the point of the batch: every number,
  coordinate transform, before/after, timeline, filmstrip, JSON diff, or
  mechanism becomes a NATIVE animated Remotion (or Manim) beat — an infographic
  or data-viz built in the Claude palette, never a screenshot of a real app and
  never a static bullet list. If a beat could be a diagram or a chart, make it
  one. Follow the dataviz discipline (read the `dataviz` skill's palette/mark
  rules if present) but recolor to the Claude fidelity palette.
- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. EB Garamond segment titles, Title Case.
  Data/series in ink weights and tints; terracotta reserved for each beat's
  single focal element. Onda code-block for any code line. Claude UI (composer)
  appears only in the bookends (ILLUSTRATE LAW); the middle is
  concept-illustrated, never real app chrome.
- Every number, coordinate, and example shown must come from that card (or its
  cited Source path). The card's example seeds ARE the data — reproduce the
  arithmetic exactly (e.g. 728 × 2560/1456 = 1280). Invent nothing. Cite once
  per figure, small: "Source: Claude Quickstarts (Anthropic)".

DEDUPE NOTE (important): candidates 1 and 5 are BOTH coordinate-scaling
stories. Keep them distinct so they don't feel like the same video twice:
- Candidate 1 = the BROWSER case (resized web screenshot → real viewport,
  forward click scaling). Frame it around the browser viewport.
- Candidate 5 = the macOS COMPUTER-USE case (native Retina display →
  API's 1456×819 → click flowing BACKWARD to the physical screen). Frame it
  around the inverse/round-trip and the target_image_size() transform.
Give each a different central visual metaphor per its "Visual object" so a
viewer who watches both sees two angles, not a repeat.

CARD → VIDEO CONTRACT (apply to each candidate)

- Slug: kebab-case from the card's topic. Suggested:
  1 → browser-coordinate-scaling
  2 → stable-element-refs
  3 → screenshot-prompt-caching
  4 → feature-list-checkpoint-persistence
  5 → macos-computer-use-coordinate-roundtrip
- Beat 0 — ClaudeComposerAsk cold open: Liam speaks the card's HOOK, tightened.
- The turn: pose the card's "The Question" as the mystery the video answers.
- The teach: the card's "Core idea," built as motion using the card's
  "Manim move" as the governing animation verb —
    split = one image/prompt dividing into two coordinate spaces or parts;
    morph = a viewport resizing while a stable ref holds and pixels shift;
    accumulate = turns/tokens/features building up over a timeline.
- The centerpiece figure: build the card's "Visual object" natively and
  animate it, walking the card's "Example seed" arithmetic through it on
  screen. Per card:
    C1: two labeled screenshots side by side ("Claude sees 1456×819" vs
        "Desktop 1920×1080"), a clickpoint on each, and the scaling formula
        animating the point from one space to the other landing dead center.
    C2: one webpage shrinking/growing as the viewport resizes — the pixel
        pair beneath the button changes every frame while the ref= label
        stays glued to the button; Claude always targets the ref and hits.
    C3: a 50-frame filmstrip/timeline of screenshots, most identical; cache
        HITS render fast/terracotta-tagged (~0 tokens), tokenized turns render
        slow/ink; a running token counter lands 10,000 vs 100,000.
    C4: a feature_list.json mutating across session-divider lines — rows
        flipping "incomplete" → "passing", session 1 doing 1–50, session 2
        resuming at 51; git commits as an immutable ledger beneath.
    C5: two labeled screenshots ("Original 2560×1600" vs "Claude sees
        1456×819") with the round-trip: forward resize in, click backward out,
        the formula (728 × 2560/1456, 410 × 1600/819) landing on the button.
- Honesty beat (Teardown move): name the card's "Exclusions" as the edge of
  the claim — what this video deliberately does NOT cover — so scope is honest.
- Closing per your-turn: VERDICT recap card → Your Turn composer beat →
  title re-read on the @NikBearBrown brand card. The Your Turn prompt is a
  real thing a developer can run, specific to that card, read in full by Liam.
  Suggested per card:
    C1: "My model clicks at (700, 410) on a 1456×819 screenshot but my screen
        is 1920×1080 — write the scaling and land the click exactly."
    C2: "Assign stable refs to every clickable element on this page so my
        automation survives a resize."
    C3: "My computer-use agent re-sends an identical screenshot 35 times in a
        50-turn task — add prompt caching and show me the token savings."
    C4: "Externalize my agent's progress to a feature_list.json + git so it
        can resume across sessions — then prove it picks up where it left off."
    C5: "On macOS my screenshot gets resized to 1456×819 before Claude sees
        it — write the inverse transform so the click hits the native display."

THE LOOP (do this until the card list is exhausted)

1. Parse video-ideas.md into an ordered list of candidates (1..N). Write a
   batch ledger at ../anthropics/claude-quickstarts/youtube/BATCH-LOG.md with
   one row per card: slug | status (pending/built/failed) | mp4 path | notes.
2. For each candidate in order, SKIP if its youtube/<slug>/<slug>.mp4 already
   exists and probes as valid (idempotent/resumable). Else build it end to end
   per the CARD → VIDEO CONTRACT into:
   ../anthropics/claude-quickstarts/youtube/<slug>/
     - beat_sheet.json
     - <slug>.mp4 (1920x1080)
     - SOURCES.md — every on-screen claim/number mapped to the card / source.
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

Begin now with candidate 1 and work down. Do not ask for confirmation between
videos — run the whole list, then report.
```
