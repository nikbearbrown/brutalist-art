# SERIES ROADMAP — "Say What It Is: The Conductor Brief"

A how-to ai-explainer series for **INFO 7375 Assignment 5** (The Conductor Brief — one strategy
PDF, 100 pts, due June 12, 2026). Audience: **students who have built a tool over four weeks but
have never written a positioning brief or a jargon-free value sentence.** Register: **pragmatic,
step-by-step** (Liam voice, `claude-liam`, Kokoro am_onyx). The series walks a beginner from "I
have a working prototype" to "a smart person who's never seen my PRD understands exactly what
this is, who it's for, and why it wins."

> Voice/channel note: `claude-liam` per request (Liam, @NikBearBrown). `claude-hai` (students
> channel) is the one-variable alternative.

## What makes this series different from A2–A4

- **No code.** This is a WRITING assignment. Every episode is about making a sentence specific,
  a claim defensible, a criterion actionable. The tool here is Claude-as-drafting-partner (the
  assignment lists claude.ai as a resource) — draft with it, then sharpen by hand.
- **It synthesizes, not restarts.** Pull directly from A1 (context), A2 (PRD), A3 (data), A4
  (intelligence). The brief *translates* those into strategic language. Every episode says
  "open your A[n] and pull X."
- **It feeds everything downstream.** Part 1 → interface + headline; Part 3 → brand_config.json;
  Parts 4–5 → phase gates + GIGO; Part 6 → A6 positioning + the final pitch. Say this so students
  write it like it matters, because it does.

## The through-line: good / bad / hard-stop

Parts 4, 5, and 6 are the same discipline the whole course (and this video pipeline) runs on —
define what GOOD looks like, define what BAD looks like, and know when to **hard stop** vs. flag
vs. log-and-continue. That's a phase gate. Name it on camera as a transferable skill, not just an
assignment section.

## Honesty / craft threads (DOUBLE-CHECK LAW)

- **Part 1 has no partial credit for "almost clear."** The read-aloud test is the whole method:
  read it to someone who's never heard of the project — "oh, that's useful" = close; "what does
  that mean?" = rewrite. Teach the test, not a magic formula.
- **Part 6 requires SOURCES.** Competitive claims need evidence — tried it / watched the demo /
  G2 or Product Hunt reviews. "No sources cited" is a named pitfall. Same no-fluff, cite-it
  discipline as the connector reels.
- **The differentiator must be DEFENSIBLE.** "We use AI / we're cheaper / we're easier" don't
  count — the video shows why, and how to find a claim a competitor can't copy in a week.
- **Honest current-state (Part 2A).** Describe the real workaround and its real cost, not a
  strawman. Honesty is graded.

## Series doctrine (every episode)

- **Assume zero brief-writing experience.** Define every term first time (value proposition,
  user story, data contract, phase gate, GIGO, differentiator, positioning). Never "just."
- **One section per episode**, ending in the filled-in brief section, with the paste-ready
  Claude prompt that drafts it from the student's A1–A4 material — then the sharpening pass.
- **Every section traces back to Part 1.** The coherence test in each episode: does this connect
  to the one sentence?
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your
  Turn → title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "The Hardest Sentence: Your Tool in One Line (Part 1, 12 pts)" (~5 min)
- **slug:** `claude-liam-a5-01-one-sentence`
- **premise:** One sentence decides your grade, your brand, your LinkedIn headline, and your
  pitch. Get this and everything downstream gets easier; rush it and you rewrite it four times.
- **teach:** the "single most important thought" idea; the formula — **[Tool] helps [specific
  user] [specific action] so they can [specific outcome]**; the three worked examples;
  the weak-sentence tells (describes tech not outcome, lists features, "leverages/utilizes/
  AI-powered," written for a developer); the **read-aloud test**. Draft with Claude, then cut
  every word that isn't the user or the outcome.
- **traps:** tech description (-5 pts and a rewrite before A6); feature list; jargon.
- **deliverable:** the one sentence. Your Turn = a prompt that takes the A2 problem + A4 output
  and drafts five candidate sentences in the formula, then the read-aloud test to pick one.

### E2 — "Name the Human: User + Problem + 3 Stories (Part 2, 16 pts)" (~6 min)
- **slug:** `claude-liam-a5-02-user-and-stories`
- **premise:** "Marketers" isn't a user. Name the situation — the exact person, mid-task, and
  the workaround that almost works.
- **teach:** **2A** — primary user (job title/role), their situation (what they're doing when
  they reach for this), what they do instead right now (the workaround/manual process), and why
  that's not good enough (time/money/errors/missed opportunity — honest). **2B** — three user
  stories in the exact format "As a [specific role], I want [real capability] so that [human
  outcome]": core job, secondary use case, power-user edge case. Roles must be real (never
  "user"); outcomes human, not technical.
- **traps:** generic user; stories in non-standard format (-5 pts); technical "outcomes."
- **deliverable:** the user profile + three stories. Your Turn = a prompt that turns the A2 user
  + A4 capabilities into a filled user profile and three correctly-formatted stories.

### E3 — "The Data Contract: What Your Inputs Actually Mean (Part 3, 12 pts)" (~5 min)
- **slug:** `claude-liam-a5-03-data-contract`
- **premise:** A data contract is a promise: this goes in, this is what it means, this is how we
  know it's good enough. Translate your A3 sources from file formats into human meaning.
