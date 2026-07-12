# Brutalist — Claude for Video Production

> **This README is also a script.** It is the narration for the first video in the
> **"Brutalist — Claude for Video Production"** playlist on
> [@NikBearBrown](https://www.youtube.com/@NikBearBrown): *"What is Brutalist?"* Every other
> video in that playlist is made **by this toolkit, about this toolkit** — one worked example per
> video type, each rebuilding itself from its own source inputs. The playlist is the documentation.
> More at [brutalist.art](https://www.brutalist.art/).

---

## What is Brutalist?

Brutalist is a way of making videos where **Claude does the technical build and you keep the
judgment.** That division is the whole idea, and it has a name:

> **Maximally informed, minimally autonomous.**

AI code generation is fast. Left alone it runs ahead of your intent — it generates before the
idea is clear, loses track of what it already made, and quietly makes creative decisions that were
never its to make. Brutalist is the counter-architecture. The machine animates, composites,
renders, and retrieves. **You** decide what the video is for, what it should feel like, which shot
is right, and whether it's good. The tool will not take those decisions from you — even when you
ask it to.

## How a video gets made

You hand Claude a chapter, a script, a song, or a concept. It becomes a **beat sheet** — the heart
of every video, one beat per moment. Then two things happen, in this order:

**1. Fill-in — Claude makes everything it can.** The tool audits the beat sheet and renders every
beat it knows how to make well: a Manim animation, a Remotion motion graphic, a title card, a
beat-synced cut. This is the rule that keeps the labor split honest — **if the machine can build a
beat, the machine builds it.** You are never asked to hand-make something Claude already knows how
to do.

**2. Request cards — for what it honestly can't.** For the beats that need a real capture, archival
footage, a performance, or a generated AI clip, Claude doesn't guess. It leaves a **request card**
on that beat naming exactly what it needs — and for AI or archival shots, a suggested prompt or
search terms. You drop the real thing into the `pantry/`; the tool checks it, trims or stretches it
to the beat, strips sound if needed, names it, and slots it into the cut.

A request card should *only* ever be for a genuinely human beat. If you see one on a beat Claude
could have animated, that's a bug — run fill-in again. You supply the taste and the things only a
human can get; the machine supplies everything else.

## The two jobs

| Claude / the CLI does | You do |
|---|---|
| **Fill-in:** render every beat it can (Manim, Remotion, cards, cuts) | Decide what the video is *for* and who it's for |
| Composite, time to the narration, cut to the beat | Approve the script, the pacing, the look |
| Emit request cards **only** for what it can't make, with prompts | Supply the real captures, footage, and original ideas |
| Measure, conform, and name every clip | Make the creative and factual calls |
| Surface new information and ask before acting | Decide whether and when to apply it |

The boundary is enforced, not suggested. That's what makes it hold when you're in a hurry.

## Quickstart

```bash
git clone https://github.com/nikbearbrown/brutalist-art && cd brutalist-art
cp .env.example .env      # fill in only the keys you need (start with none)
./setup                   # the doctor: prints a per-feature readiness table
./art --list              # every skill (and its former house name)
```

With **zero keys** and only `ffmpeg` + Pillow, you can already build the no-key first pass:

```bash
./art todo    examples/slate-cut--base-rate     # what each beat needs, and how
./art fill-in examples/slate-cut--base-rate      # render every beat the machine can make
./art run     examples/slate-cut--base-rate      # compile; only human beats remain as cards
```

Add `ELEVENLABS_API_KEY` and you get narration; add the `higgsfield` CLI login and you get AI
video. `./setup` always tells you exactly what each feature needs and what it unlocks. See
**[CAPABILITIES.md](CAPABILITIES.md)** for the full table and **[INSTALL.md](INSTALL.md)** for
per-OS setup.

## The learning path is example-first

Every video type ships one complete example. The path is always the same: **rebuild the example
from its source inputs → confirm your setup produces the same result → then point the same skill at
your own material.** The examples climb from no-key to paid, laid out in **[LEARN.md](LEARN.md)**:

1. **slate-cut** — no keys. The zero-key first pass; every ungeneratable beat becomes a request card.
2. **sketch-explainer (silent)** — Manim, no keys.
3. **sketch-explainer (narrated)** — add ElevenLabs.
4. **explainer** — the flagship: each beat rendered by whatever tool teaches it best, composited.
5. **lecture** — a textbook chapter → an HTML lecture deck → a narrated lecture video.
6. **AI-video types** (lyric-resync, dance-video, story-film) — the higgsfield CLI.
7. **youtube-publisher** — transcript, chapters, and bookends, straight to YouTube.

## What's here

```
art                 the one entry point — ./art <skill> <target> [--flags]
setup               the doctor — dependency + key readiness, per feature
skills/
  make/             the reel factory — explainer, sketch-explainer, math-explainer,
                    music-video, bio, story-film, scout, audience-preset, … (see GLOSSARY.md)
  upload/           youtube-publisher, video-inventory
  assets/           ai-asset-gen, ai-character-id, line-art-vectorizer, diagram-redraw
  figures/          figure-planner
runtime/            the shared engine every skill runs on (scripts, animated_graphics,
                    design, voices, fonts, remotion, schema) — see runtime/README.md
examples/           one "rebuild this" starter per video type
GLOSSARY.md         old house names → new plain names (every old name still resolves)
CAPABILITIES.md     what each video type needs (keys, installs, cost, example, your input)
TODO.md             the honest backlog — promised vs. built across the Brutalist family
```

## The Brutalist principles (why it works)

The full spec is `BRUTALIST.md`; the short version is six commitments the tool keeps so you don't
have to police them:

1. **Intent before code.** The purpose and feel are yours to state, in plain language, first.
2. **A schema the AI generates against.** Naming, palette, timing conventions — the tool works
   inside them, not around them.
3. **A phase gate.** Audit → schema → generate → verify → handoff. No phase skipped under deadline.
4. **Labor separation.** Generation is the machine's; judgment, footage, and direction are yours.
   Fill-in enforces it: the machine never leaves a task for you that it could do itself.
5. **Refusal.** Ask it to make a call that belongs to you and it declines and explains why.
6. **Current knowledge, deferred action.** It reads what's new, tells you why it matters, and asks
   before touching anything.

The result is a workflow where you spend your time on what is irreducibly human — judgment,
direction, verification — and the machine spends its time on what it's actually good at:
generation, within a schema, on request, one beat at a time.

*Brutalist is by Nik Bear Brown (Bear Brown LLC). Licensed MIT. Vendor names (ElevenLabs, Higgsfield,
Remotion, Manim) are tools it drives, not part of its identity.*
