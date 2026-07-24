# SERIES ROADMAP — "Design a Mode: The Reallocation Engine"

A how-to ai-explainer series for **The Reallocation Engine — Mode Design Assignment** (a mode file
+ domain justification + worked example + a 5-min show-and-tell, 25 pts = 15 rubric + 5 presentation
+ 5 quartile). Audience: **international students / early-career technical workers who use the
engine and have never designed an operating recipe.** Register: **pragmatic how-to with a skeptical
edge** (Liam voice, `claude-liam`, Kokoro am_onyx). Four episodes, proportionate to a 25-point
design assignment. The series walks a student from "I job-search in the dark" to "a mode designed
for my exact situation that's honest about what it can and can't verify."

> Voice: `claude-liam` per request. Build into `the-reallocation-engine/youtube/`, or
> `brutalist-art/youtube/` — tell me the owning book slug.

## What the engine is (teach it in E1)

The Reallocation Engine fights **information asymmetry** in the job search — the claim that the
problem isn't motivation, it's that students can't easily see which companies sponsor H-1B, which
just got funded, or whether a posting is even live. Three layers:
- **80 Days to Stay** — 30K+ companies mapped with SEC Form D funding signals + H-1B sponsorship history
- **Job-Ops** — ATS provider detection, job-liveness checking, application tracking, pipeline integrity
- **The Cognitive Pivot** — BLS/O*NET role-quality scoring (the premium is shifting toward
  verification, system judgment, causal reasoning — work AI can't reliably do yet)
Stack: Python + Node; Greenhouse/Lever/Ashby scrapers; a Playwright liveness checker; a SOC
occupation table (1,000+ occupations with cognitive-demand scores).
`github.com/nikbearbrown/the-reallocation-engine/`

## The prime directive (the spine of every episode)

**Use collected data and tested scripts first.** Prompt an LLM only to explain, summarize, draft, or
make bounded judgments *after* the relevant data has been checked. **If data is missing, say so. If
a script doesn't exist yet, propose it — don't pretend it runs.** The best modes are the ones
clearest about what they *cannot* do. This is the same verified-first, honest-about-gaps discipline
as the recipe framework and Gru — a "mode" is an operating recipe with the GIGO gate built in.

## Honesty / craft threads (DOUBLE-CHECK LAW)

- **"Specific enough" is the test.** Not "job-seeker in tech" but "international MS in data science
  with OPT expiring in 8 months." Would a student in that *exact* situation recognize the workflow,
  or could it describe any international job-seeker?
- **Draw the verified/inferred boundary explicitly.** The whole grade turns on it — what the mode
  verifies with data vs. what it infers.
- **Don't pretend a script runs.** Propose missing scripts honestly; name the gaps.
- **Failure modes are domain-shaped** — the error hardest for *someone in this situation* to catch,
  not "the model might hallucinate."
- **Run it or simulate it — don't describe running it.** The quartile rewards evidence you actually
  did. A fabricated example without acknowledgment scores zero.

## Series doctrine (every episode)

- **Assume engine familiarity, not mode-design skill.** Define every term first time (mode, operating
  recipe, information asymmetry, ATS, Form D, H-1B sponsorship, SOC code, OPT, cognitive-demand
  score, RUN_LOG, verified vs. inferred). Never "just."
- **One deliverable per episode**, ending in the real artifact, with a paste-ready prompt to draft
  the first pass — then the "is this honest about what it can't verify?" pass.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your Turn
  → title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "What the Engine Is + Pick Your EXACT Situation" (~5 min)
- **slug:** `claude-liam-rem-01-engine-and-situation`
- **premise:** The engine makes invisible job-search signals visible. Your mode is only as good as
  how precisely you name the person it's for — and that person is you.
- **teach:** the three layers (80 Days / Job-Ops / Cognitive Pivot) and the information-asymmetry
  claim; what a **mode** is (a student-facing operating recipe — what data to check, which scripts to
  run, what output, what to log — verified-data-first); the **"specific enough" test** (the
  too-generic vs. specific-enough table — "PhD in biostatistics evaluating industry roles that
  sponsor H-1B for SOC 15-2041," not "researcher"); the example modes as starting points (biotech,
  opt-countdown, cognitive-fit, salary-floor, startup-triage). Pick your exact situation.
- **traps:** a mode for "any international job-seeker"; a situation you can't defend with real detail.
- **deliverable:** a named exact situation + a mode concept. Your Turn = a prompt that pressure-tests
  a situation against "could this describe any international job-seeker?" and tightens it.

### E2 — "Write the Mode File: Verified-Data-First (Mode Design Quality, 6 pts)" (~6 min)
- **slug:** `claude-liam-rem-02-write-the-mode`
- **premise:** The mode file is the deliverable, in the style of `modes/`. Its honesty about what it
  can't verify is what earns the points.
- **teach:** the sections — what the mode **does + when to use it**; **existing data/scripts** it
  uses (exact paths/commands from the repo — the scrapers, the liveness checker, the SOC table);
  **new data/commands proposed**, if any, each with a **justification** for why they belong; the
  **can/cannot verify** section, explicit about gaps (the prime directive); an **output format** (a
  table, report template, or log entry); and a **log template for `modes/RUN_LOG.md`**. The rule: use
  data and scripts first; prompt only to explain/summarize/judge *after* the data is checked. If a
  script doesn't exist, propose it — don't pretend.
- **traps:** a prompting recipe where a dataset/script could answer; vague "checks the company"; no
  RUN_LOG template; pretending a missing script runs.
- **deliverable:** the mode file. Your Turn = a prompt that drafts the mode in the `modes/` style,
  then the "mark every step verified-by-data vs. inferred-by-prompt" pass.

### E3 — "The Domain Justification: Name the Asymmetry + the Failure Modes (5 pts)" (~5 min)
- **slug:** `claude-liam-rem-03-domain-justification`
- **premise:** One page. Prove the mode solves a *specific* invisibility for a *specific* person —
  and name the errors that person would find hardest to catch.
- **teach:** who uses it + in what situation; **what information asymmetry it addresses** (what can
  the student not easily see without it — a sponsorship gap? a dead posting? a funding-dry ghost
  employer?); how it **connects to one or more engine layers** (80 Days / Job-Ops / Cognitive Pivot);
  and the **failure modes** — 1–2 *domain-specific* ones (the shape of the error hardest for someone
  in this exact situation to catch, e.g. "a company shows H-1B history but only for a different SOC
  code than mine — the mode would greenlight it and I'd waste a cycle").
- **traps:** a generic justification; failure modes that apply to any job-seeker; restating the assignment.
- **deliverable:** the one-page justification. Your Turn = a prompt that names the specific asymmetry
  and drafts the domain-shaped failure modes for the student's mode.

### E4 — "The Worked Example + the Show-and-Tell (4 pts + 5 pts) + ship" (~6 min)
- **slug:** `claude-liam-rem-04-worked-example-and-present`
- **premise:** Run it (or simulate it) against a real scenario, show the output honestly, then
  present it in five minutes.
- **teach:** the **worked example** — what inputs you used; what the mode produced; **what was
  verified vs. inferred**; what you'd change after seeing the output (run against a real or realistic
  scenario — a fabricated example without acknowledgment is a zero); then the **5-minute
  show-and-tell** (the domain/situation you designed for, the information asymmetry, and **one
  concrete thing you learned** from running or simulating it — no slides required, show the mode file
  directly); assemble the three parts and submit.
- **traps:** a described run with no output; no verified/inferred commentary; a fabricated example; a
  presentation that's a feature tour instead of "here's what I learned."
- **deliverable:** the worked example + the presentation + the submission. Your Turn = "run your mode
  against one real posting or company; the gap between what it verified and what it inferred is your
  whole show-and-tell."

---

## Tight cut

Three-episode version: Engine + situation + mode file (E1+E2) · Justification (E3) · Worked example +
present (E4). The 4-episode cut is better because the mode file (6 pts) and the honesty about
verified-vs-inferred each need room to land for a first-time mode designer.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `the-reallocation-engine/youtube/`
  (or `brutalist-art/youtube/` — tell me the owning book slug).
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals → QC →
  BUILD-PROMPT.md. Ground the repo paths/commands on the current `github.com/nikbearbrown/the-
  reallocation-engine/` at build time (I couldn't open the local `the-reallocation-engine/chapters/`
  — device bridge offline — so re-verify the actual `modes/`, scripts, and RUN_LOG format on disk).

## Note on the other Reallocation-Engine roadmap

Earlier I wrote **"The Reallocation Engine, Audited"** (a Computational-Skepticism validation
assignment) using a *generic* resource-reallocation framing, because I couldn't read the book. Now
that the real engine is clear — a job-search / information-asymmetry system — I can **re-anchor that
assignment and its roadmap to the actual domain** (reallocating a student's job-search attention and
applications using verified H-1B/Form D/BLS signals, validated with the course's skeptical checks).
Say the word and I'll retune it.
