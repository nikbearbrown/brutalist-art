# Claude Code Prompt — Coding Agents in the Social Sciences (16:9, claude-liam)

Source: Anthropic, "Coding agents in the social sciences" (May 27, 2026) —
anthropic.com/research/coding-agents-social-sciences (Lyttelton, Massenkoff,
Wilmers). Survey of 1,260 quantitative social scientists, Feb–Mar 2026.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. All data is embedded —
values marked (†) were digitized from the report's published figures and are
correct to the precision shown; everything else is verbatim from the article
text. Where the text rounds differently from a figure (e.g. "20%" vs the
figure's 19% reference line), use the figure value on charts and note it in
SOURCES.md. No web access needed.

```text
Build one 16:9 claude-explainer video on Anthropic's "Coding agents in the
social sciences" (May 2026) — the survey of 1,260 social scientists showing
coding agents diffusing unevenly into research: economists in, education
researchers out; juniors in, tenured out; men at twice the rate of women —
and agent users posting far more working papers while journal submissions
stay flat. All figures REBUILT as native animated graphics — never
screenshots. claude-liam channel. Free pipeline only: Kokoro voice, no
ElevenLabs, no higgsfield, no publishing, no git commit or push. Run without
approval pauses (no paid spend is possible under these constraints).

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md
- skills/make/explainer/SKILL.md (and the MOTION.md / REMOTION.md it points to)
- skills/make/your-turn/SKILL.md (closing block contract)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts

FORMAT

- 1920x1080 (16:9), 30 fps.
- Channel claude-liam: persona Liam (in for Bear), folder chip @NikBearBrown,
  voice Kokoro am_onyx, register Teardown. Do not use ElevenLabs.
- Audio-first: narration generated and measured per beat FIRST; every beat
  conforms to its audio. Length derives from the beats — expect 5–7 minutes.
- Suggested title: "Claude, Peer-Reviewed" (series style: Claude on Average,
  Claude Observed). Restate the report name in the description.

THE STORY (Teardown register)

Hook: 81% of social scientists have tried AI in their research. Only 20%
have adopted coding agents — tools that write AND run the analysis. But the
ones who have are posting 73% more working papers. The people who study the
economy are being changed by the thing they study.
Act 1 — Chatbot vs coding agent: the distinction that carries the report.
A chatbot suggests code; an agent takes a research idea and a dataset,
writes the analysis, runs it, reads the output, iterates. What was
irreducibly human in empirical research is, for the first time, automatable.
Among agent users, Claude Code dominates: 86% use it (Codex next at 31%).
Act 2 — Adoption is a gradient, and it's steep: economics 38% down to
education 4%. Steeper than the AI-use gradient. Then the who: 27% of PhD
students, 9% of full professors — adoption falls by more than half at
tenure. Male-named researchers adopt at MORE THAN TWICE the rate of
female-named (22% vs 9%). Top-25 universities run 40% higher (24% vs 17%).
All significant at p<0.05, all starker than the gaps in general AI use —
the agent era is opening MORE unequal than the chatbot era, and the gender
gap persists even among researchers who already tried AI, within the same
disciplines and career stages.
Act 3 — What they actually do with it: not the slop panic. The discourse
fears AI-written papers; the data shows AI-written CODE. 97% of agent
users generate analysis code; only about a third of all AI users have
drafted prose at all. Editing beats drafting everywhere; only economists
and management researchers commonly draft.
Act 4 — The productivity ladder and the last mile (the centerpiece):
agent users vs non-users in the same discipline and career stage — projects
started +9%, grant proposals +33%, working papers +73%… then the ladder
stops. Journal submissions +3%, resubmissions −6%: statistically nothing.
Two readings, given honestly: agents are new and papers take time to reach
journals — or agents are great at getting projects RUNNING and no help
perfecting the last mile. And the standing caveat, stated plainly:
descriptive, not causal — early adopters may simply be the already-productive.
Act 5 — The expectations paradox: researchers are optimistic about AI
writing publishable papers (88% above the scale midpoint, half at 8+), and
optimism rises with use. But 70% are MORE optimistic about paper
productivity than about the field as a whole. They believe it'll help THEM
publish — and suspect the flood might hurt the SCIENCE: congestion,
attention competition, selective reporting at scale.
Landing: this survey is the baseline of a randomized experiment — Anthropic
is handing researchers Claude Code and measuring what happens; results to
come. Meanwhile the way we study the economy and society already runs, in
part, through analysis decisions made by AI. Caveats plainly: 1,260
self-selected respondents recruited with Claude Max access, quantity
measured but not quality.

STRUCTURE (claude-explainer skeleton + your-turn closing)

- Beat 0 — ClaudeComposerAsk cold open. Liam: "Four out of five social
  scientists have tried AI. One in five lets it run the analysis. That one
  in five is pulling ahead — and it's not who you'd hope."
- Middle — the five acts, carried by the rebuilt figures below.
- Closing per your-turn: VERDICT recap card → Your Turn composer beat →
  title re-read on the @NikBearBrown brand card.
- Your Turn suggested prompt (Liam reads it in full): "Here's my research
  question and a description of my dataset. Plan the full analysis
  pipeline, then split it honestly: which steps could you run autonomously
  as a coding agent, and which decisions should stay mine?"

FIGURE 1 — CHAT VS AGENT (concept beat + stat band)
  Split-screen loop diagrams: left, the chatbot turn cycle (human asks →
  AI suggests → human runs → repeat); right, the agent loop (idea +
  dataset in → write → RUN → read output → iterate → result out), the run
  arrow in terracotta. Stat band lands: 81% have tried AI · 20% use coding
  agents · among users, Claude Code 86%, Codex 31%.

FIGURE 2 — THE DISCIPLINE GRADIENT (rebuilt dumbbell chart; † exact)
  Dumbbells per discipline, agent use (filled, terracotta focal) vs AI use
  (open circle), with reference rules at 19% (overall agent) and 81%
  (overall AI):
    Economics n=209: 38 | 91      Political Science n=216: 25 | 85
    Management Sciences n=202: 18 | 82    Psychology n=172: 12 | 81
    Sociology n=262: 11 | 78      Public Health n=84: 6 | 63
    Communication n=36: 6 | 86    Education n=45: 4 | 67
  Animate top-down; the gap between the two dots per row IS the story —
  Communication's 86% AI use vs 6% agent use gets the terracotta ring:
  trying AI is universal; letting it run the analysis is not.

FIGURE 3 — WHO ADOPTS (rebuilt disparity bars; † exact)
  Paired panels — AI use | Coding agent use — grouped rows with n chips:
    PhD student 92|27 (n=384) · 0–10y post-PhD 83|22 (n=435) ·
    11+ post-PhD 70|9 (n=439)
    Pre-tenure 87|24 (n=782) · Tenured 72|11 (n=478)
    Typically male name 81|22 (n=561) · Typically female name 78|9 (n=374)
    Top-25 83|24 (n=354) · Outside top-25 81|17 (n=906)
    Private 84|23 (n=367) · Public 80|17 (n=846)
  The move: AI-use bars land first and look nearly equal (81 vs 78 by
  gender — a 3-point gap); then the agent-use panel lands and the SAME
  comparison is 22 vs 9 — more than double. Terracotta on the gender pair.
  Caption: all differences p < 0.05. Optional career-stage line variant
  († PhD 92/27, Postdoc 89/28, Asst 81/19, Assoc 75/12, Full 68/9) if
  pacing wants a second view; otherwise skip it.

FIGURE 4 — WHAT THEY USE IT FOR (rebuilt paired bars; † exact)
  Agent users vs other AI users, share selecting each use case:
    Code 97 | 77        Edit prose 87 | 72     Method advice 77 | 63
    Lit review 76 | 60  Draft prose 54 | 30    Generate ideas 47 | 32
  Bars cascade in rank order; the Draft-prose pair gets the annotation:
  the slop panic is about writing — the adoption is about code. Aggregate
  chip: only about a third of all AI users have drafted prose at all.
  Optional quick heatmap chip by discipline († Code row: Econ 93, PolSci
  85, Soc 82, Psych 81, MgmtSci 75, Health/Educ/Comms 71) — one beat max.

FIGURE 5 — THE LADDER AND THE LAST MILE (rebuilt dot-whisker; † exact)
  Horizontal dot-whisker chart, x = agent user minus non-user as % of
  non-user mean, zero line center, controlled for discipline, career
  stage, survey week:
    Empirical projects started +9* | Grant proposals submitted +33** |
    Working papers posted +73** | Conference submissions +10 |
    Journal submissions +3 | Journal resubmissions −6
  (whiskers = 95% CI; * p<0.05, ** p<0.01 — mark significance on the
  chart.) Animate the ladder climbing: +9, +33, +73 — then the drop to
  +3 and −6 lands flat on the zero line. Terracotta on the +73, then a
  second terracotta moment on the flatline pair, captioned "the last
  mile." Narration carries both readings AND the not-causal caveat.

FIGURE 6 — THE EXPECTATIONS PARADOX (rebuilt two-panel; † digitized)
  Left: two rising lines vs number of AI use cases adopted (0→6) on the
  1–10 positivity scale — Productivity ~6.1 → ~8.6 above, Field impact
  ~4.6 → ~6.9 below; the lines rise together but NEVER meet. Right panel:
  non-agent (productivity ~7.2, field ~5.4) vs agent users (~8.6, ~7.0).
  Terracotta shades the persistent gap between the lines. Stat chips: 88%
  above the midpoint on productivity; half at 8+; 70% more optimistic
  about papers than about the field. Narration: good for my papers,
  unclear for my science.

FIGURE RULES

- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. Do NOT copy the report's blue/ochre
  styling — same data, house design. EB Garamond segment titles, Title
  Case. Bars/series in ink weights and tints; accent reserved for each
  beat's single focal element.
- Transform-don't-cut within figure beats.
- Every number shown must match the values above exactly; render †-marked
  values at the precision given and flag them in SOURCES.md as digitized
  from the report's figures. Cite once per figure, small: "Data: Anthropic,
  Coding Agents in the Social Sciences (2026)".

OUTPUTS

- youtube/claude-liam-coding-agents-social-sciences/
  - beat_sheet.json
  - claude-liam-coding-agents-social-sciences.mp4 (1920x1080)
  - SOURCES.md — every on-screen number with its source (article text vs
    digitized figure), including the 19%-vs-20% and 38%-vs-39% text/figure
    rounding notes.
- Verify the mp4 exists and plays (probe duration and frame count) before
  reporting done, and end with the beat → timestamp table.
- If a figure animation fails to render after two attempts, replace that
  beat with a slate card naming it and log the failure — never silently
  drop it.
```
