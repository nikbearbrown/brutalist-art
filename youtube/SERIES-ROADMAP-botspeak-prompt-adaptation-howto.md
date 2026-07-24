# SERIES ROADMAP — "Make It Yours, Then Break It: The Botspeak Prompt Adaptation"

A how-to ai-explainer series for **INFO 7375 (Computational Skepticism for AI) — Botspeak Prompt
Adaptation** (a six-part submission, 100 pts = 80 rubric + 20 relative quartile). Audience:
**graduate students who have read some Botspeak and have never written a five-component
specification or run an adversarial move against their own prompt.** Register: **pragmatic how-to
with a skeptical edge** (Liam voice, `claude-liam`, Kokoro am_onyx). Five episodes. The series
walks a student from "I picked a Botspeak exercise prompt" to "a domain-specific prompt I specified
before I built, ran for real, attacked, and know the failure shapes of."

> Voice: `claude-liam` per request. Build into `computational-skepticism-for-ai/youtube/` (Botspeak
> is a course text), or `brutalist-art/youtube/` — tell me the owning book slug.

## The idea this assignment teaches

**Fluency with a tool is not understanding of the system it runs on.** Adapting a generic prompt
into *your* domain, specifying it before you build it, and then attacking it is how you find the
irreducibly human part — the judgment about whether the specification is even correct. The quartile
score rewards one thing above all: **evidence you actually ran the work, not described running it.**

## Meta-resonance (one line in E1)

Spec-first, then adversarially verify your own output, then name what a fluent practitioner would
catch that the model can't — that's the same discipline an accountable pipeline uses (define the
spec, attack the result, human owns the truth). This assignment is that loop applied to a single prompt.

## The six deliverables → the rubric

1. Adapted prompt (Domain Adaptation, **21 pts**)
2. Justification in Botspeak (**11 pts**)
3. Worked example — output + commentary (**11 pts**)
4. Five-component specification, written BEFORE the prompt (Specification Rigor, **16 pts**)
5. Adversarial self-critique + revision (**11 pts**)
6. Failure-mode analysis (**10 pts**)
+ Relative quartile (**20 pts**)

## Honesty / craft threads (DOUBLE-CHECK LAW)

- **"Specific enough" is the test.** Would someone in that role immediately recognize themselves, or
  could it describe the entire adjacent profession? "Clinical pharmacist reviewing discharge meds on
  a night shift," not "healthcare professional." Bracketed placeholders left in = the prompt loses
  diagnostic power.
- **Spec BEFORE building, not retrofitted.** The five components are written first; a spec reverse-
  engineered from a finished prompt reads as one.
- **Exclusions honest about YOUR role's failure modes** — not generic. Success criteria testable.
- **Justification explains the causal connection**, not just name-drops Botspeak vocabulary — "why
  *this* role's delegation decisions look this way," not "this relates to Delegation."
- **Run it, don't describe running it.** Show the actual output; commentary is analytical (what
  worked, what failed, what you changed after seeing it, what a fluent practitioner would catch).
