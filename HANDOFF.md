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

## Current state (from git + disk, 2026-07-13)

- Branch `main`. Today's commits: `fd8c6d7` (videos 3+4 gate files + publish log), `c3cac9b`
  (caption restoration), `cc624dd` (video 4 rev-2 authoring), `714fc61` (shorts upgrade), plus the
  session wrap-up commit after this file. Remote `origin/main` is still at `fe8fb19` — **everything
  since is unpushed; `git push origin main` from the Mac sends it.**
- **Videos 1–4 are all PUBLISHED unlisted** in the "Brutalist" playlist (`PLG9H-C6rp5RU`):
  ch1 `xXKgCXc1nm4`, ch2 `7rUcwkFOhvM`, ch3 `AhdmP75PBY0`, ch4 `S7rmHr36C74` (rev 2 final,
  16/16 beats, 261.5s, includes the captions beat). Full record: `youtube/PUBLISH-LOG.md`.
- Video 4 went through **three uploads today**: rev 1 (`5iadw1MET3Q`, no captions beat), rev 2
  review cut (`PE2Zv8hBDzc`, uploaded from a master staged before `./art final`), rev 2 final
  (`S7rmHr36C74`, live and correct). The two superseded ones await Studio deletion.

## The series (this is the cursor)

Playlist **"Brutalist"** — the four series videos plus ~13 earlier brutalist experiments; the series
sits on top once the playlist is switched to manual sort (a pending Studio action). Full 26-item
build order and per-video status: `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/EXAMPLES-CAMPAIGN.md`.
**Next up: video 5 = slate-cut** (Tier 0, the no-key first pass).

## Decisions and changes recorded today

- **CC ships with every post** (`c3cac9b`): the vendored publisher had dropped caption upload; the
  ancestor `youtube_publish.py` had it. Restored — `youtube.force-ssl` scope (stale tokens force
  re-consent), `captions.insert` with backoff, idempotent via `captions.list`, `--no-captions` flag.
  `<slug>.srt` is written from the beat sheet (SOURCE narration text on measured beat windows, never
  a transcription pass); all four series videos have one. The lesson, logged in
  `CAMPAIGN-FEEDBACK.md`: *vendoring a script is a refactor — diff features against the ancestor.*
- **Video 4 rev 2** (`cc624dd`): the video explains the tool, so the captions feature joined the
  film — B03 became "four things" (adds the `.srt` line) and new beat B04A "captions ship with the
  post". `docs/posting-to-youtube.md` carries the matching sections including "The caption gap" in
  the honest record. Rebuild ran on the Mac per `youtube/posting-to-youtube/BUILD-PROMPT.md` REV 2.
- **Shorts pipeline** (`714fc61`, `runtime/scripts/shorts.py` + publisher + `./art shorts`):
  checks YouTube's hard 3:00 cap FIRST — at/under → full 16:9→9:16 reformat; over → auto-planned
  derivative cut (longest unprotected middle beats drop; hook/hero/outro protected; `--drop`/
  `--keep` override). A shortened cut rewrites the outro to say what was cut and send viewers to
  the long — the ONLY regenerated audio in a short. `pantry/<bid>-916.*` is the human replacement
  slot for center-cuts that don't work (wins over everything). Shorts always post to the "Shorts"
  playlist; the publisher anchors a derived short's description to its PARENT LONG via the ledger.
  **Not yet exercised end-to-end — the first real `./art shorts <reel>` run should be watched.**
- **Publisher --playlist default** is `$ART_PLAYLIST` (empty = required flag) after the stale
  hardcoded default created a wrong playlist mid-publish (fixed by the Mac build session).
- **`books/CLAUDE.md` (one level up, not in this repo) was rewritten**: video work routes to
  `brutalist-art/` from `books/`; a book's `youtube/` travels with that book; `brutalist-art/youtube/`
  is the meta-series exception; standing rules referenced.
- Standing rules #1–#4 unchanged (in `EXAMPLES-CAMPAIGN.md`); one addition from today's mixup:
  the master is staged AFTER `./art final` — the `mp4/<slug>.mp4 -> ../<slug>-cut.mp4` symlink
  convention prevents uploading a review cut.

## Working constraints

- Claude Code builds are folder-scoped to `brutalist-art/` for meta-series videos; book videos
  build into `<book>/youtube/<slug>/` per `books/CLAUDE.md`. Missing assets → log a `MISSING:` line.
- Never commit secrets: `.env` and `youtube/credentials/` are gitignored; media renders too.
- On the device mount, `git` cannot unlink `.git/index.lock` / `HEAD.lock` ("Operation not
  permitted") — move the stale lock aside (`mv`) and retry.
- Unlisted publishes via API need no audit; **public is a manual Studio flip — the human decides.**

## Open items

- `git push origin main` from the Mac (origin/main is behind at `fe8fb19`).
- **Studio cleanup pass**: delete superseded videos `5iadw1MET3Q` + `PE2Zv8hBDzc`; delete the
  accidental playlist "Quantum Mechanics Volume 1 (NotebookLM)" (`PLaOEYdBvYAog`); Brutalist
  playlist → sort Manual → drag ch1–ch4 to the top (ch4 right after *When Cowork*); while there,
  verify ch4's CC track and description anchor.
- First real shorts run: `./art shorts youtube/<slug>` on a finished reel, review the auto-plan,
  regenerate the funnel outro audio, compile at 1920, publish (defaults to the "Shorts" playlist).
- Flip the series videos to Public in Studio when ready.
- Video 5 = slate-cut (`EXAMPLES-CAMPAIGN.md` Tier 0). Longer-term backlog:
  `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/TODO.md` (+ candidate: `--pin-top N` playlist reorder;
  `videos.update` description push).

## Key files (absolute paths)

- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/EXAMPLES-CAMPAIGN.md` — campaign, per-video status, standing rules. **Start here.**
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/CAMPAIGN-FEEDBACK.md` — per-build refactor findings (incl. the vendoring lesson).
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/PUBLISH-LOG.md` — the honest publish record (three-upload rev history of video 4).
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/docs/` — per-video source docs; `docs/posting-to-youtube.md` includes the captions sections.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/runtime/scripts/shorts.py` — the 9:16 law (cap check, auto-shorten, pantry overrides).
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/skills/upload/youtube-publisher/scripts/publish_playlist.py` — upload + playlist + captions + funnel anchors.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/CLAUDE.md` — the books-level routing rules (youtube travels with the book).
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/art`, `runtime/`, `skills/` — the toolkit itself.

---

*To continue in a fresh session, paste:*

```
Read /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/HANDOFF.md, then continue.
```
