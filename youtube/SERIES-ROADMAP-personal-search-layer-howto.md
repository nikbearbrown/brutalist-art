# SERIES ROADMAP — "Attest Your Own Record: The Search Personal Layer"

A how-to ai-explainer series for **The Reallocation Engine — Setup Exercise: Your Search's Personal
Layer** (three files in a `search/` folder + a RUN_LOG entry + AI Use Disclosure, in your forked
repo, 25 pts = 20 mechanics + 5 depth). Audience: **international students / early-career technical
workers building their personal data layer for the first time, on a real OPT clock.** Register:
**pragmatic how-to with a skeptical edge** (Liam voice, `claude-liam`, Kokoro am_onyx). Four
episodes. The series walks a student from "the engine's scores are generic" to "three attested files
that make every score operate on my actual situation — and that I can defend in an interview."

> Voice: `claude-liam` per request. Build into `the-reallocation-engine/youtube/`, or
> `brutalist-art/youtube/` — tell me the owning book slug. Pairs with the Mode Design assignment.

## The one principle this exercise runs on

**The agent does the extraction, drafting, and formatting; you do the attesting, correcting, and
signing.** A file the agent built but you never questioned is not a verified record — it is *fluency
wearing the costume of evidence*, the exact failure mode this course exists to catch. This is the
whole course's skepticism turned inward on the one dataset you know better than any model: your own.

## Why it's the course material, not a metaphor (say it in E1 and E4)

- The **attestation pass** on `resume.json` **is a bias audit**.
- The **evidence requirement** in `gaps.md` **is the verified-data contract**.
- The **visa section** in `profile.yml` **is a gate definition** (a wrong gate produces Apply
  recommendations for roles you cannot legally take).
- The **killed gap row** is a **false positive you caught with domain knowledge the agent lacked**.
The discipline is identical to validating a model on an external dataset. The stakes, on a 90-day
OPT clock, are higher.

## Honesty / privacy threads (DOUBLE-CHECK LAW)

- **Privacy first.** `search/private-notes.md` is gitignored — honest self-assessments and raw gap
  admissions live there; everything else in `search/` is written knowing a stranger may read it. The
  videos never ask a student to expose sensitive info publicly.
- **Find real errors, not formatting fixes.** At least three in `resume.json` — a shifted date, a
  quietly promoted title, a skill inferred from a course you barely passed, a "led" that was
  "one of five." "Look harder — they're there."
- **Mark STEM eligibility UNCERTAIN if your DSO hasn't confirmed it.** Don't assert a gate the engine
  will treat as legally binding.
- **Evidence over feelings.** Every gap cites a posting, an O*NET requirement, or a pattern across
  three postings. "A gap with no evidence is a feeling, not a finding — feelings go in private-notes."
- **Plans are outputs, not activities.** "Take a course" fails; a gap closes when *someone else* can
  verify it — a shipped project, a published piece, a credential from an external issuer.
- **The killed row needs a real critique**, not a diplomatic "not relevant" — name what the agent got
  wrong about *your* situation.
- **The AI Use Disclosure "What the AI could not do" is a specific instance**, not "AI drafted, I
  reviewed" — one thing the agent got wrong about your situation that took your knowledge to catch.

## Series doctrine (every episode)

- **Assume no prior repo/data-hygiene experience.** Define every term first time (fork, gitignore,
  attestation, structured record vs. prose, gate, OPT/STEM/DSO, O*NET, SOC code, evidence column,
  RUN_LOG). Never "just."
- **One artifact per episode**, ending in the real file, with the paste-ready agent prompt that
  drafts the first pass — then the attestation/correction pass that is the actual assignment.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your Turn
  → title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "Extract & Attest Your Résumé: Find the Three Errors (Steps 0–1)" (~6 min)
- **slug:** `claude-liam-psl-01-resume-attest`
- **premise:** The centerpiece. The agent will extract your résumé fluently — and get things wrong
  about your own past. Catching those is the assignment, not overhead.
- **teach:** why the personal layer matters (without it every score is generic; with it the
  sponsorship tier, fit score, timeline factor, and Apply/Consider/Skip operate on *your* situation);
  **Step 0 privacy** (`mkdir -p search`; gitignore `search/private-notes.md`); **Step 1 extract** —
  point the agent at your résumé (PDF/docx/LinkedIn export) → `search/resume.json` as **structured
  records with typed fields**, one entry per job/degree/skill/cert, not pasted prose; then the
  **attestation pass** — find at least three things the import got wrong (a date, a promoted title,
  an inferred skill, a solo-claim that was a team), fix them, and add the `attested / attested_date /
  attestation_note` block. "Extraction is fluent; you are the source of truth."
- **traps:** prose instead of typed fields; "no errors found" (look harder); trivial formatting fixes
  passed off as attestation; committing private notes.
- **deliverable:** an attested `resume.json` + the three-error note. Your Turn = "have the agent
  extract, then find the three things it got wrong about *your* past — a promoted title is the most
  common; it's in there."

