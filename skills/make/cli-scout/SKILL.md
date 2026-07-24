---
name: cli-scout
description: >
  Mine a book for "X with Claude" candidates — concepts that become a CLI video
  (Claude composer in — the Claude Remotion template, not a bash terminal —
  vox output). Subject-adaptive: technical/quantitative books
  get the BUILD lane ("build/measure/simulate X with Claude Code", output = a
  plot/table/sim/number); biology, history, and humanities books get the RESEARCH
  lane ("research/investigate X with Claude", output = a synthesized doc / timeline
  / comparison / figure). Writes reviewable cards to [book]/youtube/cli-ideas.md —
  each detailed enough that the `cli` builder can turn an approved one into a reel.
  Use when the user types `cli-scout [book]`, asks for "X with Claude" topics, CLI-
  video ideas, or "what could we build/research with Claude from this book". Produces
  cards, never videos. The human picks; `cli` builds.
---

# cli-scout — find the "X with Claude" topics

You find the concepts in a book that make excellent **CLI videos** and write them
as candidate cards. A CLI video shows prompts typed into the Claude composer,
the actual generated code, and the **output** as a vox-explainer beat. Your job is to spot the
concepts where *doing the thing with Claude* — building it, measuring it,
researching it — is a better teacher than explaining it, and to name the artifact
the run produces. You stop at the card. You do not write beat sheets or narrate.

## The prime rule: this is VIDEO, never a still
Every candidate becomes an explainer **video**. The output beat is always a
**moving** visualization — a Manim scene, a Remotion scene, a d3 animation, or a
screen-recording — or a **slate** the human fills with media. A static png is
never the output of a CLI video. If a card's payoff feels like "a plot", describe
it as the *animation* of that plot (the curve drawing, the point sweeping, the
bars growing) and pick Manim/Remotion/d3.

## Every card is built in the required spine
The `cli` builder wraps each approved card in the fixed CLI-video spine: INTRO →
**PROBLEM** (what/why/context/stakes) → the CLI loop **with ≥1 revision**
(ASK → CODE → OUTPUT → CHANGE → OUTPUT) → **SUMMARY** → **NEXT STEPS** → OUTRO. Write
cards so they feed that spine: the card's **Hook** becomes the PROBLEM beat's
why-care; the **change** field is the required revision; the **Teardown angle** is
the SUMMARY's point; and name a concrete NEXT STEP the viewer can act on (often
"run it on your own data" or a pointer to a sibling card).

## The one classification: BUILD vs RESEARCH lane
Read the concept and ask: **can it be reduced to a script whose output is a
deterministic computed artifact?**
- **BUILD lane** (engineering, CS, math, physics, data, embedded, anything
  quantitative): yes. → "Build/measure/simulate X with Claude Code." The output
  is a plot, a table, a benchmark number, a simulation, a working module. This is
  the default for technical books.
- **RESEARCH lane** (biology, history, humanities, law, policy, medicine-as-
  evidence, social science): the payoff is a *synthesis/judgment over sources or
  evidence*, not a computed number. → "Research/investigate X with Claude." Claude
  is the research assistant: gather → cross-check → synthesize → lay out. The
  composer shows the research prompts; the output is the synthesized artifact (a
  sourced brief, a timeline, a comparison table, an annotated map, a figure).
A book can mix lanes chapter to chapter; classify each candidate on its own.

## Two rich sources (check both)
1. **The book's own "build with Claude" exercises.** Many textbooks now carry
   per-chapter LLM/Claude-Code exercises or projects (e.g. a running toolkit built
   across chapters). Each is a near-ready BUILD candidate — harvest the project
   name, what it builds this chapter, and the payoff, and turn it into a card.
2. **Buildable/researchable prose concepts.** A concept qualifies when *running
   it* beats *stating it*: a rounding-error you can watch, a curve with a cliff you
   can plot, a trade-off you can measure, a claim you can cross-check against
   sources. Skip concepts whose whole value is a static definition.

## The card schema (every card, verbatim)
```
## Candidate NN — [Title: "Build/Measure/Research X with Claude"]
- Source: [book]/chapters/[file].md   (+ "LLM Exercise" if harvested from one)
- Lane: BUILD (Claude Code)  |  RESEARCH (Claude assistant)
- Hook: the one-line reason to watch — a gap, a surprise, a thing that shouldn't work but does.
- The artifact: what the run PRODUCES (the payoff). Be concrete: "a σ(t) curve with the doubling time marked", "an int8-vs-fp32 error histogram", "a sourced 6-event timeline".
- Prompt seed: the actual `claude "…"` ASK — the prompt typed into the composer.
- Read / check: what to verify in the generated code AND in the output (the CODE + OUTPUT beats' payoff).
- Human supplies (Claude can't): the real asset(s) the human must produce because Claude/CLI cannot — a trained model file, a labeled dataset, a hardware capture (measured latency, current draw, scope trace), a real benchmark run, a screen-recording of the actual run. State clearly when a **synthetic/illustrative stand-in** (the book's figures, generated arrays, an analytic curve) is acceptable for the video, vs when **only real data is authentic**. Write "Nothing — fully synthetic" when Claude can do it end to end. THIS FIELD IS MANDATORY: the human must know the real work before approving.
- Output medium: **Manim | Remotion | d3 (animated) | screen-recording mp4 | slate** — the output beat of an explainer VIDEO is always motion or a slate the human fills. **Never a static png.** If a single frame seems to be the artifact, animate its reveal/transform or make it a slate.
- The change: the iterate (the CHANGE beat) — one diff that deepens or stresses it.
- Teardown angle: the design judgment / trade-off the output exposes (this is the voice).
- Exclusions: the rabbit holes to cut — derivations, second datasets, tangential history.
- Score: N/10  (BUILD bar: the artifact must be runnable in <~40 lines and its output must be the lesson; RESEARCH bar: the question must be answerable from citable sources and the synthesis must be checkable).
```

## Commands
### `cli-scout [book-folder]` — mine one book
1. Read the chapter list. Harvest any per-chapter Claude/LLM exercises first (source 1).
2. Read chapters; detect BUILD/RESEARCH candidates (source 2); classify each lane.
3. Write (or append to) `[book-folder]/youtube/cli-ideas.md`: header
   `# [Book Title] — CLI Video Ideas ("X with Claude")`, one card per candidate,
   numbered, ordered by Score. NEVER renumber/rewrite existing cards; continue numbering.
4. Report: candidates found, how many BUILD vs RESEARCH, how many ≥8, the file path.

### `cli-scout [chapter file(s)]` — restrict to specific chapters. Append.
### `rank [book-folder]` — re-score `cli-ideas.md`; mark split/merge/drop; never delete.

## Output rules
- Cards are self-contained: a reader who never opened the chapter understands the
  artifact, the prompt, and the output shape from the card alone.
- Every BUILD card names a prompt seed AND the output medium — that is the contract
  the `cli` builder reads to place the ASK beat and the OUTPUT slot.
- If you can't name the artifact the run produces, it is not a CLI-video card yet —
  it may be a plain vox-explainer (send it to `scout`) instead.
- Never write narration or beats here. Stop at the card.
