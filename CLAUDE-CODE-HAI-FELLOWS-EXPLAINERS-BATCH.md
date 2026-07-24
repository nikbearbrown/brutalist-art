# Claude Code Prompt — Humanitarians AI Fellow Explainer Videos (batch, claude-liam)

Turns the two Substack export zips into a fleet of claude-liam explainer
videos — one per substantive article — with fellow/founder credit and the
Humanitarians AI bridge-program framing baked into every one.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Source zips (already on disk):
- `/Users/bear/Documents/CoWork/bear-textbooks/books/TMP/L8LmVcz6RaK3s_pceg83RQ.zip`  (zip1 — Zebonastic / game design)
- `/Users/bear/Documents/CoWork/bear-textbooks/books/TMP/uNl-naqmR8a14Uw1NFA2JA.zip`  (zip2 — Humanitarians AI research)

This is a TWO-PHASE job. Paste PHASE 1 now. Review the manifest it writes.
Then tell Claude Code to run PHASE 2 on the approved rows. Free pipeline only:
Kokoro voice, no ElevenLabs, no higgsfield, no publishing, no git commit or
push, throughout both phases.

Shared rules for the whole job (read once, apply everywhere):

- Channel: claude-liam (persona Liam in for Bear, Kokoro am_onyx, register
  Teardown, folder chip @HumanitariansAI). Format 1920x1080 (16:9), 30fps.
- Read AGENTS.md, CLAUDE-BRAND.md, skills/make/ai-explainer/SKILL.md,
  skills/make/explainer/SKILL.md (+ its MOTION.md / REMOTION.md), and
  docs/remotion-best-practices/SKILL.md before building anything.
- AUTHORSHIP CREDIT (per article):
  * If the article's author/byline/signature is anyone OTHER than Nik Bear
    Brown, credit that person on screen as "<Name> — Humanitarians AI Fellow".
  * If the author is Nik Bear Brown, credit "Nik Bear Brown — Founder,
    Humanitarians AI".
  * Many HAI articles are third-person profiles of a fellow's project; in
    those, the named researcher/builder is the Fellow to credit.
  * If no author is detectable, credit "Humanitarians AI Fellow" generically
    and FLAG the row in the manifest so a human can fill the name in.
- PROGRAM FRAMING (every video, in the outro, spoken by Liam + on a card):
  "Humanitarians AI is an educational bridge program where Fellows learn
  experiential AI by doing AI — building real projects and shipping real
  research." Keep the wording tight; do not pad.
- IMAGES: you may reuse any image in the article. Article images are remote
  Substack CDN URLs embedded in the HTML. Download each article's images into
  that video's media/ folder and animate them (Ken Burns push/pan, reveal
  wipes, callout rings, cross-dissolve) rather than showing them static.
- ANIMATE ANYTHING YOU CAN: any number, comparison, before/after, pipeline,
  ranking, or mechanism in the article becomes a native animated Remotion beat
  in the Claude palette (cream #FAF9F5, warm ink #3D3929, terracotta #D97757
  as the one accent). Only fall back to the article's own image when you can't
  rebuild the idea as motion.
- Claude UI (composer) appears only in the bookends (ILLUSTRATE LAW).

============================================================================
PHASE 1 — CLASSIFY, DETECT, HARVEST, MANIFEST  (run this now; build nothing)
============================================================================

```text
PHASE 1 of the Humanitarians AI Fellow explainer batch. Do NOT build any
video, generate any audio, or render anything in this phase. Produce a review
manifest only. No git commit or push.

1. Unzip both source zips into a scratch area you control (e.g.
   youtube/hai-fellows/_source/zip1 and _source/zip2):
   - books/TMP/L8LmVcz6RaK3s_pceg83RQ.zip  -> zip1
   - books/TMP/uNl-naqmR8a14Uw1NFA2JA.zip  -> zip2
   Treat the zips as read-only inputs.

2. Enumerate article HTML files under each posts/ folder. INCLUDE substantive
   articles from BOTH zips. EXCLUDE and log as skipped:
   - Any *.opens.csv, *.delivers.csv, email_list*.csv (analytics, not articles).
   - Editorial/how-to/meta posts: "how-to-use-the-substack-editor",
     "coming-soon", and any post whose body is a platform tutorial or
     publication announcement rather than content.
   - Stub/near-empty posts (very short bodies, or filenames that are just a
     token like "295", "bf6", "4ff", "969") — skip if the body has no real
     article.
   - Duplicate slugs: keep ONE canonical copy, skip the rest. Known dupes:
     the two "the-ai-editor-that-actually-made" (199346070 / 199352009) and
     the "80-days-data ... sample" vs "... full" pair — keep the fuller one,
     skip the other. Detect any other near-identical slug pairs the same way.
   Everything that survives is a BUILD CANDIDATE. (This includes the game-
   design essays and book reviews per the "every substantive article" scope.)

3. For each build candidate, extract:
   - slug + a human title (from the article's H1 / first heading; fall back to
     the de-slugged filename).
   - source zip (zip1=Zebonastic / zip2=Humanitarians AI) and file path.
   - AUTHOR + credit type, applying the AUTHORSHIP CREDIT rules above. Look for
     an explicit byline/signature first; then the named fellow/researcher the
     piece profiles; else mark UNKNOWN and flag. State which signal you used.
   - a one-sentence concept: the single teachable idea the video will carry.
   - article kind: fellow-project | fellow-research | profile | essay |
     book-review | tool-launch | other. (Used later to pick emphasis, not to
     exclude.)
   - image inventory: list every distinct Substack CDN image URL in the HTML,
     with a note on what each depicts. Do NOT download yet in Phase 1 unless
     trivial — just inventory (record count + URLs).
   - a rough runtime estimate via duration-planner reasoning (do not fix a
     clock; derive from content — most of these are 2-4 min).
   - proposed output slug: hai-fellows/<kebab-title>.

4. Write the manifest to youtube/hai-fellows/MANIFEST.md:
   - A table of every build candidate: title | zip | author | credit type
     (Fellow / Founder / UNKNOWN-flag) | kind | image count | est. runtime |
     output slug.
   - A separate "Skipped" table: file | reason.
   - At the top: totals (candidates, skips), a count of UNKNOWN-author rows
     that need a human name, and any duplicate pairs you collapsed.
   - Also emit youtube/hai-fellows/manifest.json with the same rows in machine
     form, so Phase 2 can consume it directly.

5. STOP after writing the manifest. Report: how many candidates, how many
   skipped, how many UNKNOWN-author rows, and the list of UNKNOWN rows by title
   so a human can supply names. Do not proceed to building.
```

