# How to create a lecture deck

A **lecture deck** turns book chapters into animated HTML slide decks with
idea-highlighting and synced audio, then to video. There are **two levels** — a
batch path for a whole book, and a premium single-lecture path with your cloned voice.

## Level A — a whole book, every chapter (the batch path)

This is the "point it at a book, get a video per chapter" flow you're picturing. It is
the **`build_lectures.py`** pipeline (it drives the `animated-deck` engine).

```
python3 books/build_lectures.py <book>       # one book, every chapter
python3 books/build_lectures.py --all        # all claude-named books with chapters/
python3 books/build_lectures.py --list       # show scope, build nothing
```

For each chapter `.md` it builds an **animated `deck.html`** *and* an **`.mp4`**:
- **animated HTML deck** — via `build_deck_anim.py`
- **idea highlighting** — `idea_align.py` aligns/highlights each idea to the narration
- **synced audio** — Kokoro voice (`am_onyx`), free/local, timed to the deck
- **→ mp4** — `render_deck_video.py`

It's **idempotent**: a chapter whose `deck.html` and `.mp4` already exist and are newer
than the source `.md` is skipped; a failed render retries once, logs, and continues.
Rules of the format live in `docs/lecture-deck-rules.md` and
`docs/animated-deck-rules.md`.

> Naming note: what you called "deck-lecture on a book repo" is this script. It isn't a
> named skill yet — it's `books/build_lectures.py`. See the note at the bottom.

## Level B — one premium lecture, in your voice (the `deck-lecture` skill)

Use the **`deck-lecture`** skill when you want a single lecture at the highest fidelity:
your **ElevenLabs voice clone**, karaoke word-by-word captions, and teaching-voice
scripts that *discuss* each slide rather than read it.

- **Input:** a **finished** `.dc.html` deck whose slides carry `data-speaker-notes`.
  (deck-lecture does **not** build the deck from a chapter — it starts from a deck.)
- **Flow:** extract slides → **you approve the expanded scripts (GATE, before spend)** →
  TTS clarity audit → voice-clone audio (master clock) → captions → Remotion render.
- **Output:** a narrated lecture video, one slide = one beat = one MP3 over the live slide.

```
deck-lecture <deck.dc.html>
```

## Which level do I want?

| Goal | Use |
|---|---|
| A video for **every chapter** of a book, free/local voice, fast | **`build_lectures.py <book>`** (Level A) |
| **One** lecture, polished, in **your cloned voice** with karaoke captions | **`deck-lecture`** skill (Level B) |
| Just the animated deck + idea highlighting (no narration yet) | the **`animated-deck`** skill |

## Open item — make the batch a named skill

The batch capability (Level A) works today but lives as a **loose script**
(`books/build_lectures.py`), so Claude Code won't reach for it by name and "point
deck-lecture at a book" doesn't invoke it. Recommended: promote it to a skill (e.g.
`book-lectures <book>`, or as `deck-lecture --book <book>` mode) so the whole thing is
two named doors — **`claude-explainer`** for reels and **`deck-lecture`/`book-lectures`**
for chapter decks.
