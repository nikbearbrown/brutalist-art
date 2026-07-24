# Session Build Manifest — everything produced this session

A complete inventory of what was built, where it lives, and what's still pending sync to your
Mac. Grouped into four bodies of work: **toolkit changes**, **the ai-explainer reel series**,
**batch build prompts**, and **the INFO 7375 course roadmaps**.

Two locations are referenced throughout:
- **Mac** = `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/…` (committed via the device bridge)
- **Cloud** = the session workspace (delivered to you in chat, **not yet written to the Mac** — the bridge's file tools went offline partway through)

---

## 1. Toolkit & infrastructure changes  ✅ on your Mac

| Change | File | What happened |
|---|---|---|
| **New `skill-teardown` modifier** | `skills/make/ai-explainer/SKILL.md` | Added a second modifier (sibling of `profile`) that auto-arms when the reel's source is a SKILL.md: same bookends, body breaks the skill down and demos it live (SELF-DEMO LAW) with a slate fallback. Names "Claude, Seeded" as the exemplar. |
| **Skill rename** | `claude-explainer` → `ai-explainer` | Reserved-word (`claude`) blocked the Cowork importer. Renamed the folder, the `name:` field, **47 path references** across the repo, and added a GLOSSARY alias. (Interim name `fidelity-explainer` was rejected by you.) Description tightened to 1013 chars (under the 1024 cap). Old name still triggers + resolves. |
| **GLOSSARY alias** | `GLOSSARY.md` | Added `claude-explainer → ai-explainer` row so the old name resolves through the `art` dispatcher. |
| **Vercel MCP noted installed** | `AGENTS.md` | Added a "Connected MCP servers" section documenting `npx add-mcp https://mcp.vercel.com`, reinstall/authorize commands, and the account-equivalent-access caution. |
| **HARD STOP money rule** | `AGENTS.md` (top of file + core principles) | Added an unmissable rule: any MCP/tool about to spend, buy, subscribe, or renew is a **hard stop** — ask a human, wait for an explicit yes. Overrides `--dangerously-skip-permissions`, pauses mid-batch/unattended, applies even to official tools. |

---

## 2. The ai-explainer reel series (Liam voice)  ✅ on your Mac

Five complete reels, each built into `brutalist-art/youtube/<slug>/` as a full package:
**beat_sheet.json** (durations locked to measured audio) · **PEDAGOGY.md** (GATE P audit, VERDICT: PASS) ·
**SOURCES.md** (every claim traced/verified) · **BUILD-PROMPT.md** (paste-ready Mac render prompt) ·
**mp3/** (Kokoro `am_onyx` Liam narration, one per beat, $0.00). Visuals still to render on your Mac.

| # | Title | Slug | Subject | Beats | Runtime | Type |
|---|---|---|---|---|---|---|
| 1 | **Claude, Restrained.** | `claude-liam-theme-factory` | Anthropic's theme-factory skill (the consent gate) | 12 | 4:50 | skill-teardown (exemplar) |
| 2 | **Claude, Gated.** | `claude-liam-connect-linkedin` | Connecting Claude to LinkedIn (the 3-job asymmetry) | 13 | 6:16 | standard explainer |
| 3 | **Claude, Grounded.** | `claude-liam-google-workspace` | Gmail/Calendar/Drive connectors (Gmail can't send) | 12 | 5:40 | standard explainer |
| 4 | **Claude, Trusted.** | `claude-liam-vercel-mcp` | Vercel MCP (`buy_domain`, account-equivalent access) | 12 | 5:58 | standard explainer |
| 5 | **Claude, Paused.** | `claude-liam-money-hard-stop` | Why the money hard-stop rule exists | 10 | 4:28 | standard explainer |

**Shared discipline across all five:** audio-first (measured narration = master clock); every
factual claim web-verified where dated (hiQ settlement, Vercel `buy_domain` schema, Gmail
"cannot send" verbatim, "Always enable human confirmation") and logged in SOURCES.md; datable
specifics stripped or flagged (stale tool counts, version headers); REBUILD LAW (no screenshots —
native rebuilt graphics); ILLUSTRATE LAW (Claude UI only in bookends); a `your-turn` handoff prompt;
title-restate outro. Free pipeline throughout (Kokoro, no paid spend).

**Also on Mac:** `CLAUDE-CODE-THEME-FACTORY-EXPLAINER.md` (the original theme-factory build prompt at repo root).

**One cleanup item:** a stray empty folder `claude-liam-linkedin-declined/` exists in the cloud workspace — ignore or delete; nothing was built there.

---

## 3. Batch build prompts  ✅ on your Mac

Two resumable, ledger-driven Claude Code prompts (each builds many reels unattended on your Mac,
Liam voice, 16:9, free pipeline; stop-and-repaste safe):

| File | What it builds | Scale |
|---|---|---|
| `CLAUDE-CODE-ANTHROPICS-SKILLS-EXPLAINERS-BATCH.md` | One skill-teardown reel per **unique SKILL.md under `anthropics/`** | ~400 unique skills (635 files); canonical `skills/` first; auto-opens each finished video |
| `CLAUDE-CODE-TOOLKIT-SKILLS-EXPLAINERS-BATCH.md` | One skill-teardown reel per **brutalist-art skill** (the meta-series) | ~46 skills; builds into `brutalist-art/youtube/`; auto-opens each |

Both write a ledger (`…BATCH-LOG.md`) as the resume state, dedupe, order best-first, and honor the
money hard-stop rule structurally by pinning to the free pipeline.

---

## 4. INFO 7375 course roadmaps — the full semester  ⏳ in cloud, pending Mac sync

Fourteen "series roadmaps," each breaking one assignment into a sequence of **hands-on how-to
ai-explainer episodes** (Liam voice, **Pragmatist** register, beginner-first). Every episode card
carries: premise, numbered teach-steps, beginner traps, the graded deliverable it produces, an
est. length, and a paste-ready Your Turn prompt. One `SERIES-ROADMAP-brand-launch-howto.md` (A8)
made it to the Mac before the bridge dropped; **the other thirteen are delivered in chat only.**

| Assignment | Roadmap file | Episodes | Sync |
|---|---|---|---|
| A1 — Foundation Setup (Figma) | `SERIES-ROADMAP-a1-foundation-howto.md` | 7 | ⏳ chat only |
| A2 — Madison PRD | `SERIES-ROADMAP-a2-prd-howto.md` | 7 | ⏳ chat only |
| A3 — Collect Data (n8n) | `SERIES-ROADMAP-a3-data-howto.md` | 7 | ⏳ chat only |
| A4 — Add Intelligence & Scale | `SERIES-ROADMAP-a4-intelligence-howto.md` | 7 | ⏳ chat only |
| A5 — Conductor Brief | `SERIES-ROADMAP-a5-conductor-brief-howto.md` | 7 | ⏳ chat only |
| A5A — Interface (Path A) | `SERIES-ROADMAP-a5a-wrap-your-tool-howto.md` | 6 | ⏳ chat only |
| A5B — Recipe Framework (Path B) | `SERIES-ROADMAP-a5b-build-the-recipe-howto.md` | 6 | ⏳ chat only |
| A6 — Brand Strategy & Naming | `SERIES-ROADMAP-a6-brand-identity-howto.md` | 7 | ⏳ chat only |
| Midterm — Investor Pitch Video | `SERIES-ROADMAP-a7-investor-pitch-howto.md` | 7 | ⏳ chat only |
| A7 — Visual Identity & Wireframes | `SERIES-ROADMAP-a7-visual-identity-howto.md` | 6 | ⏳ chat only |
| A8 — Website / Resumes / LinkedIn | `SERIES-ROADMAP-brand-launch-howto.md` | 8 | ✅ on Mac |
| A9 — Brand Storytelling | `SERIES-ROADMAP-a9-storytelling-howto.md` | 6 | ⏳ chat only |
| A10 — Substack Thought Leadership | `SERIES-ROADMAP-a10-thought-leadership-howto.md` | 5 | ⏳ chat only |
| Capstone — Complete Brand System | `SERIES-ROADMAP-capstone-brand-system-howto.md` | 6 | ⏳ chat only |

**~92 how-to episode cards** total, one consistent house shape, with honesty threads in every one
(the read-aloud gut-check, cite-your-sources, don't-fake-the-user-test, published-live-not-a-draft,
human-owns-the-truth) and toolkit tie-ins wired where they fit:

- `nina` (brand strategist) → A6, A7
- `brandy` (competitive audit) → A6, A7, Capstone
- `madison-pitch` (venture pitch) → Midterm, Capstone
- `skep:*` (Substack engine) → A10
- Brutalist/Remotion + `deck-lecture`/`brutalist-slides` → Midterm, Capstone production

The roadmaps deliberately chain: A1 context → A2 PRD → A3 data → A4 intelligence → A5 strategy
(+5A/5B forks) → A6 brand → pitch → A7 visual → A8 launch → A9 stories → A10 platform → Capstone
integration. Each assignment's output is the next one's input.

---

## Sync status at a glance

- **✅ Written to your Mac** (bridge was up): the `ai-explainer` rename + GLOSSARY + AGENTS.md rules; all 5 reels (full packages); both batch prompts; the theme-factory build prompt; the A8 roadmap.
- **⏳ In the cloud workspace only** (delivered in chat, bridge dropped): the other **13 course roadmaps**.

The device bridge's file tools (`device_stage_files` / `device_commit_files` / `device_bash` /
`device_list_dir`) have been offline for the latter part of the session — only `get_device_info`
responds, even though the books folder shows connected. That's why the 13 roadmaps didn't commit,
and why I couldn't open the local Madison folder (I used the GitHub repo instead).

**To fix:** reopen or refocus the Claude desktop app to restore the bridge — then I commit all 13
in one pass. If it stays down, starting this task again *on your computer* (the "Run this task"
picker, desktop app) works with your folders directly and sidesteps the bridge.

---

## Suggested next steps

1. **Restore the bridge → commit the 13 pending roadmaps** to `brutalist-art/youtube/`.
2. **Master INFO 7375 series index** — stitch all 14 roadmaps into one ordered ~92-episode playlist.
3. **Semester batch prompt** — a single resumable Claude Code prompt that builds every course
   how-to reel on your Mac (same ledger pattern as the two skill batches).
4. **Render the 5 finished reels** — each folder's `BUILD-PROMPT.md` builds its visuals on your Mac.
5. **Delete** the stray empty `claude-liam-linkedin-declined/` folder.
