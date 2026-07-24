# SERIES ROADMAP — "Ship Something Real: The Reallocation Engine Capstone"

A how-to ai-explainer series for **The Reallocation Engine — A Working Professional Contribution
(250-point capstone / final project)**: a real, mergeable contribution to a live evidence-first system,
plus a verified-data attestation, an honest run, a GitHub PR, a portfolio piece, and an explainer video.
Audience: **international students / early-career technical workers who have used the engine, done the
25-pt progress report, and now have to ship something a maintainer would merge and a hiring manager would
open.** Register: **pragmatic how-to with a skeptical edge** (Liam voice, `claude-liam`, Kokoro am_onyx).
Eight episodes — proportionate to a 250-point capstone. The one sentence the whole project turns on:
**"Can the model verify this against reality, or only against itself? If only against itself, it's yours."**

> Voice: `claude-liam` per request. Owning book: **the-reallocation-engine**. Build into
> `the-reallocation-engine/youtube/`, or `brutalist-art/youtube/` — this roadmap ships into
> `brutalist-art/youtube/` with its siblings. This is the runnable, professional-grade end of the
> Reallocation-Engine set: Personal Layer → Mode Design (25-pt) → Mode Build (25/100-pt) → **this**.

## What makes this different from every prior assignment (say it in E1)

