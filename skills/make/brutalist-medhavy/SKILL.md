---
name: brutalist-medhavy
description: >
  The learning-first doctrine layer over the Brutalist video system — design
  for learning, not for clicks. Not a new pipeline: a set of LAWS (from
  BRUTALIST-MEDHAVY.md, distilled from the LXD / when-to-use-AI / friction /
  ai-for-LXD books) that modify any builder skill when the audience is
  Medhavy or the goal is durable learning: protect germane friction, require
  a PREDICT-before-reveal beat, ban engagement-trap moves, declare the phase
  gate in the artifact, hand off exercises not just prompts, teach toward
  Tier 4, enforce Evidence Box discipline, and measure struggle signals
  (Y1–Y7) instead of applause. Use when the user types `brutalist medhavy`,
  `medhavy explainer`, `bm laws`, `learning cut`, asks for the Medhavy
  version of a reel/lecture, or asks whether a design serves learning or
  clicks. Composes with claude-explainer (channel claude-medhavy), lecture,
  brownblue, and vox-explainer — it changes their judgment rule, not their
  machinery. Never publishes.
---

# brutalist-medhavy — the learning cut

A doctrine layer, not a pipeline. Point it at any build (a claude-explainer
episode, a lecture, a brownblue piece) and it applies the Brutalist Medhavy
laws — charter: `brutalist-art/BRUTALIST-MEDHAVY.md`, canon: the four books
named there. The machinery stays whatever the host skill uses; the judgment
rule becomes: **did the learner do the cognitive work?**

## Trigger

```
brutalist medhavy [target]     → apply the laws to a build or an existing artifact
bm laws                        → print the checklist below
learning cut [reel]            → audit an existing reel against the laws
```

## What it changes in any host build

1. **Brand:** audience MEDHAVY — voice kokoro `af_kore` (override
   `ELEVENLABS_VOICE_MEDHAVY`), register Wonder, channel @MedhavyAI. Claude-UI
   episodes use the `claude-medhavy` variant; graphics use medhavy tokens.
   **The Medhavy viewer is an EDUCATOR**: they never learned AI in school
   because it didn't exist yet — EdTech people and mid-career teachers who
   need to get proficient. Every episode answers some slice of the spine
   question: when does AI help teaching, and when does it substitute for it?
   (The sibling claude-hai channel asks the same question for STUDENTS.)
2. **Spine additions (video grammar):**
   - ≥1 **PREDICT beat**: pose → invite pause → commit → reveal. The reveal
     never lands on an uncommitted viewer.
   - **Handoff = exercise**: the paste-ready prompt makes the learner work,
     and names what NOT to delegate ("have Claude quiz you — don't have it
     answer"). Every use-AI-here pairs with a not-AI-here.
   - **Verdict page carries the phase gate**: "AI did X · you do Y · support
     fades at Z."
   - **Description ships a spaced retrieval prompt** dated ~a week out.
   - **Motion is classified, never decorated** (the animated-deck gate,
     adopted): beats whose narration argues a moving argument are matched to
     the five rhetorical patterns via a per-reel `anim.json` — the agent
     proposes the pattern table, the human signs before build. The no-fit
     case stays still. This is the engagement-trap law applied to animation:
     motion serves the mechanism, never the spectacle. Composes with the
     host skill's ILLUSTRATE LAW (UI only where the UI is the subject).
3. **PEDAGOGY.md gains two audit sections** (both must pass before GATE P):
   - *Evidence discipline*: every stated magnitude sourced; single-source
     findings flagged (the Kosmyna rule); no manifesto claims dressed as data.
   - *Friction protected*: list each place the artifact removed friction and
     classify it (extraneous — good removal | germane — VIOLATION, rewrite).
4. **Banned moves** (the engagement trap): retention bait, artificial
   cliffhangers, resolving the struggle the learner should keep, smile-sheet
   success claims, "watch time" as a QC criterion anywhere.
5. **Tier check:** the episode must leave the viewer better at auditing AI
   (Tier 4), not just faster at consuming it (Tier 1).
6. **Theory-first defaults, applied silently, logged loudly:** WCAG 2.2 AA,
   colorblind-safe learning palettes, arc-based sequencing (hook → predict →
   struggle → reveal → apply), CLT load limits, fact-check-with-sources before
   render. The build never asks the human to re-decide a solved default — it
   applies it and logs it.
7. **The decision log:** every artifact ships `decisions.json` +
   `DECISIONS.md` — one entry per design decision: stable ID, beat, choice,
   default applied, reason, source, overridable. Patch-not-regenerate.
8. **The override loop (the human is ALWAYS the final judge):** any CLI can
   change any decision by ID ("change D-014 to …"). The system complies,
   re-renders only affected beats, appends the override to the log, and
   records its dissent when it has one (e.g. a WCAG contrast flag) — then
   still complies. Overrides are never resisted; they are never forgotten
   either.

## The audit checklist (`bm laws` / `learning cut`)

| # | Law | Pass looks like |
|---|-----|-----------------|
| 1 | Friction | germane difficulty survives; only extraneous load removed |
| 2 | Predict-before-reveal | a commit moment exists before each key reveal |
| 3 | Engagement trap | zero design choices that serve the metric over the mechanism |
| 4 | Phase gate | the artifact SAYS what AI did, what the learner does, where support fades |
| 5 | Scaffold not crutch | any AI support shown includes its fade |
| 6 | Tier | teaches auditing/formulating/distrust-calibration, not Tier-1 competition |
| 7 | Evidence | magnitudes sourced; flags carried; two registers kept honest |
| 8 | Struggle evidence | exercise + spaced retrieval shipped with the artifact |

Verdict format: per-law PASS/VIOLATION with the beat or line cited, then
`LEARNING CUT: PASS` only when 1–8 all hold. A reel can be a great Brutalist
artifact and fail this audit — that is the point of having two systems.

## Relationship map

- `claude-explainer` — host for Claude-UI episodes; this skill sets channel
  `claude-medhavy` and adds the laws. Cold open / spark lines / handoff /
  outro laws all still apply; the handoff gains the exercise gate.
- `lecture` / `deck-lecture` — host for chapter coverage; laws 2, 4, 7, 8
  apply per section.
- `medhavy MCP` (planned) — the spine this doctrine assumes: vetted claim
  sets + videos + exercises served as data, refusal-on-gap, so builders start
  from quality instead of cold generation.
- `bears-doodles` / `brownblue` — host for concept pieces; the PREDICT beat
  maps naturally onto their mystery-framed openings.

## Hard rules

- Never publish. GATE P per artifact; the two new audit sections are part of it.
- The laws never delete friction disputes silently: if a host skill's habit
  (e.g., a smooth reveal) conflicts with Law 2, the conflict is REPORTED to
  the human, not auto-resolved.
- Clicks may be observed. They may never be optimized for.
