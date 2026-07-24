# SERIES ROADMAP — "Plan It Like a PM: Your Madison PRD"

A how-to ai-explainer series for **INFO 7375 Assignment 2** (Plan Your Madison Project
Like a Pro — a single Figma board + a screen-grab, 100 pts). Audience: **students who have
never written a PRD, done a gap analysis, or built an n8n workflow.** Register: **pragmatic,
step-by-step** (Liam voice, `claude-liam`, Kokoro am_onyx). The series walks a beginner from
"pick a lane" to "someone could build my project from this PRD."

> Voice/channel note: `claude-liam` per request (Liam, @NikBearBrown). `claude-hai`
> (students channel) is the one-variable alternative.

## Two facts to keep straight on camera (honesty — DOUBLE-CHECK LAW)

1. **Madison is the framework; n8n is the build tool. They are not the same thing.** Madison
   (github.com/Humanitariansai/Madison) is an open-source, agent-based AI *marketing* framework
   — five agent layers under an orchestration layer. n8n is a separate visual workflow-automation
   app where the student builds the actual runnable MVP. The assignment pairs them: design
   Madison-style agents (Part 4a), then make ONE of them concrete as an n8n workflow (Part 4b).
   n8n is **not** mentioned in Madison's own docs — say so; don't imply Madison ships n8n nodes.
2. **The deadline text is inconsistent in the source.** The header says due **May 22, 2026**;
   the submission block says **January 23, 2026**. Flag this on screen as "confirm the real
   deadline with your instructor" — do not pick one silently. (Also: the assignment says submit
   in **Canvas**, and the file name is `LastName_FirstName_Week2.png`.)

## Madison grounding (from the live README, verified 2026-07-18 — re-check at build)

- **Five agent layers:** Intelligence (market analysis/insights) · Content (create/optimize/
  distribute across channels) · Research (survey analysis, customer insight) · Experience (AI
  concierge, customer journey) · Performance (measure/optimize; multi-armed bandit).
- **Named components students can anchor an agent to:** MarketMind Research (secondary market/
  competitor research) · Brand Voice Personalization (voice-consistency via NLP) · AI Concierge
  Systems · Multi-Armed Bandit Optimization (Thompson sampling for campaign A/B tests) ·
  Knowledge-graph brand-perception tracking. Integrations: **Bellman** (reinforcement learning)
  and **Popper** (evidence-based validation / bias detection).
- **Orchestration layer:** cross-project validation, dynamic resource allocation, continuous
  learning. This is the "how the agents communicate" backbone for Part 4a's diagram.

## Series doctrine (every episode)

- **One Figma board, labeled sections, comments enabled.** Every episode adds its section.
- **Assume zero PRD/product experience.** Define every term first time (PRD, MVP, user story,
  success metric, node, gap analysis, ATS). Never "just."
- **Scope discipline is the whole grade.** Repeat the red flags on camera: "no solving world
  hunger," "no team-of-10 scope," "must be buildable in Week 3." The success test: *someone
  could build your project from your PRD.*
- **AI drafts, student owns the truth.** Each episode shows the prompt that drafts the section
  from the student's real job + gaps, then the fact-check/tighten pass.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your
  Turn (the section) → title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "Pick a Lane: Find the ONE Real Job (10 pts)" (~5 min)
- **slug:** `claude-liam-a2-01-pick-a-lane`
- **premise:** You can't plan a project that gets you hired if you haven't named the job. One
  real posting you could apply for in 6–12 months — not a job type, a posting.
- **teach:** how to find a real posting (LinkedIn/Indeed/company careers); capture company +
  exact title, link/screenshot, the **top 3 technical requirements** they list, one sentence on
  why this role. Then the excellence move: **find the hiring manager on LinkedIn**, note their
  background/team. Put it all on the board.
- **traps:** "Software Engineer somewhere"; no link; 3 vague requirements; no reason.
- **deliverable:** the Dream-Job card. Your Turn = a prompt that reads a pasted job posting and
  extracts the title, top-3 technical requirements, and likely team context.

### E2 — "Gap Analysis: What's Between You and That Job (20 pts)" (~6 min)
- **slug:** `claude-liam-a2-02-gap-analysis`
- **premise:** The four-column table that turns "I'm not qualified yet" into a plan — and into
  your Madison project.
