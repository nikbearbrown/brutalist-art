# PUBLISH-LOG — "Brutalist — Claude for Video Production" playlist
# append-only — this log is the basis for the next video, "posting to YouTube"

## Session start — 2026-07-13

Publishing three videos to @NikBearBrown, playlist "Brutalist", chapter order.
Channel: nikbearbrown
Privacy requested: unlisted (expected to land as PRIVATE — API compliance audit pending)

### Prereq check — PASS

| Video | mp4 master | description.txt | ch# | title |
|-------|-----------|----------------|-----|-------|
| what-is-brutalist | youtube/what-is-brutalist/mp4/what-is-brutalist.mp4 ✓ (REVIEW cut, intentional) | 1110 bytes ✓ | 1 | What is Brutalist? |
| installs | youtube/installs/mp4/installs.mp4 ✓ | 920 bytes ✓ | 2 | Installs, .env & Credentials |
| when-cowork-helps-claude-code | youtube/when-cowork-helps-claude-code/mp4/when-cowork-helps-claude-code.mp4 ✓ | 1016 bytes ✓ | 3 | When Cowork Can Help Claude Code |

OAuth creds: youtube/credentials/nikbearbrown/client_secret.json ✓, youtube_token.json ✓

Skill read: skills/upload/youtube-publisher/SKILL.md — note: ART_HOME env not set;
passing --client and --token explicitly to avoid path mis-resolution.

### DRY RUN — 2026-07-13

Command:
  python3 skills/upload/youtube-publisher/scripts/publish_playlist.py \
    youtube/what-is-brutalist youtube/installs youtube/when-cowork-helps-claude-code \
    --playlist "Brutalist" --channel nikbearbrown --privacy unlisted \
    --client youtube/credentials/nikbearbrown/client_secret.json \
    --token youtube/credentials/nikbearbrown/youtube_token.json \
    --ledger youtube/credentials/nikbearbrown/youtube_publish_ledger.json \
    --dry-run

Output:
  [yt] publish order (by chapter):
     ch1  What is Brutalist?
     ch2  Installs, .env & Credentials
     ch3  When Cowork Can Help Claude Code
  [yt] dry-run — authenticating read-only preview
  [yt] found playlist 'Brutalist' → PLG9H-C6rp5RU
  [yt] (dry-run) would upload what-is-brutalist
  [yt] (dry-run) would upload installs
  [yt] (dry-run) would upload when-cowork-helps-claude-code
  [yt] done.

VERDICT: order correct (ch1→ch2→ch3), playlist exists, OAuth valid. Proceeding with real upload.

### REAL UPLOAD — Run 1 — 2026-07-13

Command: (same, without --dry-run)

Output:
  [yt] found playlist 'Brutalist' → PLG9H-C6rp5RU
  [yt] uploading what-is-brutalist.mp4 …
  [yt] uploaded → https://youtu.be/xXKgCXc1nm4
  ERROR: HttpError 400 "Playlist should use manual sorting to support position."
  Detail: the "Brutalist" playlist uses auto-sort; passing position= in
  playlistItems.insert() is rejected when the playlist doesn't have manual ordering.
  what-is-brutalist uploaded to YouTube but NOT yet added to playlist.

FIX: Removed "position": pos from the playlistItems.insert() body in publish_playlist.py.
  This is a toolkit bug — the script should not require manual sorting. Fix committed inline.

### REAL UPLOAD — Run 2 — 2026-07-13

Command: (same script, fixed position removal)

Output:
  [yt] found playlist 'Brutalist' → PLG9H-C6rp5RU
  [yt] what-is-brutalist already uploaded → xXKgCXc1nm4
  [yt] added what-is-brutalist to playlist at position 0
  [yt] uploading installs.mp4 …
  [yt] uploaded → https://youtu.be/7rUcwkFOhvM
  [yt] added installs to playlist at position 1
  [yt] uploading when-cowork-helps-claude-code.mp4 …
  [yt] uploaded → https://youtu.be/AhdmP75PBY0
  [yt] added when-cowork-helps-claude-code to playlist at position 2
  [yt] done.

