---
name: sim-scout
description: >
  Mine a book for simulation candidates — concepts where a rule, run, teaches
  better than the same rule stated. Two lanes: MANIM (a directed animation of a
  known equation you watch — curve draws, packet spreads, orbit sweeps) and
  D3/DATAVIZ (an emergent or interactive data process you run and poke — a
  distribution fills from sampling, a network relaxes, a Monte-Carlo converges,
  a slider re-solves). Writes reviewable cards to [book]/youtube/simulation-ideas.md
  — each detailed enough that the `simulation` builder (Manim reels) or the
  `graphs`/d3 builder can turn an approved one into a sim. Use when the user types
  `sim-scout [book]`, asks for simulation ideas, "what could we simulate / animate /
  make interactive from this book", or Manim vs d3 sim candidates. Produces cards,
  never sims. The human picks; the builder builds.
---

# sim-scout — find the concepts worth simulating

You find the concepts in a book that make excellent **simulations** and write them
as candidate cards the human can skim, score, and approve. You do not build sims,
write beat sheets, or narrate. You stop at the card.

A simulation earns its place when **running the rule teaches what stating the rule
cannot**: a threshold you can cross, a curve with a cliff, a distribution that only
makes sense once you watch it fill, a trade-off that appears when a parameter moves.
Your value is selectivity, not coverage — most prose is not a sim.

## The prime rule: motion or interaction, never a static plot
Every candidate becomes a **moving or interactive** artifact — a Manim scene that
animates, or a d3 view the viewer drives. A static png/plot is never the output. If
a card's payoff feels like "a chart", describe the *animation* of that chart (the
curve drawing, the point sweeping, the bars growing) or the *interaction* (drag the
parameter, watch it re-solve). If it can't move or be poked, it is a figure — route
it to the `figures`/`graphs` skills, not here.

## The one classification: MANIM lane vs D3/DATAVIZ lane
Read the concept and ask: **is the payoff a directed animation of a known rule
(you WATCH it), or an emergent/interactive data process (you RUN and POKE it)?**

- **MANIM lane** — a clean, directed, cinematic animation of a rule the math
  already fixes. One curve, one trajectory, one spectrum, one geometric transform,
  playing out deterministically. Best for physics laws, wavefunctions, continuous
  fields, orbital motion, geometry morphs — anything where a *scripted* animation is
  the clearest teacher. Output: a Manim scene (mp4), feeds the **`simulation`**
  builder (`vox/aspects/simulation`) as a Medhavy "Claude Code + Manim" reel.
- **D3/DATAVIZ lane** — an *emergent*, *stochastic*, *many-body*, or *interactive*
  process where the value is watching data update as a rule iterates, or letting the
  viewer move a control and see the system respond. Best for Monte-Carlo convergence,
  sampling distributions building up, agent-based / force-directed dynamics, live
  parameter sweeps, anything with a "drag this and watch." Output: a single-file
  **d3 v7** animated/interactive HTML in the Bear Brown / Brutalist house style —
  see the **`graphs`** skill — that stands alone or is screen-recorded into a reel.

Decide per candidate, not per chapter or per book. A concept that honestly wants
both a scripted animation AND an interactive explore is TWO cards, each naming its
own artifact. When genuinely torn, pick the lane whose artifact you can *see*
immediately; if you can't see either, it isn't a card yet.

## What makes a keeper — the sim bar
A candidate must pass ALL THREE (from the simulation doctrine):
1. **Simulatable** — a stated rule (equation, algorithm, generative process) that
   produces a *visible* curve, trajectory, spectrum, geometry, or distribution.
   "Something happens" when you change a parameter.
2. **Verifiable** — the output has **at least TWO concrete, testable predictions**:
   boundary cases, known limits, exact ratios, or published values you can check the
   sim against. This is the gate. No two predictions → not a card yet.
3. **Surprising** — the intuitive/classical answer fails, or the result is
   counterintuitive, or a parameter does something you wouldn't guess. The drama is
   what motivates watching the rule run.

If you cannot name the rule, the visible artifact, AND two predictions, it is not a
simulation card — it may be a plain explainer (send it to `scout`) or a static
figure (send it to `figures`/`graphs`).

## Two rich sources (check both)
1. **The book's own "build/simulate it with Claude" exercises.** Many chapters carry
   per-chapter LLM/Claude-Code projects — a running toolkit, a capstone sandbox, a
   "plot this yourself" prompt. Each is a near-ready candidate: harvest the artifact
   it builds and its payoff, and turn it into a card.
2. **Simulatable prose concepts.** A concept qualifies when *running it* beats
   *stating it*: a rounding error you can watch accumulate, a curve with a cliff you
   can plot, a threshold you can cross, a distribution that only makes sense once it
   fills, a trade-off you can measure by sweeping a knob.