- **teach:** for each A3 source — name; what it IS (file type, record count, update frequency);
  what it REPRESENTS in plain English (what the data means for the user's problem, not the schema);
  how we know it's good (a checkable **quality standard** — "every record has a date, a source
  URL, and 20+ words," not "the data is good"); the local path (`data/verified/…`). Note this
  becomes `brand_config.json` in 5B.
- **traps:** describing the file instead of the meaning; "the data is good" (not a standard).
- **deliverable:** the data contract. Your Turn = a prompt that converts the A3 inventory into
  plain-English "what it represents" + a checkable quality standard per source.

### E4 — "What Good Looks Like: Your Phase Gates (Part 4, 12 pts)" (~5 min)
- **slug:** `claude-liam-a5-04-good-looks-like`
- **premise:** A phase gate is a human checkpoint. At each step, what does a correct, trustworthy
  output actually look like — specifically enough to make a yes/no call?
- **teach:** write a "good looks like" for **3+ steps** — data ingestion (what's true about the
  raw data), validation / the GIGO gate (what must be true before tools read it), AI processing
  (what the output contains, what makes you trust it), final output (what a non-technical user can
  understand and act on). Specific beats "the output looks right." This IS your phase-gate
  criteria — the same discipline this pipeline's own GATE P uses.
- **traps:** vague criteria you can't act on; skipping the validation gate.
- **deliverable:** 3+ "good looks like" statements. Your Turn = a prompt that drafts actionable
  good-criteria for each step of the student's pipeline.

### E5 — "What Bad Looks Like: The GIGO Layer + When to Hard Stop (Part 5, 12 pts)" (~5 min)
- **slug:** `claude-liam-a5-05-bad-looks-like`
- **premise:** The mirror of Part 4. What does garbage look like for YOUR tool — and what happens
  when it shows up? Knowing when to hard-stop is a real skill, not a formality.
- **teach:** write a "bad looks like" for **3+ steps**, each with a **trigger** and a **response**
  — **hard stop** / **flag for review** / **log and continue** — and WHY that response. Ingestion
  (what makes raw data dangerous to build on), validation (patterns that signal a cleaning
  problem), AI (output wrong enough to mislead the user). Frame hard-stop honestly: some failures
  must stop the line, not get logged and ignored — the same instinct behind the money hard-stop
  rule (know the one door that shouldn't swing on autopilot).
- **traps:** failure modes with no response; treating every error as "log and continue."
- **deliverable:** 3+ failure modes with triggers + responses. Your Turn = a prompt that lists
  the garbage-input/output patterns for the student's tool and assigns each a stop/flag/log response.

### E6 — "The One Thing: Your Defensible Differentiator (Part 6, 16 pts)" (~6 min)
- **slug:** `claude-liam-a5-06-the-one-thing`
- **premise:** One defensible claim — the thing no direct competitor does quite the same way for
  your specific user. Not a feature list. This becomes your A6 positioning and your pitch.
- **teach:** **6A** — three competitors, each with an honest "what they do well," a specific gap
  "for our user," and a **source** (tried it / demo / G2 / Product Hunt); then the gap all three
  share. **6B** — the formula: **"the only [category] that [specific capability] for [specific
  user] without [the barrier competitors impose]"**; why it matters (tie back to the Part 2 user);
  why it's defensible (can't be copied in a week). The weak-one-thing tells (AI / cheaper / easier
  / a feature list).
- **traps:** a claim any tool could make; no sources (named pitfall); feature list.
- **deliverable:** three sourced competitor analyses + one defensible differentiator. Your Turn =
  a prompt that pressure-tests a draft differentiator against "could a competitor copy this in a
  week?" and rewrites it until the answer is no.

### E7 — "Assemble & Ship the Brief" (~4 min) — closer
- **slug:** `claude-liam-a5-07-assemble-submit`
- **premise:** Six sharp sections don't help if they don't connect — or if the file's named wrong.
- **teach:** the **coherence pass** (does every section trace back to Part 1? do the stories match
  the user? does the one-thing solve the stated problem?); assemble into one **PDF**, named
  **`LastName_FirstName_A5_ConductorBrief.pdf`** (PDF only); read the deductions on camera
  (-15 any section missing, -5 non-standard stories, -5 tech-not-value Part 1). Then "where this
  goes next" — Part 1 → 5A interface + headline; Part 3 → 5B brand_config.json; Parts 4–5 → phase
  gates + GIGO; Part 6 → A6 positioning + pitch.
- **deliverable:** the submitted PDF. Your Turn = "read your Part 1 sentence to someone who's never
  seen the project; if they don't say 'that's useful,' that sentence is your one revision before
  you submit."

---

## Tight cut

Five-episode version: One sentence (E1) · User + stories (E2) · Data contract (E3) · Good & bad
in one phase-gate episode (E4+E5) · One thing + assemble (E6+E7). The 7-episode cut is better
because Parts 4 and 5 are separately graded (12+12) and beginners write vague criteria when the
two are blurred.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `<course-book>/youtube/`
  (or `brutalist-art/youtube/` — tell me the owning book slug).
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals →
  QC → BUILD-PROMPT.md.
- Series index: A1 (foundation), A2 (PRD), A3 (data), A4 (intelligence), A5 (this — strategy),
  A8 (launch) are now mapped. A5 explicitly feeds 5A/5B and A6. Say the word and I'll fill the
  remaining gaps (5A, 5B, A6, A7) into one master INFO 7375 series index.
