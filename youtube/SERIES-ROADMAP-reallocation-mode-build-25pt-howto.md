# SERIES ROADMAP — "Make It Run (Lite): The Reallocation Engine Mode Build, 25-Point"

A how-to ai-explainer series for **The Reallocation Engine — Mode Build Assignment (25-Point
Version)** (a runnable mode file + domain justification + a real worked run + a GitHub PR + a 3–5 min
**explainer video**, 25 pts = 20 rubric + 5 video). Audience: **international students / early-career
technical workers who designed a mode on paper and now have to make one that actually executes — on
a tighter budget than the 100-pt build.** Register: **pragmatic how-to with a skeptical edge** (Liam
voice, `claude-liam`, Kokoro am_onyx). Four episodes. The one word that separates this from the
design assignment: **run.** Nothing has to be perfect — it has to be honest, and it has to have
actually run. The one thing that separates it from the 100-pt build: the proof of running is **your
own uncut screen recording**, not a live show-and-tell.

> Voice: `claude-liam` per request. Build into `the-reallocation-engine/youtube/`, or
> `brutalist-art/youtube/` — this roadmap ships into `brutalist-art/youtube/` with its siblings.
> This is the lighter cut of `SERIES-ROADMAP-reallocation-mode-build-howto.md` (100-pt): same spine,
> four episodes instead of five, and the in-class presentation is replaced by a recorded explainer
> video whose graded core is **one unscripted, uncut segment of a live terminal run.**

## The rubric this version grades (say the split in E1)

- **Mode Design — 8 pts.** The runnable mode file: honest lifecycle status, gates not votes, an
  output contract, every named command actually exists.
- **Domain Justification — 7 pts.** One page proving the mode solves a *specific* invisibility for a
  *specific* person, with domain-shaped failure modes.
- **Worked Run — 5 pts.** A real run: commands verbatim, real output pasted, a clean verified/inferred
  split, and a deliberate break attempt.
- **Explainer Video — 5 pts (20% of the grade).** 3–5 minutes, and it must contain **at least one
  unscripted, uncut segment showing a live terminal run.** The uncut run is the point — a polished
  screencast with the terminal edited out fails the one thing this component tests.

## The engine (recap in E1) + the prime directive

Evidence-first job-search system fighting information asymmetry across three layers — **80 Days to
Stay** (Form D + H-1B history), **Job-Ops** (ATS detection, posting liveness), **The Cognitive
Pivot** (BLS/O*NET role-quality scoring). Governed by **SNICKERDOODLE.md** (the constitution) and
indexed by **DOMAIN.md**. **Prime directive: use verified local data and tested scripts first; use
an LLM only to explain, summarize, draft, or make bounded judgments *after* the data is checked.**
`github.com/nikbearbrown/the-reallocation-engine/`

## Curriculum convergence (one line in E1)

The repo's constitution is **SNICKERDOODLE.md** — the same `/snickerdoodle` Gru generates — and the
recipe lifecycle (DRAFT → SPECIFIED → RUNNABLE-SAMPLE → RUNNABLE-LIVE → VERIFIED) is Gru's RUNNABLE
graduation with evidence attached. The typed `[TODO]` and the gate discipline are the same across
Gru, the A5B recipe framework, and this engine. One discipline, three courses.

## The honesty rule is GRADED, not decorative (the spine)

- **Run it. Paste the real terminal output — don't describe it.** Output fabricated without
  acknowledgment is a **zero**. In this version the video makes that literal: the grader watches it
  run.
- **The lifecycle status is a claim, and every claim needs evidence.** A mode honestly marked
  **RUNNABLE-SAMPLE with one real run and a clear-eyed list of what it cannot do scores higher than
  one marked VERIFIED with no evidence.** Editing status without evidence is a violation, not a
  promotion.
- **Typed `[TODO]` for scripts that don't exist yet** — label their output *proposed*, never as if it
  ran.
- **The verified/inferred boundary is the heart of the grade.**
- **Attestation must include a deliberate attempt to BREAK it.** "Did not test: an empty list is the
  new 'it works'."
- **Gates, not votes.** Liveness and visa timeline are hard stops with testable conditions.
- **Stop conditions:** the mode refuses to produce a score rather than guess.
- **Privacy is enforced by the tree.** `private/` and `data/ats/` are gitignored; `npm run doctor`
  checks it; a PR that leaks personal data is not gradeable — **and the video must never show real PII
  on screen** (use a fictional résumé/scenario and a public example URL).
- **"Specific enough":** the workflow is recognizable to a student in *that exact situation*, not any
  international job-seeker. The best submissions are clearest about what the mode CANNOT do.

