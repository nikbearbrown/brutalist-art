# BRUTALIST MEDHAVY — design for learning, not for clicks

The parallel Brutalist. Same machinery — beat sheets, the shared belt, phase
gates, AI generates / human judges — with the judgment rule swapped. Brutalist
asks *"is it good?"* (taste, watchability). Brutalist Medhavy asks *"did it
teach?"* — and refuses to accept clicks as the answer.

**One sentence (the series', inherited whole):** Learning requires struggle,
teaching requires judgment, and AI that does either for you produces the
appearance of both without the substance — the answer is not less AI but a
precise division of labor between what machines do well and what human
cognition alone constitutes.

## Canon

The doctrine is not invented here; it is distilled from four books, which are
this system's constitution. Every law below carries its source.

1. `learning-experience-design-lxd` — the discipline; the engagement trap (Ch 1);
   cognitive machinery and desirable difficulties (Ch 3); friction to keep vs.
   remove (Ch 6); scaffold or crutch (Ch 12); beyond the smile sheet (Ch 14).
2. `learning-when-to-use-and-when-not-to-use-ai` — the Hattie hinge (Ch 1) and
   the bucket-by-bucket account of where AI helps, where it substitutes, and
   where the human core is not negotiable (Chs 2–19).
3. `friction-measuring-the-learning-struggle` — the artifact is no longer
   enough (Ch 1); what genuine learning leaves behind (Ch 2); the seven
   struggle signals Y1–Y7 and the ensemble (Chs 3–10).
4. `ai-for-learning-experience-design` — the crutch effect (Ch 2), the
   scaffold (Ch 3), tutoring interactions, trust, and the full integration.

## The judgment rule (what changes from Brutalist)

Brutalist: agents check the determinable; the human checks the judgeable —
*interesting, worth watching.* Brutalist Medhavy keeps the split and replaces
the human's question: **did the learner do the cognitive work, and would they
still be able to do it next week?** Watch-time, likes, completion, and the
smile sheet are explicitly inadmissible as success evidence (lxd Ch 1, Ch 14).
The artifact is no longer enough (friction Ch 1); the evidence is the struggle
trace, not the applause.

## The Laws

**1. FRICTION LAW.** The struggle is the mechanism, not the price (series
theme 1; lxd Ch 3). Every artifact protects germane difficulty and removes
only extraneous load (lxd Ch 6). Concretely for video: a Medhavy explainer
may pose a struggle it does not immediately resolve — it sets the prediction
up and makes the viewer commit before the reveal. Smoothness is a defect when
it removes the trigger.

**2. PREDICT-BEFORE-REVEAL LAW.** Prediction error is the trigger (dopamine
fires on expectation violated — lxd Ch 3). Every Medhavy explainer carries at
least one PREDICT beat: the question posed, an explicit pause invitation, a
commit ("write down your guess"), then the reveal. The reveal without the
commitment is entertainment.

**3. ENGAGEMENT-TRAP LAW.** Never optimize the artifact for clicks (lxd Ch 1:
learners love products that don't teach; Bastani: 48% better during practice,
17 points worse on the unassisted exam — fluency felt like mastery and wasn't).
No engagement bait, no artificial cliffhangers, no smoothing that exists only
to hold retention curves. If a design choice serves the metric and not the
mechanism, it is out.

**4. PHASE-GATE LAW.** Every artifact declares its gate (series theme 2): what
AI did, what the learner must do themselves, and how support fades. In video
grammar: the handoff beat is an EXERCISE handoff — the paste-ready prompt
makes the learner do work, and it names what NOT to delegate ("have Claude
quiz you; do not have Claude answer"). Every "use AI here" pairs with a
"not AI here" (the books' Exercise 1/2 pairing).

**5. SCAFFOLD-NOT-CRUTCH LAW.** AI support shown in content must be a scaffold
— calibrated to the learner's edge and designed to fade — never a crutch that
substitutes for the germane work (ai-for-lxd Chs 2–3; lxd Ch 12). When a reel
demonstrates an AI workflow, it shows the fade: what the learner stops needing.

**6. TIER LAW.** Teach toward Tier 4 — plausibility auditing, problem
formulation, knowing when to distrust the machine (series taxonomy). Never
train humans to compete in Tier 1 (pattern recall, retrieval) — that is the
machine's tier. Every episode should leave the viewer better at judging AI
output, not just consuming it.

**7. EVIDENCE LAW.** Two registers, both honest: manifesto register for the
argument, Evidence Box register for the claims (lxd's own discipline —
Bastani cited precisely; Kosmyna carried with its single-source flag; Hattie's
d=0.40 hinge as the bar). A Medhavy artifact never states a magnitude it
cannot source. The PEDAGOGY.md gate for this brand audits evidence discipline
as hard as act structure.

**8. STRUGGLE-EVIDENCE LAW.** Where success is measured at all, measure
struggle signals, not applause: the Y1–Y7 ensemble (friction Chs 3–10) —
temporal engagement pattern, error trajectory coherence, cross-context
transfer, uncertainty calibration, social knowledge texture, retrieval
strength decay, scaffolding response curve. For videos this means: the
follow-up exercise and the spaced retrieval prompt are part of the artifact,
not marketing.

## The defaults — theory decides first, the human decides last

Brutalist Medhavy never presents a blank canvas. Every design dimension has a
theory-backed default, applied automatically and logged with its reason:

| Dimension | Default | Why (source) |
|---|---|---|
| Accessibility | WCAG 2.2 AA — contrast, captions, structure — non-negotiable at generation time | UDL and the equity test (lxd Ch 9); the cajal SVG style guide already enforces this house-wide |
| Palette | Established learning palettes: colorblind-safe (Okabe-Ito for data), low-arousal grounds, one accent | signaling without extraneous load (CTML/Mayer; the dataviz + cajal doctrine) |
| Sequencing | Arc-based: hook → predict → struggle → reveal → apply — concrete before abstract, prerequisite-ordered | the pedagogical arc (lxd Ch 6; brownblue doctrine; prediction error as trigger, lxd Ch 3) |
| Cognitive load | Segmenting, signaling, no redundancy, one idea per beat | CLT (lxd Ch 3; humanitarians-courses knowledge files) |
| Facts | Fact-checked before render; every claim carries a source; single-source findings flagged | Evidence Law; the facts/ pipeline; FACTCHECK-SPEC discipline |
| AI's role | Scaffold with a declared fade; phase gate stated in the artifact | Laws 4–5 |

Defaults are **arguments, not verdicts**. Each one is chosen because the
theory says it serves learning — and each one is written down where the human
can reach it.

## The decision log — every artifact ships its reasons

Beside every deliverable: `decisions.json` (+ readable `DECISIONS.md`). One
entry per design decision, stable ID, patch-not-regenerate:

```json
{
  "id": "D-014",
  "beat": "B03",
  "choice": "palette: ink on cream, teal reserved for the second series",
  "default_applied": "colorblind-safe categorical (Okabe-Ito order)",
  "reason": "two series → brand grammar, not rainbow; deuteranopia-safe pair",
  "source": "lxd Ch 9; dataviz palette doctrine",
  "overridable": true
}
```

This is the taxonomy's contract/log discipline applied to design itself: the
system doesn't just make choices, it makes its choices INSPECTABLE. The log is
what turns "the AI decided" into "the AI proposed, with reasons, awaiting your
verdict."

## The override loop — the human is ALWAYS the final judge

Any CLI — Claude Code, Codex, whatever comes next (the workflow is
deliberately CLI-agnostic; see `cli-agnostic-ai-tooling-for-local-project-workflows`)
— can address any decision by ID: *"change D-014 to the red/ink pair"*,
*"override the sequencing default in B04–B06, I want abstract first."* The
system complies, re-renders only what changed, and appends the override to the
log with its own dissent when it has one:
`"overridden_by": "human", "system_note": "contrast now 3.8:1, below AA — flagged, complied."`
No default is ever load-bearing enough to resist a human override. Defaults
without overridability would be paternalism; overrides without logged reasons
would be amnesia. The pair is the system.

## The service — inverted GIGO

This is a paid service in the Midjourney / Higgsfield shape: subscribe or buy
credits, connect (the Medhavy MCP), generate. What the money buys is not
generation — generation is a commodity. It buys the STARTING POINT:

- a fact-checked spine (the `facts/` corpus + every ai1-cli textbook) instead
  of cold generation,
- learning-first defaults (the table above) instead of engagement-shaped ones,
- the decision log instead of an unexplained artifact,
- and exercises + retrieval built in, because the artifact isn't done until
  the learning loop is.

GIGO cuts both ways. Everyone else's pipeline starts from a blank prompt and
inherits the prompt's quality. Medhavy users start from vetted content and
theory-grounded design, then shape it with their own CLI. Quality in, quality
out — the human's judgment is spent on judgment, not on rediscovering WCAG.

## Brand binding

- **Channel:** @MedhavyAI · **Persona:** Medhavy ("intelligent, intellectually
  brilliant" — Sanskrit) · **Register:** Wonder · **Voice:** kokoro `af_kore`
  (override `ELEVENLABS_VOICE_MEDHAVY`).
- **Claude-skin episodes** route through the `claude-medhavy` brand variant
  (claude-explainer channels table): fixed Claude palette for the UI, medhavy
  voice and register for the narration.
- **Non-UI content** (Manim results, lectures, spines) uses the medhavy token
  set (`runtime/remotion/src/tokens/medhavy.ts`).
- **The Medhavy MCP** is this system's distribution: the spine
  (`facts/` + ai1-cli textbooks), the videos, and the exercises served as
  data — vetted starting points people modify, never cold generation. The
  laws above are what the spine's pedagogy field encodes.

## Video grammar (delta from claude-explainer)

Cold open and title-restate outro unchanged. Inside: at least one PREDICT
beat (Law 2); the handoff is an exercise with an explicit do-it-yourself gate
(Law 4); the verdict page includes the phase-gate declaration ("AI did X ·
you do Y · support fades at Z"); and the description ships with a spaced
retrieval prompt dated a week out (Law 8). PEDAGOGY.md for this brand adds
two audit sections: Evidence discipline and Friction protected.

## What this system refuses

The smile sheet as proof. Completion as learning. Fluency as mastery.
Engagement as the goal instead of the exhaust. AI that answers when the
learner should have struggled. And its own manifesto stated as if it were an
Evidence Box — these laws are commitments; the books carry the citations.
