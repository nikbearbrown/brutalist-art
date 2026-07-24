# Claude Code Prompt — Anthropic Economic Index: Cadences (16:9, claude-liam)

Source: Anthropic, "Anthropic Economic Index report: Cadences" (Jun 26, 2026) —
anthropic.com/research/economic-index-june-2026-report (Massenkoff, Lyubich,
Sacher, Hitzig, Zhang, Heller, McCrory)

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. All data is embedded —
values marked (†) were digitized from the report's published figures and are
correct to the precision shown; everything else is verbatim from the article
text. No web access needed.

```text
Build one 16:9 claude-explainer video on Anthropic's Economic Index report
"Cadences" (June 2026) — the report where Anthropic's usage logs got a
heartbeat (hourly telemetry), Claude's outputs got names (artifacts), and
9,700 users got asked how AI actually feels at work (the Economic Index
Survey). All figures REBUILT as native animated graphics — never screenshots.
claude-liam channel. Free pipeline only: Kokoro voice, no ElevenLabs, no
higgsfield, no publishing, no git commit or push. Run without approval pauses
(no paid spend is possible under these constraints).

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
  conforms to its audio. Length derives from the beats — expect 6–8 minutes.
- Suggested title: "Claude on the Clock" (series style: Claude on Average,
  Claude Unsupervised). Restate the full report name in the description.

THE STORY (Teardown register)

Hook: your city has a heartbeat, and it shows up in an AI's logs. News at
7 a.m. Recipes at 6 p.m. Sleep advice at 5 a.m. Taxes on April 14. Anthropic
started sampling Claude usage hourly — and the economy's daily rhythm is
etched right into it.
Act 1 — Cadences: Claude usage mirrors the workweek. Personal conversations
jump from ~35% on weekdays to just under 50% on weekends. Weekend Claude Code
drops backend architecture and API debugging, picks up AI agent design, quant
trading, and gaming — and business-founding conversations peak Saturday and
Sunday while job applications drop. Night-and-weekend work skews toward
higher-wage occupations. And on April 14, tax conversations run eight times
the average day.
Act 2 — Artifacts: 93% of conversations produce a concrete output. Anthropic
now names them: explanations, documents, guidance, apps, queries. The economics
hide here: compute tracks the value of work. Marketing-manager tasks ($80/hr)
burn ~2.5x the tokens of editor tasks ($37/hr). Building an app costs 3x the
median conversation; an explanation costs a fifth. And in the highest-wage
tasks, MORE output from Claude comes with MORE turns from the human — the
pattern looks augmenting, not displacing.
Act 3 — Autonomy: same task, different leash. The same blog post takes a
median 13 rounds of back-and-forth in chat — and a single prompt in Claude
Code. Across 26 of 31 output types, Claude Code runs with more autonomy
(+0.37 points on a 1–5 scale overall). It's not the model — among
Sonnet-only conversations the gap persists (+0.26). The product, not the
model, sets the leash length.
Act 4 — Perceptions: the survey. ~9,700 respondents linked (privacy-preserving)
to their real usage. Close to 6 in 10 expect AI to do a bigger share of their
work within 12 months; over a third expect it to handle most or nearly all.
The kicker: expected progress is a rising tide — a software engineer and a
construction manager anticipate the SAME increment of progress next year,
regardless of how exposed their occupation already is.
Act 5 — The paradox: the people who delegate the most are the most
optimistic. Higher automation share predicts more positive expectations on
ALL six dimensions of job quality — pay, security, finding a job, meaning,
autonomy, human interaction. And heavy delegators report learning at the same
rate as everyone else, while feeling their skills grow MORE valuable. The
worry lands elsewhere: only 10% rate their own job loss as likely — but over
a third put a junior colleague's odds above 60%. It'll happen to the juniors,
not to me.
Landing: people aren't asking to be replaced or spared. Over half hope for
collaboration on meaningful work; over half hope AI eats the drudgery; a
third hope the gains are shared. Caveats plainly: survey respondents are
Claude users, not the general population — 30% computer & math (4% of US
employment), 23% management, only 12% women; self-reports can't rule out
skill erosion; automation-optimism could be selection, though it survives
controlling for user tenure.

STRUCTURE (claude-explainer skeleton + your-turn closing)

- Beat 0 — ClaudeComposerAsk cold open. Liam: "What time is it in your city?
  Claude's logs already know. Anthropic just published the economy's daily
  heartbeat — and asked 9,700 people how AI feels at work."
- Middle — the five acts, carried by the rebuilt figures below.
- Closing per your-turn: VERDICT recap card → Your Turn composer beat →
  title re-read on the @NikBearBrown brand card.
- Your Turn suggested prompt (Liam reads it in full): "What share of my work
  tasks could you do entirely on your own today — and which ones should I
  never hand over? Interview me, then give me your honest split."

FIGURE 1 — THE CLOCK (opening motion graphic; exact values)
  A 24-hour dial (or flowing hourly ribbon) on cream; request clusters light
  up around it as the day turns:
    News ~7 a.m. | Business correspondence peaks 10–11 a.m. | Recipes 6 p.m.
    at 2.3x their daily average | Media recommendations in the evening |
    Sleep advice ~5 a.m., the hours just before dawn.
  Terracotta moment: the 6 p.m. recipe spike (2.3x — the single biggest).
  Then the weekly view: personal share of conversations, ~35% weekdays →
  just under 50% weekends (weekend bands shaded). Callout chips: weekends'
  biggest Claude Code fallers (backend architecture, API debugging, data
  storage) vs risers (AI agent design, quant trading, gaming); business-
  starting peaks Sat–Sun. Keep the whole beat under 35 seconds.

FIGURE 2 — TAX DAY (quick stat beat; exact values)
  A time-series line of US tax-related conversation share: flat, then a
  cliff-face spike — April 14 at 8x the average May day, April 15 about as
  high, sharp drop April 16. Rest-of-world line stays flat underneath.
  One terracotta vertical rule on April 15, labeled "US filing deadline."

FIGURE 3 — WHAT CLAUDE MAKES (ranked bars + regrouping; exact values)
  93% of Claude conversations produce an artifact. Top artifacts:
    Explanations 17 | Documents & reports 15 | Guidance 11
  Then regroup the bar field: conversational outputs ~1/3, written
  deliverables ~1/3, code & technical work ~1/6.
  Second movement — "what it's FOR" splits (chips or paired mini-bars):
    Mostly personal: creative writing, guidance, recipes (>80% personal)
    Mostly work: database queries 82 | blogs & articles 81 | marketing 80
    Split down the middle: plans (44 work / 49 personal), translation
    (42 work / 44 personal)
  Optional chip: work conversations' top outputs — documents 20, explanations
  9, email drafts 7, analyses & summaries 6; personal — explanations 25,
  recommendations 22.

FIGURE 4 — COMPUTE TRACKS VALUE (the economics centerpiece; exact values)
  4a. Wage-vs-tokens scatter (both log scale): the positive slope IS the
  story. Named points: Marketing managers $80/hr vs Editors $37/hr —
  ~2.5x the tokens. Terracotta outlier ring: Pharmacists $68/hr vs
  Statistical assistants $24/hr — 1/20th the tokens. Caption: 44% of the
  wage gradient is explained by output mix.
  4b. Artifact token ranges (log box plot or ranked bars, normalized to
  median = 1): apps >3x the median conversation; explanations ~1/5.
  4c. The tercile table as an animated stat band (top- vs bottom-wage
  tercile): 2.07x tokens | 1.34x Claude output per turn | 1.53x as many
  user turns | extended thinking 34% vs 31%.
  Terracotta moment on 1.53x turns — narration: more from Claude does NOT
  mean less from the human; that's augmentation's signature.

FIGURE 5 — THE LEASH (autonomy split bars; exact values)
  Paired bars per output type, chat/Cowork vs Claude Code, on the 1–5
  autonomy scale — Code higher in 26 of 31 types; overall gap +0.37;
  scripts & code snippets +0.53. Center-stage comparison, big type:
    Blog post in chat: median 13 rounds of back-and-forth.
    Blog post in Claude Code: 1 prompt.
  Counter-argument beat (Teardown move): "It's just Opus, right?" — 54% of
  Code sessions run Opus vs 10% of chat. Then kill it: Sonnet-only gap still
  +0.26. Chip: autonomy and token use rise together, r = 0.68.
  Optional quick chip from the reading-level result: Claude answers ~1 year
  of education above the prompt; widest where users describe a thing to
  build — images +2.6, games +1.9, apps +1.7; near zero for blogs (−0.1),
  academic papers (0.0), email (+0.3).

FIGURE 6 — THE RISING TIDE (rebuilt from report Fig 3.3; exact values)
  Two scatter panels: occupation-mean stated task share (y) vs observed
  exposure (left) and Eloundou et al. (2023) theoretical exposure (right).
  Grey dots: share reported doable today. Orange dots: expected in 12
  months. Dashed 45° reference line. Animate: grey field lands with its
  shallow best-fit line; orange field lands ABOVE it; the two best-fit
  lines draw in — essentially PARALLEL. Terracotta moment: the gap between
  the lines, held constant across the x-axis. Narration: everyone expects
  the same increment of progress — a rising tide. Stat band before or
  after: ~6 in 10 chose a higher band for next year; over a third expect
  AI to do most or nearly all of their tasks in 12 months. Side chips:
  reported exposure runs ~10pp lower in high-income countries, and ~10pp
  lower for 15+ years of experience vs first-year workers — but expected
  PROGRESS is flat across both.

FIGURE 7 — WHOSE JOB CHANGES (rebuilt from report Fig 3.5; † digitized)
  Two stacked-bar panels — Responsibilities change | Job loss — for Self,
  Peer, Junior, Senior; stacks: Very Likely (>80%) solid terracotta, Likely
  (60–80%) tint.
    Responsibilities change totals†: Self 46 (20 VL) | Peer 39 (13 VL) |
    Junior 55 (31 VL) | Senior 39 (19 VL)
    Job loss totals†: Self 9 (4 VL) | Peer 17 (7 VL) | Junior 40 (18 VL) |
    Senior 20 (9 VL)
  Animate: responsibilities panel first (everyone expects change), then job
  loss (the floor drops) — and the Junior bars pulse. Narration beats: 10%
  rate their own job loss likely — slightly BELOW the ~13.4% annualized US
  separation rate; of those who do, 38% name AI; over a third put a junior
  colleague's odds above 60%. The oldest bias in forecasting: it'll happen
  to someone else — specifically, someone junior.

FIGURE 8 — THE DELEGATION PARADOX (rebuilt from report Figs 3.6 + 3.7)
  8a († digitized). Six bars with CI whiskers — change in share positive
  per +1 SD (22pp) of automation share: Economic (terracotta): Pay +4.7
  (mean 56%) | Security +4.0 (42%) | Finding a job +4.5 (52%). Intrinsic
  (ink tint): Meaning +3.5 (59%) | Autonomy +2.9 (70%) | Human interaction
  +3.8 (36%). All six positive — the people who hand over the most expect
  the best outcomes.
  8b. Two trend lines vs automation share: "AI increases the market value
  of my skills" (57% overall) RISES; "I learn more with AI" (68% overall)
  stays FLAT. Narration: the feared trade — delegate more, learn less —
  does not show up in self-reports; caveat plainly that self-reports can't
  rule out skill erosion. Stat chips: productivity gains reported in speed
  86%, scope 82%, quality 69%; cost savings 27%.
  Honest-selection beat: could be the enthusiasts self-selecting — but the
  estimates barely move controlling for user tenure.

FIGURE 9 — WHO USES IT DIFFERENTLY (rebuilt from report Fig 3.8; exact)
  Four bars, women − men, in outcome SDs, occupation-controlled, CI
  whiskers: Work-use share −0.09 | Claude Code share −0.24 (6.3pp) |
  Automation share −0.33 (7.3pp) | Total active minutes +0.24.
  The one positive bar is the terracotta moment: women (12% of the linked
  sample) delegate less and code less — but log MORE active time,
  a signature of more iterative, collaborative use.

FIGURE 10 — DREAM BIG (closing; exact values)
  The survey's last question: "what do you hope an economy shaped by AI
  looks like in ten years?" Three theme bands rise like a skyline:
    Augmentation — collaborate with AI on meaningful work: >50%
    Automation — AI takes the drudgery, more free time: just over 50%
    Shared prosperity — gains widely shared: ~1/3
  Narration lands the report's own arc: not replacement, not rescue —
  collaboration, relief, and a fair split. Keep it under 25 seconds; it
  hands off to the verdict card.

FIGURE RULES

- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. Do NOT copy Anthropic's cream/orange
  report styling wholesale — same data, house design. EB Garamond segment
  titles, Title Case. Bars/series in ink weights and tints; accent reserved
  for each beat's single focal element.
- Transform-don't-cut within figure beats.
- Every number shown must match the values above exactly; render †-marked
  values without decimals beyond the precision given. Cite once per figure,
  small: "Data: Anthropic Economic Index, Cadences (June 2026)".

OUTPUTS

- youtube/claude-liam-economic-index-cadences/
  - beat_sheet.json
  - claude-liam-economic-index-cadences.mp4 (1920x1080)
  - SOURCES.md — every on-screen number with its source line; flag the
    †-digitized values as read from report Figures 3.5/3.6/3.8.
- Verify the mp4 exists and plays (probe duration and frame count) before
  reporting done, and end with the beat → timestamp table.
- If a figure animation fails to render after two attempts, replace that
  beat with a slate card naming it and log the failure — never silently
  drop it.
```