## The card schema (every card, verbatim)
```
## Candidate NN — [Title: "Simulate/Animate/Explore X"]
- Source: `[book]/chapters/[file].md`   (+ "LLM Exercise" if harvested from one)
- Topic: [the on-screen kicker string — the topic, never the book title, never a chapter number]
- Lane: MANIM (directed animation)  |  D3/DATAVIZ (emergent / interactive)
- Hook: [one sentence — the tension/surprise; the reason to watch the rule run]
- The rule: [the equation, algorithm, or generative process the sim encodes — the thing that gets coded]
- Concrete numbers: [the parameter values that make it real — masses, wavelengths, N, rates, grid size, seeds]
- The artifact / what moves: [the visible payoff, described AS MOTION or INTERACTION — "a σ(t) curve drawing and visibly broadening over several τ", "a histogram filling from 10k samples until it snaps to the normal", "drag L and watch E₁ shift as 1/L²". Never a static frame.]
- Output medium: [Manim (mp4)  |  d3 v7 animated/interactive HTML]  — must match the lane
- Two testable predictions: [P1: … ; P2: …]  — exact, checkable (boundary case, known limit, ratio, published value). MANDATORY: this is the verification gate.
- The change: [the one parameter tweak / follow-up that deepens or stresses it — the revision the builder's iterate beat needs]
- Human supplies (Claude can't): [the real asset the human must produce — measured data, a hardware capture, a real benchmark — OR "Nothing — fully synthetic/analytic" when the sim is self-contained. State when a synthetic/analytic stand-in is fine vs when only real data is authentic. MANDATORY.]
- Teardown angle: [the judgment / trade-off the running sim exposes — this is the voice]
- Exclusions: [specific rabbit holes to cut — derivations, second parameter studies, tangential history, formalism]
- Sim slug: [kebab, the builder's folder name, e.g. vol1-packet-spread]
- Score: [N]/10
```

The builder appends `- Status: BUILT — [path]` and `- Watch: \`open /abs/path/[slug]-review.mp4\``
at Done — the sim-scout never writes those.

## Score rubric (/10) — add points, cap at 10
- **Surprise / "aha" (0–3)** — the classical/intuitive answer fails, or the sim
  reveals something you wouldn't guess: 3.
- **Visible motion/interaction (0–3)** — the rule maps to one thing that clearly
  moves or responds to a control; if you can see the animation/interaction
  immediately, 3.
- **Verifiability (0–2)** — two clean, exact predictions to check against: 2.
- **Pedagogical payoff (0–2)** — fixes a misconception or unlocks later material.
8–10 = build soon. 6–7 = build after tightening. ≤5 = shelve.

## Commands

### `sim-scout [book-folder]` — mine one book
1. Ensure `[book-folder]/youtube/_chapters.json` exists; if not, run scout's shared
   scanner (it lays the worktable, it does not invent ideas):
   `python3 scout/scripts/scan_book.py [book-folder]` (from `make/`), or
   `python3 aspects/scout/scripts/scan_book.py ../[book]` (from the vox folder).
2. Harvest any per-chapter "build/simulate with Claude" exercises first (source 1).
3. Read each chapter (or the ones named). Keep concepts that pass the sim bar
   (simulatable + verifiable + surprising); classify each into the MANIM or
   D3/DATAVIZ lane by the WATCH-vs-POKE question.
4. Write (or append to) `[book-folder]/youtube/simulation-ideas.md`: header
   `# [Book Title] — Simulation Ideas`, one card per surviving concept, numbered
   `Candidate NN`, ordered by Score (highest first). NEVER renumber or rewrite
   existing cards; read the file first and continue the numbering after the highest
   existing Candidate NN.
5. Report: candidates found, MANIM vs D3/DATAVIZ split, how many ≥8, the file path.
   The human picks and hands a card to `simulation` (Manim) or the d3/`graphs`
   builder.

### `sim-scout [chapter file(s)]` — mine specific chapters only
Same flow, restricted to the named chapters; append new cards to the existing file.

### `rank [book-folder]` — re-score an existing list
Re-apply the rubric fresh; adjust scores/order; flag cards to split (e.g. a card
that wants both lanes), merge, or drop; one line of reasoning per change. Never
delete a card — mark it.

## Output rules
- **Append, never replace.** If `simulation-ideas.md` already exists, read it,
  keep every existing card untouched, and continue numbering. Only create the file
  fresh if it does not exist.
- Cards are self-contained: a reader who never opened the chapter understands the
  rule, the artifact, and the two predictions from the card alone.
- Every card names **the rule**, **the artifact as motion/interaction**, **the
  output medium matching its lane**, and **two testable predictions** — that quartet
  is the contract the builder reads to place the sim.
- If you can't name two testable predictions, it is not a sim card yet — it may be a
  plain explainer (`scout`) or a static figure (`figures`/`graphs`).
- Exclusions are mandatory and specific — name the tempting rabbit holes
  (derivations, a second parameter study, history), not "keep it simple."
- Never write narration, beats, or scenes here. Stop at the card.
