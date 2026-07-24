# Claude Code Prompt — What 81,000 People Want from AI (16:9, claude-liam)

Source: Anthropic, "What 81,000 people want from AI" (Mar 18, 2026) —
anthropic.com/features/81k-interviews (Huang, Carter, et al.)

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. All data is embedded —
these values are exact from the article's published dataset, so figures use
real numbers, not approximations. No web access needed.

```text
Build one 16:9 claude-explainer video on Anthropic's "What 81,000 people want
from AI" (March 2026) — the largest, most multilingual qualitative study ever
conducted: 80,508 people, 159 countries, 70 languages, interviewed by Claude
itself. All figures REBUILT as native animated graphics — never screenshots.
claude-liam channel. Free pipeline only: Kokoro voice, no ElevenLabs, no
higgsfield, no publishing, no git commit or push. Run without approval pauses
(no paid spend is possible under these constraints).

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
  conforms to its audio. Length derives from the beats — expect 5–7 minutes.

THE STORY (Teardown register)

Hook: last December, Anthropic pointed an AI interviewer at its own users and
asked one question — if you could wave a magic wand, what would AI do for you?
80,508 people across 159 countries answered, in 70 languages.
Act 1 — What people hope for: professional excellence tops the list, but dig
in and the real ask is living better, not working faster. Automating email
turns out to mean cooking with your mother on a Tuesday.
Act 2 — Is it delivering? 81% said AI has taken a step toward their vision.
Productivity dominates, but the most affecting stories are access: the mute
worker who built a text-to-speech bot, the butcher who became an entrepreneur.
Act 3 — What people fear: unreliability first, then jobs and autonomy. And
jobs-and-economy concern is the single strongest predictor of how someone
feels about AI overall.
Act 4 — The core finding, "light and shade": hope and fear don't divide people
into camps — they coexist inside the SAME person. Someone who values emotional
support from AI is three times more likely to also fear depending on it. The
benefits are lived; most harms are still hypothetical — except unreliability,
the one tension where the dark side is both bigger AND lived.
Act 5 — Around the world: 67% net positive globally, no country below 60% —
but wealthier regions want AI to manage life's complexity while developing
regions want it to create opportunity, and the wealthy worry more.
Landing: there are no AI optimists and pessimists. There are people organized
around what they value, holding hope and fear at once. Caveats plainly: these
are active Claude users, early adopters; the interview asked hopes first.

STRUCTURE (claude-explainer skeleton)

- Beat 0 — ClaudeComposerAsk cold open. Liam: "Anthropic asked 81,000 people
  one question: if you could wave a magic wand, what would AI do for you?"
- Middle — the five acts, carried by the rebuilt figures below. Weave in 3–4
  short verbatim quotes as full-screen typographic beats (serif, quote marks,
  attribution chip) — suggested: the 100-150 text messages healthcare worker;
  "I left work on time and picked up my daughter from daycare" (software
  engineer, Japan); "Now people are afraid that they're the horses" (US);
  "You just have to run faster and faster to stay in place" (freelancer,
  France). Quotes must be verbatim from the source.
- Second-to-last — Your Turn composer beat, suggested prompt typed in:
  "If I could wave a magic wand, what would AI do for me?"
- Last — @NikBearBrown brand card, title restated.

FIGURE 1 — THE SCALE (opening motion graphic)
  A field of dots pours onto the screen — each dot four respondents — forming
  a loose globe/world silhouette. Counters tick up: 80,508 people · 159
  countries · 70 languages. Caption: interviewed by Anthropic Interviewer, a
  version of Claude. This beat sells the scale; keep it under 20 seconds.

FIGURE 2 — WHAT PEOPLE HOPE FOR (ranked horizontal bars, exact values)
  Professional excellence 18.8 | Personal transformation 13.7 | Life
  management 13.5 | Time freedom 11.1 | Financial independence 9.7 | Societal
  transformation 9.4 | Entrepreneurship 8.7 | Learning & growth 8.4 | Creative
  expression 5.6  (1% articulated no vision)
  Animate: bars grow in rank order; then narration regroups them — roughly a
  third are "making room for life" (highlight those bars together as the
  terracotta moment), a quarter better work, a fifth becoming someone better.

FIGURE 3 — WHERE AI HAS DELIVERED (ranked horizontal bars, exact values)
  Productivity 32.0 | AI hasn't delivered 18.9 | Cognitive partnership 17.2 |
  Learning 9.9 | Technical accessibility 8.7 | Research synthesis 7.2 |
  Emotional support 6.1
  Animate: "81% said yes" lands first as a big stat; bars follow; the "AI
  hasn't delivered" bar renders in muted gray, visually distinct. End on
  emotional support — smallest bar, heaviest stories.

FIGURE 4 — WHAT PEOPLE WORRY ABOUT (ranked horizontal bars, exact values)
  Unreliability 26.7 | Jobs & economy 22.3 | Autonomy & agency 21.9 |
  Cognitive atrophy 16.3 | Governance 14.7 | Misinformation 13.6 |
  Surveillance & privacy 13.1 | Malicious use 13.0 | Meaning & creativity
  11.7 | Overrestriction 11.7 | Wellbeing & dependency 11.2 | Sycophancy
  10.8 | Existential risk 6.7  (11% no concern; avg 2.3 concerns each)
  Animate: bars cascade; then Jobs & economy pulses with the terracotta ring —
  narration: the strongest predictor of overall AI sentiment.

FIGURE 5 — LIGHT AND SHADE (the centerpiece; five paired bar charts, exact)
  Each tension: benefit bar left (split: expect-it lighter / have-seen-it
  darker), harm bar right (same split). Values (% mentioning; expect/seen):
    Time-saving 50 (13/37)        vs Illusory productivity 18 (1 expect/17 seen)
    Learning 33 (3/30)            vs Cognitive atrophy 17 (9 expect/8 seen)
    Economic empowerment 28 (9/19) vs Economic displacement 18 (14 expect/4 seen)
    Better decision-making 22 (3/19) vs Unreliability 37 (8 expect/29 seen)
    Emotional support 16 (3/13)   vs Emotional dependence 12 (7 expect/5 seen)
  Animate: pairs slide in one at a time, benefit first, harm answering it.
  Two terracotta moments: (1) decision-making — the ONE tension where the harm
  bar out-grows the benefit bar, both deeply lived; (2) a callout chip on
  emotional support: "3x more likely to also fear dependence — the same
  person."
  Narration lands the pattern: benefits are experienced, systemic harms are
  still mostly anticipated — a reflection of how early we are.

FIGURE 6 — AROUND THE WORLD (two quick beats, exact values)
  6a. Sentiment stat band: 67% net positive globally; no country below 60%.
      "No concerns" rates as small paired chips: Sub-Saharan Africa 18%,
      Central Asia 17%, South Asia 17% — versus North America 8%, Oceania 8%,
      Western Europe 9%.
  6b. Quadrant scatter: x = jobs/economy concern (avg 22%), y = negative
      sentiment toward AI (avg 33%), bubble size = respondents. Points:
      Western Europe (22.5, 35.6) | Oceania (24.3, 35.5) | North America
      (24.6, 34.5) | East Asia (21.9, 34.5) | Southern & Eastern Europe
      (22.1, 34.0) | Central Asia (15.9, 31.1) | South Asia (21.5, 30.8) |
      North Africa (18.2, 30.6) | Middle East (19.9, 29.2) | Southeast Asia
      (19.3, 28.3) | Latin America & Caribbean (18.5, 26.3) | Sub-Saharan
      Africa (18.2, 24.2)
      Animate: dashed average lines draw first; wealthy-region bubbles land
      top-right, developing-region bubbles bottom-left; the split IS the story.
  Optional 6c if pacing allows: a compact two-column slope chart, North
  America vs Sub-Saharan Africa top visions — Life management 17.7 vs 8.1,
  Entrepreneurship 8.1 vs 16.0 — the manage-complexity vs create-opportunity
  contrast in two crossing lines.

FIGURE RULES

- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. Do NOT copy Anthropic's green/blue
  figure styling — same data, house design. EB Garamond segment titles,
  Title Case. Bars/series in ink weights and tints; accent reserved for each
  beat's single focal element.
- Transform-don't-cut within figure beats.
- Every number shown must match the values above exactly. Cite once per
  figure, small: "Data: Anthropic, What 81,000 People Want from AI (2026)".

OUTPUTS

- youtube/claude-liam-81k-interviews/
  - beat_sheet.json
  - claude-liam-81k-interviews.mp4 (1920x1080)
  - SOURCES.md — every on-screen number and quote with its source line.
- Verify the mp4 exists and plays (probe duration and frame count) before
  reporting done, and end with the beat → timestamp table.
- If a figure animation fails to render after two attempts, replace that beat
  with a slate card naming it and log the failure — never silently drop it.
```
