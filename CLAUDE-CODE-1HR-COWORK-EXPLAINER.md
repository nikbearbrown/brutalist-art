# Claude Code Prompt — "1 Hour on Claude Cowork" (16:9, claude-liam, Teardown, NBB logo)

Source: infographic "1 Hour on Claude Cowork" by Ruben Hassid, from "How to AI"
(how-to-ai.guide). This video RE-TEACHES that one-hour setup plan in the
Teardown voice, fact-checked and corrected — it does not just narrate the
graphic.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. The corrected content and
narration spine are embedded — no web access needed.

```text
Build one 16:9 claude-explainer video that teaches the "1 Hour on Claude
Cowork" setup plan (originally an infographic by Ruben Hassid / How to AI),
REWRITTEN in the Teardown voice and fact-checked. All graphics REBUILT as
native animation — do NOT lift or show the source infographic image (it's a
third-party graphic); rebuild everything, especially the clock. NBB logo
present throughout. claude-liam channel. Free pipeline only: Kokoro voice, no
ElevenLabs, no higgsfield, no publishing, no git commit or push. Run without
approval pauses.

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md
- skills/make/explainer/SKILL.md (and the MOTION.md / REMOTION.md it points to)
- skills/make/nbb/SKILL.md            (NBB brand mark / logo + Teardown register)
- runtime/voices/teardown/VOICE.md    (if present — the Teardown register spec)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts

FORMAT

- 1920x1080 (16:9), 30 fps.
- Channel claude-liam: persona Liam (in for Bear), voice Kokoro am_onyx,
  register TEARDOWN (Feynman × MKBHD — sharp, plain, names the trade-off, no
  hype, no bullet-reading). Do not use ElevenLabs. Folder chip @NikBearBrown.
- NBB LOGO: small low-opacity corner bug (lower-right) on every beat, full-size
  on the outro brand card. Use the NBB mark from the nbb skill / runtime assets
  (NikBearBrownOpen/Outro); if no logo file exists, render a clean
  "@NikBearBrown" wordmark in the Claude serif.
- Audio-first: narration generated and measured per beat FIRST; every beat
  conforms to its audio. Expect ~4–6 minutes.

FACT-CHECK / DOUBLE-CHECK PASS (do this to the content, not just repeat it)

The source infographic is mostly right about how Cowork works, but rewrite in
Teardown voice and correct these before scripting:
- DO NOT hardcode a model version. The graphic says "Opus 4.6 + Extended
  Thinking." Say instead: "pick the most capable model available and turn
  Extended Thinking on" — never name a version number that will date the video.
- Treat "11 official plugins" and the specific filenames
  ("about-me.md", "anti-AI-writing-style.md", "> 50 random uploads") as the
  source author's convention AT TIME OF WRITING, not fixed facts. Teach the
  PRINCIPLE (context-as-files beats prompting; one strong markdown file beats a
  pile of uploads) and attribute the framing to the source. Do not assert a
  plugin count as a permanent number.
- Keep and trust the genuinely-correct spine: real read/write folder access;
  Global Instructions apply to every task; the read-only-vs-write folder
  protocol; Projects with their own instructions, scheduled tasks, and SCOPED
  memory (Claude remembers only inside that Project); AskUserQuestion clickable
  forms; slash commands via "/"; connectors + scheduled tasks.
- Credit on screen, small: "Infographic: Ruben Hassid — How to AI
  (how-to-ai.guide)". This is a rewrite/teach of their plan, credited.

THE SCRIPT (Teardown voice — the corrected one-hour plan; polish the wording,
keep the substance and the trade-offs)

Hook: "Everybody wants to 'set up' their AI and never does. Here's the whole
thing in one hour — one clock, six wedges, no wasted minutes. And the version
going around the internet has one bug in it. We'll fix it on the way."

Teaching order (logical build; the clock still shows all six wedges summing to
60 minutes):
  1. Build your folder — 10 min. Cowork gets REAL read/write access to a folder
     on your machine, so step one is physical: one "CLAUDE COWORK" folder, four
     subfolders — About Me, Templates, Projects, Claude Outputs. The trade-off,
     said plainly: real disk access is the whole superpower and the whole risk —
     keep the folder tight, because everything in it is fair game.
  2. Set Global Instructions — 10 min. Settings → Cowork → Edit Global
     Instructions. These are the rules Claude follows on EVERY task, before you
     type anything. The one that earns its keep: the folder protocol — which
     folders are read-only, which are writable. That line is the difference
     between an assistant and a loose cannon.
  3. Create a Cowork Project — 10 min. Import a project or point it at an
     existing folder. Each Project gets its own folder, its own custom
     instructions, its own scheduled tasks — and the real unlock, SCOPED
     memory: Claude remembers what it did inside THIS Project only. Not one
     global blob. A container.
  4. Write your .md files — 15 min (the biggest wedge, and where people
     underinvest). Context as files beats context as prompting. One good
     markdown file — who you are, how you write, what you never want — is worth
     more than a pile of random uploads. The more of your context lives as
     files, the less you re-explain every session. (Attribute the
     "one great .md beats fifty uploads" framing to the source.)
  5. Run your first task — 5 min. The highest-leverage prompt isn't a command,
     it's: "I want to [task]. Ask me questions first." Claude turns that into
     clickable forms instead of guessing. And pick the most capable model with
     Extended Thinking on — no version numbers, they rot.
  6. Plugins, connectors & schedule — 10 min. Official plugins across Sales,
     Marketing, Legal, Finance; type "/" for slash commands; wire up your
     connectors; set tasks to run on a schedule. Customize a plugin for your own
     company so the slash commands speak your language.

Landing: an hour of setup buys you months of not re-explaining yourself. The
machine does the work; you keep the judgment — and now it knows where your
files live.

STRUCTURE (claude-explainer skeleton)

- Beat 0 — ClaudeComposerAsk cold open: Liam delivers the hook, teases the "one
  bug we'll fix."
- Middle — the six wedges, each its own beat, driven by the CLOCK figure below.
- Second-to-last — Your Turn composer beat, prompt typed in: "I want to set up
  my Cowork workspace. Ask me questions first."
- Last — @NikBearBrown brand card (full NBB logo) + title restated + the
  "Infographic: Ruben Hassid — How to AI" credit chip.

CENTERPIECE FIGURE — THE HOUR CLOCK

A clean 60-minute pie clock in the Claude palette (NOT a copy of the source
art). Six wedges sized to their minutes: 10 / 10 / 10 / 15 / 5 / 10. As each
wedge's beat begins, that wedge fills with terracotta and its 2–3 sub-points
animate in beside it (icons + short labels), then it settles to muted ink as
the next wedge lights up. A sweeping hand advances through the hour so the
viewer always feels "where we are in the 60 minutes." Terracotta is the ONE
accent — only the active wedge is terracotta at any moment. The running total
of minutes ticks up in a corner (10 → 20 → 30 → 45 → 50 → 60).

PER-WEDGE MICRO-ANIMATIONS (rebuild, animate — do not show static bullets)

- Build your folder: a folder opens into four labeled subfolders sliding out;
  a small lock icon underlines "keep it tight."
- Global Instructions: a settings path animates (Settings → Cowork → Edit),
  then two folder chips flip to "read-only" and "write."
- Create a Project: a Project card spawns its own mini-folder + a clock (
  scheduled tasks) + a memory chip labeled "scoped to this Project."
- Write .md files: one glowing .md file on the left outweighs a teetering stack
  of "uploads" on the right — a literal balance tipping toward the single file.
- Run first task: a composer types "…Ask me questions first," which morphs into
  a clickable AskUserQuestion form; an "Extended Thinking" toggle flips on (no
  model number shown).
- Plugins/connectors/schedule: a "/" is typed and a slash-command menu drops;
  connector tiles snap in; a task lands on a weekly schedule strip.

RULES

- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. EB Garamond Title Case segment titles.
  NBB logo bug is the one persistent brand element.
- Teardown voice throughout: short sentences, concrete, name the trade-off,
  zero hype, no reading bullets aloud. Liam is teaching, not listing.
- Transform-don't-cut; the clock hand and wedges MOVE, never hard-cut.
- Only claims that are actually true about Cowork go on screen; the corrected
  items above are mandatory. Do not invent numbers.

OUTPUTS

- youtube/claude-liam-1hr-cowork/
  - beat_sheet.json
  - claude-liam-1hr-cowork.mp4 (1920x1080)
  - SOURCES.md — the source credit (Ruben Hassid / How to AI), plus a short
    "corrections applied" list (model-version, plugin-count, filenames) so the
    fact-check is documented.
- Verify the mp4 exists and plays (probe duration + frame count) before
  reporting done, and end with the beat → timestamp table.
- If a figure animation fails to render after two attempts, replace that beat
  with a slate card naming it and log the failure — never silently drop it.
```