- **The adversarial move must be RUN and produce a substantive revision** — a named move (steelman /
  edge-case probe / assumption surface / devil's advocate) that actually changed the prompt.
- **Failure modes are domain-shaped** — "the shape of the hallucination hardest for someone in this
  role to catch," not "the model might hallucinate."

## Series doctrine (every episode)

- **Assume Botspeak familiarity, not specification/adversarial skill.** Define every term first time
  (bracketed field, five-component spec, the Loop, Nine Capacities, adversarial move, steelman,
  discernment, failure mode). Never "just."
- **One deliverable per episode**, ending in the real artifact, with a paste-ready prompt to draft
  the first pass — then the "make it specific / attack it" pass.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your Turn
  → title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "Pick a Botspeak Prompt & Nail 'Specific Enough' (Domain Adaptation, part of 21 pts)" (~5 min)
- **slug:** `claude-liam-bs-01-pick-and-scope`
- **premise:** The whole grade turns on how precisely you name your role. "Healthcare professional"
  describes a thousand jobs; "clinical pharmacist on a night shift" describes one.
- **teach:** select one LLM Exercise prompt from Botspeak (Ch 0–13) that fits your work; the
  **"specific enough" test** (the too-generic vs. specific-enough table — bounded, recognizable role;
  the test: would someone in that role see themselves, or could it describe the adjacent profession?);
  identify the bracketed fields you'll replace and the role-specific content you'll need (task types,
  stakeholders, failure modes, tools — named precisely). This is the setup for the 21-point component.
- **traps:** a role that's really a whole profession; picking a prompt that doesn't fit your domain.
- **deliverable:** the chosen prompt + a bounded role statement. Your Turn = a prompt that pressure-
  tests a role against the "adjacent profession" test and tightens it until it's recognizable.

### E2 — "Spec Before You Build: The Five Components (Specification Rigor, 16 pts)" (~6 min)
- **slug:** `claude-liam-bs-02-five-component-spec`
- **premise:** You specify before you build — because knowing what a correct prompt looks like before
  you write it is the skill. Retrofit a spec and it shows.
- **teach:** write the five-component specification, domain-specific: **Intent** (what this prompt is
  for), **Constraints** (what it must respect), **Success Criteria** (testable — a pass/fail you could
  check), **Exclusions** (honest about *your role's* typical failure modes — not generic), **Output
  Format** (the shape you need back). All five present, none collapsed together.
- **traps:** only stating intent; generic exclusions; success criteria you can't test; writing the
  spec after the prompt.
- **deliverable:** the five-component spec. Your Turn = a prompt that drafts the five components for
  the student's role, then the "make the exclusions honest to *this* role" pass.

### E3 — "Adapt It + Justify It in Botspeak (Domain Adaptation 21 + Justification 11)" (~6 min)
- **slug:** `claude-liam-bs-03-adapt-and-justify`
- **premise:** Now translate — every bracketed field becomes role-specific, filtered through your
  spec — and explain *why* your choices map to Botspeak, causally, not by name-drop.
- **teach:** replace **every** bracketed field with non-generic, role-specific content (task types,
  stakeholders, failure modes, tools named precisely); use the spec from E2 as the filter. Then the
  **justification**: cite **Loop steps, the Nine Capacities, or the Specification components by name**
  and explain the **causal connection** — *why this role's delegation/discernment/verification looks
  the way it does*, not "this relates to Delegation."
- **traps:** placeholders left in; fields generic enough to swap into an adjacent role; a justification
  that asserts Botspeak links instead of explaining them.
- **deliverable:** the adapted prompt + the justification. Your Turn = a prompt that drafts the field
  translations, then the "explain the causal Botspeak link for each key choice" pass.

### E4 — "Run It & Attack It: Worked Example + Adversarial Self-Critique (11 + 11)" (~6 min)
- **slug:** `claude-liam-bs-04-run-and-attack`
- **premise:** Two moves that separate real work from described work — actually run the prompt, then
  turn an adversarial move on your own prompt and change it.
- **teach:** the **worked example** — run the adapted prompt, include the output (full or meaningfully
  excerpted), and write **analytical** commentary (what worked, what failed, what you changed after
  seeing it, what a fluent practitioner in your domain would catch that you did or didn't). Then the
  **adversarial self-critique** — pick a move (steelman / edge-case probe / assumption surface /
  devil's advocate), **run it against your own prompt**, and make a **substantive revision** the
  critique clearly drove.
- **traps:** describing the run without the output; commentary that's descriptive not analytical; an
  adversarial move named but not run; a cosmetic revision.
- **deliverable:** the output + commentary + the adversarial move + the revision. Your Turn = a prompt
  that runs a chosen adversarial move against the student's prompt and proposes a defensible revision.

### E5 — "Name What Breaks + Ship: Failure Modes (10 pts) + assemble the six parts" (~5 min)
- **slug:** `claude-liam-bs-05-failure-modes-and-ship`
- **premise:** The last skeptical move — name the failures *shaped like your domain*, the ones
  hardest for someone in your role to catch. Then submit all six parts.
- **teach:** identify **2–3 domain-specific failure modes** — the *shape* of the hallucination or
  error that would be hardest for someone in this role to catch (not "the model might hallucinate")
  — and connect them to **Discernment (Ch 6)** or the **Nine Capacities (Ch 2)**. Then assemble the
  single document with all six labeled parts (adapted prompt · justification · worked example · the
  spec · adversarial critique · failure modes) and submit. Remember the quartile rewards evidence you
  *ran* the work.
- **traps:** generic failure modes; one failure mode with no analysis; a missing deliverable.
- **deliverable:** the failure-mode analysis + the assembled submission. Your Turn = a prompt that
  surfaces the domain-shaped failure modes for the student's prompt and ties each to a Botspeak capacity.

---

## Tight cut

Four-episode version: Pick+scope+spec (E1+E2) · Adapt+justify (E3) · Run+attack (E4) · Failure modes
+ ship (E5). The 5-episode cut is better because Specification Rigor (16 pts) and the adaptation
(21 pts) are the two heaviest components and each deserves its own beat.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `computational-skepticism-for-ai/
  youtube/` (or `brutalist-art/youtube/` — tell me the owning book slug).
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals → QC →
  BUILD-PROMPT.md. **Re-verify the Botspeak chapter references** (Nine Capacities Ch 2, Discernment
  Ch 6, the Loop, the five-component Specification) against the current edition at build time — I
  grounded on the assignment's citations.
- Course series: this joins the Computational-Skepticism set (Week-1 Boondoggle Report + the
  Reallocation Engine, Audited). Say the word and I'll map the remaining weekly validation exercises
  and the research-project milestones into one course series index, alongside the INFO 7375 branding set.
