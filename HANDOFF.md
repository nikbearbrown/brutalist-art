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

## Current state (verified against git + disk, 2026-07-13 status audit)

- Branch `main`, HEAD `9a6390f` (end-of-day handoff commit). `origin/main` is at `e7acb89` —
  **seven commits unpushed** (`596d860` Onda check, `b2725ab` Suno path, `abd6307` cost-test
  sheet, `ec6ea20` merge slicer, `e8197f8` session skill, `d72cfc5` songbird, `9a6390f` handoff).
  `git push origin main` from the Mac sends them. Note: a stale `.git/index.lock` exists on the
  device mount and can't be unlinked there — move it aside from the Mac if git refuses to run.
- **Substantial uncommitted work from active Mac build sessions** — the last commit is not the
  full picture: the 916 portrait Remotion scenes are authored (`runtime/remotion/src/` Root.tsx +
  four scene components modified), `shorts.py`/`generate_audio.py`/`art` carry session-side edits,
  all four series reels have compiled `short/` folders, the cost-test reel has both review cuts +
  COST-LOG.md + layout audits, and video 19b (`session-karaoke-audiogram`) is fully authored.
  These commit when their builds pass their gates.
- **Known blocker: `ELEVENLABS_API_KEY` is invalid (HTTP 401).** All four shorts hit it when
  regenerating the rewritten outro B99 — each currently carries a 16-second SILENCE placeholder
  outro. The key must be fixed, then `generate_audio.py --only B99` re-run per short and the
  shorts recompiled, before the review cuts are worth approving.
- The `youtube/` folder has also accumulated **non-series side-project folders** from music-video /
  dance / recitation sessions (all untracked): `boogeyman`, `c-is-for-cookie`,
  `five-little-speckled-frogs`, `godel`, `itsy-bitsy-spider`, `lift-every-voice-and-sing`,
  `little-red-cap`, `miniver-cheevy`, `mon-homme`, `prufrock`, `who-s-gonna-bell-that-cat`, plus a
  `higgsfield/` docs folder at the root. These are not part of the Brutalist meta-series; whether
  they stay here or move with their books (per `books/CLAUDE.md` routing) is an open call.

## The series (published)

Playlist **"Brutalist"** (`PLG9H-C6rp5RU`), all unlisted: ch1 `xXKgCXc1nm4`, ch2 `7rUcwkFOhvM`,
ch3 `AhdmP75PBY0`, ch4 `S7rmHr36C74` (rev 2 final, 16/16, captions beat). Superseded video-4
uploads (`5iadw1MET3Q`, `PE2Zv8hBDzc`) and the accidental "Quantum Mechanics Volume 1 (NotebookLM)"
playlist (`PLaOEYdBvYAog`) were queued for manual Studio deletion — **still unverified as of the
2026-07-13 audit** (a remote check was attempted but blocked; needs a human Studio pass, along
with the playlist manual-sort drag putting ch1–ch4 on top).
Record: `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/PUBLISH-LOG.md`.

## In flight (four threads)

1. **Video 5 — "Suno vs 11 Labs Cost Test"** (`youtube/suno-vs-11-labs-cost-test/` +
   `-11labs/` variant): THE VIDEO IS THE EXPERIMENT — its narration voiced both ways. The decision
   stands that **both voice versions publish** (each description cross-links the other; the human
   picks only which is PRIMARY = chapter 5). State verified: both review cuts compiled
   (2026-07-13 14:43/14:44), both layout audits clean (10 snapshots, 0 errors, 0 warnings each),
   COST-LOG.md drafted with **three open [HUMAN] fields** (Suno credits per generation, plan cost,
   wall time of the Suno steps) — B08's cost-table scene renders only after those are filled.
   No finals yet (`mp4/` holds only review cuts). Remaining: human fills COST-LOG fields +
   approves both review cuts → B08 update → gates → both finals → publish with cross-links →
   the music-bed version (needs the Suno **(Instrumental)** stem downloaded to pantry/; a
   continuous bed muxed under the finished cut — music is never sliced per beat).
2. **Shorts for videos 1–4**: further along than the previous handoff recorded — all four
   (`what-is-brutalist`, `installs`, `when-cowork-helps-claude-code`, `posting-to-youtube`) have
   portrait `short/` builds with review AND cut mp4s compiled, Onda-check rewiring done, beat-drop
   plans logged in each BUILD-LOG. **But every outro B99 is a silence placeholder** (the
   ELEVENLABS_API_KEY 401 above) — fix key, regenerate four B99s, recompile, then human approval
   on the four review cuts, then publish (shorts always to the "Shorts" playlist; descriptions
   anchor to the parent long; the publisher does both automatically). A shorts.py double-count
   display bug (beat_dur returns estimated when actual=0 is falsy) is logged in
   CAMPAIGN-FEEDBACK.md.
