---
name: claude-refactor
description: >
  Retrofit a book's EXISTING videos into the claude-explainer format —
  without rebuilding them. Points at a book folder and writes ONE self-
  contained REFACTOR.MD into [book]/youtube/; the human then tells Claude
  Code "read REFACTOR.MD" and it does the rest, video by video. The refactor
  replaces each video's open with the Claude cold open (composer typing the
  video's question), replaces the outro with the Claude title-restate outro,
  inserts the handoff beat, and applies the ASK→RESULT law retroactively:
  before every Manim or generated visual, insert a composer micro-beat
  showing a realistic Claude prompt that could generate that scene. Inner
  scenes are REUSED as-is wherever possible. Posting routes by topic from
  books/YouTube.json: topic "Physics" → playlist "Claude for Physics", etc.
  Use when the user types `refactor [book]`, `claude refactor`, or asks to
  convert/retrofit a book's existing videos to the claude-explainer style.
  Excludes HTML-deck / lecture videos. Never posts without per-video human
  approval.

---

# claude-refactor — old videos, new front door

One command, one artifact: `refactor [book]` writes `[book]/youtube/REFACTOR.MD`.
Everything Claude Code needs is inside that file — laws digest, the book's
topic and target playlist, the video inventory with a suggested cold-open
question per video, and the per-video procedure. The human's entire interface
afterward is: *"read REFACTOR.MD"*, then `next` / feedback / `skip` / `stop`.

## Trigger

```
refactor [book-folder]
```

## What the generator does (this skill, before Claude Code is involved)

1. **Resolve the destination.** Read `books/YouTube.json`; find the book's
   entry → `topic` and `channel`. Target playlist = **"Claude for [topic]"**
   (the refactored cuts get their own playlist family; the original
   "Brutalist [topic]" playlists are untouched).
2. **Inventory `[book]/youtube/`.** Every subfolder with a `beat_sheet.json`
   is a candidate. **Exclude:** HTML-deck / lecture videos (anything derived
   from `.dc.html`, anything under `lectures/` or `*-lectures/`, beat sheets
   with deck/slide patterns) and brand-variant dirs (`nbb-*`, `hai-*`,
   `medhavy-*` PREFIXED derivatives of a canonical reel — refactor the
   canonical, not the echo). Reels whose own preset is a channel (e.g.
   `medhavy` build videos) stay in scope but route to that channel's claude
   variant (`claude-medhavy` — persona, voice, register from the channels
   table in the claude-explainer SKILL).
3. **Draft the ask per video.** From each reel's title/premise, write the
   viewer-question the composer will type in the new cold open — plain and
   short: "What is the photoelectric effect?", "Who was Max Planck?",
   "Why can a particle walk through a wall?". Build videos get build
   commands: `claude "build a 1D quantum eigensolver with Manim"`.
4. **Write `[book]/youtube/REFACTOR.MD`** from the template below, inventory
   table filled, and report: `[book]: N videos in scope (excluded: M)`.

## What REFACTOR.MD instructs Claude Code to do (per video, one at a time)

1. Read the reel's `beat_sheet.json` — the master. Read
   `brutalist-art/CLAUDE-BRAND.md` and `brutalist-art/skills/make/ai-explainer/SKILL.md` once at the start.
2. **Replace the open** (SlateCard title beat, brand open, whatever is first)
   with the Claude cold open: `ClaudeComposerAsk`, command = the video's
   question from the inventory table, greeting from the hello lexicon with the
   Wagwan check computed on the reel slug, topic eyebrow = `[TOPIC] · [HOOK]`,
   segment = the video's title in Title Case.
3. **Replace the outro** (OutroCTA / brand outro) with `ClaudeTitleOutro`
   restating the video's title, handle beneath.
4. **Insert the handoff beat** second-to-last (HANDOFF LAW: greeting
   `Your turn.`, a paste-ready prompt extending the video's topic,
   runningText `paste this into Claude…`).
5. **Keep every inner beat and its media.** Reuse existing mp4s, stills, and
   narration audio untouched wherever they exist. Unfilled media stays as
   PIPELINE slates. THEN apply the ASK→RESULT law retroactively: immediately
   before each generated visual (Manim GRAPHIC beats, Remotion graphics,
   D3 charts), insert a composer micro-beat with a REALISTIC prompt that
   could generate that exact scene — e.g. before a step-potential Manim:
   `claude "write a Manim scene: quantum step potential, incoming plane wave, show partial reflection"`
   — runningText `rendering Manim…`. The result beat that follows is the
   existing media, untouched.
6. **Narration:** write narration ONLY for new beats (cold open, ask
   micro-beats — one short line or silent, handoff, outro). Never rewrite
   existing inner narration. New audio via
   `python3 runtime/scripts/generate_audio.py [reel] --only [new beat ids]`;
   GATE P applies — update the reel's PEDAGOGY.md with a refactor addendum
   ending `VERDICT: PASS` before any spend.
7. **Conform + render** the refactored cut to `[reel]/media/claude-cut.mp4`
   (audio-first: frames from measured mp3s; existing beats keep their timing).
8. **Report and STOP.** Per-beat changes, runtime, QC stills (cold open, one
   ask→result pair, handoff, outro). Wait for the human:
   `next` → next video · feedback → fix THIS video, re-render changed beats
   only · `skip` → move on · `stop` → summarize.
9. **Posting (gated).** Only after the human explicitly approves a cut:
   stage upload metadata — title, description (include the prompts shown in
   the video — they are the description's best content), playlist
   **"Claude for [topic]"**, channel from YouTube.json — using the existing
   posting tooling (`brutalist-art/youtube/posting-to-youtube/` conventions).
   Upload happens only on an explicit "post it" per video. Never auto-post.

## Hard rules

- HTML-deck / lecture videos are permanently out of scope — never refactor them here.
- Reuse before you regenerate: an existing inner beat's media is never
  re-rendered unless the human asks.
- All claude-explainer laws apply to the NEW beats (cold open, spark lines on
  any new composer beats, handoff, title-restate outro, one terracotta).
- GATE P per reel before any audio spend. No bypass.
- Posting requires explicit per-video human approval. The playlist family is
  "Claude for [topic]" — never post refactored cuts to the Brutalist playlists.
