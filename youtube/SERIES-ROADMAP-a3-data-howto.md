# SERIES ROADMAP — "Shop for Ingredients: Collect Your Madison Data"

A how-to ai-explainer series for **INFO 7375 Assignment 3** (Collect Data for Your Madison
Agent — an n8n workflow + docs + data file + demo, 100 pts, due May 29, 2026). Audience:
**students who have never installed n8n, built a workflow, or cleaned a dataset.** Register:
**pragmatic, step-by-step** (Liam voice, `claude-liam`, Kokoro am_onyx). The series walks a
beginner from "I have a problem from Assignment 2" to "one working pipeline, 100 clean records,
and documentation a peer could replicate."

> Voice/channel note: `claude-liam` per request (Liam, @NikBearBrown). `claude-hai` (students
> channel) is the one-variable alternative.

## The two rules that run through every episode

- **Quality over quantity.** 50–100 clean records beat 1,000 messy ones. Excellence is
  150–300 records, **NOT** 1,000+. Say it in every episode; it's the whole grading philosophy.
- **Collect once, reuse forever.** Run the workflow once, SAVE the data, then work from the
  saved file — so a data source can't cut you off mid-project. This is also why Tier-3 live
  sources are banned.

## Honesty / accuracy notes (DOUBLE-CHECK LAW)

- **n8n setup commands** (`npm install -g n8n`, `n8n start`, browser to `http://localhost:5678`)
  are from the assignment and n8n's own docs — re-verify against the current n8n version at
  build time; the UI moves. Cite n8n.io/docs and the course YouTube playlist on screen.
- **Tier-3 sources are taught as AVOID, not "here's how."** LinkedIn API (approval/expense),
  Twitter/X free tier (cuts you off), Reddit live scraping (blocks you), business-verification
  APIs. The lesson is *why* they fail a student project and what to use instead — same
  get-blocked reality the connector reels covered. No scraping-evasion content.
- **Excellence is comparative this time** — state it honestly: everyone who does it well gets
  the 80 base; the 20 excellence points go to the cleanest/most-reliable/best-presented work
  in the class. It's "do it better," not "do more."
- Local commands run on the student's OWN machine (localhost:5678) — the video shows the steps;
  it never implies the data or n8n runs "in the cloud."

## Series doctrine (every episode)

- **Assume zero tooling.** Define every term first time (n8n, node, workflow, RSS, API, record,
  CSV/JSON, dedupe, schema). Name every button. Never "just."
- **One deliverable per episode**, ending in the actual artifact (a wired node, a saved file, a
  doc section), with the paste-ready prompt that starts it.
- **AI helps you steer, not skip.** Prompts draft the data-inventory text, the setup guide, the
  cleanup logic — the student runs and verifies. Claude is the co-pilot, n8n does the work.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your
  Turn → title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "Ingredients First: Pick 3 Sources with the Tier System" (~5 min)
- **slug:** `claude-liam-a3-01-pick-sources`
- **premise:** Before you build anything, decide what you're collecting and from where — and
  the tier system saves you a week of fighting sources that block you.
- **teach:** go back to the A2 problem; **Tier 1 (start here):** public datasets (Kaggle,
  HuggingFace, Google Dataset Search, Data.gov, GitHub), RSS feeds (no login), YouTube Data API
  (10k/day free), NewsAPI (100/day free). **Tier 2 (caution):** pre-saved Kaggle Twitter/Reddit
  archives (not live). **Tier 3 (avoid, and why):** LinkedIn API, Twitter/X free tier, Reddit
  live scraping, business-verification APIs. How to search Kaggle for "[your topic] dataset" and
  find 2–3 RSS feeds. The two rules stated up front.
- **traps:** picking Tier-3 sources; chasing volume; sources unrelated to the problem.
- **deliverable:** a source plan (3 Tier-1 sources mapped to the A2 problem). Your Turn = a
  prompt that takes the A2 problem and suggests 3 Tier-1 sources + the fields worth saving.

### E2 — "Install n8n and Meet the Workflow Builder" (~5 min)
- **slug:** `claude-liam-a3-02-install-n8n`
- **premise:** n8n is a visual pipeline builder — drag boxes, connect them, run. First, get it
  running on your own machine.
- **teach:** what n8n is (define it — visual workflow automation; nodes = steps); the two
  commands (`npm install -g n8n`, then `n8n start`); open `http://localhost:5678`; a tour of the
  canvas — the node panel, adding a node, connecting nodes, the Execute button; what "runs on
  your computer" means. Point to n8n.io/docs and the course YouTube playlist for deeper help.
- **traps:** node not installed; wrong port; expecting a cloud app.
- **deliverable:** n8n running locally, blank canvas open. Your Turn = "install n8n, run
  `n8n start`, open localhost:5678, and add one Start node."

### E3 — "Build the Pipeline, Part 1: Wire Up Your 3 Sources (40-pt core)" (~7 min)
- **slug:** `claude-liam-a3-03-wire-sources`
- **premise:** The heart of the grade — a workflow that pulls from three different places. Build
  the 6-step skeleton and connect the first three data nodes.
