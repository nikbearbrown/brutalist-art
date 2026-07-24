# SERIES ROADMAP — "Make It Run: The Reallocation Engine Mode Build"

A how-to ai-explainer series for **The Reallocation Engine — Mode Build Assignment** (a runnable
mode file + domain justification + a real worked run + a GitHub PR + a 5-min show-and-tell, 100 pts
= 80 rubric + 20 quartile). Audience: **international students / early-career technical workers who
designed a mode on paper (the 25-pt version) and now have to make one that actually executes.**
Register: **pragmatic how-to with a skeptical edge** (Liam voice, `claude-liam`, Kokoro am_onyx).
Five episodes. The one word that separates this from the 25-pt assignment: **run.** Nothing has to
be perfect — it has to be honest, and it has to have actually run.

> Voice: `claude-liam` per request. Build into `the-reallocation-engine/youtube/`, or
> `brutalist-art/youtube/` — tell me the owning book slug. This is the runnable successor to the
> Mode Design roadmap (design → build); it reuses the domain-justification craft and adds
> execution, the recipe lifecycle, attestation, and the PR.

## The engine (recap in E1) + the prime directive

Evidence-first job-search system fighting information asymmetry across three layers — **80 Days to
Stay** (Form D + H-1B history), **Job-Ops** (ATS detection, posting liveness), **The Cognitive
Pivot** (BLS/O*NET role-quality scoring). Governed by **SNICKERDOODLE.md** (the constitution) and
indexed by **DOMAIN.md**. **Prime directive: use verified local data and tested scripts first; use
an LLM only to explain, summarize, draft, or make bounded judgments *after* the data is checked.**
`github.com/nikbearbrown/the-reallocation-engine/`

## Curriculum convergence (one line in E1)

The repo's constitution is **SNICKERDOODLE.md** — the same `/snickerdoodle` that Gru generates — and
the recipe lifecycle (DRAFT → SPECIFIED → RUNNABLE-SAMPLE → RUNNABLE-LIVE → VERIFIED) is Gru's
RUNNABLE graduation with evidence attached. The typed `[TODO]` and the gate discipline are the same
across Gru, the A5B recipe framework, and this engine. One discipline, three courses.

## The honesty rule is GRADED, not decorative (the spine)

- **Run it. Paste the real terminal output — don't describe it.** Output fabricated without
  acknowledgment is a **zero**.
- **The lifecycle status is a claim, and every claim needs evidence.** A mode honestly marked
  **RUNNABLE-SAMPLE with one real run and a clear-eyed list of what it cannot do scores higher than
  one marked VERIFIED with no evidence.** Editing status without evidence is a violation, not a
  promotion.
- **Typed `[TODO]` for scripts that don't exist yet** — label their output *proposed*, never as if
  it ran.
- **The verified/inferred boundary is the heart of the grade.**
- **Attestation must include a deliberate attempt to BREAK it.** "Did not test: an empty list is the
  new 'it works'."
- **Gates, not votes.** Liveness and visa timeline are hard stops with testable conditions.
- **Stop conditions:** the mode refuses to produce a score rather than guess.
- **Privacy is enforced by the tree.** `private/` and `data/ats/` are gitignored; `npm run doctor`
  checks it; a PR that leaks personal data is not gradeable.
- **"Specific enough":** the workflow is recognizable to a student in *that exact situation*, not any
  international job-seeker. The best submissions are clearest about what the mode CANNOT do.

## Series doctrine (every episode)

- **Assume the design skill (from the 25-pt version), teach the execution + hygiene.** Define every
  term first time (conformance check, dry-run, recipe lifecycle, phase gate, output contract,
  attestation, typed TODO, fork/branch/PR, `npm run doctor`). Never "just."
- **One deliverable per episode**, ending in the real artifact, with the exact command to run — then
  the "paste the real output / mark verified-vs-inferred" pass.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your Turn
  → title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "Get the Engine Running + Read the Constitution" (~6 min)
