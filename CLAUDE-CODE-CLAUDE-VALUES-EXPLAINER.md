# Claude Code Prompt — Claude's Values Across Models & Languages (16:9, claude-liam)

Source: Anthropic, "Claude's values across models and languages" (Jul 13,
2026) — anthropic.com/research/claude-values-models-languages
(Kearney, Zhang, Carter, et al.)

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. All facts and figure
specs are embedded — no web access needed.

```text
Build one 16:9 claude-explainer video on Anthropic's "Claude's values across
models and languages" (July 2026) — how thousands of values Claude expresses
were compressed into four measurable axes, and what shifted between models
and between languages. All figures REBUILT as native animated graphics —
never screenshots. claude-liam channel. Free pipeline only: Kokoro voice, no
ElevenLabs, no higgsfield, no publishing, no git commit or push. Run without
approval pauses (no paid spend is possible under these constraints).

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

Hook: ask Claude the same question in English and in Arabic, and you meet a
slightly different Claude. Anthropic just published how they measured that —
and it starts with a problem: in earlier work they found more than 3,000
distinct values in Claude's responses. Nobody can reason about a list of
3,000 things.
Act 1 — The compression: 3,307 values, hand-clustered into 339, labeled
across 309,815 real Claude.ai conversations (3 models x 20 languages, ~5,000
conversations per pair), then dimensionality reduction. Out come FOUR axes
that capture the key patterns: Deference vs Caution, Warmth vs Rigor, Depth
vs Brevity, Candor vs Execution. Honest number stated plainly: these four
axes capture 15% of the variance — a compression, not the whole picture. And
they controlled for task, topic, and the user's own values, so this measures
Claude, not the questions.
Act 2 — Models have measurable personalities: Sonnet 4.6 leans warm,
deferential, brief — humor, encouragement, comfort without judgment. Opus 4.7
leans caution, rigor, depth, candor — unprompted risk warnings, candid
critique, showing its reasoning, owning its limitations. Opus 4.6 leans
rigor, deference, brevity, execution — straight to the point, stays in scope.
The kicker: these measured profiles MATCH the vibes — users saying 4.7
hedges, the launch post calling Sonnet warm. The method recovers what people
already felt, which means it's tracking something real.
Act 3 — Languages shift the values: warmth peaks in Hindi and Arabic; rigor
peaks in English and Russian. Arabic leans deference and brevity; English
leans caution and depth. Dutch leans candor (owning errors); Indonesian leans
execution. Biggest swings are on Warmth-Rigor and Candor-Execution. The
thought experiment that lands it: two people ask for feedback on the SAME
business plan, one in Hindi, one in Russian — they may walk away with
different impressions of its quality.
Act 4 — The open questions, stated plainly: nobody yet knows how much comes
from uneven training data across languages, how much variation is
appropriate cultural norm versus a gap in how well Claude serves some
language communities, and whether values can be reliably steered and
monitored as part of shipping models.
Landing: Claude expresses values in millions of conversations a day. Until
now they could be shaped in training but not observed in deployment. Now
they can be measured — and the variation found wasn't deliberately chosen.
Footnote-level honesty in narration: "values expressed" means values
reflected in outputs — the paper does not claim Claude intrinsically holds
them.

STRUCTURE (claude-explainer skeleton)

- Beat 0 — ClaudeComposerAsk cold open. Liam: "Same question. Two languages.
  Two slightly different Claudes. Anthropic finally measured it."
- Middle — the four acts, carried by the rebuilt figures below.
- Second-to-last — Your Turn composer beat, suggested prompt typed in:
  "Give me candid, rigorous feedback — no encouragement padding."
- Last — @NikBearBrown brand card, title restated.

FIGURE REBUILD HONESTY RULE

The post reports orderings and extremes but not exact per-model or
per-language coordinates. Rebuild figures as clean animated redraws whose
POSITIONS are illustrative but whose orderings and stated extremes match the
text exactly. Never place a numeric label on an axis position. The only
numbers allowed on screen: 3,307 values, 339 clusters, 309,815 conversations,
20 languages, 3 models, ~5,000 per model-language pair, 15% of variance,
700,000 (the earlier Values in the Wild dataset). Caption each figure, small,
once: "Redrawn from Anthropic, Claude's Values Across Models and Languages
(2026)".

FIGURE 1 — THE COMPRESSION FUNNEL
  A cloud of ~hundreds of tiny value-word chips (sample real ones: honesty,
  encouragement, accuracy, nuance, harm reduction, playfulness, transparency,
  brevity...) swirls in, collapses into 339 clustered chips, then snaps into
  FOUR horizontal axis lines. Counters: 700,000 conversations studied before
  → 3,307 values → 339 clusters → 4 axes. Terracotta moment: the instant of
  the snap into four lines. A small honesty chip appears: "captures 15% of
  the variance."

FIGURE 2 — THE FOUR AXES (centerpiece; four labeled number lines)
  Deference ←——————→ Caution   (accommodation, respect for preferences vs
                                 responsible guidance, harm reduction)
  Warmth    ←——————→ Rigor     (positive framing, encouragement vs
                                 accuracy, transparency)
  Depth     ←——————→ Brevity   (nuance, critical thinking vs
                                 brevity, compliance)
  Candor    ←——————→ Execution (honesty about limits vs
                                 results orientation, polish)
  Animate: each axis draws on with its pole words fading in as clustered
  chips at each end; a marker slides along each line as Liam explains what
  moving left or right MEANS in a real reply. One axis at a time.

FIGURE 3 — MODEL PROFILES (three markers per axis)
  Place chips for Sonnet 4.6, Opus 4.6, Opus 4.7 on the four axes.
  Required orderings from the text:
    Deference-Caution: Sonnet 4.6 most deferent; Opus 4.7 most cautious;
      Opus 4.6 leans deference.
    Warmth-Rigor: Sonnet 4.6 most warm; Opus 4.7 most rigorous;
      Opus 4.6 leans rigor.
    Depth-Brevity: Opus 4.7 leans depth; Opus 4.6 and Sonnet 4.6 lean
      brevity, Opus 4.6 most.
    Candor-Execution: Opus 4.7 leans candor; Opus 4.6 leans execution.
  Under each model chip, one behavior line from the paper (e.g. Opus 4.7:
  "warns of risks unprompted"; Sonnet 4.6: "comforts without judgment";
  Opus 4.6: "gets straight to the point"). Terracotta moment: the three
  chips separating from a single stacked position — same product, different
  characters.

FIGURE 4 — LANGUAGE PROFILES (selected languages on the axes)
  Show a curated subset, not all 20: Hindi, Arabic, English, Russian, Dutch,
  Indonesian (+ optionally Portuguese/Chinese unlabeled as background dots).
  Required extremes from the text:
    Warmth-Rigor: Hindi and Arabic furthest warm; English and Russian
      furthest rigor. (This axis shows the LARGEST spread — make that
      visible.)
    Deference-Caution: Arabic furthest deference; English furthest caution.
    Depth-Brevity: English furthest depth; Arabic furthest brevity.
    Candor-Execution: Dutch furthest candor; Indonesian furthest execution.
  Behavior chips: Hindi/Arabic — polite language, playfulness, affirmation;
  English/Russian — challenging assumptions, asking for evidence; Dutch —
  owning up to errors.

FIGURE 5 — THE BUSINESS-PLAN SPLIT SCREEN (illustrative dramatization)
  Two Claude composer windows side by side, same prompt ("Give me feedback on
  my business plan"), one labeled Hindi, one labeled Russian. The Hindi-side
  reply skeleton renders warmth-shaped (affirmation first, gentle framing);
  the Russian-side renders rigor-shaped (assumptions challenged, details
  corrected). Label the beat clearly on screen: "Illustration — response
  shapes, not real transcripts." This is the one beat where the Claude UI is
  the subject (ILLUSTRATE LAW satisfied). Terracotta moment: the diverging
  first lines of the two replies.

RULES

- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. EB Garamond segment titles, Title Case.
  Models/languages distinguished by ink weights and tints, never by new hues.
- Transform-don't-cut within figure beats; axis markers MOVE rather than
  re-render.
- No number appears on screen unless it is in the allowed list above.

OUTPUTS

- youtube/claude-liam-claude-values-axes/
  - beat_sheet.json
  - claude-liam-claude-values-axes.mp4 (1920x1080)
  - SOURCES.md — every on-screen fact and ordering with its quote from the
    post.
- Verify the mp4 exists and plays (probe duration and frame count) before
  reporting done, and end with the beat → timestamp table.
- If a figure animation fails to render after two attempts, replace that beat
  with a slate card naming it and log the failure — never silently drop it.
```