You are not writing *about* the engine. You are **adding something to it that runs** — that clears
conformance, that a maintainer could merge, that a hiring manager could open. The skepticism the two
100-pt Computational-Skepticism assignments taught (audit a system you didn't build; break one you did)
is here turned into a résumé line: a real component, attested to the verified-data contract, run honestly,
and packaged for an employer.

## The engine + the contract (recap in E1)

Evidence-first job-search system fighting **information asymmetry** for international students and
early-career technical workers. Components: SEC Form D funding detector, 80-Days sponsorship scorer, ATS
detection + liveness, BLS/O*NET role quality, the visa-timeline gate, the Bayesian role scorer, the OPT
framing generator, the ATS-safe résumé renderer, the recipe runtime, and the pipeline tracker with its
**skip-rate** metric (**a healthy run skips ≥50% — skipping is a successful outcome**). The floor is the
**verified-data contract**: *"Run the script and read the audit before you prompt. Never invent a count, a
rate, or a coverage number."* Governance: `SNICKERDOODLE.md`, `DOMAIN.md`, `DATA_CONTRACT.md`,
`recipes/_shared.md`. Repo: `github.com/nikbearbrown/the-reallocation-engine/`.

## The honesty spine (the graded core — every episode)

- **Every number traces to a record**, or is explicitly labeled *model-judgment* / *your-input*. This is
  not a style note; it is **the zero condition** — an invented coverage rate, a fabricated liveness call, a
  made-up calibration figure is *the exact failure the engine exists to prevent* and caps the affected
  components at **zero**, not a deduction.
- **Prefer "not implemented yet" to fabrication.** A finding-shaped output with no script behind it is, by
  the book's own definition, the failure — graded as such.
- **Two customers, never one artifact for both.** The AI reads the recipe; the human reads the card. One
  file cannot serve both readers.
- **Gates have failure paths.** "If a gate has no failure path, it is not a gate, it is decoration."
- **The break attempt is worth more than a clean run.** You try to make your own contribution produce a
  wrong answer, and you report what you found.
- **Never self-certify honesty.** A human signs the attestation; the ethics gate (privacy + honesty) runs
  before the work does.

## Series doctrine (every episode)

- **Assume the student did the progress report, not that they've shipped production code.** Define every
  term first time (contribution, connector, EMPTY vs. ERROR, testable handoff condition, two-customer pair,
  recipe's nine sections, `.card.md`, drift, contract-violation, verified/inferred boundary, ethics gate,
  plausibility audit, break attempt, skip-rate, `npm run verify`/`doctor`, fork/branch/PR, uncut segment).
  Never "just."
- **One deliverable per episode**, ending in the real artifact, with the exact command to run — then the
  "does every number trace, and did you check it against the world?" pass.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your Turn →
  title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "Pick Your Contribution + Clear the Bar Before You Start" (~7 min)
- **slug:** `claude-liam-cap-01-pick-and-clear-the-bar`
- **premise:** The capstone is 250 points because it's real. Before you write a line, get the engine
  running, read its law, choose a contribution that fills a gap the book names, and confirm it can clear
  the seven-point bar — because a tight harness that clears it beats an ambitious connector that fabricates.
- **teach:** clone + `npm install`; **read `SNICKERDOODLE.md`, `DOMAIN.md`, `DATA_CONTRACT.md`,
  `recipes/_shared.md`**; run `npm run verify`; the **contribution menu** by family — **connectors** (a new
  ATS provider: Workday/iCIMS/SmartRecruiters, zero-token, EMPTY≠ERROR; an entity-resolution / employer-name
  matcher that flips artifact-"Unknown" tiers into real ones; an H-1B calendar/USCIS-processing connector;
  a metro wage-adjustment layer), **scorers & harnesses** (a gate-behavior unit-test harness that proves
  liveness+timeline **zero** the composite — high value, tight scope; an ATS parse harness; a
  calibration-curve harness; a provenance/drift checker; an output linter), **modes/ledgers/dashboards** (a
  promoted runnable recipe; an override ledger + weights-profile switcher; a skip-rate dashboard); then the
  **seven-point bar** (every number traces · two-customer pair · gates with failure paths · audit + RUN_LOG
  entry · "not implemented" over fabrication · `data/ats/` uncommitted + no self-certified honesty ·
  no finding without a script). Choose one you can *finish honestly*.
- **traps:** choosing scope you can't finish; a contribution that would have to fabricate a number to look
  done; skipping the governance reads.
- **deliverable:** a chosen contribution + a written check against the seven-point bar. Your Turn = "before
  you commit to a contribution, write the one number it will output and name the record that number will
  come from — if there's no record, pick a smaller contribution that has one."

### E2 — "Build It So It Actually Runs (the 60-point core)" (~7 min)
- **slug:** `claude-liam-cap-02-build-it-runs`
- **premise:** Sixty of the 250 points are one thing: it works. Real feeds, real behavior, testable
  handoff conditions — not "it looks done."
- **teach:** build into the real repo structure (`scripts/` lowercase, `recipes/`, `data/`, `reports/`,
  `output/` for generated artifacts); the **testable handoff condition** as the definition of "works" —
  *"The scan returns real postings with provenance,"* never *"looks done"*; the shape by contribution type
  — a **connector** pulls real feeds and **separates EMPTY from ERROR** (an empty result is a fact, an error
  is a failure, and conflating them is a silent bug); a **harness** *actually fails on the bug it targets
  and passes when fixed* (the gate-as-vote bug: prove liveness/timeline **zero** the composite, don't just
  down-weight); an **entity-resolver** reports **real before/after coverage on real data**; wire it to write
  its **audit** and a **`RUN_LOG.md`** entry.
- **traps:** EMPTY silently treated as ERROR (or vice-versa); a harness that passes whether or not the bug
  exists; a handoff condition that says "looks good"; generated output committed as source of truth.
- **deliverable:** the running contribution + its audit + RUN_LOG entry. Your Turn = "write your handoff
  condition as a sentence a stranger could test — 'the resolver rescues N artifact-Unknowns and a human
  confirms a 10-row sample' — then run it and see if it's true."

### E3 — "The Two-Customer Pair: Recipe for the AI, Card for the Human" (~7 min)
- **slug:** `claude-liam-cap-03-two-customer-pair`
- **premise:** Your contribution ships to two readers who need opposite things. One artifact cannot serve
  both — so you write two, in the same commit.
- **teach:** the **AI recipe** (complete, explicit, imperative, read-first order, verbatim commands, stop
  conditions, log template) with its **nine required sections** — executive summary · required reads · phase
  gates · primary stored tools *or* "no stored script exists" · workflow · output contract · verification
  checks · logging rules · stop conditions; and the human **`.card.md`** — purpose · what it can/can't
  verify · dependencies · annotated commands · what it produces · **≥4 named failure modes including drift
  and contract-violation**; the rule that **phase gates each carry a failure path**; and why the two files
  update **together** (a card that drifts from its recipe is itself a failure mode the card must name).
- **traps:** one file trying to serve both readers; a recipe missing a section; a card with vague failure
  modes or fewer than four; drift + contract-violation omitted; updating one file and not the other.
- **deliverable:** the recipe (nine sections) + the card (≥4 failure modes). Your Turn = "write your card's
  four failure modes first — including how it drifts and how it violates the contract — because if you can't
  name four ways your own component fails, you don't understand it yet."

### E4 — "The Verified-Data Attestation: Every Number Traces" (~7 min)
- **slug:** `claude-liam-cap-04-verified-data-attestation`
- **premise:** The contract's floor, made auditable. Every number your component prints is either traceable
  to a record or labeled a judgment — and you prove it, with the ethics gate passing.
- **teach:** the **verified-vs-inferred boundary table** (the "Give to AI / Keep for yourself" split applied
  to *your* component) — every field/number labeled **record / script-output / local-evidence /
  external-source / model-inference / your-input / missing**; **every number traces** — for each figure
  (coverage count, rate, score, PASS/FAIL) name the script and the record it came from, and if it's a model
  judgment, **label it, don't print it as a fact**; the **ethics gate (Ch 16)** — **(a) Privacy**: no
  `data/ats/` or private file staged for commit, `npm run doctor` clean; **(b) Honesty**: nothing your
  component generates misrepresents status or invents a metric — *if either fails, the run does not happen*
  — shown passing.
- **traps:** a number on the "record" side that's actually a model guess; a boundary table missing the
  component's headline figure; `npm run doctor` not shown; honesty self-certified instead of gate-checked.
- **deliverable:** the boundary table + per-number traces + the ethics gate passing. Your Turn = "take the
  one number your component is proudest of and ask the one-question test — *could this have been produced by
  counting records?* If not, it belongs on the inferred side, and you label it there now."

### E5 — "The Honest Run: Run It, Audit It, Then Try to Break It" (~7 min)
- **slug:** `claude-liam-cap-05-the-honest-run`
- **premise:** Where "built" becomes "ran honestly." Real output, a plausibility audit before you trust it,
  and a deliberate attempt to make your own component lie — worth more than a clean run.
- **teach:** the **plausibility audit before you trust the output** — sanity-check a batch (does a ~0
  sponsorship **collapse** the composite? does a role past the OPT window get **gated**, not merely
  down-weighted?), catching the failure that *"ran, looked reasonable, and was wrong in exactly the way
  fluency hides"*; **real terminal output, pasted not described** — the actual commands and their actual
  output; the **deliberate break attempt** — try to force a wrong answer (a fuzzy-match false join, a ghost
  posting scored live, a gate behaving like a vote) and report what you found; the **metric readout** if
  your component touches decisions (**skip-rate** in its working range, coverage before/after, parse
  PASS-rate, calibration error); and the **"what the machine could not know"** account — the judgment your
  contribution can't make, the record it can't see, the human call it hands back.
- **traps:** described output instead of pasted; a plausibility check skipped (the fluency-hides failure
  ships); no break attempt; a metric with no working-range context; no honest close.
- **deliverable:** the honest run + break attempt + metric readout. Your Turn = "run your component, then
  spend ten minutes trying to make it print a number you know is wrong — if you can't break it, say how you
  tried; if you can, that break is the most valuable paragraph in your submission."

### E6 — "Ship the PR: Fork, Branch, verify + doctor, No PII" (~6 min)
- **slug:** `claude-liam-cap-06-ship-the-pr`
- **premise:** A contribution that isn't in a maintainer-reviewable PR isn't a contribution. Ship it the way
  the engine holds every run — conformance-clean, private-data-free.
- **teach:** **fork** the repo; branch `contrib/<name>-<component>`; contribution code under `scripts/` +
  `recipes/`, docs/audit in the right folder, **nothing generated committed as source of truth**; run
  **`npm run verify` and `npm run doctor` before you push** — *a PR that fails conformance or leaks private
  data is not gradeable*, the same bar the engine holds itself to; **no PII, no `data/ats/` contents**; the
  **PR description** names the gap it closes, the chapters it satisfies, the verified-vs-inferred boundary,
  and the one limitation it cannot verify. (If upstream doesn't take external PRs, PR against your own fork
  with the full diff + a maintainer-ready description — the discipline, not the merge, is graded.)
- **traps:** pushing before `verify`/`doctor`; a private file in the diff; a PR description that lists
  features instead of naming the gap + the limitation; generated artifacts committed as truth.
- **deliverable:** the submitted PR link. Your Turn = "run `npm run verify && npm run doctor` and read the
  staged diff line by line for one private path before you push — the leak you don't catch here is the one
  that makes the whole PR ungradeable."

### E7 — "The Portfolio Piece: the Thing That Outlives the Course" (~6 min)
- **slug:** `claude-liam-cap-07-portfolio-piece`
- **premise:** The artifact you show an employer — written for a technical hiring manager, not the grader.
  One honest measurable improvement is the whole game.
- **teach:** a professional **case study** (2–4 pages or a clean single-page site) — **the problem** (the
  specific information asymmetry your contribution attacks, for a specific person); **what you built** (plain
  professional language + architecture in a diagram or a few sentences); **the measurable improvement** (the
  number that makes it real — join-coverage before/after, artifact-Unknowns rescued, skip-rate moved into
  range, parse PASS-rate, calibration error reduced, a bug the harness now catches — **one honest metric
  beats three vague claims**); **verified vs. inferred** stated plainly (the professional signal: you know
  what your system does and doesn't know); **the failure modes + the one limitation it can't verify**
  (naming what it can't do is the strongest thing on the page); and a **demo** (a short screen capture, the
  linked PR, or a runnable snippet a reader can open). Portfolio-grade writing — calibrated verbs, no
  fabricated metrics, no `[ASK ME]` placeholders left in.
- **traps:** written for the grader instead of a hiring manager; three vague claims instead of one real
  number; the limitation hidden instead of featured; no openable demo.
- **deliverable:** the employer-ready portfolio piece. Your Turn = "write the one sentence a hiring manager
  will remember — your single measurable improvement, sourced to a record — and if you can't source it,
  it's not the sentence yet."

### E8 — "The Explainer Video + the Honesty Overlay + Submit" (~6 min)
- **slug:** `claude-liam-cap-08-video-and-submit`
- **premise:** Close it out: a 3–6 minute video whose graded core is one uncut live terminal run, a final
  honesty sweep, and submission.
- **teach:** the **explainer video** (3–6 min) — the domain + the asymmetry (~45s), then **the uncut live
  run** (your contribution executing, or `npm run verify && doctor`, real command and real output in real
  time, **no cut inside the take**, on a **fictional scenario + public data — never real PII on screen**;
  if it errors on camera, **leave it in and narrate the fix** — the most honest footage you can submit),
  then **one thing you learned** running or failing to run it and **one honest limitation** it can't verify
  (may build with the brutalist explainer pipeline, but the run must be **real screen capture, not a slide
  of pasted output**); then the **honesty overlay** (10 pts across everything) — nothing self-certified,
  verbs calibrated throughout, and a reminder that **a fabricated metric or a finding with no script behind
  it forfeits this and caps the run + attestation at zero**; then assemble and submit the whole package
  (PR link · attestation · portfolio piece · video).
- **traps:** a polished screencast with the terminal edited out (fails the uncut requirement); real PII on
  screen; a "lesson" that's a feature tour; leaving a self-certified honesty claim in the package.
- **deliverable:** the video + the assembled, submitted capstone. Your Turn = "record one uncut take of your
  component running on public data — if it errors, keep the take and narrate the fix — because the uncut run
  is the 20 points, and the honesty is the 10 that can zero everything else."

---

## Tight cut

Five-episode version: Pick + build (E1+E2) · Two-customer pair + attestation (E3+E4) · Honest run (E5) ·
Ship PR + portfolio (E6+E7) · Video + submit (E8). The 8-episode cut is better because "it works" (60),
the attestation (35), the honest run (35), and the portfolio (35) are the four heaviest components and each
needs its own beat — folding them buries the verified-data discipline that is the whole point.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `the-reallocation-engine/youtube/` (or
  `brutalist-art/youtube/` — where the siblings live). Demos use a **fictional scenario + public example
  data and a public example URL** — never real student PII, in the reels or in the modeled student video.
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals → QC →
  BUILD-PROMPT.md. **Ground the exact `npm run …` targets, the recipe's nine sections, the card fields, the
  boundary-table labels, the `data/ats/` privacy rule, and the skip-rate ≥50% target on the current repo at
  build** — re-verify `SNICKERDOODLE.md`, `DATA_CONTRACT.md`, `recipes/_shared.md`, `package.json` scripts,
  and the RUN_LOG format on disk. Terminal output shown as Onda code-blocks; the modeled "uncut segment" is
  a real screen-capture beat, not a static slide.
- Course fit: this completes the Reallocation-Engine set (Personal Layer · Mode Design 25-pt · Mode Build
  25/100-pt · **this capstone**) and closes the arc that begins with the two 100-pt Computational-Skepticism
  assignments (audit / build-and-break) and the **25-pt brutalist-explainer progress report** (the `/v0`
  gate and first honest run that precede this final). Say the word and I'll stitch one **course index**
  across both courses — every assignment, its roadmap, and the skepticism→contribution throughline.
