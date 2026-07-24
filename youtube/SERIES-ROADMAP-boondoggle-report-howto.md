# SERIES ROADMAP — "Name the Handoff: The Boondoggle Report"

A how-to ai-explainer series for **INFO 7375 (Computational Skepticism for AI) — Week 1: The
Boondoggle Report** (a Gru-generated SDD + a 600–900 word reflection, 25 pts, due before Week 2).
Audience: **graduate students, week one, who have never used Gru, written an SDD, or read a
human/AI task split.** Register: **pragmatic how-to with a skeptical edge** (Liam voice,
`claude-liam`, Kokoro am_onyx). Deliberately **short** — four episodes — to match a 25-point
first-week assignment. The series walks a student from "I have an app idea" to "a Boondoggle Score
I can read and say something true about."

> Voice: `claude-liam` per request. Build into `computational-skepticism-for-ai/youtube/` (the
> course), or `brutalist-art/youtube/` — tell me the owning book slug.

## The one idea this whole assignment teaches

**You must specify precisely before you can evaluate precisely.** The Boondoggle Score forces the
question the course is built around — *which cognitive work belongs to the human, and why?* — and
makes it explicit *before* the technical machinery arrives. The intellectual core is the
**solve-verify asymmetry**: producing AI output is cheap; verifying it is expensive. Every episode
points at that.

## Meta-resonance (one line in E1)

The Boondoggle Score is a delegation map with the accountability made explicit — the same
human/AI split, hard-handoff, and "verify before you trust it" discipline as an accountable
pipeline's phase gates. This assignment is that idea in its purest, earliest form.

## Honesty / course threads (DOUBLE-CHECK LAW)

- **Don't clean up Gru's output.** Errors, flags, and pushback are *evidence the tool worked* —
  submit them unedited. The only thing you add is the required personal paragraph after /v1.
- **Show iteration.** An SDD that accepted Gru's first output with no engagement of the phase gates
  earns **zero**. Second attempts, corrected formulations, resolved pushback are the point.
- **"If /v0 stops you cold, that's the assignment working."** Work through the pushback, don't
  override it.
- **Describing is not analyzing.** The reflection must say what the score *means*, not what it
  *contains* — full credit reads as useful to an engineer who never did the assignment.
- **This is not a prompt-engineering exercise** and not about a good-looking SDD. It's whether you
  can distinguish the work a capable AI does from the work that needs a human standing outside it.

## Series doctrine (every episode)

- **Assume the coding skill, not the specifying/validating skill.** Define every term first time
  (Gru, SDD, phase gate, Boondoggle Score, supervisory capacity, handoff condition, solve-verify
  asymmetry, mechanical execution vs. judgment-about-specification). Never "just."
- **One deliverable per episode**, ending in the real artifact (an SDD section, the score, a
  reflection prompt), with the exact Gru command to run — then the "engage the pushback" pass.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your Turn
  → title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "Meet Gru & Scope Your App: The /v0 Gate" (~5 min)
- **slug:** `claude-liam-bd-01-meet-gru-and-v0`
- **premise:** Before you can evaluate an AI system, you have to specify one precisely. Gru is the
  fastest way to build that muscle — and its first gate will stop a vague idea cold. Good.
- **teach:** what Gru is (a software-design-documentation system built on the Irreducibly Human
  curriculum); set it up (a Claude Project with the Gru system prompt, or paste it + `/help` to
  confirm); **scope a small, real app** in a domain you actually know (the good candidates: finance
  flagger, annotation tool, clinic scheduler, moderation dashboard, test generator, calibration
  tracker); the anti-patterns ("an AI assistant for X" is too broad; 2–3 components is too simple;
  thin domain knowledge will be exposed); run **`/v0`** — the problem-formulation gate — and **work
  through the pushback** if it stops you (that's the assignment working). `/v0` names the *thing
  being built* (not the problem it solves), the insertion point, and the output.
- **traps:** too-broad or too-simple app; a domain you can't defend; overriding `/v0`'s pushback.
- **deliverable:** a scoped app + a passed `/v0`. Your Turn = "run `/v0` on your app; if it pushes
  back, don't argue — rewrite until the one-sentence naming is specific."

### E2 — "Build the SDD: /v1 → /s1 (and write the one paragraph that's yours)" (~6 min)
- **slug:** `claude-liam-bd-02-build-the-sdd`
- **premise:** Run the sequence and let Gru push. The SDD is only worth grading if it shows the
  pushback you resolved.
- **teach:** run in order — **`/v1`** (problem summary that could distinguish *this* system from a
  generic one; comparable systems; success condition), **`/v2`** (3–4 non-negotiable principles
  *with the collision test completed*), **`/v3`** (core flows concrete at every step — never "the
  system processes the request"), **`/v4`** (5–8 *testable* need statements, each with a pass/fail
  condition), **`/s1`** (each component with inputs, outputs, edge cases, scope boundary — every
  component mapped to a Need). Then the **required personal addition after /v1**: 3–5 sentences in
  your own voice on what Gru's pushback changed about how you understood the problem (or, if it
  accepted your first formulation, whether it was genuinely tight or you got lucky). **Do not edit
  Gru's output** — the flags are evidence.