3. **Video 19b — "Session, Karaoke & Audiogram"** (`youtube/session-karaoke-audiogram/`): fully
   authored — PEDAGOGY.md, beat_sheet.json, scenes.py (5 Manim beats, SYNTAX OK), Remotion props
   verified against exact zod schemas, Suno export files ready (`.suno.1.txt`, `.suno.style.txt`,
   chunk map). ⛔ **At its human gate**: paste the style + lyrics files into Suno, generate with
   Bear's voice, download the VOCAL-ONLY stem to
   `youtube/session-karaoke-audiogram/pantry/session-karaoke-audiogram-vocals-1.wav`, then signal
   ready (Claude runs `./art suno-slice` + Manim + Remotion + `./art run`). Uses the Byron audio
   as its worked example.
4. **"She Walks in Beauty"** (`youtube/she-walks-in-beauty/pantry/`): Byron 1814, mastered wav +
   song.txt in pantry, unchanged since the last handoff. Builds with the **recitation-film** skill
   (performance = master clock, GATE 0 alignment, karaoke-as-CC). The stanza breaks differ from
   Byron's printed 6/6/6 — the adaptation marker applies. Feeds 19b.

## Decisions and capabilities added 2026-07-13 (all in committed docs)

- **The Suno voice path** (`b2725ab`, `ec6ea20`): `./art suno` exports narration as `.suno.N.txt`
  (4000-char chunks, beats never split) + `.suno.style.txt` session notes + a chunk map; the human
  generates in Suno and drops the VOCAL-ONLY stem in `pantry/`; `./art suno-slice` cuts it into
  `mp3/beat-*.mp3` with measured durations — the same interface `generate_audio.py` produces, so
  downstream never knows the engine. Over-split stems reconcile via the **expected-duration merge**
  (DP on narration-length shares, cuts at the biggest silences; off-target refuses). The first
  real stem (3:33, 27 silence segments → 13 beats, worst Δ −4.0s) sliced clean. GATE P applies.
  Backlog: `--align` forced-alignment mode as the gold path.
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
- **Campaign additions**: 19a cost test (in flight), 19b "Session, Karaoke & Audiogram" (now
  authored, at its audio gate — see thread 3).

## Working constraints

- Standing rules #1–#4 in `EXAMPLES-CAMPAIGN.md` govern every build (feedback logged first; verify
  renders BY LOOKING; Remotion only via `remotion_scenes.py` foreground; props match zod or the beat
  renders demo defaults — "CANCER BIOLOGY" on screen is the tell).
- Audio-first: narration (either engine) is the master clock. One folder = one video.
- `books/CLAUDE.md` (one level up) routes video work here; a book's `youtube/` travels with the book;
  `brutalist-art/youtube/` is the meta-series exception (side-project folders listed above are
  pending that routing call).
- Never commit secrets (`.env`, `youtube/credentials/`) or media renders. On the device mount, stale
  `.git/*.lock` files can't be unlinked — move them aside and retry.
- Unlisted publishes need no audit; public is a manual Studio flip — the human decides.

## Smithsonian Open Access library (added 2026-07-22)

A METADATA-FIRST pipeline for CC0 archival stills feeding vox beats in
`deep-explainer` and `ai-explainer` reels. Three new files + library directory:

