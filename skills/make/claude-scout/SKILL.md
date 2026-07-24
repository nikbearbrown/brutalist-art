---
name: claude-scout
description: >
  Mine books for CLAUDE-EXPLAINER video candidates — reels in the claude brand
  (Claude desktop UI as the set: composer cold open, callout annotations,
  Teardown register, Bear's voice). Scans a book's chapters and writes ONE
  reviewable candidate file at [book]/youtube/claude-explainer.md, each card
  detailed enough that the claude-explainer builder can turn an approved one
  straight into a beat sheet. SCOPE (initial): only book folders whose name
  contains "claude" (case-insensitive), excluding underscore-prefixed scratch
  dirs. Use when the user types `claude scout`, `claude-scout`, `cscout`, or
  asks to scan for claude explainers / claude reel ideas / claude video
  candidates. Produces cards, never videos, never audio spend, never publishes.
  The human picks; approved cards go to skills/make/ai-explainer.
---

# claude-scout — find the reels hiding in the claude books

One pass per book: read the teaching prose, find the concepts that are best
taught **through the Claude UI itself**, and write builder-ready candidate
cards to `[book]/youtube/claude-explainer.md`. The human reviews the file and
hands winners to the `claude-explainer` skill (brand law: `brutalist-art/CLAUDE-BRAND.md`).

## Trigger

```
claude scout                → all in-scope books
claude scout [book-folder]  → one book
```

## Scope (initial — deliberately narrow)

Book folders directly under `books/` whose name contains `claude`
(case-insensitive). Exclude any folder starting with `_` (scratch), and
exclude `brutalist-art` internals. As of writing that means:
`brutalist-d3-x-claude`, `brutalist-figma-claude`, `claude`,
`claude-agentic-ai`, `claude-code-for-students`, `claude-code-for-teachers`,
`claude-cowork`, `claude-for-education-a-practitioners-guide`,
`claude-prompt-engineering`, `musinque-music-promotion-and-claude`,
`musinque-suno-and-claude`, `workplace-software-skills-claude`.
Widening beyond `*claude*` folders is a later, human-approved pass.

## What qualifies (brand fit)

A candidate earns a card only if the Claude UI **is the set**, not a backdrop:

- a workflow beat — type THIS into the composer, THIS happens (ask → run → files back)
- a skill/prompt pattern demo (`/skill-creator`, a saved playbook, a magic word)
- a knob correction — a setting people mis-set (effort dial, connectors, context)
- an anatomy shot — one screen + up to 6 callout annotations ("oversimplified" style)
- a claim fact-check — a circulating claim about Claude, graded on screen

Route away: general theory/math → `bears-doodles-scout` or `brownblue`;
figure-shaped ideas → `figures`; anything needing more than ~2 minutes of
narration probably wants `lecture`, not a reel. When in doubt, one question:
**"can the whole lesson land as callouts on one screen plus a typed ask?"**
No → not a claude-explainer.

## Per book, do:

1. **Read** `chapters/*.md` main teaching prose (skip frontmatter, exercises,
   apparatus). Skim `youtube/` for existing reel slugs — never duplicate one.
2. **Detect zones** that pass the brand-fit test above. Cap at **8 cards** per
   book, ranked best-first. Fewer honest cards beat padded lists — a book may
   legitimately yield 2.
3. **Write** `[book]/youtube/claude-explainer.md` in the card format below
   (overwrite any previous scout output; it is a generated file).
4. **Report** one summary line per book: `[book]: N candidates (top: [slug])`.

## Card format (builder-ready)

```markdown
## C[NN] — [Working Title, Title Case]

- **slug:** [kebab-case]
- **source:** chapters/[file].md §[section]   (every claim must trace here)
- **premise:** [one sentence — the tension or correction that earns the reel]
- **channel:** claude (Bear default) | claude-hai | claude-medhavy | claude-musinique
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `[what types into the composer — lead with a /skill token when real]`
  - topic: `[EYEBROW · CAPS]`   · segment: `[Title Case, never all caps]`
  - greeting: `[hello], [persona]` — hello from the lexicon (SKILL: claude-explainer);
    Wagwan check: sum(ord(c) for c in slug) % 10 == 0 → "Wagwan, Bear" (show the mod value)
- **spine:** B00 ASK → B01..B0n [one claim/step per beat] → VERDICT → title-restate outro (OUTRO LAW)
- **callouts (≤6, one per beat):** title (≤4 words) + body (≤3 short lines) + what it points at
- **other slots:** code-block (Onda) / Manim fragment / human screen-recording — per beat, if any
- **register notes:** the Teardown judgment — what holds, what oversells, the one line to land
- **est length:** [seconds at ~2.6 words/s; reels target 60–150s]
```

## Hard rules

- Cards only. **No beat sheets, no audio, no renders, no publishing.** The
  builder (`claude-explainer`) owns everything downstream of human approval.
- Every premise and claim carries a **source pointer** into the book. No card
  from vibes.
- Respect the brand laws in every card: cold open on the UI, title-restate
  outro, Title Case segments, one terracotta accent, hello-lexicon greeting
  with the deterministic Wagwan check.
- Existing reel slugs in `youtube/` are off-limits — dedupe before writing.