### E2 — "Your Profile: Facts, Not Aspirations (Step 2, profile.yml)" (~5 min)
- **slug:** `claude-liam-psl-02-profile`
- **premise:** The profile is where a hopeful assumption becomes a wrong gate. Answer the intake as
  facts, then correct any drift toward what sounds good.
- **teach:** the intake answered as facts — **target role** specific enough to drive the scorer
  ("data scientist at a biotech startup," not "something in tech"); **visa & timeline** (type, auth
  end date, OPT unemployment days used, **STEM eligibility marked "uncertain" until your DSO
  confirms**, an 80-day buffer target); **geography** honest about real constraints; **industry &
  size** with hard exclusions; **sponsorship requirement stated explicitly as a gate** (no
  sponsorship history → skip-regardless of fit). Review the draft and correct anything that drifts
  toward flexibility you don't actually have — a false flexibility produces Apply recs for roles you
  can't take.
- **traps:** a vague target role; STEM asserted without DSO confirmation; claimed flexibility you
  lack; sponsorship left implicit.
- **deliverable:** `profile.yml` with real dates + an explicit sponsorship gate. Your Turn = "fill the
  visa section from your actual documents; if any line reflects a hope instead of a document, mark it
  uncertain."

### E3 — "gaps.md: Evidence, Not Feelings (Step 3)" (~6 min)
- **slug:** `claude-liam-psl-03-gaps`
- **premise:** The gap table is where discipline shows. Every gap grounded in something checkable,
  every plan an output someone else can verify — and two edits that prove you read your own situation.
- **teach:** the agent drafts the table (**Gap · Evidence the target demands it · What I have · Plan
  to close it**) by comparing the attested `resume.json` against the `profile.yml` target; the
  **evidence column** must cite a real posting, an O*NET requirement for the target SOC, or a pattern
  across three postings ("a gap with no evidence is a feeling — feelings go in private-notes.md");
  the **plan column** must be a **verifiable closing condition** (a shipped project / published piece
  / external credential — not "take a course"); then the two required edits — **kill one wrong row**
  (with a real critique of what the agent got wrong about your situation) and **rewrite one row in
  your own words**. `gaps.md` is a place things *leave* — a closed gap becomes a new `resume.json`
  entry.
- **traps:** gaps sourced to the agent's confident inference; plans that are activities not outputs;
  a killed-row reason that's diplomatic ("not relevant") instead of a critique.
- **deliverable:** `gaps.md` with a killed row (explained) + a row in your own voice. Your Turn = "for
  your top gap, find the posting or O*NET line that proves the target demands it — if you can't, it's
  a feeling, and it goes in private-notes."

### E4 — "The Verification Check, Log It & Ship (Steps 4–5 + Disclosure)" (~5 min)
- **slug:** `claude-liam-psl-04-verify-log-ship`
- **premise:** Last pass — turn the course's skepticism on your own three files, log it honestly, and
  submit the fork.
- **teach:** the **verification check** answered honestly in RUN_LOG — is every `resume.json` entry
  traceable (or did the agent promote a title / extend a date / add an undefendable skill)? does the
  `profile.yml` visa section reflect your actual documents (STEM → "uncertain" if unconfirmed)? does
  every `gaps.md` evidence cell cite something real (or did the agent invent the demand signal from
  training data — the verified-data contract violation applied to your own career)? Then the
  **RUN_LOG entry** (the three files, the three attestation errors, the top gap, the killed row + why,
  the `profile.yml` field you corrected — no `private-notes` contents); the **AI Use Disclosure** with
  a **specific "What the AI could not do"** (one thing the agent got wrong about your situation);
  submit the forked repo link to Canvas.
- **traps:** a verification check that rubber-stamps; a disclosure that describes a workflow not a
  judgment; leaking private notes into the log.
- **deliverable:** the RUN_LOG entry + disclosure + submitted fork. Your Turn = "answer the three
  verification questions out loud — the one you hesitate on is the one the agent got away with; go fix
  that file before you push."

---

## Tight cut

Three-episode version: Extract+attest+profile (E1+E2) · gaps.md (E3) · Verify+log+ship (E4). The
4-episode cut is better because the attestation pass and the evidence-not-feelings discipline are the
two conceptual keys, and each is where students most often let the agent's fluency stand unquestioned.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `the-reallocation-engine/youtube/`
  (or `brutalist-art/youtube/` — tell me the owning book slug). Privacy note: demos use a *fictional*
  résumé/profile on screen — never real student PII.
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals → QC →
  BUILD-PROMPT.md. Ground the file schemas (`resume.json` fields, `profile.yml` keys, `gaps.md`
  columns, RUN_LOG format) on the current repo at build (device bridge offline — re-verify on disk).
- Course fit: this setup exercise + the Mode Design assignment now form the Reallocation-Engine pair,
  alongside the Computational-Skepticism set (Boondoggle Report, Botspeak Prompt Adaptation, the
  Reallocation Engine "Audited" assignment, and the "What Is Gru?" helper series). Say the word and
  I'll stitch a single **course index** across both courses.
