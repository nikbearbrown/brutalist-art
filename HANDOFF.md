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
human owns taste and judgement; the machine does the mechanical build.

## Current state (from git + disk, end of 2026-07-13)

- Branch `main`, HEAD `d72cfc5`. `origin/main` is at `e7acb89` — **six commits unpushed**
  (`596d860` Onda check, `b2725ab` Suno path, `abd6307` cost-test sheet, `ec6ea20` merge slicer,
  `e8197f8` session skill, `d72cfc5` songbird). `git push origin main` from the Mac sends them.
- **Substantial in-flight, UNCOMMITTED work from active Mac build sessions** — do not treat the last
  commit as the full picture: the 916 portrait Remotion scenes are authored (`runtime/remotion/src/`
  Root.tsx + BrutalistTerminalOpen/NikBearBrownTerminalAsk/NikBearBrownCodeBlock/BrutalistCommentCTA
  modified), `shorts.py`/`generate_audio.py`/`art` carry session-side edits, all four series reels
  have `short/` folders, and the cost-test reel has a compiled review cut + COST-LOG.md +
  layout-audit artifacts. These commit when their builds pass their gates.

## The series (published)

Playlist **"Brutalist"** (`PLG9H-C6rp5RU`), all unlisted: ch1 `xXKgCXc1nm4`, ch2 `7rUcwkFOhvM`,
ch3 `AhdmP75PBY0`, ch4 `S7rmHr36C74` (rev 2 final, 16/16, captions beat). Superseded video-4 uploads
(`5iadw1MET3Q`, `PE2Zv8hBDzc`) and the accidental "Quantum Mechanics Volume 1 (NotebookLM)" playlist
were queued for manual Studio deletion — verify in Studio whether that cleanup happened.
Record: `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/PUBLISH-LOG.md`.

## In flight (three threads)

1. **Video 5 — "Suno vs 11 Labs Cost Test"** (`youtube/suno-vs-11-labs-cost-test/`): THE VIDEO IS
   THE EXPERIMENT — its narration voiced both ways. The decision stands that **both voice versions
   publish** (people compare; each description cross-links the other; the human picks only which is
   PRIMARY = chapter 5). Suno take sliced (mp3-suno/), ElevenLabs take generated (mp3-11labs/),
   review cut compiled, COST-LOG.md started, variant folder `youtube/suno-vs-11-labs-cost-test-11labs/`
   created. Remaining: both reels through QC gates → both finals → publish with cross-links → the
   music-bed version (needs the Suno **(Instrumental)** stem downloaded to pantry/; a continuous bed
   muxed under the finished cut — music is never sliced per beat).
2. **Shorts for videos 1–4**: `short/` folders exist in all four reels; the Onda-check cycle
   (REMOTION beats rewired to `<pattern>916` compositions, portrait re-renders, no center-cuts of
   generated media) was the active work. Gate: approval on four review cuts, then publish — shorts
   always to the "Shorts" playlist, descriptions anchor to the parent long (publisher does both
   automatically).
3. **"She Walks in Beauty"** (`youtube/she-walks-in-beauty/pantry/`): Byron 1814, session-directed
   Suno reading in Bear's voice, mastered wav + song.txt in pantry. Builds with the
   **recitation-film** skill (performance = master clock, GATE 0 alignment, karaoke-as-CC). Note the
   stanza breaks differ from Byron's printed 6/6/6 — the adaptation marker applies. Feeds video 19b.

## Decisions and capabilities added 2026-07-13 (all in committed docs)

- **The Suno voice path** (`b2725ab`, `ec6ea20`): `./art suno` exports narration as `.suno.N.txt`
  (4000-char chunks, beats never split) + `.suno.style.txt` session notes + a chunk map; the human
  generates in Suno and drops the VOCAL-ONLY stem in `pantry/`; `./art suno-slice` cuts it into
  `mp3/beat-*.mp3` with measured durations — the same interface `generate_audio.py` produces, so
  downstream never knows the engine. Over-split stems reconcile via the **expected-duration merge**
  (DP on narration-length shares, cuts at the biggest silences; off-target refuses). GATE P applies.
- **session is a skill** (`e8197f8`, `skills/make/session/`): direct the reading, don't label it —
  style-box session notes + `[spoken word — delivery]` tags per beat (per-beat `"delivery"` field
  overrides); the breath rule ("a full breath of silence between sections") is what keeps slicing
  clean. Poems take the authored path; exact text; adaptation-marker duty downstream.
