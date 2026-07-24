# SERIES ROADMAP — "Wrap It & Test It: Interface, Users, Positioning"

A how-to ai-explainer series for **INFO 7375 Assignment 5A (Path A)** (Interface, User Testing,
and Market Positioning — one PDF + a live public interface, 100 pts, due June 19, 2026). Audience:
**students who have a working Madison tool and have never built a Gradio/Streamlit UI, deployed
to a public URL, or run a structured user test.** Register: **pragmatic, step-by-step** (Liam
voice, `claude-liam`, Kokoro am_onyx). The series walks a beginner from "my tool runs in n8n /
a script" to "a stranger can open a URL and use it — and I learned what to fix by watching them."

> Path note: this is the **Path A** branch (interface). Path B (the recipe / brand_config) is a
> separate assignment. Voice: `claude-liam` per request; `claude-hai` (students channel) is the
> one-variable alternative.

## The line that runs through the whole series

**"The interface is not the product. The learning is the product."** Every episode points at the
real goal: make the tool usable by someone who isn't you, then find out — honestly — what breaks
when they touch it. Grades reward real confusion honestly reported, not "everyone loved it."

## Honesty / craft threads (DOUBLE-CHECK LAW) — this assignment is built on them

- **The user test must be REAL.** Three real users who match the Part 2 persona — **not
  classmates, not family, not you** (−10 each). "If your report says everyone understood
  everything immediately, we have questions." The video teaches recruiting the closest honest
  match, running a think-aloud, and reporting genuine confusion. This is the don't-fake-your-data
  ethic (A3/A4) applied to UX research.
- **The revised one-thing must actually change.** Identical to the original = you didn't learn
  anything (a named pitfall). The revision must cite what the test revealed.
- **Human output, never JSON** (carryover from A4): the interface shows something a non-technical
  user can read and act on, not a dataframe or an API blob.
- **Public and working at submission.** Deployed to a real URL (Hugging Face Spaces / Streamlit
  Community Cloud) that opens right now — broken/missing URL is −20.
- **Positioning axes must be real.** They reflect what the Part 2 user actually cares about, not
  two vague or identical dimensions.
- Re-verify Gradio/Streamlit + the deploy platform UI at build time; interface screens are
  REBUILT natively (REBUILD LAW), not screen-grabbed.

## Series doctrine (every episode)

- **Assume zero UI/deploy experience.** Define every term first time (Gradio, Streamlit, widget/
  component, deploy, public URL, empty/error state, think-aloud test, positioning matrix, white
  space). Never "just."
- **One deliverable per episode**, ending in the real artifact (a running app, a documented test,
  a matrix), with the paste-ready prompt that starts it.
- **Everything traces to the Conductor Brief.** Inputs come from Part 3 (data contract), outputs
  from Part 4, the user from Part 2, the one-thing from Part 6. Say it each episode.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your
  Turn → title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "Wrap It in a UI: Build a Gradio or Streamlit Interface (Part 1, build)" (~7 min)
- **slug:** `claude-liam-a5a-01-build-interface`
- **premise:** Your tool works — but only for you, in code. An interface is the box a stranger
  can drive without ever seeing the engine.
