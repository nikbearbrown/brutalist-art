# Posting to YouTube — publish the series the way the machine should

The companion doc to **video 4** in the *Brutalist — Claude for Video Production* playlist. The three
videos before it are the worked example: this is the true record of pushing *What is Brutalist?*,
*Installs*, and *When Cowork Can Help Claude Code* to YouTube — what the toolkit does, what went
wrong, and where the line between the machine and you falls. Meta, like the rest: a video about
posting the videos before it, posted the same way.

## The gap, and why the API instead of drag-and-drop

A finished cut on disk is not on YouTube. You could drag each file into YouTube Studio — but a manual
upload makes you retype the title, paste the description, re-enter tags, set the category, find the
playlist, and drag the video into chapter order, every time, by hand. The toolkit publishes through
the **YouTube Data API** instead, so all of that comes from the beat sheet and travels with the
upload: title, a full transcript-style description, tags, the Education category, playlist membership,
and chapter order. The automation is the point — it's exactly what Studio uploads lose.

## What each video needs

Four things per folder, all of which the pipeline already produced:

- `mp4/<slug>.mp4` — the master to upload. *What is Brutalist?* ships its **review** cut on purpose
  (it keeps the review label it explains); *Installs* and *When Cowork* ship their clean `-cut`
  finals.
- `description.txt` — the full description.
- `beat_sheet.json` metadata — `title`, `tags`, and `chapter_number`, which sets the playlist order.
- `<slug>.srt` — the caption track (CC), written **from the beat sheet**: SOURCE narration text on
  measured beat windows. The machine already knows every word and exactly when it lands, so the
  captions are right by construction — not an auto-transcription guess.

For this batch: `chapter_number` 1, 2, 3 → *What is Brutalist?* first, then *Installs*, then *When
Cowork Can Help Claude Code*.

## What the publisher does

One command (`publish_playlist.py`, wrapped by the youtube-publisher skill): it finds — or creates —
the **"Brutalist"** playlist by title, uploads each master with a resumable `videos.insert`, and adds
each video to the playlist at its chapter position, so the playlist reads in order regardless of
upload order. A small local **ledger** records each uploaded video's ID, so a re-run skips what's
already up instead of double-posting. And it uploads each folder's `<slug>.srt` as an English
caption track (`captions.insert`) — idempotent like everything else: a video that already carries a
track is skipped, and a caption failure never blocks the upload or the playlist.

## What actually happened (the honest record)

- **One real bug, one fix.** The first run uploaded *What is Brutalist?* but crashed before the
  playlist insert: the playlist uses auto-sort, and the script was sending a `position=` field, which
  the API rejects for an auto-sorted playlist (`manualSortRequired`). Removing `position` fixed it;
  the ledger meant the re-run skipped the already-uploaded video and finished cleanly.
- **Privacy and the audit.** All three landed **unlisted**, exactly as asked — so unlisted uploads do
  *not* require the API compliance audit. **Public** is the gated part: until a client's audit is
  approved, YouTube can lock API-uploaded videos, so going public is a manual visibility flip you make
  yourself in Studio (which the audit doesn't gate). The machine posts; you decide what goes live.
- **Quota.** `videos.insert` costs 1,600 units against a 10,000/day default — about **six uploads a
  day**. Three was comfortable; a longer run batches across days, and the ledger tracks the boundary.
- **Credentials.** The publisher resolves `youtube/credentials/<channel>/` from the repo root
  automatically (a path bug that used to force `ART_HOME`/explicit flags is fixed).
- **The caption gap.** The vendored publisher had silently dropped CC upload — the experiment
  publishers shipped every video with an `.srt` caption track; the first series publish didn't. A
  review caught it the same day: the `force-ssl` scope, `captions.insert`, and `.srt` emission were
  restored, and caption tracks were backfilled onto the live videos. Clients want their captions
  right — and captions from the beat sheet *are* right, because the machine already knows every word.

## Cross-links: the funnel

Publishing also wires the series together by default. Every **short**'s description points to the
intro **video**, *What is Brutalist?*; every **long**'s points to the series **playlist**,
*Brutalist*. (The native "Related video" chip on a Short is a Studio-only setting; the description
link is the part the API can automate.)

## The split

The machine does the mechanical publish that a hand-upload loses — transcript-style description,
chapter order, tags, playlist, the caption track, the idempotent ledger. What it does **not** do is decide what the
world sees: the videos sit unlisted until *you* watch them and flip them public. Posting is one more
place the labor divides the same way the whole series argues it should — the machine plays every
part; you own what ships.

---

*The video that tells this: [`youtube/posting-to-youtube/`](../youtube/posting-to-youtube/). The
publish session it's built from: `youtube/PUBLISH-LOG.md`. The three examples:
[`what-is-brutalist`](../youtube/what-is-brutalist/), [`installs`](../youtube/installs/),
[`when-cowork-helps-claude-code`](../youtube/when-cowork-helps-claude-code/).*