## Series doctrine (every episode)

- **Assume the design skill (from the 25-pt Mode Design version), teach the execution + hygiene.**
  Define every term first time (conformance check, dry-run, recipe lifecycle, phase gate, output
  contract, attestation, typed TODO, fork/branch/PR, `npm run doctor`, uncut segment). Never "just."
- **One deliverable per episode**, ending in the real artifact, with the exact command to run — then
  the "paste the real output / mark verified-vs-inferred" pass.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your Turn →
  title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "Get It Running + Design the Mode (Mode Design, 8 pts)" (~7 min)
- **slug:** `claude-liam-mb25-01-run-and-design`
- **premise:** You can't build a mode that runs until the engine runs — and on a 25-point budget, get
  it running and design the mode in one sitting, honest about where you landed.
- **teach:** clone + `npm install`; **read SNICKERDOODLE.md, DOMAIN.md, AGENTS.md, recipes/README.md**;
  run the **conformance check** `npm run verify`, then one **side-effect-free run** to anchor the mode
  (e.g. `npm run ats:scan -- --dry-run`, `npm run ats:liveness -- <job-url>` as a GATE not a vote,
  `npm run score`) and **capture the real output**. Then write the mode in `recipes/` style, named for
  your situation (`case-biostat-h1b-soc-15-2041.md`): the **status frontmatter + recipe lifecycle**
  (be honest — RUNNABLE-SAMPLE beats a hollow VERIFIED); **Purpose** (what + exactly when);
  **Source Inventory** (exact paths/commands that *actually exist*); **proposed additions** as typed
  `[TODO]`; **phase gates** (liveness + visa timeline, each with a testable condition); **what it
  can/cannot verify** (the heart of the grade); the **output contract** (agent log JSON + human report
  — one artifact cannot serve both readers); **stop conditions**; a **RUN_LOG template**. The prime
  directive and the privacy rule (`private/`, `data/ats/` gitignored; `npm run doctor` enforces).
- **traps:** designing before the engine runs; a command in the mode that doesn't exist; a status
  claim with no evidence; one artifact for both readers; gates written as votes; committing PII.
- **deliverable:** a running engine + captured anchor output + the mode file. Your Turn = "run
  `npm run verify`, then one dry-run command; paste the output — then draft the mode in recipe format
  and check every named command actually exists."

### E2 — "The Domain Justification (7 pts)" (~5 min)
- **slug:** `claude-liam-mb25-02-domain-justification`
- **premise:** One page proving the mode solves a *specific* invisibility for a *specific* person —
  and naming the errors that person would find hardest to catch.
