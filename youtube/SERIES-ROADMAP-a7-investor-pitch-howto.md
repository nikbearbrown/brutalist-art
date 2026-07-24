# SERIES ROADMAP — "Sell the Vision: Your Investor Pitch Video"

A how-to ai-explainer series for **INFO 7375 Assignment 7** (Video Pitch to Investors — the
midterm: a recorded video + PDF slide deck, 100 pts, due July 10, 2026). Audience: **students who
have a Madison project at any stage and have never pitched to investors or produced a branded
video.** Register: **pragmatic, step-by-step** (Liam voice, `claude-liam`, Kokoro am_onyx). The
series walks a beginner from "I have a tool and no idea how to sell it" to "an 8-minute pitch a
non-technical investor would actually fund."

> Voice: `claude-liam` per request; `claude-hai` (students channel) is the one-variable alternative.

## Toolkit tie-in (this is the meta-loop — say it in E1 and E6)

- **Content:** the house **`madison-pitch`** skill was built for exactly this — an 8-minute,
  10-slide venture pitch for a non-technical audience, with a **jargon audit**, an **8-minute
  timing check**, and a **skeptical-VC score** (provenance gate: every stat sourced or labeled).
  The Your Turn prompts route students to `madison-pitch` for the deck and the timing/jargon passes.
- **Production (the excellence differentiator):** the assignment names **Remotion** as the way to
  make a *branded pitch video that stands out* — and Brutalist-art is a Remotion toolkit. Students
  comfortable with code can produce the top-25% production tier with the toolkit's Remotion +
  `deck-lecture` / brutalist-slides path. This is the one assignment where Bear's own video
  toolkit is the student's production tool.

## The philosophy that runs through every episode

- **80/20 + Kawasaki 10/20/30.** Ship the full pitch professionally = 80 points (a B). Memorable
  and investable = the final 20 (an A). **10 slides max, 8 minutes hard cap, 30-point minimum
  font.** Say it every episode.
- **You're selling the vision, not the code.** "Investors care where the car goes, not how the
  engine works." Stage doesn't matter — concept, mockup, prototype, or MVP are all valid.
- **Zero jargon.** The whole pitch must land for smart money that knows nothing about n8n, APIs,
  or Python. The translation guide is a core tool, not a footnote.

## Honesty / craft threads (DOUBLE-CHECK LAW)

- **8 minutes is a HARD cap.** Practice, time yourself, edit mercilessly. Over time loses points —
  the video teaches rehearsing until timing is automatic, and `madison-pitch`'s timing check.
- **Test zero-jargon on a real non-technical person** before recording (a named checklist item).
  If they don't get it, rewrite — same read-aloud honesty as the UVP gut-check.
- **Sell what you have; don't apologize for unfinished code.** Transparency about stage is a
  strength ("investors fund ideas"). No fake "it's basically done."
- **Every number sourced or labeled** (the `madison-pitch` provenance gate) — rough revenue
  estimates are fine if labeled as estimates; invented precision is not.
- **Production quality can't rescue weak content.** Either path (Zoom or Remotion) earns the 80% on
  content; polish is the excellence tier. Don't over-invest in video if the pitch is unclear.

## Series doctrine (every episode)

- **Assume zero pitch experience.** Define every term first time (pitch, UVP, GTM, business model,
  proof of concept, the ask, 30-point font, picture-in-picture). Never "just."
- **One or two slides per episode**, ending in the drafted slide + spoken script, with the
  paste-ready `madison-pitch` (or plain) prompt that drafts it.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your
  Turn → title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "Pitch Like Kawasaki: 10 Slides, 8 Minutes, 30-Point Font" (~5 min)
- **slug:** `claude-liam-a7-01-the-pitch-arc`
- **premise:** The rules that make investor pitches work — and the 80/20 truth about what earns
  the A.
- **teach:** the 10/20/30 rule; the 80/20 philosophy (ship = 80, memorable = 20); who the audience
  is (smart money, non-technical, cares about problems/solutions/profits); the full 10-slide arc
  with per-slide time budgets (title 15s → problem 75s → solution 75s → magic 45s → business 50s →
  GTM 50s → competition 45s → dev plan 40s → POC 75s → ask 30s). Introduce `madison-pitch`.
- **traps:** more than 10 slides; no time budget; treating it as a code demo.
- **deliverable:** the pitch outline + time budget. Your Turn = `madison-pitch` Prompt 0 (intake)
  to scaffold all 10 slides from the Madison project.

### E2 — "The First Two Minutes: Title + Problem (Slides 1–2)" (~5 min)
- **slug:** `claude-liam-a7-02-title-and-problem`
- **premise:** If the problem isn't clear in minute one, nothing else matters. Open memorable, then
  make them feel the pain.
- **teach:** **Slide 1** — project name, your name, a memorable one-line description (reuse the
  Conductor Brief Part 1 sentence / A6 UVP). **Slide 2** — the problem/opportunity: what it is, why
  anyone should care, and **quantify the pain in dollars, time, or frustration** (labeled numbers).
- **traps:** a forgettable title; a vague problem; unquantified pain.
- **deliverable:** slides 1–2 + script. Your Turn = a prompt that turns the Conductor Brief problem
  into a quantified, non-technical problem slide.

### E3 — "Sell the Solution & the Magic, Simplified (Slides 3–4)" (~5 min)
- **slug:** `claude-liam-a7-03-solution-and-magic`
- **premise:** The aha moment in plain English — and your secret sauce in one sentence a
  seventh-grader gets.
