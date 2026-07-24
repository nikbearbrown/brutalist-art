# Using Brutalist — a Humanitarians AI Fellows Series (map)

**What this is.** A complete onboarding curriculum, in claude-explainer style,
Liam voice, @HumanitariansAI branding, that takes a Fellow from "I did research
this week" to "my explainer is live in the Fellows Research playlist." Every
episode is a short claude-liam reel; together they are the full "how to use
Brutalist" course.

**Voice / brand (every episode).** claude-liam (Kokoro `am_onyx`, IN-FOR-BEAR
LAW — Liam signs "Liam, in for Bear"), folder chip **@HumanitariansAI**, HAI
logo bug, register Teardown-warm (a welcome, not a takedown). Free pipeline
only. Build into `brutalist-art/youtube/hai-brutalist-<slug>/` (toolkit
meta-series exception to the ownership rule). Contact for the system + keys +
Gaurav's publish script: **hr@humanitarians.ai**. Publish target:
youtube.com/@humanitariansai, **Fellows Research** playlist.

**Reuse note.** Several topics already have non-HAI builds
(`what-is-brutalist`, `installs`, `posting-to-youtube`, `cowork-setup`,
`claude-liam-hai-how-to-explainer-videos`). The batch REBRANDS those topics as
HAI episodes in new `hai-brutalist-*` folders (don't overwrite the originals),
and builds the NEW episodes fresh. `claude-liam-hai-how-to-explainer-videos`
stays the series TRAILER / index (E00).

---

## The arc (novice → shipping → contributing)

| # | Slug | Title | Status | One-line premise |
|---|---|---|---|---|
| E00 | (exists) `claude-liam-hai-how-to-explainer-videos` | How to Make Explainer Videos for Your Research | BUILT — trailer/index | The whole loop in one video; the episodes below expand each step. |
| E01 | `hai-brutalist-what-is` | What Is Brutalist? | REBRAND | A self-contained toolkit that turns your work into explainer videos with Claude — one entry point, `./art`. |
| E02 | `hai-brutalist-why-video` | Why Make a Video of Your Research | NEW | Invisible work stays invisible; a two-minute explainer gives your research a face and an audience. |
| E03 | `hai-brutalist-install` | Install & Set Up | REBRAND | Email hr@humanitarians.ai, drop in the skills, `cp .env.example .env`, `./setup --install`, `./art keys`. |
| E04 | `hai-brutalist-week-folder` | Your Week in a Folder | NEW | One folder per week — notes, code, figures, data, draft — is the raw material Claude reads for stories. |
| E05 | `hai-brutalist-run-claude-code` | Run Claude Code | NEW | One command in that folder: `caffeinate claude --dangerously-skip-permissions` — awake, unblocked, end-to-end. |
| E06 | `hai-brutalist-the-prompt` | The Prompt: Generic → Specific | NEW | Start from the generic batch prompt; steer it with YOUR week; add "Liam, for [your name] and Humanitarians AI." |
| E07 | `hai-brutalist-beat-sheet` | What's a Beat Sheet? | NEW | The beat sheet is the heart of every reel; audio-first — measured narration is the master clock. |
| E08 | `hai-brutalist-voices` | Voices: Free vs Cloned | NEW | Kokoro is free and the default; ElevenLabs (Bear's clone) is opt-in and passes a human gate before any spend. |
| E09 | `hai-brutalist-make-it-move` | Make It Move | NEW | Every number, chart, and mechanism is REBUILT as native Manim/Remotion motion — never a screenshot; ASK→RESULT. |
| E10 | `hai-brutalist-watch-revise` | Watch & Revise | NEW | Plain-language notes in, better video out; the frame-level visual QC pass before anything ships. |
| E11 | `hai-brutalist-publish` | Publish to the Channel | REBRAND | Gaurav's script (hr@humanitarians.ai) → @humanitariansai → the Fellows Research playlist. |
| E12 | `hai-brutalist-profile-a-fellow` | Profile a Fellow | NEW | The student/profile mode: turn a feature article about a person into a reel that lands their one idea. |

Optional extensions (build only if asked): `hai-brutalist-scout-a-folder`
(mine a folder for video ideas), `hai-brutalist-batch` (build every idea in one
run), `hai-brutalist-cowork-setup` (HAI rebrand of cowork-setup).

---

## Per-episode capsule (thesis + centerpiece the builder animates)

- **E01 What Is Brutalist** — thesis: "a self-contained video factory you drive
  with one command." Centerpiece: the pipeline rail IDEAS → SCRIPT/BEATS →
  AUDIO → VISUALS → ASSEMBLE → PUBLISH, `./art` lighting each stage.
- **E02 Why Make a Video** — thesis: "the work is already done; this gives it a
  face." Centerpiece: a paper/PDF shrinking into a 2-min reel that many people
  actually watch — reach as the payoff.
- **E03 Install & Set Up** — thesis: "five minutes from zero to ready."
  Centerpiece: an Onda terminal checklist — email chip hr@humanitarians.ai →
  `cp .env.example .env` → `./setup --install` → `./art keys` all green.
- **E04 Your Week in a Folder** — thesis: "one folder = the raw material."
  Centerpiece: a folder filling with labeled cards (notes, code.py, figure.png,
  data.csv, draft.md).
- **E05 Run Claude Code** — thesis: "one command, awake and unblocked."
  Centerpiece: the command typed live with per-token callouts —
  `caffeinate` (stay awake) · `--dangerously-skip-permissions` (run end to end).
- **E06 The Prompt** — thesis: "the specifics are what make it yours."
  Centerpiece: generic prompt (grey) vs the same prompt with terracotta
  insertions — project, result, figure, takeaway, "Liam, for [name] and
  Humanitarians AI."
- **E07 Beat Sheet** — thesis: "audio-first — narration is the master clock."
  Centerpiece: a beat_sheet.json with beats; each beat's measured MP3 sets its
  on-screen duration; change audio → timing conforms.
- **E08 Voices** — thesis: "free by default, cloned by choice, gated always."
  Centerpiece: two lanes — Kokoro (free, local, `am_onyx`) vs ElevenLabs (Bear
  clone, GATE P before spend); the gate as a terracotta checkpoint.
- **E09 Make It Move** — thesis: "rebuild the idea as motion; never screenshot."
  Centerpiece: a source figure being redrawn as a native animated chart, then
  the ASK→RESULT receipt (composer prompt → the graphic it made).
- **E10 Watch & Revise** — thesis: "plain language in, better video out."
  Centerpiece: a player with a revise loop ("this number's wrong" arcs back,
  the card updates) → the visual-QC frame grid catching a defect.
- **E11 Publish** — thesis: "one script from finished file to live episode."
  Centerpiece: Gaurav's script (chip hr@humanitarians.ai) → @humanitariansai →
  the new video sliding into the Fellows Research playlist row.
- **E12 Profile a Fellow** — thesis: "make invisible work visible." Centerpiece:
  a feature article compressing to its one thesis line, then that person's
  projects rebuilt as concept illustrations; credit card with their real links.

Each episode ends with the standard your-turn closing whose HANDOFF prompt is
the natural next action (E03's is the install command; E06's is the generic
prompt seed; E11's is "publish this to Fellows Research"). E00 links the arc.
