# SERIES ROADMAP — "Make It Smart: Add Intelligence & Prove It Scales"

A how-to ai-explainer series for **INFO 7375 Assignment 4** (Scale Your Thing & Add
Intelligence — an enhanced n8n workflow + real outputs + scale test + Figma package, 100 pts,
due June 5, 2026). Audience: **students who built the A3 data pipeline and have never added an
AI node, produced a real output, or stress-tested a workflow.** Register: **pragmatic,
step-by-step** (Liam voice, `claude-liam`, Kokoro am_onyx). The series walks a beginner from
"my A3 workflow collects data" to "it does something smart, produces something a human can use,
and I know exactly where it breaks."

> Voice/channel note: `claude-liam` per request (Liam, @NikBearBrown). `claude-hai` (students
> channel) is the one-variable alternative.

## The one rule that runs through the whole series

**Raw JSON is NOT an output.** If understanding it requires opening n8n or parsing JSON, it's
not done. The test in every relevant episode: *could a non-technical person use this?* Say it
often — the assignment docks **-25 points** for JSON-only outputs.

## Honesty / accuracy threads (DOUBLE-CHECK LAW)

- **Honest scale testing, not aspirations.** The assignment penalizes fake scale testing
  **-20 points** ("It should handle 1000 requests" with no evidence). The video teaches actually
  running 50+ requests on TEST data, measuring real times, and documenting real breaking points —
  including an honest "No, it can't run 24/7 because…". This is the no-marketing-fluff lesson.
- **Test/sandbox accounts only for any posting.** Test Twitter, test email, local files — never
  a real account, never spam, never anything that breaks a platform's rules. File outputs
  (PDF/HTML/CSV/chart image) are the safe default the video should recommend first. (Same
  get-blocked reality as the A3 Tier-3 list and the connector reels.)
- **AI calls cost money — so the scale test computes real cost.** "Cost per 100 requests,"
  "monthly cost at 1000/day." Good place to remind: it's a paid AI service; store keys in n8n
  credentials, watch spend, and if any node is wired to *buy* something, that's a human hard stop
  (ties to the money hard-stop rule).
- **"Intelligence" must actually reason, not reformat.** AI that just re-words text doesn't earn
  Part 1; the video shows the difference (analyze → decide/generate/route), not a paraphrase node.
- Everything runs on the student's OWN machine (localhost:5678); the video never implies cloud.
- Re-verify n8n's current AI/error-node names and the AI service's UI at build time; workflow
  screens are REBUILT natively (REBUILD LAW), not screen-grabbed.

## Series doctrine (every episode)

- **Evolution, not revolution.** You're upgrading A3, not rebuilding it. Every episode references
  the A3 workflow and shows the *before/after* improvement.
- **Assume zero AI-node experience.** Define every term first time (AI node, prompt, token, error
  branch, retry/backoff, stress test, throughput, exec summary, architecture diagram). Never "just."
- **One deliverable per episode**, ending in a real artifact, with the paste-ready prompt that
  starts it. Excellence is competitive — state it plainly.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your
  Turn → title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "Add the Smarts: One AI Node That Reasons (Part 1, 20 pts)" (~7 min)
- **slug:** `claude-liam-a4-01-add-intelligence`
- **premise:** The whole assignment turns on one honest question — does your workflow now
  *decide, analyze, or generate*, or does it just move data? Add ONE AI capability that clearly
  does the former.
- **teach:** open the A3 workflow; add ONE AI node (an AI/LLM node or HTTP Request to an AI
  service, key in credentials) that TRANSFORMS or ACTS on the data — sentiment/archetype
  detection, pattern/trend analysis, insight generation, or routing to different outcomes. Write
  a good prompt for it. Document what the AI **learns, decides, or produces**. Show the
  before/after vs A3. The line to hold: real reasoning, not "reformat this text."
- **traps:** AI that just paraphrases; complexity without intelligence; key hard-coded in the node.
- **deliverable:** the enhanced workflow with one smart node. Your Turn = a prompt that turns the
  student's A3 data + A2 problem into a specific AI task (input → decision/output) worth adding.

### E2 — "Handle It Gracefully: Errors That Don't Crash the Workflow (Part 1 error req)" (~5 min)
- **slug:** `claude-liam-a4-02-error-handling`
- **premise:** Real intelligence includes failing well. When the AI times out or returns garbage,
  the workflow should bend, not break.
- **teach:** the three n8n options (an **error workflow**, **On-Error branches** on critical
  nodes, or **try/catch in a Function node**); the patterns — **retry with exponential backoff**,
  **log the error and continue with the next item**, **notify + pause**. What to guard: API rate
  limits/timeouts, missing/invalid data, malformed AI responses, network issues. Fill the
  error-handling doc table (what could go wrong / how we handle it).
- **traps:** no error handling (-10 pts); a workflow that dies on one bad record; undocumented.
- **deliverable:** error branches + the error-handling doc block. Your Turn = a prompt that lists
  the failure modes for the student's specific AI step and the handling for each.

### E3 — "Complete the Loop: Turn JSON into Something a Human Can Use (Part 2A, 15 pts)" (~6 min)
- **slug:** `claude-liam-a4-03-real-output`
- **premise:** This is where most projects lose points. The AI's raw JSON is intermediate data —
  now turn it into a thing a person can open.