- **traps:** cosmetic cleanup of Gru's output; vague flows; needs with no pass/fail; a component
  with no Need; skipping the personal paragraph.
- **deliverable:** the SDD `/v0`→`/s1` + the personal paragraph. Your Turn = "run `/v1` through
  `/s1`; paste the full output including every flag, then write your 3–5 sentence addition."

### E3 — "Generate & Read the Boondoggle Score (/claude) + the Solve-Verify Asymmetry" (~6 min)
- **slug:** `claude-liam-bd-03-boondoggle-score`
- **premise:** `/claude` produces the score — the sequenced human/AI task split. This is the answer
  to "which work is the human's" made explicit. Learn to read it before you analyze it.
- **teach:** run **`/claude`**; what a complete score contains — **labeled supervisory capacities on
  every human step**, **copy-pasteable prompts on every Claude step**, **testable handoff conditions
  on every Claude step**, and a **score summary with the distribution table** and the **2–3
  highest-risk handoffs**. Then the concept the whole course turns on: the **solve-verify asymmetry**
  — producing AI output is cheap, verifying it is expensive; that asymmetry is *why* the human steps
  land where they do. Point at the score's most expensive verification step as a preview of Prompt D.
- **traps:** a score missing capacities/prompts/handoff conditions; treating it as a to-do list
  instead of a claim about human judgment.
- **deliverable:** the full Boondoggle Score. Your Turn = "run `/claude`; find the one Claude step
  whose *following* human step needs the most domain knowledge — that's your solve-verify anchor."

### E4 — "Read the Answer: The Boondoggle Reflection (4 prompts) + Ship" (~7 min)
- **slug:** `claude-liam-bd-04-reflection-and-ship`
- **premise:** The score is the answer; the reflection is whether you can read it and say something
  true. Analyze, don't describe.
- **teach:** the four prompts (150–200 words each, ~600–900 total, **cite your own score**):
  **A — The Split** (the SUPERVISORY CAPACITY DISTRIBUTION: which capacity appears most/least, what
  that says about your app's domain; address any zero-count flag specifically — gap or genuine
  property?); **B — The Hardest Handoff** (pick one of Gru's highest-risk handoffs; a *concrete*
  failure — what an engineer would wrongly accept from Claude and the downstream consequence —
  connected to one of the **four skeptical moves** from Chapter 1); **C — Where Gru Was Right / Where
  You Disagreed** (one task you'd reassign human↔Claude, argued with the **mechanical-execution vs.
  judgment-about-specification** frame — not intuition); **D — Solve-Verify Applied** (the single
  step where verification is most expensive relative to production; what a team that skipped it would
  ship, and how long until they found out). Then assemble the **one PDF/Markdown** — full SDD
  (unedited + your paragraph) + the four labeled prompts, app name at the top — and submit.
- **traps:** describing what the score contains instead of analyzing what it means; "the engineer
  might miss something" (not concrete); Prompt C argued from intuition; Prompt D as a general
  observation.
- **deliverable:** the reflection + submitted document. Your Turn = "for Prompt D, name the one step
  and estimate the discovery timeline with reasoning — if you can't name a specific step, you're
  describing, not analyzing."

---

## Tight cut

Three-episode version: Gru + `/v0` + SDD in one (E1+E2) · Boondoggle Score + solve-verify (E3) ·
Reflection + ship (E4). The 4-episode cut is better because the SDD sequence and the score each
need their own beat for a first-week student meeting Gru for the first time.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `computational-skepticism-for-ai/
  youtube/` (or `brutalist-art/youtube/` — tell me the owning book slug).
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals → QC →
  BUILD-PROMPT.md. **Re-verify Gru's current command set and behavior** (nikbearbrown.com/tools/
  gru-tool + the course system prompt) at build time — I grounded on the assignment's documented
  commands; the tool may have moved.
- This is the **Week-1** on-ramp; it pairs with the bigger "Reallocation Engine, Audited" assignment
  roadmap (the solve-verify asymmetry introduced here is the graded spine there). Say the word and I
  can map the rest of the Computational Skepticism assignments (the weekly validation exercises,
  the research project milestones) into one course series index alongside the INFO 7375 branding set.
