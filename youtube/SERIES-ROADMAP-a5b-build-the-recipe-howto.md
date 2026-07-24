# SERIES ROADMAP — "Build the Recipe: Make Your Tool Conductor-Ready"

A how-to ai-explainer series for **INFO 7375 Assignment 5B (Path B)** (Nik's Recipe-Based
Framework — a PDF + brand_config.json + recipe file, 100 pts, due June 19, 2026). Audience:
**students who have a working Madison tool and have never written a machine-readable config, a
conductor recipe, or defined typed phase gates.** Register: **pragmatic, step-by-step** (Liam
voice, `claude-liam`, Kokoro am_onyx). The series walks a beginner from "my pipeline runs" to
"a conductor — Claude Code, a colleague, or my future self — can run it with confidence and stop
it with judgment."

> Path note: this is the **Path B** branch (recipe/architecture). Path A (Gradio/Streamlit
> interface) is the sibling assignment. Voice: `claude-liam` per request; `claude-hai` (students
> channel) is the one-variable alternative.

## The through-line: know when to stop

Path B's entire point is **accountable AI** — a pipeline where the conductor knows exactly when
to STOP and ask a human, and why. That is the same discipline as the money hard-stop rule and
this video pipeline's own GATE P: define what GOOD looks like, define what BAD looks like, and
name the hard stop. The five judgment types ARE hard stops. Name that on camera as a rare,
hireable skill — "most people who use AI never define failure modes before they run."

## The architecture, up front (teach before building)

- **Four layers:** External sources (never trust) → `data/raw/` (ingest contract: did we get
  what we expected?) → `data/verified/` (GIGO gate: does it meet the brief's quality standard?)
  → `logs/reports/` (human review: does the output make sense for the user?).
- **Every handoff is a contract** — sourced from Conductor Brief Parts 4 (good) and 5 (bad).
- **Five judgment types (hard stops, not optional check-ins):** PA Pipeline Approval · PF
  Pipeline Failure · TO Tool Output Review · IJ Ingest Judgment · EI Exception Intervention. A
  gate that says "human reviews here" without naming the type is **incomplete** (−10 pts).

## Honesty / accuracy threads (DOUBLE-CHECK LAW)

- **Valid JSON or it's not gradeable.** brand_config.json must pass a JSON validator. The video
  shows running it through one before submit.
- **Only GIGO-passed records in `data/verified/`.** 25+ per source, no raw dumps; the README
  documents the gate AND the rejections (how many failed and why — honesty is graded).
- **Phase gates must name the judgment type** (PA/PF/TO/IJ/EI) — repeated every relevant episode.
- **Open TODOs need real blockers.** "Waiting on a DEV implementation / external access" is
  acceptable; "I haven't decided yet" is **not**.
- **Config and recipe are SEPARATE files** in Canvas (−20 each if bundled only in the PDF).
- **Couldn't verify the recipe-standardization rules or Gru docs** (recipes folder is
  robots-blocked; Gru/snickerdoodle are course-internal). Ground on the assignment's own template;
  **read `github.com/nikbearbrown/madison/tree/main/recipes` README + the Gru command reference
  at build time** and reconcile before recording. Do not invent rules.

## Series doctrine (every episode)

- **Path B is "harder to show" — so document it clearly.** No URL to demo; a JSON file and a
  recipe. The clarity IS the portfolio piece. Say it.
- **Assume zero config/recipe experience.** Define every term first time (machine-readable, JSON
  field, phase gate, GIGO, judgment type, TODO type, conductor, ingest contract). Never "just."
- **Everything maps to the Conductor Brief.** tool_summary→P1, primary_user→P2A, data_sources→P3,
  phase_gates→P4+P5, one_thing→P6B. "If a field is vague, your brief is vague — fix the brief first."
- **One deliverable per episode**, ending in the real artifact, with the paste-ready prompt that
  drafts it from the brief.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your
  Turn → title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "The brand_config.json: Your Brief as Machine-Readable JSON (Part 1, 25 pts)" (~6 min)
- **slug:** `claude-liam-a5b-01-brand-config`
- **premise:** The config is your Conductor Brief a machine can read. Every field maps to a part
  of the brief — and an empty field is a signal the brief itself is incomplete.
