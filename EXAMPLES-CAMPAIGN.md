# Examples campaign — the toolkit tests itself by building every video

**The principle: you can't test the system without testing the system.** Static inspection guesses
at what's broken; building a real video of every type *finds* what's actually broken. So the old
"Phase 4.5 (fix first) then Phase 5 (build examples)" collapses into one loop — **validation by
construction.** Each example is simultaneously the acceptance test for its video type *and* the
shipped example that teaches it. Fixes are discovered by building, not guessed up front.

**Keys are validated free first.** Step 2 is `./art keys` — a no-spend live probe of every key/voice before any paid build (see the table). Every video here is **meta**: made *by* the toolkit, *about* the toolkit — the
"Brutalist — Claude for Video Production" playlist. The first is **"What is Brutalist?"**

## Where this runs

On **your machine, in Claude Code** — it has the ElevenLabs key, the `higgsfield` CLI, Manim,
Playwright/Chromium, Node/Remotion. (This cloud session set the campaign up; it can't render.)
Run unattended is fine (`claude --dangerously-skip-permissions`) — the render contract holds
(retry ≤5×, skip, human redoes).

## Scope: confined to `brutalist-art/` — report-and-add (the self-containment test)

Claude Code operates **only inside `brutalist-art/`**. It may NOT reach outside the folder — no
`../vox/`, no `../unreal-reels/`, no absolute paths to `books/…`, no `~/…`. Keys come from
`brutalist-art/.env` (already copied from `vox/.env`).

This is deliberate: it turns the "clone-and-go" goal into an enforced test. When a build needs
something that isn't in the folder, Claude Code does NOT quietly resolve it against a parent repo —
it **stops and reports** in the BUILD-LOG:

```
MISSING: <what it needed> — was at <where it used to live, if known> — blocks <which beat/step>
```

Then **we add it** — vendor the file/asset into `brutalist-art/` (a script → `runtime/scripts/`,
a shared asset → `runtime/`, a font → `runtime/fonts/`, brand media → the folder or an `ART_*`
path) — and re-run. Every `MISSING` report is one more reach-out eliminated. When the campaign
finishes with zero `MISSING` left, the toolkit is genuinely self-contained: a fresh clone builds
every video type with nothing but `brutalist-art/` + `.env`.

(This is why the campaign is the real acceptance test for the whole refactor: a reach-out that
static inspection missed becomes a loud `MISSING` the moment a real build needs it.)

## Standing rules (every build, every iteration)

1. **Log human feedback FIRST.** Before acting on any instruction I give, append it verbatim to the
   video's `BUILD-LOG.md` under a `## HUMAN FEEDBACK — <date>` heading. This is automatic — I should
   never have to ask for it.
2. **Verify renders by LOOKING.** Never report a visual fix as done without extracting a frame and
   checking it. "The box fits now" is only true if a mid-frame PNG shows the text inside the border.
   A fix that was discussed but not visually verified is not a fix.

## The loop (per video type)

1. **Build** it with Claude Code (start from the type's `BUILD-PROMPT.md`; `what-is-brutalist`
   already has one). One self-contained folder under `youtube/<slug>/`.
2. **Log everything** to `youtube/<slug>/BUILD-LOG.md`: every command run, every error hit, the
   fix applied, and the final result (beats rendered / beats left for human). Append-only.
3. **If something doesn't work, fix it** — in the *toolkit*, not just the example. A broken script,
   a stale path, a missing SKILL.md, a palette gap → fix in `runtime/`/`skills/`, commit with a
   message naming the video that surfaced it. **If the thing is simply not in the folder, log a
   `MISSING:` line and stop that thread** — the human vendors it in (report-and-add), then continue.
   The fix is the point; the example proved it was needed.
4. **Ship the example** — the finished folder stays as the CAPABILITIES/LEARN example for that type.
5. **Mark verified** in the table below (⬜ → ✅), note the commit(s) that fixed anything.

A type isn't "done" until its example builds end-to-end (minus genuinely-human beats) and every
breakage it hit is fixed and committed.

## The report that comes back to the refactor

Each build must end by appending a **structured feedback block** to its `BUILD-LOG.md` AND to the
shared **`CAMPAIGN-FEEDBACK.md`** at the repo root — so every build aggregates into one report the
refactor consumes (to update TODO, INSTALL, the doctor, and the vendor list). Format, verbatim:

```
## REFACTOR FEEDBACK — <video slug> — <YYYY-MM-DD>
MISSING (vendor into brutalist-art):
  - <file/asset> — was at <source, if known> — needed for <step/beat>
FIXED (toolkit bugs this build surfaced):
  - <what was wrong> — <file changed> — commit <hash>
DEPS (had to install / must be installed to build this type):
  - <dep> — for <step>   (e.g. "remotion node_modules — cd runtime/remotion && npm install")
STILL BLOCKED (needs a human decision / key / asset):
  - <what> — <what it needs>
RESULT: <N> beats rendered, <M> left for the human (list the M)
```

This block is the deliverable *to the refactor*. Paste `CAMPAIGN-FEEDBACK.md` back to the refactor
session; it maps 1:1 onto: MISSING → vendor list, FIXED → confirmed regressions closed, DEPS →
INSTALL.md + `./setup` rows, STILL BLOCKED → open gates.

## Build order — climb the key ladder (no-key first, so core-pipeline breakage surfaces first)

Legend: 🔑 keys needed · 📁 existing folder to rebuild-and-verify · ✨ new folder to create.

### Tier 0 — no keys (ffmpeg + Pillow; Manim/Node where noted). Fixes the core `./art run`/`fill-in`.
| # | Video | Skill | Folder | Status | Notes |
|---|---|---|---|---|---|
| 1 | **What is Brutalist?** | explainer + terminal | ✨ `youtube/what-is-brutalist` | ✅ | **DONE** — 16/16 beats rendered (174s, narrated); 0 MISSING; **5 toolkit bugs found & fixed** (commit `50df886`). 3 beats flagged for pacing review (B11/B06/B02). |
| 2 | **Installs, .env & credentials** | explainer + terminal | ✨ `youtube/installs` | ⬜ | **.env, credentials, npx/pip/venvs, the paid services + clone-your-voice.** Has `beat_sheet.json` (15 beats) + `BUILD-PROMPT.md`; source doc `docs/Installs.md`. Fully pipeline (0 human beats). **Second — build next.** |
| 3 | slate-cut | (compile) | 📁 `examples/slate-cut--base-rate` | ⬜ | the no-key first pass; verify `./art run` + request cards |
| 4 | previz | (fill_slates) | ✨ `youtube/previz-*` | ⬜ | any beat sheet → all-slate timing pass |
| 5 | line-art-vectorizer | line-art-vectorizer | ✨ `youtube/*` | ⬜ | vtracer, no key |
| 6 | figure-planner | figure-planner | ✨ `youtube/*` | ⬜ | **author its SKILL.md first** (D5), then a figure |
| 7 | sketch-explainer (silent) | sketch-explainer | ✨ `youtube/*` | ⬜ | Manim only, no key |

**GATE — key check (free, not a video).** **Run `./art keys` BEFORE any paid build.** Free live probes (ElevenLabs `/user`+`/voices`, higgsfield `account status`, YouTube `channels.list`=1 unit). Confirms every key/voice is valid + shows quota/credits. No spend. Fix any ❌ before Tier 1+.

### Tier 1 — ElevenLabs (narration)
| # | Video | Skill | Folder | Status |
|---|---|---|---|---|
| 8 | sketch-explainer (narrated) | sketch-explainer | ✨ | ⬜ |
| 9 | math-explainer | math-explainer | ✨ (+LaTeX) | ⬜ |
| 10 | explainer | explainer | 📁 `examples/explainer--size-paradox` | ⬜ |
| 11 | terminal-screencast | terminal-screencast | 📁 `examples/terminal-screencast--compression-journey` | ⬜ |
| 12 | bio | bio | ✨ (`--length` 3:00) | ⬜ |
| 13 | code-walkthrough | code-walkthrough | ✨ | ⬜ |
| 14 | kids-video | kids-video | ✨ | ⬜ |
| 15 | recitation-film | recitation-film | ✨ (+faster-whisper) | ⬜ |
| 16 | **deck-lecture** | deck-lecture | ✨ (vendor `animated-deck`; +Playwright) | ⬜ | restore one of the 34 lectures as the example |
| 17 | story-film (narration) | story-film | 📁 `examples/00-story-film-demos` | ⬜ |

### Tier 2 — higgsfield CLI (AI image/video)
| # | Video | Skill | Folder | Status |
|---|---|---|---|---|
| 18 | lyric-resync | lyric-resync | ✨ | ⬜ |
| 19 | dance-video | dance-video | ✨ | ⬜ |
| 20 | ai-asset-gen | ai-asset-gen | ✨ | ⬜ |
| 21 | collage-ads | collage-ads | ✨ | ⬜ |

### Tier 3 — local audio (bring a WAV)
| # | Video | Skill | Folder | Status |
|---|---|---|---|---|
| 22 | music-video | music-video | 📁 `examples/music-video--c-is-for-cookie` | ⬜ |
| 23 | lyric-overlay | lyric-overlay | ✨ | ⬜ |

### Final
| # | Video | Skill | Folder | Status |
|---|---|---|---|---|
| 24 | youtube-publisher | youtube-publisher | (publishes the built playlist) | ⬜ | OAuth; publishes everything above as the real playlist. **API quota: ~6 uploads/day** — the default 10,000 units/day ÷ 1,600 units per `videos.insert` = ~6, NOT the console's "100 uploads/day" (that limit never binds). So ~23 videos = ~4 days via API, unless you request a quota increase (adjustable, needs audit) or upload some manually via Studio (web uploads don't touch the API quota). **Chosen: publish via the API, batched ~6/day over ~4 days** (keeps the automation — transcript, chapters, description, playlist order, bookends — that Studio uploads lose). The API quota resets at **midnight Pacific (3:00 AM ET)**; the `ART_PUBLISH_LEDGER` tracks what's already up, so each daily run publishes the next unpublished batch until the playlist is complete. Can be a daily scheduled task. |

### Helpers to exercise along the way (not videos; no dedicated example)
`scout`, `cli-scout`, `script-writer`, `audience-preset`, `shot-planner`, `duration-planner`,
`explainer-deepen`, `reel-updater`, `remotion-explainer`, `component-showcase` (riff), `slate-filler`
— each gets used in service of the builds above; log any breakage the same way.

## Known fixes this campaign will force (from the TODO scan — expect to hit these early)

- `examples/*/scenes.py` import a dead `aspects/…` path → repoint to `runtime/manim` (Tier-0 #2/#9/#10).
- GATE F needs `PROMPTS.md`; QC gates now in `runtime/qc/` — verify they pass.
- `./art fill-in` doesn't exist yet — build it when the first Tier-0 video needs it.
- `figure-planner` has no SKILL.md (#5). No `LICENSE`. Manim registry missing `brutalist`+`musinique`.
- `deck-lecture` (#15) needs `animated-deck` vendored + Playwright.

Each of these should surface *as a build failure with a log entry*, get fixed in the toolkit, and
get a commit. That's the campaign working as intended: the videos find the bugs.