- **`runtime/scripts/smithsonian_index.py`** — build/update the index.
  API mode (recommended): `python3 runtime/scripts/smithsonian_index.py` (reads
  `SI_API_KEY` from `.env`). S3 streaming mode (no key): `--s3`. Scoped to 7
  register units (NMAH, NASM, NPG, NMAAHC, SIL, SIA, SAAM) — CC0 + has-image
  only. Writes `library/smithsonian/index.jsonl` (JSONL, one row per object:
  id / title / unit / credit / object_type / date / thumbnail_url / tokens) and
  `index_meta.json` (build stats). **Architecture note:** API-mode index does
  NOT store image_url (the search API response doesn't include the download URL
  reliably); image_url is resolved at fetch time via `/content/{id}`. S3-mode
  index DOES store image_url (full EDAN records available in the S3 files).
  Run with `--stats` to see row counts.
  Add `SI_API_KEY=` to `.env` (free key from https://api.data.gov/signup/).

- **`runtime/scripts/smithsonian_fetch.py`** — per-object fetch + upscale +
  shelve. Input: `--id <SI_ID>` or a text query (interactive picker). Steps:
  (1) resolve from index; (2) if no image_url in record, call SI content-detail
  endpoint `GET /content/{id}?api_key=KEY` to resolve full-res CC0 URL;
  (3) download full-res CC0 image; (4) upscale with
  `tpai --cli <in> --output <dir> --format jpg` (Topaz Photo AI at
  `/Applications/Topaz Photo AI.app/Contents/Resources/bin/tpai`); (5) shelve
  to `library/smithsonian/images/si-<id>-<slug>.jpg` with mandatory
  `.source.txt` sidecar (CC0, id, title, credit, resolved URL); (6) with
  `--copy <reel> --beat <BID>`, drops the result into
  `<reel>/pantry/<BID>-<slug>.png` for pantry intake. Scoring ranks apparatus
  types (computer, console, instrument) +1.5 over ephemera (pamphlet, manual)
  -1.0. Already-shelved images returned from cache — no re-download.

- **`runtime/scripts/pantry_search.py`** — extended to query BOTH the local
  doodle library AND the Smithsonian index. Smithsonian hits are labeled
  `[smithsonian]` with credit and thumbnail URL shown. The `--copy` flag still
  works for local hits; for SI hits it prints the exact `smithsonian_fetch.py`
  command. `--source local|smithsonian|all` (default: all).

- **`library/smithsonian/`** — the library root: `index.jsonl`, `index_meta.json`,
  `images/` (shelved CC0 stills), `README.md` (full setup + runtime loop docs).

**Runtime loop** (per vox beat):
```
pantry_search "<terms>"  →  look at SI thumbnails  →  smithsonian_fetch --id <ID> --copy <reel> --beat <BID>  →  pantry.py <reel>
```

**Key rule**: NEVER bulk-download media. One image per explicit accept.
CC0 = rights cleared; the `.source.txt` sidecar is the full provenance record.

## Open items

- Fix `ELEVENLABS_API_KEY` (401) — blocks the four shorts' B99 outros.
- `git push origin main` (seven commits behind).
- Cost-test thread: fill the three `[HUMAN]` COST-LOG fields → B08 table scene → approve both
  review cuts → gates → two finals → publish both with cross-linked descriptions (human picks the
  PRIMARY for chapter 5) → music-bed version (needs the Instrumental stem in pantry/).
- Shorts thread: after the key fix + B99 regen + recompile, four review cuts through approval →
  publish to "Shorts".
- 19b: generate the Suno vocal stem (steps in `youtube/session-karaoke-audiogram/BUILD-LOG.md`
  gate block) → signal ready.
- Studio (still unverified): delete `5iadw1MET3Q` and `PE2Zv8hBDzc`; delete playlist
  `PLaOEYdBvYAog`; Brutalist playlist → Manual sort, ch1–ch4 dragged to the top.
- Byron: build `she-walks-in-beauty` with recitation-film.
- Decide where the non-series `youtube/` side-project folders live.
- Backlog candidates noted in feedback: `--plug` cliffhanger flag for the shorts outro; a
  remotion_scenes.py guard that hard-fails when zod validation falls back to demo defaults;
  `--align` forced-alignment mode for suno_slice; `--pin-top` playlist reorder; `videos.update`
  description push; shorts.py duration double-count fix. Longer list:
  `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/TODO.md`.

## Key files (absolute paths)

- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/EXAMPLES-CAMPAIGN.md` — campaign + standing rules. **Start here.**
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/CAMPAIGN-FEEDBACK.md` — per-build findings (vendoring lesson, Onda check, merge slicer, first-stem results).
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/PUBLISH-LOG.md` — the honest publish record.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/runtime/scripts/` — `suno_export.py`, `suno_slice.py`, `shorts.py`, `align.py`, `generate_audio.py`, `stage_publish.py`.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/skills/make/session/SKILL.md` and `skills/make/songbird/SKILL.md` — the new skills.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/skills/upload/youtube-publisher/scripts/publish_playlist.py` — upload + playlist + captions + anchors.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/suno-vs-11-labs-cost-test/` (+ `-11labs/` variant), `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/session-karaoke-audiogram/`, and `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/she-walks-in-beauty/` — the in-flight reels.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/CLAUDE.md` — books-level routing (youtube travels with the book).

---

*To continue in a fresh session, paste:*

```
Read /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/HANDOFF.md, then continue.
```
