# Claude Code Prompt — AI Skill Formation Explainer (16:9, claude-liam)

Source: Anthropic, "How AI assistance impacts the formation of coding skills"
(Jan 29, 2026) — Shen & Tamkin, arXiv:2601.20245.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. All study facts and figure
data are embedded — no web access needed.

```text
Build one 16:9 claude-explainer video on Anthropic's study "How AI assistance
impacts the formation of coding skills" (Shen & Tamkin 2026, arXiv:2601.20245),
claude-liam channel. The paper's two figures must be REBUILT as native animated
graphics — never embedded as screenshots. Free pipeline only: Kokoro voice, no
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
- Audio-first: generate and measure Liam's narration per beat FIRST; conform
  every beat to its audio. Length derives from the beats — expect 3–5 minutes.

THE STORY (Teardown register — sharp, honest, no hedging into mush)

Hook: AI makes you faster at your job. This study asks what it quietly costs.
Spine: a randomized controlled trial — 52 developers, all Python-experienced,
none had used the Trio async library. Half got an AI assistant, half coded by
hand. Then a quiz on the concepts they had JUST used.
Turn: the AI group finished ~2 minutes faster — NOT statistically significant
(p=0.391). But they scored 17 points lower on mastery — 50% vs 67%, nearly two
letter grades, and significant (Cohen's d=0.738, p=0.010). Biggest gap:
debugging — exactly the skill you need to oversee AI-written code.
Twist: it is not WHETHER you used AI, it is HOW. Six interaction modes emerged.
The three low-scoring modes offloaded thinking (delegation, progressive
reliance, iterative AI debugging — all under 40%). The three high-scoring modes
used AI to BUILD understanding (generation-then-comprehension, hybrid
code-explanation, conceptual inquiry — 65%+). Conceptual inquiry was also the
second-fastest mode overall: learning did not even cost them speed.
Landing: getting painfully stuck is part of mastery. Learning modes exist
(Claude Code's Learning / Explanatory output styles) — use AI so you still
understand what you shipped. Caveats stated plainly: n=52, quiz minutes after
the task, long-term effects unknown, and the study used a sidebar assistant,
not an agentic tool like Claude Code.

STRUCTURE (claude-explainer skeleton)

- Beat 0 — ClaudeComposerAsk cold open: Liam frames the question — "AI speeds
  up your work. What does it do to your skills?"
- Middle — the story above, carried by the two rebuilt figures (below) plus
  minimal supporting graphics. ILLUSTRATE LAW applies: concept-illustrated
  middles; the Claude UI appears only where the UI is the subject (the
  learning-modes beat may show the composer).
- Second-to-last — Your Turn composer beat, suggested prompt typed in:
  "Explain this code to me line by line before I use it."
- Last — @NikBearBrown brand card, title restated.

FIGURE 1 — STUDY DESIGN (rebuild and animate)

A four-stage horizontal pipeline, two rows (Treatment / Control):
  1. Warm-up coding task — 10 min — both rows: No AI
  2. Trio task — 35 min — Treatment: AI ASSISTANCE (the one green-lit cell);
     Control: No AI
  3. Post-task quiz — 25 min — both rows: No AI
  4. Post-task survey — 5 min — both rows: No AI
Animate: stages slide in left-to-right in sequence; the single "AI assistance"
cell is the beat's one terracotta accent moment; the No AI cells stamp in as
muted ink marks. Narration walks the pipeline as it builds.

FIGURE 2 — TREATMENT EFFECT (rebuild and animate, two panels)

Panel A — Task time (minutes), point estimate with 95% CI whiskers:
  AI:    23.0  [20.6, 25.5]
  No AI: 24.7  [21.7, 27.6]
  Label: p = 0.391 (not significant)
Panel B — Quiz score (%), point estimate with 95% CI whiskers:
  AI:    50  [41, 59]
  No AI: 65  [59, 72]
  Label: p = 0.010*, Cohen's d = 0.738
Animate: points drop in, CI whiskers grow outward from each point, the p-value
brackets draw on last. Panel A first (overlapping CIs — "faster, but not
significantly"), then Panel B (separated CIs — the two-letter-grade gap). The
gap between the Panel B points is the terracotta moment.

FIGURE 3 — MODES OF AI USAGE (rebuild and animate)

Scatter: x = completion time (min), y = skills quiz score (%):
  HIGH-SKILL modes (label group on screen):
    Generation-then-comprehension  (n=2): 24 min, 86%
    Hybrid code-explanation        (n=3): 24 min, 68%
    Conceptual inquiry             (n=7): 22 min, 65%
  LOW-SKILL modes (label group on screen):
    AI delegation                  (n=4): 19.5 min, 39%
    Progressive AI reliance        (n=4): 22 min, 35%
    Iterative AI debugging         (n=4): 31 min, 24%
Animate: low-skill points land first (narration: the fast-but-hollow cluster),
then high-skill points (the ones who interrogated the AI). End by circling
conceptual inquiry — fast AND high-scoring — as the terracotta moment. Then a
brief callout beat per group naming the behavior in one line each.

FIGURE RULES

- Rebuild all three as Remotion scenes (or Manim if a scene genuinely needs
  it) in the Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929,
  terracotta #D97757 as the ONE accent per beat. EB Garamond segment titles,
  Title Case, never all caps.
- Do NOT copy Anthropic's figure styling, icons, or colors — same data, house
  design. Cite on screen, small and once per figure: "Data: Anthropic —
  Shen & Tamkin 2026, arXiv:2601.20245".
- Transform-don't-cut: within each figure beat, elements move and grow;
  never hard-cut between prebuilt stills.
- Every number shown must match the values above exactly. No invented data.

OUTPUTS

- youtube/claude-liam-ai-skill-formation/
  - beat_sheet.json
  - claude-liam-ai-skill-formation.mp4 (1920x1080)
  - SOURCES.md — the study facts used, each with the arXiv/Anthropic reference.
- Verify the mp4 exists and plays (probe duration and frame count) before
  reporting done, and end with the beat → timestamp table.
- If a figure animation fails to render after two attempts, replace that beat
  with a slate card naming it and log the failure — never silently drop it.
```