- **slug:** `claude-liam-mb-01-get-it-running`
- **premise:** You can't build a mode that runs until the engine runs. Clone it, read its law, and
  get one real command to execute before you design anything.
- **teach:** clone + `npm install`; **read SNICKERDOODLE.md, DOMAIN.md, AGENTS.md, recipes/README.md**;
  run the **conformance check** `npm run verify`; then a real **side-effect-free run** to anchor your
  mode — e.g. `npm run ats:scan -- --dry-run` (no writes), `npm run ats:liveness -- <job-url>` (a
  GATE, not a vote), `npm run score` (BLS/O*NET scorer); **capture the real terminal output**. The
  prime directive; the privacy rule (`private/`, `data/ats/` gitignored; `npm run doctor` enforces;
  artifacts from private data write back into `private/`).
- **traps:** designing before the engine runs; skipping the constitution; committing personal data.
- **deliverable:** a running engine + captured output from one real command. Your Turn = "run
  `npm run verify`, then one dry-run command; paste the output — that's your worked-run anchor."

### E2 — "Design the Runnable Mode: Lifecycle, Gates, Output Contract (Mode Design, 24 pts)" (~7 min)
- **slug:** `claude-liam-mb-02-design-the-mode`
- **premise:** The mode file is the primary deliverable — and now every command it names must
  actually exist, and its status must be honest about where you landed.
- **teach:** write it in `recipes/` style, named for your situation
  (`case-biostat-h1b-soc-15-2041.md`); the **status frontmatter + recipe lifecycle** (DRAFT →
  SPECIFIED → RUNNABLE-SAMPLE → RUNNABLE-LIVE → VERIFIED — be honest); **Purpose** (what + exactly
  when to use it); **Source Inventory** (exact paths/commands that *actually exist* —
  `data/80-days-to-stay/…`, `data/BLS/…`, `npm run …`, `scripts/…`); **proposed additions** with a
  justification, each a **typed `[TODO]`**; **phase gates** (liveness + visa timeline are GATES not
  votes, each with a testable condition); **what it can/cannot verify** (the heart of the grade);
  the **output contract** (an agent log JSON + a human report — **one artifact cannot serve both
  readers**); **stop conditions** (refuse to score rather than guess); a **RUN_LOG template**.
- **traps:** a command that doesn't exist; a status claim with no evidence; one artifact for both
  readers; gates written as votes; a fuzzy verified/inferred line.
- **deliverable:** the mode file. Your Turn = a prompt that drafts the mode in the recipe format,
  then the "does every named command actually exist, and is the status honest?" pass.

### E3 — "The Domain Justification (20 pts)" (~5 min)
- **slug:** `claude-liam-mb-03-domain-justification`
- **premise:** One page proving the mode solves a *specific* invisibility for a *specific* person —
  and naming the errors that person would find hardest to catch.