============================================================================
PHASE 2 — BUILD  (run only after the human approves the manifest)
============================================================================

Before pasting Phase 2, the human edits `youtube/hai-fellows/MANIFEST.md`
(and/or manifest.json): fix any wrong authors, fill UNKNOWN names, and delete
any rows they do NOT want built. Phase 2 builds exactly the rows that remain.

```text
PHASE 2 of the Humanitarians AI Fellow explainer batch. Build a claude-liam
explainer for EVERY row remaining in youtube/hai-fellows/manifest.json (the
human has curated it). Free pipeline only: Kokoro am_onyx, no ElevenLabs, no
higgsfield, no publishing, no git commit or push. Run without approval pauses;
this is an unattended batch.

For EACH manifest row, in a per-article folder youtube/hai-fellows/<slug>/:

1. Download that article's images (from the URLs in the row) into
   <slug>/media/. If a download fails after two tries, proceed without it and
   log the miss in that folder's SOURCES.md — never block the whole video on
   one image.
2. Read the article body and build the beat sheet:
   - Beat 0: ClaudeComposerAsk cold open. Liam frames the article's core
     question/hook in one or two lines.
   - Middle: teach the article's ONE central idea, carried by animated beats.
     Rebuild every number, comparison, pipeline, before/after, ranking, or
     mechanism as native Remotion motion in the Claude palette. Use the
     downloaded article images as supporting footage (animated, never static)
     where they add something a rebuild can't.
   - Credit beat: near the end, a card + Liam line crediting the author per
     the row's credit type ("<Name> — Humanitarians AI Fellow" OR "Nik Bear
     Brown — Founder, Humanitarians AI").
   - Program beat: the Humanitarians AI bridge-program framing, verbatim per
     the shared rule — "an educational bridge program where Fellows learn
     experiential AI by doing AI — building real projects and shipping real
     research."
   - Your Turn beat: composer with a suggested prompt relevant to the
     article's topic.
   - Brand card: @HumanitariansAI + title restated.
3. Audio-first: generate and measure Liam's narration per beat FIRST; conform
   every beat to its audio. Length derives from the beats.
4. Fidelity: cream page, warm ink, terracotta as the ONE accent per beat, EB
   Garamond Title Case segment titles. Transform-don't-cut within beats.
5. Honesty: never invent statistics, quotes, or results not in the article. If
   the article makes a claim without a number, teach the claim, don't fake a
   figure. Every on-screen number traces to the article; record them in the
   folder's SOURCES.md.
6. Output per article: beat_sheet.json, <slug>.mp4 (1920x1080), SOURCES.md
   (facts + author + image credits). Verify each mp4 exists and plays (probe
   duration + frame count) before moving to the next row.

BATCH DISCIPLINE:
- Process rows independently; one article's failure must not stop the batch.
  If a video fails to render after two attempts, write a FAILED.md in its
  folder explaining why and continue.
- Maintain youtube/hai-fellows/BUILD-LOG.md: append one line per article —
  done / failed / skipped, with runtime and any notes.
- When finished, write youtube/hai-fellows/SERIES-INDEX.md: every built video
  with its title, author credit, runtime, and folder — and a suggested
  playlist order grouping fellow projects, research, essays, and reviews.
- End the run with counts: built, failed, total runtime of the fleet, and the
  path to SERIES-INDEX.md.
```