- **teach:** build the table on Figma — **They Want | I Have | Gap to Fill | Madison Could Help
  By…** — with **3+ real, job-specific gaps** (use the posting from E1). How to be honest about
  "I Have." How to connect each gap to a Madison capability without hand-waving (e.g. "need
  AI/ML portfolio" → "build a multi-agent workflow on Madison's Content layer"). Excellence:
  **research the company's actual tech stack** and name specific tools/frameworks in the table.
- **traps:** generic gaps; vague "Madison will help somehow"; no job connection.
- **deliverable:** the gap table. Your Turn = a prompt that takes the job's requirements + the
  student's current skills and drafts the 4-column gap table with Madison mappings to refine.

### E3 — "Write a PRD Like a PM, Part 1: Problem & Solution (20 of 40 pts)" (~6 min)
- **slug:** `claude-liam-a2-03-prd-problem-solution`
- **premise:** A PRD is how a real product manager says "here's what we're building and why it
  matters" before anyone writes code. First half: the problem, and your Madison answer to it.
- **teach:** what a PRD is (define it). **Problem Statement** (10 pts): a *specific* problem the
  target company/role faces, WHO experiences it, the cost of not solving it. **Proposed Solution**
  (10 pts): your Madison-powered approach, why Madison vs. alternatives, what's technically
  interesting. Reference the Nina example on camera (industry-grounded framing: real study
  numbers, not vibes). Show the drafting prompt, then the "make the problem specific" pass.
- **traps:** problem too broad ("marketing is hard"); no cost stated; "why Madison" unanswered.
- **deliverable:** PRD problem + solution sections. Your Turn = a prompt that pressure-tests a
  problem statement for specificity and drafts the "why Madison" paragraph.

### E4 — "Write a PRD Like a PM, Part 2: User Stories & Success Metrics (20 of 40 pts)" (~6 min)
- **slug:** `claude-liam-a2-04-prd-stories-metrics`
- **premise:** Two things separate a real PRD from an essay: user stories in the exact format,
  and metrics you can actually measure.
- **teach:** **User Stories** (10 pts): write 3 in the exact template — "As a [role], I want
  [feature] so that [benefit]" — specific and achievable (walk the accessibility-checker
  example). **Success Metrics** (10 pts): what improves and BY HOW MUCH — time saved, errors
  reduced, cost cut — plus HOW you'd measure it. Excellence: pull a real number from industry
  research; name the APIs/tools you'll integrate; include an edge case / failure mode.
- **traps:** stories missing the "so that" benefit; unmeasurable metrics ("it'll be better");
  no measurement method.
- **deliverable:** PRD stories + metrics sections. Your Turn = a prompt that converts feature
  ideas into correctly-formatted user stories and proposes measurable success metrics.

### E5 — "Design Your 3 Madison Agents (15 of 30 pts)" (~6 min)
- **slug:** `claude-liam-a2-05-agent-design`
- **premise:** Now the architecture. Three agents, each with ONE specific job, and a simple
  picture of how they talk.
- **teach:** the five Madison layers at a glance (Intelligence · Content · Research · Experience
  · Performance) and the named components (MarketMind, Brand Voice Personalization, AI Concierge,
  Multi-Armed Bandit/Thompson sampling, knowledge graphs; Bellman/Popper). Pick **3 agents**,
  give each a name + specific job tied to the PRD problem; draw a **simple communication diagram**
  (who sends what to whom — the orchestration-layer idea, kept beginner-simple). Excellence prep:
  show a **data schema** between two agents (what the message actually looks like).
- **traps:** three agents that do the same thing; no communication flow; agents unrelated to the
  problem; inventing Madison features that don't exist (keep to the real layers/components).
- **deliverable:** the agent-design section. Your Turn = a prompt that maps a PRD problem to 3
  distinct Madison agents with roles and a message flow.

### E6 — "Scope the MVP: ONE n8n Workflow (15 of 30 pts)" (~6 min)
- **slug:** `claude-liam-a2-06-n8n-mvp`
- **premise:** Design is infinite; Week 3 is not. This is where you pick the ONE thing you'll
  actually build — and honestly name what you won't.
- **teach:** what **n8n** is (define it — a visual workflow-automation tool; nodes = steps;
  you wire input → process → output) and how it relates to Madison (n8n is where ONE agent's
  logic becomes a runnable workflow; Madison is the design language). Define the **one workflow**,
  the **3–5 nodes** you'll use, and the input → process → output flow. Then the honesty beat:
  **what you WON'T build** (scope boundary). Excellence: name **specific n8n nodes you
  researched** and show the **data schema/format** passed between nodes.
- **traps:** a workflow with 15 nodes; "I'll build all three agents"; no explicit out-of-scope
  list; naming n8n nodes you haven't looked up.
- **deliverable:** the MVP-scope section. Your Turn = a prompt that turns one agent's job into a
  realistic 3–5 node n8n workflow with an explicit "not building" list.

### E7 — "Ship It: Figma Link + Screen-Grab Submission" (~4 min) — closer
- **slug:** `claude-liam-a2-07-submit`
- **premise:** Two submissions, specific rules, easy points to lose. Don't lose them.
- **teach:** final board pass (labeled sections, consistent styling, comments enabled, public/
  link-accessible); export a **screen grab of the WHOLE board**, PNG or PDF, **5–25 MB**, named
  **`LastName_FirstName_Week2.png`**; submit **both** the Figma link and the file in **Canvas**.
  Read the deduction list on camera (-5 not on Figma, -10 unrealistic scope, -15 no Madison
  integration, -5 missing screen grab). Flag the deadline discrepancy — confirm the real date.
- **deliverable:** the two submitted items. Your Turn = "share your board with a classmate,
  ask if they could build your project from it — if not, that's your revision list."

---

## Tight cut

Five-episode version: Pick-a-lane (E1) · Gap analysis (E2) · Full PRD in one (E3+E4) ·
Architecture + n8n in one (E5+E6) · Submit (E7). PRD and architecture are the heaviest
(40 + 30 pts), so splitting them (the 7-episode cut) is the better teaching call.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `<course-book>/youtube/`
  (or `brutalist-art/youtube/` as a channel series — tell me the owning book slug).
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals →
  QC → BUILD-PROMPT.md. Re-verify the Madison README + n8n node names at build time.
- Series index note: this is A2; I've now mapped A1 (foundation), A2 (this), and A8 (launch).
  Say the word and I'll fill 3–7 into one master INFO 7375 series index.
