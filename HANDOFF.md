# HANDOFF — brutalist-art

**This repository is the source of truth.** Verify against the files (`git log`,
`EXAMPLES-CAMPAIGN.md`, the `youtube/` and `docs/` folders) rather than trusting this summary —
including this file. Where this disagrees with the files, the files win. Refresh this file with the
`handoff` skill at the end of a session so the one-line restart prompt below stays accurate.

## What this is

`brutalist-art` is a clone-and-go toolkit for making explainer + terminal videos with Claude Code,
Manim, and Remotion — audio-first, one self-contained folder per video (`youtube/<slug>/`, with
`beat_sheet.json` as the heart). It is also producing a meta YouTube series, **"Brutalist — Claude
for Video Production"** on @NikBearBrown: every video is made *by* the toolkit and *about* it. The
human owns taste and judgement; the machine does the mechanical build. That split ("you are the
conductor") is the series' running argument.

## Current state (from git + disk)

- Branch `main`, latest commit `d3b2e64` (this HANDOFF). Remote `origin` =
  github.com/nikbearbrown/brutalist-art; `origin/main` is at `fe8fb19`, so **local is ahead — commits
  `fe8fb19..d3b2e64` are unpushed** (a `git push origin main` from the Mac sends them).
- Uncommitted: `EXAMPLES-CAMPAIGN.md`, `CAMPAIGN-FEEDBACK.md`, and
  `youtube/posting-to-youtube/beat_sheet.json` modified; untracked build outputs for **videos 3 and 4**
  (`youtube/when-cowork-helps-claude-code/` and `youtube/posting-to-youtube/`: BUILD-LOG.md, scenes.py,
  gate files) plus `youtube/PUBLISH-LOG.md`. These are legitimate build/publish outputs — commit them
  once the cuts are confirmed good.

## The series (this is the cursor)

Playlist **"Brutalist"** — order = order made, *What is Brutalist?* always first. Full 26-item build
order and per-video status live in `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/EXAMPLES-CAMPAIGN.md`.

- **1 — What is Brutalist?** — BUILT. Ships its *review* cut on purpose (it keeps the review label it
  explains). PUBLISHED unlisted: https://youtu.be/xXKgCXc1nm4
- **2 — Installs, .env & Credentials** — BUILT (final `-cut`, frames verified). PUBLISHED unlisted:
  https://youtu.be/7rUcwkFOhvM
- **3 — When Cowork Can Help Claude Code** — BUILT (final `-cut`, 16/16). PUBLISHED unlisted:
  https://youtu.be/AhdmP75PBY0
- **4 — Posting to YouTube** — BUILT (a `-review` cut exists; **final `-cut` + publish still pending**).
- Playlist: https://www.youtube.com/playlist?list=PLG9H-C6rp5RU (three videos in it, unlisted).
- Next after video 4: **video 5 = slate-cut** (see EXAMPLES-CAMPAIGN.md, Tier 0).

Each video is self-contained under `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/<slug>/`: `beat_sheet.json` (heart),
`BUILD-PROMPT.md` (hand this to a fresh Claude Code session to build it), `README.md`, `BUILD-LOG.md`.
Its narration source is `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/docs/<slug>.md`.

## Decisions and standing rules (recorded in files)

- **Standing rules #1–#4** (in EXAMPLES-CAMPAIGN.md): (1) log human feedback first; (2) verify renders
  by looking at an actual frame and the `qc-sheet.png`; (3) render Remotion **only** via
  `runtime/scripts/remotion_scenes.py` (foreground — never background `npx remotion render`, never
  poll `ps`); (4) match Remotion `shot.remotion.props` to each component's zod schema, or the beat
  renders `Root.tsx` demo defaults (cancer / photoelectric placeholders).
- One folder = one video; audio-first; `beat_sheet.json` is the heart, `todo.json`/`STATUS.md` derived.
- `./art final <reel>` → clean master (`<slug>-cut.mp4`, no label); `./art run <reel>` → review cut.
- Publisher (`skills/upload/youtube-publisher/scripts/publish_playlist.py`): `--playlist "Brutalist"`,
  per-channel creds in `youtube/credentials/<channel>/` (gitignored). Default cross-links: shorts →
  intro video, longs → series playlist (`ART_ANCHOR_*` in .env). Unlisted publishes via API with no
  audit; **public** is gated by the compliance audit → do it as a manual Studio visibility flip.

## Working constraints

- Claude Code builds are **folder-scoped**: work only inside `brutalist-art/`; if something's missing,
  log a `MISSING:` line and stop that thread — don't reach into parent repos.
- Never commit secrets: `.env` and `youtube/credentials/` are gitignored. Media (mp4/mp3/png,
  `manim/`, `media/`) is gitignored too.
- On the device mount, `git` recreates `.git/index.lock` and can't unlink it ("Operation not
  permitted"). Move the lock aside and retry the commit.

## Open items

- Push the unpushed commits: `git push origin main` from the Mac (origin/main is behind at `fe8fb19`;
  local is `d3b2e64`).
- Commit the untracked build outputs for videos 3 and 4 (BUILD-LOG, scenes.py, gate files) and
  `youtube/PUBLISH-LOG.md` once those cuts are confirmed good.
- Video 4: `./art final youtube/posting-to-youtube`, review it, then publish (chapter_number 4 slots
  it after *When Cowork* in the Brutalist playlist).
- Flip the three published videos to Public in YouTube Studio when ready (API-public is audit-gated).
- Deferred by the user: shorts "Related video" chips + long-form end cards.
- Longer-term backlog in `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/TODO.md` (palette registry: add brutalist+musinique to Manim; vendor
  animated-deck as deck-lecture; `./art fill-in`; figure-planner SKILL.md; LICENSE).

## Key files (absolute paths)

- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/EXAMPLES-CAMPAIGN.md` — the campaign, per-video status, and standing rules. **Start here.**
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/CAMPAIGN-FEEDBACK.md` — per-build refactor findings.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/docs/` — per-video source docs + `README.md` index.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/<slug>/` — one folder per video (`beat_sheet.json`, `BUILD-PROMPT.md`, `BUILD-LOG.md`).
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/PUBLISH-LOG.md` — the publish-session record (basis of video 4).
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/TODO.md` — longer-term backlog. `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/art`, `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/runtime/`, `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/skills/` — the toolkit itself.

---

*To continue in a fresh session, paste:*

```
Read /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/HANDOFF.md, then continue.
```
