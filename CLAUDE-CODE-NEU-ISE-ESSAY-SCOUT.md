# Claude Code Prompt — Scout the NortheasternISE essays for claude-explainer (Liam) videos

Scouts the Substack export for ESSAYS (not people-profiles) and writes
reviewable claude-explainer candidate cards — Humanitarians AI explainer
videos, claude-liam voice, each card crediting the essay's AUTHOR (Liam names
them on screen and aloud). Produces cards only — no videos, no spend.

Source zip (already on disk):
`/Users/bear/Documents/CoWork/bear-textbooks/books/TMP/5UJLKT7uS5qEBkJNU3hMSg.zip`

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. This is a SCOUT pass —
candidate cards only. No rendering, no audio, no publishing, no git commit/push.

```text
Scout the NortheasternISE Substack export for ESSAY-based claude-explainer video
candidates and write reviewable cards. Discovery pass ONLY: propose, rank, never
build. No rendering, no audio, no paid services, no git commit/push. Run without
approval pauses.

READ COMPLETELY BEFORE ACTING
- AGENTS.md
- skills/make/scout/SKILL.md            (candidate-card FORMAT and rubric — follow it)
- skills/make/ai-explainer/SKILL.md  (so cards target the claude-explainer
  builder correctly; note the claude-liam voice + @HumanitariansAI branding)

SCOPE — what counts as an ESSAY here
An ESSAY is a substantive analytical, explanatory, technical, or opinion article
carrying ONE teachable idea — the kind a claude-explainer can teach. Examples the
human named (use as calibration seeds):
- "Standard Internships Put You Near the Work. Co-op Puts You In the System." —
  author Aditi Shinde — experiential-learning / systems-vs-proximity argument.
- "The Math Behind Why Your Spotify Discover Weekly Is So Addictive" — author
  Shravya Ushake — technical review of a recommender + its AI-ethics questions.

EXCLUDE (log each under "Skipped", one-line reason — never silently drop):
- PEOPLE-PROFILES (feature stories ABOUT a named person — those go through the
  separate profiles batch, not this one; e.g. The Cost of the Pivot, The
  Architect Who Didn't Wait, The Precision of Honest Work, The Builder Who Said
  No, The Engineer Who Fixes…, The Builder's Grammar, QEMA-G, The Honest Gambit,
  The Lab That Builds by Doing, Why Most AI Projects Fail…, The Weight of What
  You Build, a profile of Yadeesh K R, My Tech Journey).
- Job postings & career-fair notices; the weekly job "harvest"/Lever/Greenhouse
  dataset digests; interview case studies; the Substack-editor how-to; any
  *.opens.csv / *.delivers.csv / email_list.csv / posts.csv (analytics); and
  near-empty stubs (e.g. 188842210.389.html, 190420683.*, 191506558.*).
- Pure book-catalog entries MAY be included ONLY if the review carries a distinct
  teachable idea of its own; otherwise skip.

SURVEY, ATTRIBUTE, ROUTE
1. Unzip ../TMP/5UJLKT7uS5qEBkJNU3hMSg.zip into a read-only scratch dir (e.g.
   ../humanitarians_html/youtube/_neu-ise-source/). Enumerate posts/*.html.
2. For each post: read title + subtitle + body; classify ESSAY vs SKIP.
3. AUTHOR ATTRIBUTION (required for every ESSAY — Liam must credit them):
   the export HTML does NOT contain bylines. Recover the author by fetching the
   live post — URL = https://northeasternise.substack.com/p/<slug> where <slug>
   is the html filename with the leading "<postid>." stripped and the trailing
   ".html" removed (e.g. 193127655.the-math-behind-why-your-spotify.html →
   /p/the-math-behind-why-your-spotify). Read the byline there. Seed the two
   known ones (Aditi Shinde; Shravya Ushake). If a byline can't be recovered,
   set AUTHOR: UNKNOWN and FLAG the card so a human fills it in — never invent an
   author, and never ship a card without an author decision.

CANDIDATE CARDS
- One card per essay, in the scout SKILL.md card format. A rich essay may yield
  1–2 cards; most yield 1. Aim for QUALITY: name ONE concrete, teachable,
  ideally counterintuitive idea — not "summarize the essay."
- Every card includes, in ADDITION to the SKILL.md fields:
  * Source: post id + html path AND the live /p/<slug> URL.
  * AUTHOR: the essay's byline (or UNKNOWN + flag).
  * LIAM CREDIT LINE: the exact on-screen/spoken credit the claude-explainer
    build must use — pattern: "Based on the essay by <Author>, for the
    NortheasternISE / Humanitarians AI." Liam credits the author in B00 (cold
    open) AND on the SOURCES/outro card. (This is the whole point of the pass —
    the author is named, every time.)
  * Suggested builder: claude-explainer. Suggested channel/voice: claude-liam,
    @HumanitariansAI folder chip, Teardown-warm.
  * A derived runtime estimate (short/medium) and 2–4 concrete visual beats
    (native animation / infographic — REBUILD LAW; the essay's mechanism,
    numbers, or before/after made to move).

RANK
- Score each on the SKILL.md rubric (teachability, visual potential, audience
  pull, freshness). Put the ranked list at the top of the output.

OUTPUT
- Write everything to ../humanitarians_html/youtube/essay-video-ideas.md:
  a header note (format + author-credit rule), the ranked table, the cards, then
  the "Skipped (with reason)" section. If ../humanitarians_html/youtube/ already
  has an essay-video-ideas.md, APPEND new cards and note it's a delta pass — do
  not clobber existing cards.
- Print a one-line summary: N essay cards written, M posts skipped, K authors
  flagged UNKNOWN. Build nothing.
```