- **teach:** pick **Gradio** vs **Streamlit** (Gradio = fastest for input→output tools, great on
  HF Spaces; Streamlit = more layout control — a 20-second decision, don't shop); wire the
  **input fields** from the Part 3 data contract with clear labels; call your Madison tool; render
  a **human-readable output** (formatted text/table/chart/file — never a JSON blob); add
  **plain-English error handling** (a friendly message, not a stack trace). The test: *could my
  Part 2 user finish a task without me in the room?*
- **traps:** JSON output; cryptic errors; inputs a non-technical user can't understand; a local
  notebook.
- **deliverable:** a working local interface. Your Turn = a prompt that scaffolds a Gradio/
  Streamlit app around the student's tool with labeled inputs and a human-readable output.

### E2 — "Deploy It Public + Document It: URL, Walkthrough, 3 Screenshots (Part 1, ship)" (~6 min)
- **slug:** `claude-liam-a5a-02-deploy-and-document`
- **premise:** "Works on my machine" is worth zero here. Get it onto a public URL, then document
  it the way the rubric asks.
- **teach:** deploy to **Hugging Face Spaces** (Gradio) or **Streamlit Community Cloud** — the
  push/connect flow, the requirements file, getting the live URL; confirm it opens for someone
  else. Then the **1A walkthrough** (300–400 words: each input field + why it matters, the output
  display + why that format, **one design decision** and why for your Part 2 user, and the error
  handling with an example). Then the **1B screenshots**: empty state (does it explain itself?),
  completed run (real output), error state (the actual plain-English message).
- **traps:** broken URL at submission (−20); a missing requirements file; screenshots of JSON.
- **deliverable:** the public URL + walkthrough + three screenshots. Your Turn = a prompt that
  drafts the interface walkthrough from the deployed app's real fields and output.

### E3 — "Run a Real User Test: Three Strangers, Think-Aloud (Part 2, 25 pts)" (~7 min)
- **slug:** `claude-liam-a5a-03-user-test`
- **premise:** This is the part students fake — and the graders can tell. A real test produces
  confused users and at least one thing you didn't anticipate. That's the gold.
- **teach:** recruit **3 real users** who match the Part 2 persona (**not classmates/family/you**;
  if no exact match, find the closest and note the gap — that's honest work); the protocol — hand
  them the URL, say only "I'd like to watch you use it and hear your thinking," ask them to
  **think aloud**, take notes on **where they pause, re-read, ask**; the four end questions (what
  did it help you do / what confused you / would you use it again / why); **do not defend it —
  listen.** Document each tester honestly (role, what they actually did in order, where they got
  confused, an end quote). Then make **at least one change** driven by feedback — OR a defended
  decision NOT to change (holding the line, with the reason, scores well).
- **traps:** testing classmates/family (−10); "everyone loved everything"; defending instead of
  listening; no change decision.
- **deliverable:** three documented sessions + a change (or defended non-change). Your Turn = a
  prompt that turns raw test notes into the structured per-tester report + a change decision.

### E4 — "The Positioning Matrix: Find Your White Space (Part 3A, 12 pts)" (~5 min)
- **slug:** `claude-liam-a5a-04-positioning-matrix`
- **premise:** A 2×2 that shows where you sit and where nobody else does — with axes that matter
  to YOUR user, not generic ones.
- **teach:** pick **two axes** that reflect the Part 2 user's real priorities (ease vs. depth,
  cost vs. speed, technical barrier vs. output quality, specialist vs. generalist); place your
  **three A5/Conductor-Brief competitors** and **your tool**, each with a reason; name the **white
  space** — the open position you claim and why it exists / why competitors don't occupy it. Draw
  the diagram (hand-drawn + photographed is fine — "the diagram is required; the polish is not").
- **traps:** vague or identical axes; placements with no reasoning; no diagram (−8).
- **deliverable:** the positioning matrix + white-space statement. Your Turn = a prompt that
  proposes two user-relevant axes and places all four tools with justification to refine.

### E5 — "Sharpen the One-Thing with What You Learned (Part 3B, 13 pts)" (~5 min)
- **slug:** `claude-liam-a5a-05-refined-one-thing`
- **premise:** Your Conductor Brief guessed your differentiator. The user test either confirmed
  it, killed it, or handed you a better one. Revise honestly.
- **teach:** paste the **original one-thing** (Conductor Brief Part 6B); state **what the test
  revealed** (confirmed? contradicted? a different differentiator surfaced? — be honest); write
  the **revised statement** in the formula ("the only [category] that [capability] for [user]
  without [barrier]"); explain **why the revision matters**, tied to specific tester feedback. If
  the test changed nothing, that's a red flag — push on whether you really listened.
- **traps:** revised = identical to original (means no learning); revision not tied to test evidence.
- **deliverable:** the revised one-thing with evidence. Your Turn = a prompt that takes the
  original claim + the test findings and drafts a sharper, evidence-backed differentiator.

### E6 — "Assemble & Ship the PDF" (~4 min) — closer
- **slug:** `claude-liam-a5a-06-assemble-submit`
- **premise:** One PDF, a live URL that must still work, specific deductions.
- **teach:** the submission-checklist pass (working public URL, 300–400 word walkthrough, three
  screenshots, three test sessions, a change decision, the matrix diagram, the revised one-thing);
  confirm the **URL still opens** right before submitting; assemble one **PDF** named
  **`LastName_FirstName_A5A_WrapYourTool.pdf`** (PDF only); read the deductions on camera
  (−20 broken URL, −10 fewer than 3 testers, −10 classmate/self testers, −8 no matrix, −15 any
  section missing). Where it goes next: this feeds A6 (naming + brand identity).
- **deliverable:** the submitted PDF. Your Turn = "open your public URL in a private browser
  window — if it doesn't load for a stranger, that's your one fix before you submit."

---

## Tight cut

Five-episode version: Build (E1) · Deploy+document (E2) · User test (E3) · Positioning matrix +
one-thing in one (E4+E5) · Assemble (E6→folded). The 6-episode cut is better because Part 3's two
halves are separately graded (12+13) and the revised one-thing needs its own beat to land the
"it must actually change" rule.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `<course-book>/youtube/`
  (or `brutalist-art/youtube/` — tell me the owning book slug).
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals →
  QC → BUILD-PROMPT.md. Re-verify Gradio/Streamlit + HF Spaces/Streamlit Cloud UI at build time.
- Series index: A1, A2, A3, A4, A5, A5A (this), A8 are now mapped. A5A is the Path A fork of A5
  and feeds A6 (brand identity). Remaining to complete the set: A5B (Path B), A6, A7. Say the word
  and I'll finish the master INFO 7375 series index.
