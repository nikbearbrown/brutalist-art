# Claude Code Prompt — Embedded AI Explainers (full batch, claude-liam)

Rebuilds/creates a claude-explainer video (Liam voice) for EVERY idea in the
embedded-ai book's two scout lists — the 22 concept cards AND the 13 CLI cards
— and keeps going until each has a finished mp4 or a logged failure. Every
video is carried by native animated visualizations and infographics.

Two source card lists:
- `/Users/bear/Documents/CoWork/bear-textbooks/books/embedded-ai/youtube/video-ideas.md`  (22 concept cards)
- `/Users/bear/Documents/CoWork/bear-textbooks/books/embedded-ai/youtube/cli-ideas.md`     (14 cards; #14 is a series umbrella, not a video)

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. It is a resumable LOOP.
Per the ownership rule, videos build INTO the embedded-ai book's own youtube/
folder. Free pipeline only — Kokoro voice, no ElevenLabs, no higgsfield, no
publishing, no git commit or push.

Current state (for context — the prompt re-checks it itself): the CLI cards
already have scaffolded `claude-liam-cli-<slug>/` folders (a
`beat_sheet.claude-liam.json` exists) but their mp4/ folders are EMPTY — none
are rendered. The 22 concept cards have no builds yet.

```text
Build one claude-explainer video (16:9, claude-liam) for EVERY idea in the
embedded-ai book's two scout lists, and keep going until all are built. This
is a large batch LOOP (≈35 videos), not a single video. Free pipeline only:
Kokoro voice, no ElevenLabs, no higgsfield, no publishing, no git commit or
push. Run start-to-finish without approval pauses (no paid spend is possible
under these constraints) — the human reviews the finished mp4s at the end, not
between videos.

READ COMPLETELY BEFORE ACTING (once, then apply to every card)

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md
- skills/make/explainer/SKILL.md (and the MOTION.md / REMOTION.md / EQUATIONS.md it points to)
- skills/make/your-turn/SKILL.md (closing block contract)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts
- ../embedded-ai/youtube/video-ideas.md   (PART A card list — 22 concept cards)
- ../embedded-ai/youtube/cli-ideas.md      (PART B card list — 13 CLI cards + 1 series umbrella)
- For any card, its Source chapter under ../embedded-ai/chapters/*.md — confirm
  every number the card cites before you animate it.

SHARED RULES (every video in the batch)

- Channel claude-liam: persona Liam (in for Bear), folder chip @NikBearBrown,
  voice Kokoro am_onyx, register Teardown. Do not use ElevenLabs.
- Format 1920x1080 (16:9), 30 fps. Audio-first: narration generated and
  measured per beat FIRST; every beat conforms to its audio. Length follows
  the card's band (concept cards are short; CLI cards run longer) — derived
  from beats, not padded to a clock.
- AUDIENCE = embedded / TinyML engineers shipping models to constrained
  hardware (MCUs, coin cells, accelerators). Teardown register.
- VISUALIZE EVERYTHING YOU CAN — this is the point of the batch. Every number,
  budget, curve, waterfall, roofline, pareto front, current-vs-time trace,
  quantization grid, pruning cliff, or mechanism becomes a NATIVE animated
  Manim/Remotion beat — an infographic or data-viz in the Claude palette,
  never a screenshot and never a static bullet list. Each card names a "Visual
  object" and a "Manim move" (scan / trace / accumulate / split / morph /
  spread / slosh) — build exactly that object and let the named move govern
  its animation. Follow the dataviz discipline (read the `dataviz` skill's
  palette/mark rules if present) but recolor to the Claude fidelity palette.
- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. EB Garamond segment titles, Title Case.
  Curves/series/bars in ink weights and tints; terracotta reserved for each
  beat's single focal element (the shortfall, the cliff, the ship state).
  Onda code-block for any code line. Claude UI (composer) appears only in the
  bookends (ILLUSTRATE LAW); the middle is concept-illustrated, never app chrome.
- Every number and example shown must come from that card and its Source
  chapter — reproduce the arithmetic exactly (e.g. 104 days → 11 days; int8
  4 MB→1 MB; ship state 1.725 MB / 240 ms / 90.6%). These are the book's
  illustrative figures, not measured claims — label them as the chapter's
  worked example, never as benchmarked results. Cite once per figure, small:
  "Source: Embedded AI (Bear Brown), Ch. NN".

CARD → VIDEO CONTRACT (apply to each candidate, both lists)

- Beat 0 — ClaudeComposerAsk cold open: Liam speaks the card's HOOK, tightened.
- The turn: pose the card's question/mystery as what the video answers.
- The teach: the card's "Core idea," built as motion using the card's named
  "Manim move" and its "Visual object" as the centerpiece figure — walk the
  card's example numbers through it on screen.
- Honesty beat (Teardown move): name the card's "Exclusions" as the edge of
  the claim — what this video deliberately does NOT cover. For CLI cards, also
  state the card's "Human supplies (Claude can't)" line plainly (e.g. these
  are the chapter's illustrative figures; real numbers need a trained model +
  dataset Claude cannot train).
- Closing per your-turn: VERDICT recap card → Your Turn composer beat →
  title re-read on the @NikBearBrown brand card. The Your Turn prompt is a
  real thing an engineer can run, specific to the card, read in full by Liam.
  For CLI cards, base it on the card's own "Prompt seed" (the claude "..."
  one-liner) so the viewer can literally paste it.

PART A — THE 22 CONCEPT CARDS (video-ideas.md)  → NEW builds
- Slug: claude-liam-<short-concept> (kebab, derived from the title), e.g.
  Candidate 01 → claude-liam-doorbell-power-budget;
  Candidate 04 → claude-liam-nine-weights-convolution. Keep slugs short and
  distinct from the CLI slugs below.
- Build into ../embedded-ai/youtube/<slug>/.
- OVERLAP HANDLING: some cards warn of overlap (01↔02 duty-cycle/battery;
  04↔05 convolution↔depthwise). Build each as its OWN video, kept distinct by
  honoring each card's Exclusions. Only if two drafts come out genuinely
  identical, merge them, ship one, and log the merge — do not publish a
  near-duplicate.

PART B — THE 13 CLI CARDS (cli-ideas.md, Candidates 01–13)  → REDO as claude-explainer
- These were previously scaffolded as claude-liam but never rendered (their
  mp4/ dirs are empty). REDO each as a proper claude-explainer and RENDER it.
- Slug: claude-liam-cli-<slug> (the folders already exist). Map by concept:
  01 compression-journey, 02 int8-mash, 03 pruning-cliff, 04 roofline,
  05 battery-life, 06 brownout, 07 prune-benchmark, 08 latency-predictor,
  09 pareto-selector, 10 deploy-runner, 11 distill, 12 memory-verdict,
  13 realtime-verdict. (Match to the existing claude-liam-cli-* folder names;
  if a mapping is ambiguous, pick the closest existing folder and note it.)
- If a folder already has a usable beat_sheet.claude-liam.json, build from it;
  otherwise author the beat sheet fresh from the card. Recast the "BUILD
  (Claude Code)" lane as a claude-explainer: the technique is TAUGHT with the
  card's Manim visual object as the hero (the four-bar compression waterfall,
  the int8 mash grid, the pruning cliff curve, the roofline, the pareto
  front), and the card's Prompt seed appears as the Your Turn the viewer runs.
- Build into ../embedded-ai/youtube/claude-liam-cli-<slug>/.
- SKIP Candidate 14 (the "Build the TinyML Feasibility Toolkit" series) — it is
  a playlist umbrella over 01–13, not a standalone video. Log it as skipped.

THE LOOP (do this until BOTH lists are exhausted)

1. Parse both card lists into one ordered work list: PART A candidates 01–22,
   then PART B candidates 01–13 (skip B-14). Write a batch ledger at
   ../embedded-ai/youtube/BATCH-LOG.md with one row per video:
   list | card# | slug | status (pending/built/failed/merged/skipped) |
   mp4 path | notes.
2. For each item in order, SKIP if its <slug>/mp4/<slug>.mp4 already exists and
   probes as valid (idempotent/resumable — safe to re-run). Else build it end
   to end per the CARD → VIDEO CONTRACT into its <slug>/ folder:
     - beat_sheet.json (claude-liam)
     - mp4/<slug>.mp4 (1920x1080)
     - SOURCES.md — every on-screen number mapped to card + chapter, flagged
       as the chapter's illustrative figures.
3. Verify each mp4 exists and plays (probe duration and frame count) before
   marking it built. Then update BATCH-LOG.md and MOVE ON.
4. If a beat's animation fails to render after two attempts, replace THAT beat
   with a slate card naming it and log it — never silently drop a beat, never
   let one bad beat stop the video.
5. If a whole video fails after a genuine attempt, mark it "failed" with the
   reason in BATCH-LOG.md and CONTINUE — one failure must not halt the batch.
6. Stop only when every item is built / failed / merged / skipped. Then print
   the final BATCH-LOG table and, per built video, its beat → timestamp table.

Begin now with PART A candidate 01 and work all the way through PART B. Do not
ask for confirmation between videos — run the whole list, then report.
```