- **songbird is a skill** (`d72cfc5`, `skills/make/songbird/`): THE SEQUENCING LAW (Entry–Beat–Exit,
  visual + musical continuity lanes) for every generated-clip prompt chain; engine map (song/boogie →
  music-video/dance-video authoring, `plug` → shorts-funnel cliffhanger, `169` → outpainting,
  parameter rule → style strings verbatim on every prompt line).
- **Shorts law** (`714fc61`, `596d860`, `runtime/scripts/shorts.py`): cap check first (≤3:00 → full
  reformat; over → auto beat-drop plan, hook/hero/outro protected); shortened cuts rewrite the outro
  to name the cuts and point to the long (the only regenerated audio); `pantry/<bid>-916.*` is the
  human override slot; **THE ONDA CHECK** — REMOTION beats are typed by the sheet, never by folder,
  rewired to `<pattern>916` compositions, never center-cut.
- **Captions law** (`c3cac9b`): CC ships with every post — `<slug>.srt` from the beat sheet (source
  text on measured windows), `captions.insert`, idempotent, `force-ssl` scope.
- **Publisher**: `--playlist` defaults from `$ART_PLAYLIST` (stale hardcoded default caused a wrong
  playlist mid-publish); all-shorts runs default to "Shorts"; derived shorts anchor to their parent
  long via the ledger; masters are staged AFTER `./art final` (the rev-2 review-cut mixup lesson —
  `mp4/<slug>.mp4 -> ../<slug>-cut.mp4` symlink convention).
- **Campaign additions**: 19a cost test (in flight), 19b "Session, Karaoke & Audiogram"
  (BUILD-PROMPT ready — session + `align.py` word clock + lyric-overlay audiogram, Byron threaded
  through as the worked example).

## Working constraints

- Standing rules #1–#4 in `EXAMPLES-CAMPAIGN.md` govern every build (feedback logged first; verify
  renders BY LOOKING; Remotion only via `remotion_scenes.py` foreground; props match zod or the beat
  renders demo defaults — "CANCER BIOLOGY" on screen is the tell).
- Audio-first: narration (either engine) is the master clock. One folder = one video.
- `books/CLAUDE.md` (one level up) routes video work here; a book's `youtube/` travels with the book;
  `brutalist-art/youtube/` is the meta-series exception.
- Never commit secrets (`.env`, `youtube/credentials/`) or media renders. On the device mount, stale
  `.git/*.lock` files can't be unlinked — move them aside and retry.
- Unlisted publishes need no audit; public is a manual Studio flip — the human decides.

## Open items

- `git push origin main` (six commits behind).
- Cost-test thread: gates → two finals → publish both with cross-linked descriptions (human picks
  the PRIMARY for chapter 5) → music-bed version (needs the Instrumental stem in pantry/).
- Shorts thread: four review cuts through approval → publish to "Shorts".
- Studio: verify the video-4 cleanup (two superseded deletions + wrong playlist) and the playlist
  manual-sort drag (series ch1–ch5 on top) happened.
- Byron: build `she-walks-in-beauty` with recitation-film; then video 19b.
- Backlog candidates noted in feedback: `--plug` cliffhanger flag for the shorts outro; a
  remotion_scenes.py guard that hard-fails when zod validation falls back to demo defaults; `--align`
  forced-alignment mode for suno_slice; `--pin-top` playlist reorder; `videos.update` description
  push. Longer list: `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/TODO.md`.

## Key files (absolute paths)

- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/EXAMPLES-CAMPAIGN.md` — campaign + standing rules. **Start here.**
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/CAMPAIGN-FEEDBACK.md` — per-build findings (vendoring lesson, Onda check, merge slicer).
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/PUBLISH-LOG.md` — the honest publish record.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/runtime/scripts/` — `suno_export.py`, `suno_slice.py`, `shorts.py`, `align.py`, `generate_audio.py`, `stage_publish.py`.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/skills/make/session/SKILL.md` and `skills/make/songbird/SKILL.md` — the new skills.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/skills/upload/youtube-publisher/scripts/publish_playlist.py` — upload + playlist + captions + anchors.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/suno-vs-11-labs-cost-test/` (+ `-11labs/` variant) and `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/she-walks-in-beauty/` — the in-flight reels.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/CLAUDE.md` — books-level routing (youtube travels with the book).

---

*To continue in a fresh session, paste:*

```
Read /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/HANDOFF.md, then continue.
```
