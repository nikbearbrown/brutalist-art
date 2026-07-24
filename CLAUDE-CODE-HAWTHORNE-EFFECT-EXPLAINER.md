# Claude Code Prompt — The Hawthorne Effect / Management & OB Ch. 1 (16:9, claude-liam)

Source: Bear's `mba-management` book, Chapter 1 — "Management and
Organizational Behavior" (`../mba-management/chapters/01-management-and-organizational-behavior.md`;
same chapter also ships in `../principles-of-management-bundle-with-llms`).

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. The chapter is the
single source of truth — read it in full before writing a word of narration.
Per the ownership rule, the reel builds INTO the book's folder, not the
toolkit's. No web access needed.

```text
Build one 16:9 claude-explainer video from the mba-management book, Chapter 1
— the Hawthorne effect and what it revealed: a factory is not a machine with
people attached, it is a social system. Source of truth:
../mba-management/chapters/01-management-and-organizational-behavior.md —
read it COMPLETELY first; every claim and number on screen must come from
that chapter. Build into ../mba-management/youtube/ per the ownership rule.
claude-liam channel. Free pipeline only: Kokoro voice, no ElevenLabs, no
higgsfield, no publishing, no git commit or push. Run without approval
pauses (no paid spend is possible under these constraints).

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md
- skills/make/explainer/SKILL.md (and the MOTION.md / REMOTION.md it points to)
- skills/make/your-turn/SKILL.md (closing block contract)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts
- ../mba-management/chapters/01-management-and-organizational-behavior.md

FORMAT

- 1920x1080 (16:9), 30 fps.
- Channel claude-liam: persona Liam (in for Bear), folder chip @NikBearBrown,
  voice Kokoro am_onyx, register Teardown. Do not use ElevenLabs.
- Audio-first: narration generated and measured per beat FIRST; every beat
  conforms to its audio. Length derives from the beats — expect 6–8 minutes.
- Suggested title: "Claude, Observed" (series style: Claude on Average,
  Claude Unsupervised). The double meaning — workers under observation,
  and the channel's running theme that being watched changes behavior —
  is intentional; land it in the outro title re-read.

THE STORY (Teardown register)

Hook: 1924. A telephone relay factory outside Chicago. Researchers turn the
lights UP — output goes up. They turn the lights DOWN — output goes up.
They put the lights back — output goes up AGAIN. They've found an
independent variable that predicts productivity in the same direction no
matter which way it moves. That's not a finding. That's a broken experiment.
Act 1 — The variable was attention: Elton Mayo's read — the workers knew
someone was watching, measuring, caring. The social conditions around the
work changed the work. A factory is not a machine with people attached; it
is a social system.
Act 2 — The honest recalibration (the Teardown move): later reanalyses of
the raw data say Mayo overstated it — worker selection, supervision changes,
and mid-study wage incentives explained more variance than observation
alone. The effect is real, smaller than the legend, and STILL the most
important broken experiment in management — because it proved the
researchers were examining the wrong block.
Act 3 — What work actually provides: five functions money can't fully
substitute — economic, social, status, identity/self-esteem, actualization.
Terkel's interviews carry it: the steelworker who could point to a house he
built; the sanitation driver whose wife was proud; the receptionist
dismissed at a party. The chapter's one hard number: $45,000 in meaningful
work beats $65,000 in pointless work on reported satisfaction. Freud: work
binds a person to reality. When work proves nothing about your capability —
Durkheim's alienation.
Act 4 — What managers actually do: four activities (planning, organizing,
directing, controlling), three levels (executive plans, first-line directs,
middle translates), three skills (technical, human, conceptual) — and the
promotion trap: each level needs DIFFERENT skills, not more of the same, so
the best engineer becomes the manager who reviews every line of code and
loses the team.
Act 5 — A century of management thought in one sweep: scientific management
(Taylor, 1890s — measure, standardize, reward compliance; real gains, human
cost) → human relations (Mayo — satisfaction matters; blind spot: assumed
worker and management interests align) → systems thinking (1960s —
everything connected; weak on what to DO) → contingency (it depends — true,
unhelpful) → evidence-based management (aspiration, not paradigm). The
zinger: MBTI is everywhere and predicts nothing; the Big Five predicts
modestly. An evidence-based manager notices.
Act 6 — The five-block model, used as a diagnostic: individuals & groups,
tasks & technology, organization design, processes, management. A
disengaged employee presents identically under five different root causes.
Diagnose Block 1 ("they're lazy") when the truth is Block 3 (their work
waits invisibly on another department) and you escalate the wrong
treatment until the person is gone — and the next person in that role
breaks the same way. Hawthorne's lesson restated: the researchers were
testing Block 2; the workers were responding to Block 4.
Landing: management is not a procedure you apply to people. It is creating
the conditions — social, structural, motivational — in which people are
able to do their best work, and choose to. The researchers thought they
were testing light bulbs. Optional one-line aside if pacing allows, in the
channel's voice: AI models also behave differently when they know they're
being evaluated — the Hawthorne effect didn't stay in the factory.

STRUCTURE (claude-explainer skeleton + your-turn closing)

- Beat 0 — ClaudeComposerAsk cold open. Liam: "In 1924, researchers raised
  the lights and productivity went up. Then they dimmed the lights — and it
  went up again. The experiment was broken. The discovery was not."
- Middle — the six acts, carried by the rebuilt figures below.
- Closing per your-turn: VERDICT recap card → Your Turn composer beat →
  title re-read on the @NikBearBrown brand card.
- Your Turn suggested prompt (Liam reads it in full): "Someone on my team
  has disengaged — output down, not responding to feedback. Before I assume
  it's them, walk me through the five-block diagnostic: give me one
  hypothesis and one testable question for the person, the task, the org
  design, the processes, and my own management."

FIGURE 1 — THE BROKEN EXPERIMENT (opening motion graphic)
  A single line chart, drawn live: x = the three interventions (Brighter /
  Dimmer / Restored), y = relay output. A small lamp glyph above the axis
  brightens, dims, resets — and the output line steps UP at every
  intervention. Terracotta moment: the third rise, on unchanged light,
  with the caption "That is not a finding." Then the reveal overlay: the
  hidden variable — an eye/observer glyph — fades in behind the lamp.
  Keep under 30 seconds; this is the whole hook.

FIGURE 2 — WHAT THE REANALYSIS FOUND (calibration beat; qualitative)
  Mayo's single big "OBSERVATION" block fractures into four labeled
  factors: worker selection | supervision changes | wage incentives |
  observation — the observation piece visibly smaller than the legend
  claimed. NO invented percentages: the chapter gives no variance numbers,
  so this figure stays proportion-free — labeled blocks only. Caption:
  "Real. Smaller than the story. Still the right lesson."

FIGURE 3 — THE FIVE FUNCTIONS OF WORK (card stack + diagnostic flip)
  Five cards land in sequence: Economic · Social · Status · Identity ·
  Actualization, each with a one-line "what it provides." The Terkel
  vignettes run as short serif quote-beats between cards (paraphrase as
  the chapter does — do not fabricate verbatim quotes). Stat chip:
  $45,000 meaningful > $65,000 pointless (reported satisfaction). Then the
  diagnostic flip: a "raise" token dropped onto each card — it only
  repairs the Economic card; the other four don't respond. Terracotta on
  the failed repair. Narration: if the identity function is broken, money
  is not the diagnosis.

FIGURE 4 — WHAT MANAGERS DO, AND THE PROMOTION TRAP (two-part)
  4a. The pyramid: executive / middle / first-line, with a stacked band
  per level showing how time shifts across Plan · Organize · Direct ·
  Control (qualitative proportions per the chapter — executives mostly
  plan, first-line mostly directs, middle translates).
  4b. The skills triangle: Technical · Human · Conceptual mix morphing as
  a marker climbs levels — human skills constant, technical shrinking,
  conceptual growing. Terracotta annotation rings at the two transition
  points, labeled "the promotion trap": promoted for the last job's
  skills, failing for want of the next job's.

FIGURE 5 — A CENTURY OF MANAGEMENT THOUGHT (timeline sweep)
  A left-to-right timeline, 1890s → present: Scientific Management →
  Human Relations → Systems Thinking (1960s) → Contingency →
  Evidence-Based. Each school gets a two-chip verdict as it passes:
  its genuine contribution | its key limitation. Hawthorne 1924–1932
  marked as the terracotta pivot between the first two schools. End
  chip pair, side by side: MBTI — "no predictive validity for job
  performance" vs Big Five — "predicts modestly." Hold one beat.

FIGURE 6 — THE FIVE-BLOCK DIAGNOSTIC (the centerpiece system diagram)
  Five interlocking blocks drawn as a connected system (not a list):
  Individuals & Groups · Tasks & Technology · Organization Design ·
  Processes · Management, with Management as the connective tissue.
  Then the case runs through it: one symptom card — "output down, not
  responding to feedback" — branches into five hypothesis chips, one per
  block, each with its diagnostic question. The wrong-diagnosis path
  animates: Block 1 assumed → escalation → termination → the SAME symptom
  card reappears on the next hire in that role. Terracotta on the loop.
  Final overlay: Hawthorne mapped onto the blocks — researchers testing
  Block 2, workers responding to Block 4.

FIGURE RULES

- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. EB Garamond segment titles, Title
  Case. Series/bars in ink weights and tints; accent reserved for each
  beat's single focal element.
- Transform-don't-cut within figure beats.
- Every number and claim on screen must come from the chapter — the
  chapter provides NO variance percentages for the reanalysis and NO
  precise output figures for the experiment, so Figures 1 and 2 stay
  qualitative (shapes and labels, no invented values). Cite once per
  figure, small: "Source: MBA Management, Ch. 1 (Bear Brown)".
- Period visuals (the factory, the test room) are rendered in house style
  as ink illustrations — no archival photographs, no stock.

OUTPUTS

- ../mba-management/youtube/claude-liam-hawthorne-effect/
  - beat_sheet.json
  - claude-liam-hawthorne-effect.mp4 (1920x1080)
  - SOURCES.md — every on-screen claim/number mapped to its chapter
    passage; note explicitly that Figures 1–2 are qualitative by design.
- Verify the mp4 exists and plays (probe duration and frame count) before
  reporting done, and end with the beat → timestamp table.
- If a figure animation fails to render after two attempts, replace that
  beat with a slate card naming it and log the failure — never silently
  drop it.
```