- **teach:** **Slide 3** — how the tool fixes the problem, the aha explained simply, **no jargon**.
  **Slide 4** — the magic: "We use AI to…" (one sentence), why it wasn't possible before,
  PageRank-level simplicity. Walk the **translation guide** on camera ("n8n workflow" → "automated
  system"; "multi-agent orchestration" → "multiple AI assistants working together"; etc.).
- **traps:** technical jargon; a feature list instead of the aha; a magic slide only an engineer
  understands.
- **deliverable:** slides 3–4 + script. Your Turn = `madison-pitch` jargon-audit pass on the
  solution + magic slides.

### E4 — "The Business Case: Model, GTM, Competition, Ask (Slides 5–7 + 10)" (~6 min)
- **slug:** `claude-liam-a7-04-business-case`
- **premise:** This is where "cool project" becomes "fundable business." Four slides that show you
  thought about money, customers, rivals, and the ask.
- **teach:** **Slide 5** business model (how you make money; pricing — subscription/one-time/
  freemium; rough, labeled revenue estimates); **Slide 6** GTM (how you get your first 10
  customers; channels; use Claude to brainstorm for the specific tool); **Slide 7** competition
  (who else, why you win, the unfair advantage — reuse A6 positioning / the one-thing); **Slide 10**
  the ask (funding/resources/help, timeline, a clear call to action).
- **traps:** no monetization; "everyone is my customer"; superficial competition; no clear ask.
- **deliverable:** slides 5–7 + 10 + script. Your Turn = prompts (Claude / `madison-pitch`) that
  draft a pricing model, a first-10-customers GTM, and a one-line ask.

### E5 — "Proof of Concept at ANY Stage (Slides 8–9)" (~5 min)
- **slug:** `claude-liam-a7-05-proof-of-concept`
- **premise:** You don't need finished code — you need to show honestly where you are and make it
  compelling.
- **teach:** **Slide 8** dev plan (current status: concept/mockup/prototype/MVP; what's left;
  timeline + milestones); **Slide 9** POC (working code → show it running; mockups → walk the user
  journey; concept → wireframes or the workflow diagram). Be transparent about stage — investors
  appreciate it. Sell what you have; don't apologize.
- **traps:** apologizing for no code; vague concept; overclaiming the stage.
- **deliverable:** slides 8–9 + script. Your Turn = a prompt that frames the honest current stage
  as a strength and drafts the milestone timeline.

### E6 — "Record It: Zoom (fast) vs Remotion/Brutalist (standout)" (~6 min)
- **slug:** `claude-liam-a7-06-record-it`
- **premise:** Two valid paths — the fast one that gets the 80%, and the branded-video one that
  competes for the top 25%.
- **teach:** the **low-effort path** (Zoom: screen-share slides, record locally/cloud — fast,
  totally acceptable); the **quality path** (Remotion / Loom / Descript — production quality signals
  investor-readiness; Remotion is a React video framework, and the **Brutalist-art toolkit +
  `deck-lecture` / brutalist-slides** can turn a slide deck into a branded pitch video). The
  requirements either way: **8-minute hard cap** (rehearse until automatic), **face visible** at
  some point, slides visible (screen-share/PiP/embedded), **clear audio** (test mic, quiet room,
  headphones), export MP4/MOV or a shared link.
- **traps:** over 8 minutes; bad audio; reading from slides; over-investing in production over content.
- **deliverable:** the recorded pitch video. Your Turn = "record one timed take; if you're over 8
  minutes or reading your slides, that's the note for take two."

### E7 — "Ship It: Export, Name, Submit + the Jargon Test" (~4 min) — closer
- **slug:** `claude-liam-a7-07-ship-the-pitch`
- **premise:** Last gates — prove it's jargon-free and on time, then submit exactly what's asked.
- **teach:** the pre-submission checklist (timed under 8 min; **zero jargon tested on a real
  non-technical friend/family**; a visual on screen; problem clear in minute one; business model
  in; specific ask; face on camera; audio tested); export the **video** (MP4/MOV or link) and the
  **PDF slide deck**; name them **`YourName_MadisonPitch.mp4`** and **`YourName_MadisonPitch.pdf`**;
  submit both to Canvas. "No submission = no grade."
- **deliverable:** the submitted video + PDF. Your Turn = "play your pitch for someone who's never
  heard of the project; every place they look confused is a jargon fix before you submit."

---

## Tight cut

Five-episode version: The arc (E1) · Problem→Solution→Magic (E2+E3) · Business + POC (E4+E5) ·
Record (E6) · Ship (E7). The 7-episode cut is better because each slide cluster is separately
scored and beginners under-build the business slides.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `<course-book>/youtube/`
  (or `brutalist-art/youtube/` — tell me the owning book slug). `madison-pitch` is the drafting
  engine for content; Remotion + `deck-lecture` / brutalist-slides is the production path shown in E6.
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals →
  QC → BUILD-PROMPT.md.
- Series index: the full INFO 7375 arc is now mapped — A1 (foundation), A2 (PRD), A3 (data), A4
  (intelligence), A5 (strategy) + A5A/A5B (interface/recipe), A6 (brand), A7 (this — pitch), A8
  (launch). Say the word and I'll stitch a single **master INFO 7375 series index** (one ordered
  playlist across all assignments) and, if you want, a resumable batch prompt that builds the whole
  semester's how-to reels on your Mac.