- **teach:** who uses it + the **exact situation** ("PhD in biostatistics evaluating industry roles
  that sponsor H-1B for SOC 15-2041"); the **information asymmetry** (what they can't easily see —
  sponsorship for their specific SOC, a dead posting, a funding-dry ghost employer); the connection to
  **one or more engine layers**; the **failure modes** — 1–2 *domain-specific* ones (the shape of the
  error and **for whom it's hardest to catch**, e.g. "a company shows H-1B history but only for a
  different SOC than mine — the mode greenlights it and I burn a cycle").
- **traps:** a generic justification; failure modes that fit any job-seeker; restating the assignment.
- **deliverable:** the one-page justification. Your Turn = a prompt that names the specific asymmetry
  and the domain-shaped failure modes for the student's mode.

### E3 — "The Worked Run: Run It, Then Try to Break It (Worked Run, 5 pts)" (~6 min)
- **slug:** `claude-liam-mb25-03-worked-run`
- **premise:** Where "designed" becomes "ran." Real output, a clean verified/inferred split, and a
  deliberate attempt to break your own mode — the break attempt is worth more than a clean run.
- **teach:** run the mode (or its existing parts) against a real/realistic scenario; **inputs**
  (anonymized if from private data); **commands run verbatim + real terminal output pasted, not
  described**; the **verified vs. inferred** line-by-line split (what the data/scripts established vs.
  what you or an LLM judged); **verification** (re-ran with `--dry-run`, parsed the JSON, cross-checked
  a count against the source, **deliberately tried to break it**); the **Attestation** block (Tested
  table — Ran / Saw / Expected, including the break attempt; Did not test — an honest list; Broke
  during testing, fixed); **reflection** (what worked, what it missed, next steps — "nothing is
  perfect; say where yours isn't"). Note: **this run is also the raw material for the video's uncut
  segment in E4** — record your screen while you do it here.
- **traps:** described output instead of pasted; a fuzzy verified/inferred split; no break attempt; a
  reflection with no real run.
- **deliverable:** the worked run + attestation. Your Turn = "run your one real command, paste the
  output, then try to make it produce a wrong score — and hit record before you start, because that
  take is your video."

### E4 — "Ship It: PR + the Explainer Video with an Uncut Live Run (Video 5 pts + submission)" (~6 min)
- **slug:** `claude-liam-mb25-04-ship-and-record`
- **premise:** Two submissions, conformance-clean, plus a 3–5 minute video whose graded core is one
  unscripted, uncut segment of the terminal actually running. The PR proves it runs in the real tree;
  the uncut segment proves *you* ran it.
- **teach:** append the **RUN_LOG entry** (date, mode, inputs, outputs, result, open issues — no
  secrets/PII); **scrub `private/` and `data/ats/`**; the **zip** (`reallocation-<name>-mode.zip` —
  mode file, justification, worked run + attestation, RUN_LOG, any new scripts/sample data); the
  **GitHub PR** (fork; branch `mode/<name>-<domain>`; mode under `recipes/`, justification + worked run
  under `assignments/submissions/<name>/`; run **`npm run verify` and `npm run doctor` before
  pushing** — a PR that fails conformance or leaks private data isn't gradeable; PR title names the
  domain + the lifecycle stage you reached). Then the **explainer video** (3–5 min): a tight arc — the
  domain + the asymmetry (~45s), **the uncut live run** (the required segment — screen-record the real
  terminal executing your mode or its parts, unedited, output appearing in real time; a fictional
  scenario + public URL, no real PII), then **one honest limitation it cannot verify** and **one thing
  you learned from running or failing to run it**. Recording mechanics: any free screen recorder;
  don't cut inside the run take; if it errors on camera, **leave it in and narrate the fix** — that's
  the most honest footage you can submit.
- **traps:** a PR failing `verify`/`doctor`; leaked PII (in the tree *or on screen*); a status claim
  above the evidence; a video that's a polished feature tour with the terminal edited out (fails the
  uncut requirement); a scripted "run" that's actually a slide of pasted output.
- **deliverable:** the zip + the PR + the 3–5 min video. Your Turn = "record one uncut take of
  `npm run verify && npm run doctor` and your one real command; if it errors, keep the take and narrate
  the fix — the uncut run is the 5 points, not the polish."

---

## Tight cut

Three-episode version: Run + design + justification (E1+E2 folded) · Worked run (E3) · Ship + record
(E4). The 4-episode cut is better because Mode Design (8 pts) and the Domain Justification (7 pts) are
the two heaviest written components and each earns its own beat; folding them buries the justification.

## What changed from the 100-pt roadmap (so you can build either)

- **Five episodes → four.** The 100-pt "Get it running" (E1) and "Design the mode" (E2) fold into one
  E1 here; the point weights are smaller (Mode Design 8 vs. 24, Worked Run 5 vs. 16), so they don't
  each need a standalone beat.
- **In-class show-and-tell → recorded explainer video.** The 100-pt E5 presentation becomes E4's
  video. The graded core moves from "hold to time in front of the class" to **"one unscripted, uncut
  live-terminal-run segment"** — so the coaching shifts from stage presence to *don't cut the run
  take, and keep real PII off the screen.*
- **Everything else is identical:** the recipe lifecycle, gates-not-votes, the output contract, the
  attestation-with-break-attempt, the verified/inferred split, the PR + `verify`/`doctor` gate, and
  the privacy tree.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `brutalist-art/youtube/` (owning book
  slug per the sibling roadmaps). Privacy: demos — and the modeled student video — use a *fictional*
  résumé/scenario and a public example URL, never real student PII.
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals → QC →
  BUILD-PROMPT.md. **Ground the exact `npm run …` targets, script paths, data paths, and the recipe
  frontmatter on the current repo at build** — re-verify `SNICKERDOODLE.md`, `package.json` scripts,
  `recipes/`, and the lifecycle field names on disk. Terminal output shown as Onda code-blocks; the
  modeled "uncut segment" is shown as a real screen-capture beat, not a static slide.
- Course fit: this is the lighter twin of the 100-pt Mode Build and completes the Reallocation-Engine
  set — **Personal Layer** setup, **Mode Design** (25-pt paper), **Mode Build 25-pt** (this) and
  **Mode Build 100-pt** (runnable) — alongside the Computational-Skepticism set (Boondoggle, Botspeak,
  the "Audited" assignment, the "What Is Gru?" helper). Say the word and I'll stitch one **course
  index** across both courses.