- **teach:** walk the schema field by field — `tool_summary` (P1), `primary_user`
  (role/situation/workaround, P2A), `data_sources[]` (name/local_path/record_type/update_freq/
  quality_gate, P3), `phase_gates[]` (step/good_looks_like/bad_looks_like/response/**judgment_type**,
  P4+P5), `one_thing` (P6B), `conductor_note` (one sentence of domain knowledge the recipe can't
  capture). Then **validate the JSON** in a validator (invalid = ungradeable). The rule: vague
  field → go fix the brief first.
- **traps:** config disconnected from the brief; missing judgment types; invalid JSON.
- **deliverable:** a valid brand_config.json. Your Turn = a prompt that maps the student's
  Conductor Brief sections into the exact config schema, then a validation check.

### E2 — "The Verified Data Folder: Prove Your Inputs Are Clean (Part 2, 20 pts)" (~5 min)
- **slug:** `claude-liam-a5b-02-verified-folder`
- **premise:** `data/verified/` is proof your inputs exist, are clean, and passed your own gate —
  not a place you dump raw API responses.
- **teach:** one subfolder per Part 3 source; **25+ verified records each** (cleaned, deduped,
  passing the stated quality gate); a **README.md** documenting each subfolder (record count, last
  update date, quality gate applied); and — the honesty beat — **records rejected and why** (how
  many failed the gate, what failed). Only GIGO-passed records; no raw, no unvalidated.
- **traps:** raw dumps; no README; records that never passed the gate; hiding the rejections.
- **deliverable:** the verified folder + README. Your Turn = a prompt that drafts the README
  (per-source counts, gate, rejection summary) from the student's A3 data.

### E3 — "Four Layers, Five Hard Stops: The Framework (primer)" (~5 min)
- **slug:** `claude-liam-a5b-03-framework-primer`
- **premise:** Before you write the recipe, understand the architecture you're writing inside —
  four layers, contracts at every handoff, and five kinds of human hard stop.
- **teach:** the four layers (External → `data/raw/` → `data/verified/` → `logs/reports/`) and
  the conductor's job at each; contracts = Brief Parts 4 & 5; the **five judgment types**
  (PA/PF/TO/IJ/EI) with a plain example of each and when it fires. Frame them as hard stops that
  encode judgment — the accountable-AI idea. This is the conceptual spine E4 depends on.
- **traps:** treating gates as optional check-ins; "human reviews here" with no type.
- **deliverable:** none — orientation. Your Turn = "for each of your four layer transitions, name
  which of the five judgment types applies and why."

### E4 — "Write the Recipe: The Conductor's Score (Part 3, 25 pts)" (~7 min)
- **slug:** `claude-liam-a5b-04-write-recipe`
- **premise:** The recipe is a plain-language document a conductor who's never seen your project
  can pick up and run — not pseudocode, not a flowchart.
- **teach:** **read the recipe-standardization rules first** (recipes-folder README) — recipes
  that don't follow them aren't machine-readable. Then the template: **executive summary** (3–5
  sentences: what it does, who runs it, how often, what a successful run produces); **one step per
  layer**; a **typed phase gate after each layer transition** (good-looks-like from P4,
  bad-looks-like from P5, response = hard stop/flag/log, and the **judgment type**); the **five
  TODO types** (DATA SOURCE, DEFINE, DEV, APPROVE, REPORT FIELD) for anything unresolved; and the
  **conductor note** (a paragraph on what the human must watch for).
- **traps:** steps with no phase gates; gates missing judgment types (−10); pseudocode instead of
  plain language; ignoring the standardization rules.
- **deliverable:** the recipe file (`.md`/`.txt`). Your Turn = a prompt that turns the
  brand_config + brief into a first-draft recipe in the template, with TODOs typed.

### E5 — "Run /snickerdoodle: Audit and Close Your TODOs (Part 4, 10 pts)" (~5 min)
- **slug:** `claude-liam-a5b-05-snickerdoodle`
- **premise:** /snickerdoodle is a prompt factory in Gru that hands you a Claude Code agent prompt
  to audit and harden your recipe. A well-written brief means fewer TODOs to close here.
- **teach:** the three-step workflow — (1) run **/snickerdoodle** in Gru with a plain-language
  pipeline description (3–5 sentences) → it outputs a **Claude Code agent prompt**; (2) paste that
  into **Claude Code** → it audits your recipe and adds **typed TODO items**; (3) bring the
  annotated recipe back and run **/claude** in Gru when TODOs are closed → Gru confirms it's
  ready. Document the description you used, every generated TODO, the **resolved** ones (with the
  decision), and any **open** ones (with a real blocker — never "haven't decided"). Re-verify the
  current Gru command reference at build; if the tool moved, reconcile.
- **traps:** section missing or described-not-documented; open TODOs with no blocker; skipping the
  /claude confirmation.
- **deliverable:** the documented /snickerdoodle run. Your Turn = a prompt that drafts the 3–5
  sentence pipeline description /snickerdoodle needs from the brand_config.

### E6 — "Ship It: Three Canvas Submissions" (~4 min) — closer
- **slug:** `claude-liam-a5b-06-assemble-submit`
- **premise:** Three separate files, specific names, big deductions if you bundle them wrong.
- **teach:** the submission-checklist pass (valid config, verified folder + README appendix, recipe
  with all four layers and typed gates, documented /snickerdoodle run, PDF with all four parts +
  appendices in order); submit **three** items — the **PDF**
  (`LastName_FirstName_A5B_BuildTheRecipe.pdf`), the **`brand_config.json`** as a separate file,
  and the **recipe** (`recipe_[LastName].md`/`.txt`) as a separate file. Read the deductions on
  camera (−20 config not separate, −20 recipe not separate, −10 gates missing judgment types,
  −15 any section missing). Where it goes: the config + recipe are portfolio proof of accountable-
  AI design.
- **deliverable:** the three submissions. Your Turn = "run your brand_config.json through a JSON
  validator and read your recipe to someone who's never seen the project — if they couldn't run
  it, that's your revision list."

---

## Tight cut

Five-episode version: brand_config (E1) · Verified folder (E2) · Framework primer + recipe in one
(E3+E4) · /snickerdoodle (E5) · Ship (E6). The 6-episode cut is better because the four-layer /
five-judgment-type framework is the hardest conceptual leap and beginners write typeless gates
without the primer.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `<course-book>/youtube/`
  (or `brutalist-art/youtube/` — tell me the owning book slug).
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals →
  QC → BUILD-PROMPT.md. **Before building E4/E5, read the recipes-folder standardization rules and
  the Gru /snickerdoodle + /claude reference** (I couldn't reach them — robots-blocked/internal) and
  reconcile the template + command flow with what's current.
- Series index: A1, A2, A3, A4, A5, A5A, A5B (this), A8 are now mapped. A5A and A5B are the two
  A5 forks. Remaining to complete the set: A6 (brand identity) and A7 (visual identity). Say the
  word and I'll finish the master INFO 7375 series index.