- **teach:** the 6-step pattern (Start → Source 1 → Source 2 → Source 3 → Cleanup → Save); wire
  **Source 1 = an RSS feed** (the RSS Read node — easiest, no login); **Source 2 = an API**
  (HTTP Request / NewsAPI or YouTube Data API, with the key stored in n8n credentials, never
  hard-coded); **Source 3 = a dataset** (import a downloaded Kaggle CSV via the Read/CSV node).
  Run each node and LOOK at what it returns. Keep it to fields that address the problem.
- **traps:** three sources that are really one; pasting an API key into a node instead of
  credentials; pulling 2,000 records "because you can."
- **deliverable:** three source nodes returning data. Your Turn = a prompt that picks the right
  n8n node type for each of the student's three chosen sources.

### E4 — "Build the Pipeline, Part 2: Clean, Save, Export" (~6 min)
- **slug:** `claude-liam-a3-04-clean-save-export`
- **premise:** Raw pulls are messy. The cleanup and save steps are what turn three feeds into
  one usable file — and the export is the thing you actually submit.
- **teach:** the **Cleanup node** (merge the three sources; remove duplicates; standardize dates
  to **YYYY-MM-DD**; drop records missing essential fields — title/date/source); the **Save
  node** (write **CSV or JSON** to a folder on your computer); run the whole workflow ONCE and
  land **50–200 clean records** (collect-once-reuse-forever); then **export the workflow** to
  `LastName_FirstName_A3_Workflow.json`.
- **traps:** inconsistent date formats; keeping empties/dupes; forgetting to export the JSON;
  re-running and getting cut off.
- **deliverable:** the saved data file + the exported workflow JSON. Your Turn = a prompt that
  drafts the cleanup rules (dedupe key, date format, required fields) for the student's data.

### E5 — "Make It Reliable + Prove It's Clean (Quality 16 pts + craft excellence)" (~6 min)
- **slug:** `claude-liam-a3-05-quality-and-craft`
- **premise:** Two things separate full-credit from excellent: data you can trust, and a
  workflow that doesn't crash when a source misbehaves.
- **teach:** the **quality checklist** — 80%+ complete records, essential fields in every row,
  duplicates removed, consistent dates, relevance (no filler); then **document the numbers**
  (total records, clean records, % quality rate — 8 of the 16 points are literally the numbers).
  Craft excellence: **handle the source that fails** — when a feed is slow or returns nothing,
  log "Source unavailable" and keep the other two running (the Kanishk example), don't crash.
  Reliability beats complexity.
- **traps:** undocumented quality numbers; a workflow that dies when one source is empty;
  "relevance" filler to pad the count.
- **deliverable:** the quality-numbers block + an error-handling branch. Your Turn = a prompt
  that reviews a sample of records and reports completeness %, duplicates, and date consistency.

### E6 — "Document It Like a Pro: Inventory + Setup Guide (Part 2 + presentation excellence)" (~6 min)
- **slug:** `claude-liam-a3-06-documentation`
- **premise:** Same data, different outcome — the polished PDF gets opened first. Presentation
  IS graded here, and it's comparative.
- **teach:** the **Data Inventory** using the exact template (per-source: type, amount, purpose,
  collection method, quality X/Y; then Statistics: total, clean, %, sources, "ready for A4");
  the **Setup Guide** (install steps, what to install first, where access codes go — **never
  paste real keys**, common errors + fixes); then make it LOOK professional — headings,
  consistent formatting, visual hierarchy (the "20 extra minutes" that scores higher). Assemble
  into one clean PDF.
- **traps:** copy-paste wall of text; sharing real API keys; a peer couldn't replicate it.
- **deliverable:** the documentation PDF. Your Turn = a prompt that fills the data-inventory
  template from the workflow's actual output and drafts a replicable setup guide.

### E7 — "The Demo + Ship the 4 Canvas Files" (~5 min)
- **slug:** `claude-liam-a3-07-demo-and-submit`
- **premise:** Prove it runs, then submit exactly what's asked — four files, specific names.
- **teach:** the **demo** — pick ONE: a **3-minute video** (workflow overview → run it on camera
  → show the output data) OR a **5–8 screenshot walkthrough PDF** (full workflow, key node
  configs, running, sample output — captioned, with arrows). Then the **four Canvas submissions**:
  the workflow **JSON** (`LastName_FirstName_A3_Workflow.json`), the documentation **PDF**, the
  **data file** (CSV/JSON), and the **demo**. "We care that it runs and that we understand it —
  not your production skills."
- **deliverable:** all four submission files. Your Turn = "run your workflow start to finish on
  camera once; if any step surprises you, that's the thing to fix before you record the real demo."

---

## Tight cut

Five-episode version: Sources+tiers (E1) · Install+build in one longer episode (E2+E3) ·
Clean/save/export (E4) · Quality+craft (E5) · Document+demo+submit (E6+E7). The 7-episode cut
is better here because the n8n build is the 40-point core and beginners need the build split.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `<course-book>/youtube/`
  (or `brutalist-art/youtube/` — tell me the owning book slug).
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals →
  QC → BUILD-PROMPT.md. Re-verify n8n's current install/UI + node names at build time; the
  workflow screens must be REBUILT natively (REBUILD LAW), not screen-grabbed.
- Series index: A1 (foundation), A2 (PRD), A3 (this — data), A8 (launch) are now mapped. Say the
  word and I'll fill A4–A7 into one master INFO 7375 series index (A3 explicitly sets up A4:
  "ready for Assignment 4").
