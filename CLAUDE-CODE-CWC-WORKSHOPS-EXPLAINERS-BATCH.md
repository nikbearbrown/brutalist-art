# Claude Code Prompt — CWC Workshops Explainers (batch, claude-liam)

Builds a claude-explainer video (Liam voice) for EVERY candidate in the
cwc-workshops scout list, one after another, until all are done — each one
carried by native animated visualizations and infographics.

Source card list (5 candidates):
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/cwc-workshops/youtube/video-ideas.md`

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. It is a resumable LOOP:
it works through every card and does not stop until each has a finished mp4 or
a logged failure. Per the ownership rule, videos build INTO the source book's
own folder, not the toolkit's. Free pipeline only — Kokoro voice, no
ElevenLabs, no higgsfield, no publishing, no git commit or push.

```text
Build one claude-explainer video (16:9, claude-liam) for EVERY candidate in
../anthropics/cwc-workshops/youtube/video-ideas.md, and keep going until all
of them are built. This is a batch LOOP, not a single video. Free pipeline
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
- ../anthropics/cwc-workshops/youtube/video-ideas.md (the card list)
- ../anthropics/cwc-workshops/README.md and, per card, its Source folder under
  ../anthropics/cwc-workshops/<source>/ (confirm any figure/number the card
  cites before you animate it)

SHARED RULES (every video in the batch)

- Channel claude-liam: persona Liam (in for Bear), folder chip @NikBearBrown,
  voice Kokoro am_onyx, register Teardown. Do not use ElevenLabs.
- Format 1920x1080 (16:9), 30 fps. Audio-first: narration generated and
  measured per beat FIRST; every beat conforms to its audio. Length follows
  the card's "Length band" — derived from beats, not padded to a clock.
- AUDIENCE = agent builders / practitioners following Claude workflows
  (Claude Managed Agents, Claude Code, the Agent SDK). Teardown register.
- VISUALIZE EVERYTHING YOU CAN. This is the whole point of the batch: every
  number, comparison, before/after, pipeline, ranking, tree, scatter, or
  mechanism in a card becomes a NATIVE animated Remotion (or Manim) beat —
  an infographic or data-viz built in the Claude palette, never a screenshot
  and never a static bullet list. If a beat could be a chart, make it a chart.
  Follow the dataviz discipline (read the `dataviz` skill's palette/mark rules
  if present) but recolor to the Claude fidelity palette.
- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. EB Garamond segment titles, Title Case.
  Data series in ink weights and tints; terracotta reserved for each beat's
  single focal element. Claude UI (composer) appears only in the bookends
  (ILLUSTRATE LAW); the middle is concept-illustrated, never the app chrome.
- Every number, example, and case shown must come from that card (or its
  cited Source folder). Invent no data; the card's example seeds ARE the data.
  Cite once per figure, small: "Source: Claude Code Workshops (Anthropic)".

CARD → VIDEO CONTRACT (apply to each candidate)

- Slug: kebab-case from the card's topic. Suggested:
  1 → agents-that-remember-memory-store
  2 → eval-driven-six-agent-variants
  3 → dispatch-analysts-parallel-orchestration
  4 → agent-decomposition-skills-vs-tools
  5 → rightmodel-pareto-frontier
- Beat 0 — ClaudeComposerAsk cold open: Liam speaks the card's HOOK, tightened.
- The turn: pose the card's "The Question" as the mystery the video answers.
- The teach: the card's "Core idea," built as motion using the card's
  "Manim move" as the governing animation verb —
    accumulate = pieces / entries / scores building up into a whole;
    spread = one call fanning out into parallel sessions, then converging;
    split = one monolith dividing into leaner labeled parts.
- The centerpiece figure: build the card's "Visual object" natively and
  animate it, walking the card's "Example seed" through it end to end. Each
  card names a specific data-viz — build exactly that:
    C1: a three-session timeline (amnesia → recall) with a memory-store file
        tree GROWING as the agent writes entries.
    C2: six agent variants stacked left-to-right (naive → visual → typography
        → palette → density → QA-loop) with per-task score-delta bars beneath
        each — greens for gains, terracotta for regressions.
    C3: a fan-out flow diagram — head agent → dispatch_analysts tool → three
        parallel analyst sessions (each a live progress bar) → converging
        results table the head reads and ranks (e.g. NVDA 9, AMD 6, MU 4).
    C4: a decomposition tree — the 402-line prompt splitting into a 15-line
        core + skill modules + the 12 tools, with cost/latency metrics before
        vs after (102 calls / 488 s → 3 scripts / ~100 s; ~5× faster).
    C5: a 2D pareto scatter — cost (x) vs accuracy (y), Opus/Sonnet/Haiku dots,
        the frontier curve drawn in, and the task-optimal model highlighted
        (Sonnet 90–96% "good enough," saving $0.04/call × 100,000 calls).
- Honesty beat (Teardown move): name the card's "Exclusions" as the edge of
  the claim — what this video is deliberately NOT covering — so the scope is
  honest and the viewer knows where to go next.
- Closing per your-turn: VERDICT recap card → Your Turn composer beat →
  title re-read on the @NikBearBrown brand card. The Your Turn prompt is a
  real thing a builder can run, written specific to that card, read in full by
  Liam. Suggested per card:
    C1: "Attach a memory store to my agent and show me what it writes after
        this session — then prove it recalls it in the next one."
    C2: "Run my agent on the same 10-task eval before and after this prompt
        change, and grade both structurally and semantically — did it improve?"
    C3: "Fan this workload out across parallel sub-agents, then merge their
        results into one ranked decision."
    C4: "Here's my 400-line agent prompt — decompose it into a lean core plus
        skills, and show me the token and latency delta."
    C5: "Sweep my task across Opus, Sonnet, and Haiku, plot cost vs accuracy,
        and tell me which model sits on the pareto frontier for me."

THE LOOP (do this until the card list is exhausted)

1. Parse video-ideas.md into an ordered list of candidates (1..N). Write a
   batch ledger at ../anthropics/cwc-workshops/youtube/BATCH-LOG.md with one
   row per card: slug | status (pending/built/failed) | mp4 path | notes.
2. For each candidate in order, SKIP if its youtube/<slug>/<slug>.mp4 already
   exists and probes as valid (idempotent/resumable). Else build it end to end
   per the CARD → VIDEO CONTRACT into:
   ../anthropics/cwc-workshops/youtube/<slug>/
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