- **teach:** the golden rule again (JSON ≠ output). Pick a REAL output and build the node for it —
  the safe defaults first: a **formatted PDF/HTML report**, a **CSV of recommendations**, a
  **chart image**; or (with a TEST account) an **email/Slack notification** or **posted content**.
  Then document the **end-to-end flow: Input → Processing → Output → Proof** with a screenshot/
  link proving the artifact exists.
- **traps:** submitting raw JSON (-25 pts); "it would create X" without creating X; posting to a
  real account.
- **deliverable:** one real, human-usable output + the end-to-end run doc. Your Turn = a prompt
  that picks the best human-usable output for the student's project and drafts the node/format.

### E4 — "Build the Output Gallery: 10–15 Real Examples (Part 2B, 10 pts)" (~5 min)
- **slug:** `claude-liam-a4-04-output-gallery`
- **premise:** One output proves it works; ten prove it's reliable. Run it enough to fill a
  gallery.
- **teach:** generate **10–15 usable outputs**; for each, the template — what was produced, where
  it went (with an ID/path), screenshot/file link, and an honest **quality check** ("does this
  actually work? any issues?"). Consistency across the set is the point.
- **traps:** 15 near-identical dumps; no quality check; claiming success with no proof.
- **deliverable:** the 10–15 example gallery. Your Turn = a prompt that drafts the gallery entry
  template and fills it from the workflow's real outputs.

### E5 — "Prove It Scales: The Honest Stress Test (Part 3, 20 pts)" (~6 min)
- **slug:** `claude-liam-a4-05-scale-test`
- **premise:** "It could handle 1000 requests" earns zero. Actually running 50 and reporting what
  broke earns the points — and teaches you more.
- **teach:** run **1, then 10, then 50 requests** on test data; record total time at each; find
  **what breaks first** (rate limits, memory, timeouts) and at what number; compute **cost per
  100 requests** and **estimated monthly cost at 1000/day**; answer honestly: **could this run
  24/7? yes/no because…**; note what you'd monitor. Honest breaking points > a fake 100% success
  claim.
- **traps:** fabricated numbers (-20 pts); "100% success" with no evidence; skipping the cost math.
- **deliverable:** `scale_test_results.md` with real numbers. Your Turn = a prompt that turns raw
  timing/cost measurements into the scale-test report with honest production-readiness notes.

### E6 — "Package It Like a Product: Exec Summary + Architecture Diagram (Part 4, 11 of 15 pts)" (~6 min)
- **slug:** `claude-liam-a4-06-professional-package`
- **premise:** Interview-ready materials. The one-pager and the diagram are what a hiring manager
  actually looks at.
- **teach:** the **Executive Summary** (1 Figma page): problem in 2 sentences, solution bullets,
  sample outputs/results, current performance metrics, business value, a **"Built with n8n +
  [AI service]" badge**. The **Technical Architecture diagram** (1 Figma page): data flow, every
  AI component labeled, integration points, and the **failure paths** (from E2). Design it clean —
  hierarchy, headings, not a sticky-note pile.
- **traps:** marketing fluff instead of real metrics; a diagram with no failure paths; ugly layout.
- **deliverable:** the exec-summary + architecture pages. Your Turn = a prompt that drafts the
  one-page exec summary from the project's real outputs and metrics.

### E7 — "The Demo, the Before/After, and Shipping the Files (Part 4 demo + submission)" (~5 min)
- **slug:** `claude-liam-a4-07-demo-and-submit`
- **premise:** Show growth, prove it runs, submit exactly what's asked.
- **teach:** the **3–5 minute demo** (walkthrough, key points, and a **backup plan if the live
  demo fails** — record a fallback); the **before/after vs Assignment 3** slide (the "rough draft"
  contrast); then the Canvas files — **`workflow_v2.json`**, **`demo_walkthrough.pdf` or video**,
  **`scale_test_results.md`**, and the **`outputs/`** folder — all linked from the Figma board.
  Read the deduction list on camera (-20 no intelligence gain, -25 JSON-only, -20 fake scale,
  -15 missing Figma, -10 no error handling).
- **deliverable:** the demo + all submission files. Your Turn = "run the whole workflow once on
  camera; if it stumbles, that stumble is your backup-plan script — record the fallback now."

---

## Tight cut

Five-episode version: Intelligence+errors in one (E1+E2) · Real output (E3) · Gallery+scale in
one (E4+E5) · Package (E6) · Demo+submit (E7). The 7-episode cut is better because error
handling, real output, and honest scale testing are each separately graded (and separately
penalized) — beginners lose points by blurring them.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `<course-book>/youtube/`
  (or `brutalist-art/youtube/` — tell me the owning book slug).
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals →
  QC → BUILD-PROMPT.md. Re-verify n8n AI/error nodes + the chosen AI service UI at build time.
- Series index: A1 (foundation), A2 (PRD), A3 (data), A4 (this — intelligence), A8 (launch) are
  now mapped. A4 is the payoff of A2+A3; A5–A7 would complete the Madison track. Say the word and
  I'll fill A5–A7 into one master INFO 7375 series index.