### PRIVACY STATUS CHECK — via videos.list API — 2026-07-13

| Video | ID | Privacy | Title |
|-------|----|---------|-------|
| what-is-brutalist | xXKgCXc1nm4 | **unlisted** | What is Brutalist? |
| installs | 7rUcwkFOhvM | **unlisted** | Installs, .env & Credentials |
| when-cowork-helps-claude-code | AhdmP75PBY0 | **unlisted** | When Cowork Can Help Claude Code |
| playlist "Brutalist" | PLG9H-C6rp5RU | **public** | — |

SURPRISE: All three videos landed as UNLISTED — not PRIVATE as the SKILL.md warned.
The note in the script says "a fresh YouTube API project can't make uploads public until
Google approves an API audit" — but unlisted worked. The API compliance audit may already
be approved for this channel's project, or unlisted is permitted without audit (only `public`
requires it). Either way, the actual privacy matches the requested --privacy unlisted flag.
The playlist itself is public (it was already public — we reused it, didn't create it).

### FINAL SUMMARY — 2026-07-13

Videos live:
  ch1  https://youtu.be/xXKgCXc1nm4   What is Brutalist?              (unlisted)
  ch2  https://youtu.be/7rUcwkFOhvM   Installs, .env & Credentials    (unlisted)
  ch3  https://youtu.be/AhdmP75PBY0   When Cowork Can Help Claude Code (unlisted)

Playlist: https://www.youtube.com/playlist?list=PLG9H-C6rp5RU  "Brutalist" (public)

Ledger updated: youtube/credentials/nikbearbrown/youtube_publish_ledger.json

Toolkit bug surfaced and fixed: publish_playlist.py passed position= to playlistItems.insert()
  but the playlist uses auto-sort. Removed position= — script now works with any playlist type.
  This is the kind of bug only a real publish catches. Good candidate for the next video.

ART_HOME env not set → had to pass --client/--token/--ledger explicitly.
  Future builds should set ART_HOME in .env to avoid this.

---

## Session — 2026-07-13 — Video 4 publish

### DRY RUN

Command:
  python3 skills/upload/youtube-publisher/scripts/publish_playlist.py \
    youtube/posting-to-youtube \
    --playlist "Brutalist" \
    --client youtube/credentials/nikbearbrown/client_secret.json \
    --token youtube/credentials/nikbearbrown/token.json \
    --ledger youtube/credentials/nikbearbrown/youtube_publish_ledger.json \
    --dry-run

Output:
  [yt] publish order (by chapter):
     ch4  Posting to YouTube
  [yt] dry-run — authenticating read-only preview
  [yt] found playlist 'Brutalist' → PLG9H-C6rp5RU
  [yt] (dry-run) would upload posting-to-youtube
  [yt] done.

VERDICT: ch4 in correct order, playlist confirmed. Proceeding with real upload.

### REAL UPLOAD — 2026-07-13

Output:
  [yt] found playlist 'Brutalist' → PLG9H-C6rp5RU
  [yt] uploading posting-to-youtube.mp4 …
  [yt] uploaded → https://youtu.be/5iadw1MET3Q
  [yt] added posting-to-youtube to playlist at position 0
  [yt] done.

No errors. No bug this time — position= was already removed from publish_playlist.py in the
previous session, so the fixed script ran clean.

### PRIVACY STATUS CHECK — via videos.list API — 2026-07-13

| Video | ID | Privacy |
|-------|----|---------|
| posting-to-youtube | 5iadw1MET3Q | **unlisted** |

Confirmed unlisted as expected.

### FINAL SUMMARY — 2026-07-13 (Video 4)

  ch4  https://youtu.be/5iadw1MET3Q   Posting to YouTube  (unlisted)

Playlist now has 4 videos:
  ch1  https://youtu.be/xXKgCXc1nm4   What is Brutalist?
  ch2  https://youtu.be/7rUcwkFOhvM   Installs, .env & Credentials
  ch3  https://youtu.be/AhdmP75PBY0   When Cowork Can Help Claude Code
  ch4  https://youtu.be/5iadw1MET3Q   Posting to YouTube

Ledger: youtube/credentials/nikbearbrown/youtube_publish_ledger.json updated.
Note: ledger key used this session: "youtube/credentials/nikbearbrown/youtube_publish_ledger.json"
  (the PUBLISH-LOG.md path used in the previous session was incorrect — that file is Markdown,
  not JSON. The real JSON ledger is in youtube/credentials/nikbearbrown/).

---

## Session — 2026-07-13 — Video 4 REV 2 (captions beat)

REV 2 adds B03 update (four things, .srt line) and B04A_CaptionsRight (new beat).
Supersedes https://youtu.be/5iadw1MET3Q (human deletes in Studio).

### REAL UPLOAD — REV 2 — 2026-07-13

Run 1 (wrong playlist — publisher default was stale):
  Command: python3 skills/upload/youtube-publisher/scripts/publish_playlist.py youtube/posting-to-youtube
  Output: created playlist 'Quantum Mechanics Volume 1 (NotebookLM)' → PLaOEYdBvYAog
          uploaded → https://youtu.be/PE2Zv8hBDzc
          caption track added
  BUG: publisher's --playlist default was hardcoded to "Quantum Mechanics Volume 1 (NotebookLM)"
       instead of requiring explicit input. Video uploaded to wrong playlist.
  FIX: changed default to os.getenv("ART_PLAYLIST", "") + empty-string guard. Committed.

Run 2 (correct playlist):
  Command: python3 skills/upload/youtube-publisher/scripts/publish_playlist.py
           youtube/posting-to-youtube --playlist "Brutalist"
  Output: found playlist 'Brutalist' → PLG9H-C6rp5RU
          posting-to-youtube already uploaded → PE2Zv8hBDzc
          added posting-to-youtube to playlist at position 0
          caption track already present — skipping
          done.

### HUMAN ACTION NEEDED

1. Delete accidentally-created playlist "Quantum Mechanics Volume 1 (NotebookLM)"
   (PLaOEYdBvYAog) in YouTube Studio. It has the posting-to-youtube video in it.
2. Delete superseded video https://youtu.be/5iadw1MET3Q in YouTube Studio (unlisted).

### FINAL SUMMARY — REV 2 — 2026-07-13

  ch4  https://youtu.be/PE2Zv8hBDzc   Posting to YouTube (REV 2, 16/16, captions)  (unlisted)

Playlist "Brutalist" (PLG9H-C6rp5RU) now has:
  ch1  https://youtu.be/xXKgCXc1nm4   What is Brutalist?
  ch2  https://youtu.be/7rUcwkFOhvM   Installs, .env & Credentials
  ch3  https://youtu.be/AhdmP75PBY0   When Cowork Can Help Claude Code
  ch4  https://youtu.be/PE2Zv8hBDzc   Posting to YouTube (REV 2)

Captions: posting-to-youtube.srt uploaded (16 cues, 262s) — source text on measured timing.
Ledger: youtube/credentials/nikbearbrown/youtube_publish_ledger.json updated ("posting-to-youtube": "PE2Zv8hBDzc").

### REV 2 CORRECTION — the review cut went up first — 2026-07-13

Human review caught it: PE2Zv8hBDzc was uploaded from a master staged BEFORE
`./art final` ran — the rev-2 REVIEW cut, wearing its label. The clean final
(261.5s, frame-verified: B03 four-things line, B04A captions card, no label)
existed on disk; `mp4/posting-to-youtube.mp4` now symlinks it.

Fix: ledger entry PE2Zv8hBDzc removed; publisher re-run uploaded the clean final.

### FINAL SUMMARY — REV 2 FINAL — 2026-07-13

  ch4  https://youtu.be/S7rmHr36C74   Posting to YouTube (rev 2 FINAL, 16/16, 261.5s)  (unlisted)

One publisher run = upload + playlist + captions (verify CC + position in Studio
during the cleanup pass).

HUMAN ACTIONS (Studio):
  1. Delete superseded videos: https://youtu.be/5iadw1MET3Q (rev 1) and
     https://youtu.be/PE2Zv8hBDzc (rev 2 review cut).
  2. Delete accidentally-created playlist "Quantum Mechanics Volume 1 (NotebookLM)" (PLaOEYdBvYAog).
  3. Brutalist playlist → sort Manual → drag ch1–ch4 to the top, ch4 directly
     after "When Cowork Can Help Claude Code".

Lesson for the reel: stage the master AFTER `./art final`, never between run and
final — the symlink convention (mp4/<slug>.mp4 -> ../<slug>-cut.mp4) prevents this.

---

## Kokoro: Free Voices (With Names) — 2026-07-13

  ch6  https://youtu.be/yoE2eRBS54w   Kokoro: Free Voices (With Names) (11/11, 142.7s, kokoro-onnx 0.4.7) (unlisted)

Audio: B00 ElevenLabs (Bear's clone, ~$0.02) + 10 Kokoro beats ($0.00).
CC: kokoro-free-voices.srt uploaded (11 cues).
Playlist: PLMn-aa84DxJk (Brutalist — Claude for Video Production) — created this run; ch6 at position 0.

HUMAN ACTIONS (Studio):
  1. Flip to public when ready.
  2. Drag ch6 to correct position in Brutalist playlist (after Suno vs 11 Labs, before She Walks in Beauty).
  3. Verify caption timing on the video page.
ch6-short https://youtu.be/Nm74XCgLYuM — Kokoro: Free Voices (9:16 Short, 147.2s, Shorts playlist) (unlisted)
ch6b https://youtu.be/Oxv763As98Q — Kokoro: All 28 English Voices (30/30, 196.5s, KokoroRosterCard, 19 grade corrections) (unlisted)
ch6c https://youtu.be/OjsNHrZcvhg — Kokoro: The 8 Mandarin Voices (10/10, 72.3s, bilingual CJK+EN subtitle) (unlisted)
ch6c-short https://youtu.be/443par7cVSY — Kokoro: The 8 Mandarin Voices (9:16 Short, Shorts playlist) (unlisted)
ch6e https://youtu.be/BZ557c_XSow — Kokoro: The 4 Hindi Voices (6/6, 46.3s, Devanagari+EN subtitle, CC uploaded) (unlisted)
ch6e-short https://youtu.be/R25_ZNotE98 — Kokoro: The 4 Hindi Voices (9:16 Short, Shorts playlist) (unlisted)
ch6f https://youtu.be/p2ZZlYHUPXA — Kokoro: The 9 Romance-Language Voices (11/11, 74.1s, bilingual subtitles, gender-corrected male lines, CC uploaded) (unlisted)
ch6f-short https://youtu.be/EwCLrA3QLCc — Kokoro: The 9 Romance-Language Voices (9:16 Short, Shorts playlist) (unlisted)

---

## claude-liam-ai-explainer — 2026-07-22

### REAL UPLOAD

Command:
  python3 skills/upload/youtube-publisher/scripts/publish_playlist.py \
    youtube/claude-liam-ai-explainer \
    --playlist "Brutalist" \
    --channel nikbearbrown

Output:
  [yt] authenticated as: Nik Bear Brown (UCg0cw2ouRhQ8dr114yGp0mA)
  [yt] found playlist 'Brutalist' → PLG9H-C6rp5RU
  [yt] uploaded → https://youtu.be/QzTejCPGKlc
  [yt] added claude-liam-ai-explainer to playlist at position 0
  [yt] caption track added (claude-liam-ai-explainer.srt)
  [yt] done.

  ch5  https://youtu.be/QzTejCPGKlc   Claude, Self-Taught.  (unlisted)

Playlist: https://www.youtube.com/playlist?list=PLG9H-C6rp5RU "Brutalist" (public)
Ledger updated: youtube/credentials/nikbearbrown/youtube_publish_ledger.json

HUMAN ACTIONS (Studio):
  1. Flip to public when ready.
  2. Drag ch5 into position in Brutalist playlist (after ch4 — Posting to YouTube).
  3. Verify caption timing on the video page.