- **teach:** who uses it + the **exact situation** ("PhD in biostatistics evaluating industry roles
  that sponsor H-1B for SOC 15-2041"); the **information asymmetry** (what they can't easily see —
  sponsorship for their specific SOC, a dead posting, a funding-dry ghost employer); the connection
  to **one or more engine layers**; the **failure modes** — 1–2 *domain-specific* ones (the shape of
  the error and **for whom it's hardest to catch**, e.g. "a company shows H-1B history but only for
  a different SOC than mine — the mode greenlights it and I burn a cycle").
- **traps:** a generic justification; failure modes that fit any job-seeker; restating the assignment.
- **deliverable:** the one-page justification. Your Turn = a prompt that names the specific asymmetry
  and the domain-shaped failure modes for the student's mode.

### E4 — "The Worked Run: Actually Run It, Then Try to Break It (Worked Run, 16 pts)" (~7 min)
- **slug:** `claude-liam-mb-04-worked-run`
- **premise:** This is where "designed" becomes "ran." Real output, a clean verified/inferred split,
  and a deliberate attempt to break your own mode.
- **teach:** run the mode (or its existing parts) against a real/realistic scenario; **inputs**
  (anonymized if from private data); **commands run verbatim + real terminal output pasted, not
  described**; the **verified vs. inferred** line-by-line split (what the data/scripts established vs.
  what you or an LLM judged); **verification** (re-ran with `--dry-run`, parsed the JSON,
  cross-checked a count against the source, **deliberately tried to break it**); the **Attestation**
  block (Tested table — Ran / Saw / Expected, including the break attempt; Did not test — an honest
  list; Broke during testing, fixed); **reflection** (what worked, what it missed, next steps —
  "nothing is perfect; say where yours isn't").
- **traps:** described output instead of pasted; a fuzzy verified/inferred split; no break attempt;
  a reflection with no real run.
- **deliverable:** the worked run + attestation. Your Turn = "run your one real command, paste the
  output, then try to make it produce a wrong score — the break attempt is worth more than a clean run."

### E5 — "Ship It: Zip + GitHub PR + the Show-and-Tell (Presentation 20 + submission)" (~6 min)
- **slug:** `claude-liam-mb-05-ship-and-present`
- **premise:** Two submissions, conformance-clean, plus five minutes in front of the class. The PR is
  the proof it runs in the real tree.
- **teach:** append the **RUN_LOG entry** (date, mode, inputs, outputs, result, open issues — no
  secrets/PII); **scrub `private/` and `data/ats/`**; the **zip** (`reallocation-<name>-mode.zip` —
  mode file, justification, worked run + attestation, RUN_LOG, any new scripts/sample data); the
  **GitHub PR** (fork; branch `mode/<name>-<domain>`; mode under `recipes/`, justification + worked
  run under `assignments/submissions/<name>/`; run **`npm run verify` and `npm run doctor` before
  pushing** — a PR that fails conformance or leaks private data isn't gradeable; PR title names the
  domain + the lifecycle stage you reached); the **5-min show-and-tell** (the domain, the asymmetry,
  **one thing you learned from running or failing to run it**, **one honest limitation it cannot
  verify** — show the mode file + terminal directly, hold to time).
- **traps:** a PR failing `verify`/`doctor`; leaked PII; a status claim above the evidence; a
  presentation that's a feature tour instead of "what I learned + what it can't do."
- **deliverable:** the zip + the PR + the presentation. Your Turn = "run `npm run verify && npm run
  doctor` before you push — if either fails, that's your only job before the PR is gradeable."

---

## Tight cut

Four-episode version: Get-it-running + design (E1+E2) · Justification (E3) · Worked run + attest (E4)
· Ship + present (E5→folded). The 5-episode cut is better because the mode design (24 pts) and the
worked run (16 pts) are the two heaviest components and each needs its own beat.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `the-reallocation-engine/youtube/`
  (or `brutalist-art/youtube/` — tell me the owning book slug). Privacy: demos use a *fictional*
  résumé/scenario and a public example URL — never real student PII.
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals → QC →
  BUILD-PROMPT.md. **Ground the exact `npm run …` targets, script paths, data paths, and the recipe
  frontmatter on the current repo at build** (device bridge offline — I couldn't open the local tree;
  re-verify `SNICKERDOODLE.md`, `package.json` scripts, `recipes/`, and the lifecycle field names on
  disk). Terminal output shown as Onda code-blocks, not screenshots.
- Course fit: this completes the Reallocation-Engine trio — the **Personal Layer** setup, **Mode
  Design** (25-pt paper), and **Mode Build** (this, 100-pt runnable) — alongside the
  Computational-Skepticism set (Boondoggle, Botspeak, the "Audited" assignment, and the "What Is
  Gru?" helper). Say the word and I'll stitch one **course index** across both courses.
