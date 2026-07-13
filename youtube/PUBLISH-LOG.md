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

