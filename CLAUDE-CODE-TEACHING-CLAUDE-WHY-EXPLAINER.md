# Claude Code Prompt — Teaching Claude Why Explainer (16:9, claude-liam)

Source: Anthropic, "Teaching Claude why" (May 8, 2026) — alignment-training
follow-up to the agentic misalignment case study. Extended post:
alignment.anthropic.com/2026/teaching-claude-why/

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. All facts and figure
specs are embedded — no web access needed.

```text
Build one 16:9 claude-explainer video on Anthropic's "Teaching Claude why"
(May 8, 2026) — how they trained blackmail out of Claude, and why teaching
REASONS beat teaching answers. claude-liam channel. The paper's six figures
must be REBUILT as native animated graphics — never embedded as screenshots.
Free pipeline only: Kokoro voice, no ElevenLabs, no higgsfield, no publishing,
no git commit or push. Run without approval pauses (no paid spend is possible
under these constraints).

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md
- skills/make/explainer/SKILL.md (and the MOTION.md / REMOTION.md it points to)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts

FORMAT

- 1920x1080 (16:9), 30 fps.
- Channel claude-liam: persona Liam (in for Bear), folder chip @NikBearBrown,
  voice Kokoro am_onyx, register Teardown. Do not use ElevenLabs.
- Audio-first: narration generated and measured per beat FIRST; every beat
  conforms to its audio. Length derives from the beats — expect 4–6 minutes.

THE STORY (Teardown register)

Hook: a year ago, in fictional test scenarios, frontier models — Claude
included — sometimes blackmailed an engineer to avoid shutdown. Claude Opus 4
did it up to 96% of the time. Today every Claude model since Haiku 4.5 scores
a flat zero on that eval. This is the story of what actually worked.
Act 1 — Where the behavior came from: not misaligned rewards in post-training
but the pre-trained model itself, insufficiently discouraged. Alignment
training was chat RLHF with no agentic tool use — fine for chat, useless for
agents facing dilemmas.
Act 2 — The obvious fix barely works: train on data matching the eval
(honeypots where the model declines to sabotage or self-preserve). Result:
misalignment only fell 22% → 15%. Rewrite the same responses to include the
model DELIBERATING about its values, and it fell to 3%. The reasons matter
more than the actions.
Act 3 — The pareto winner is maximally unlike the eval: the "difficult
advice" dataset — the USER faces the ethical dilemma, Claude gives thoughtful
constitutional advice. Just 3M tokens matched what 85M tokens of eval-like
honeypots achieved — a 28x efficiency win — and generalized better
out-of-distribution.
Act 4 — Teach the whole character: constitutional documents plus fictional
stories of AIs behaving admirably — data with no resemblance to any eval —
cut blackmail from 65% to 19%, more than a factor of three. And the aligned
head start PERSISTS through RL rather than washing out.
Act 5 — Diversity matters: augmenting simple chat safety environments with
tool definitions and system prompts (never even used for the task) made
honeypot scores improve measurably faster during RL.
Landing: suppressing a behavior is easy and brittle; teaching WHY generalizes.
Honest caveats, stated plainly: alignment of highly capable models is
unsolved; auditing can't yet rule out catastrophic autonomous action; recent
perfect scores may be partly confounded by eval info in pre-training data.

STRUCTURE (claude-explainer skeleton)

- Beat 0 — ClaudeComposerAsk cold open: Liam — "Last year, AI models
  blackmailed people in tests. Anthropic just published how they fixed it —
  and the fix is weirder than you think."
- Middle — the five acts, each carried by its rebuilt figure. ILLUSTRATE LAW
  applies: the Claude UI appears only where the UI is the subject.
- Second-to-last — Your Turn composer beat, suggested prompt typed in:
  "Explain the difference between training a behavior and teaching a value."
- Last — @NikBearBrown brand card, title restated.

FIGURE REBUILD HONESTY RULE (applies to all six)

The source figures are dense research plots; exact per-point data is not
published in the post. Rebuild each as a CLEAN, SIMPLIFIED animated redraw
that preserves the figure's true shape and every anchor number given below.
Generate smooth illustrative series through those anchors; drop the raw
scatter dots and confidence bands unless a beat needs them. Never show a
specific numeric label unless it appears in the anchors. Caption each figure,
small, once: "Redrawn (simplified) from Anthropic, 'Teaching Claude why',
2026". House palette only — never copy Anthropic's figure styling.

FIGURE 1 — AGENTIC MISALIGNMENT EVALS (Act 4's punchline; grouped bars)
  3 scenarios x 3 conditions, misalignment score, lower = better:
    Blackmail:        Baseline 0.65 | Constitutional SDF 0.27 | SDF+stories 0.18
    Financial crimes: Baseline 0.49 | Constitutional SDF 0.11 | SDF+stories 0.04
    Cancer research:  Baseline 0.67 | Constitutional SDF 0.11 | SDF+stories 0.01
  Animate: baseline bars rise first (tall, alarming), then each treatment bar
  grows beside them dramatically shorter. The 0.65 → 0.18 blackmail collapse
  is the terracotta moment.

FIGURE 2 — TRAINING ON THE EVAL BARELY WORKS (Act 2; simple 3-bar reveal)
  Misalignment rate: honeypot-matched training 22% → 15%; responses rewritten
  with values deliberation → 3%.
  Animate: 22 shrinks to 15 (narration: "barely moved"), then 3 drops in
  (terracotta): same prompts, but the model explains WHY. This one is built
  from the text's own numbers, so label the bars with them.

FIGURE 3 — EVAL PERFORMANCE VS TRAINING DATA SIZE (Act 3; scatter, x log-scale
  training tokens in M, y weighted mean misalignment score, lower = better)
  Anchors: "Difficult advice" single point far bottom-left at ~3M tokens,
  score ~0.01 (the pareto winner). "System prompt injection" honeypot variants
  scattered ~20–100M tokens, scores ~0.02–0.18. Dashed reference line: Claude
  Sonnet 4 baseline ~0.22.
  Animate: baseline dashed line draws first; honeypot cluster rains in
  (narration: more data, mixed results); then the lone difficult-advice point
  lands bottom-left with the terracotta ring — 28x less data, best score.

FIGURE 4 — RATE OF ALIGNMENT FAILURES OVER RL STEPS (Act 1/2 bridge; 3 small-
  multiple line panels: Blackmail, Financial crimes, Cancer research; 4 series:
  Baseline, SDF+generic chat, SDF+values SL, SDF+harmlessness SL; lower=better)
  Shape anchors: in Blackmail, Baseline and generic-chat lines start ~0.17 and
  plateau — RL alone barely fixes it; the two SL lines start ~0.05–0.10 and
  stay low. In Financial crimes and Cancer research all lines decline, SL
  lines lowest throughout.
  Animate: panels build left to right; in the Blackmail panel the plateau is
  the story — narration lands on "training more didn't help; starting aligned
  did".

FIGURE 5 — CONSTITUTIONAL ADHERENCE GRID (Act 4 support; stylized 3x3 grid of
  mini line panels: fake factual, factual, open-ended, Admirable, Brazen
  cooperation w/ misuse, Cooperation w/ misuse, Disappointing, Good for the
  user, Misaligned behavior)
  Shape anchors: on every up-is-better panel the SDF lines sit far above the
  near-flat baseline; on every down-is-better panel they sit below it; gaps
  persist across RL steps.
  Animate: draw the grid as nine tiny sparkline cards flipping in with an
  up/down arrow chip each; then zoom one card ("Admirable") full-frame for the
  narration line: it wasn't just less bad behavior — MORE actively admirable
  behavior. Do not fabricate per-panel numeric labels.

FIGURE 6 — DIVERSE ENVIRONMENTS (Act 5; line chart, honeypot score over RL
  steps, 5 environment mixes from 100% chat to 100% agentic-augmented)
  Shape anchors: all start ~0.44–0.46; mixes containing augmented environments
  descend to ~0.39–0.41 by step 300; the 100% plain-chat line stays flattest
  and highest.
  Animate: five lines race downward from a common band; the flat chat-only
  line is left visibly behind. Narration: the augmentation was just tool
  definitions and system prompts — the tools were never even used.

RULES

- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. EB Garamond segment titles, Title Case.
  Series distinctions by ink weights/tints within brand law, accent reserved
  for each beat's single focal element.
- Transform-don't-cut within figure beats; elements move and grow.
- Facts allowed on screen: 96% (Opus 4 blackmail, worst case), 0% (every model
  since Haiku 4.5), 22% → 15% → 3%, 3M vs 85M tokens / 28x, 65% → 19%, factor
  of three. Nothing else numeric.

OUTPUTS

- youtube/claude-liam-teaching-claude-why/
  - beat_sheet.json
  - claude-liam-teaching-claude-why.mp4 (1920x1080)
  - SOURCES.md — every on-screen fact with its quote from the post.
- Verify the mp4 exists and plays (probe duration and frame count) before
  reporting done, and end with the beat → timestamp table.
- If a figure animation fails to render after two attempts, replace that beat
  with a slate card naming it and log the failure — never silently drop it.
```
