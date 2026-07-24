# The claude-explainer series — next five

Derived from the Brutalist agentic-system taxonomy (handoff) + Bear's questions:
what is a SKILL.md · are we shaping an LLM's output · what is an LLM · scripts
(write once, call forever). The arc so far taught **practice** (on empty,
unsupervised); these teach the **theory that explains why the practice works**.
Ordering is pedagogical: each episode's thesis is the previous episode's
unexplained assumption.

Series law reminders: cold open on the composer · spark lines on every inner
beat · Onda code-block for anything code · verdict as a one-page artifact ·
title-restate outro · hello-lexicon greeting with the Wagwan mod-10 check.

---

## E5 — Claude, Taught.
**Question:** What is a SKILL.md exactly?
**Slug:** `claude-taught` · Wagwan check: charsum % 10 = **0 → "Wagwan, Bear"** (the deterministic rule fires — on the determinism episode)
**Premise:** A skill is frozen judgment. Not code, not config — a playbook whose
whole job is to move work DOWN the stack: from "influences" (taste, register,
judgment calls made once, at authoring time) toward "specifies" (laws, gates,
exact commands the runner can follow without asking).
**Cold-open command:** `/skill-creator teach claude my way of making videos`
**Thesis line:** "A SKILL.md is judgment, written down once, so it never has to be improvised again."
**Beat sketch:** ASK → what's IN one (Onda code-block: real SKILL.md frontmatter) →
influence half (register, taste, pickWhen) → specify half (laws, gates, file
contracts) → the amortization (authored once by Fable, run thousands of times) →
the failure mode (vague skills = improvising runners) → VERDICT artifact: "Anatomy
of a skill — one page" → outro.
**Spark lines:** "Judgment, frozen." · "Laws, not vibes." · "Written once." ·
"Runners don't improvise." · "Author high, run low."
**Ties back:** B05 of on-empty ("quality freezes into the file") — this is that
beat expanded to a full episode.

## E6 — Claude, Scripted.
**Question:** Scripts? Why write one instead of asking Claude to redo it?
**Slug:** `claude-scripted` · Wagwan: 9, not 0 → hello pick: **"Habari, Bear"** (Swahili)
**Premise:** The rewrite tax. Asking an LLM to re-derive the same deterministic
logic every run costs tokens every time and debugging every time — and it can
come out DIFFERENT each time. If the task is exact (measure durations, conform
frames, mux audio), write the script once and CALL it. The skill says what;
the script does exactly.
**Cold-open command:** `why does claude keep rewriting the same ffmpeg loop?`
**Thesis line:** "If two runs must agree, it's a script. If two runs may differ, it's a prompt."
**Beat sketch:** ASK → the rewrite tax (same logic, re-derived, re-debugged,
re-billed) → the axis (specifies vs influences — the series finally names it) →
the belt (runtime/scripts/*: one generate_audio.py, one compile.py, shared by
every brand) → the fork horror story (the same script existing twice = the bug
exists twice) → the law ("reuse before you write") → VERDICT artifact: "Script
or prompt? — one page" → outro.
**Spark lines:** "The rewrite tax." · "Exact means script." · "One belt." ·
"Forks breed bugs." · "Reuse before you write."
**Note:** the fork example is REAL in the repo (generate_audio.py exists twice) —
Teardown register loves an honest self-own.

## E7 — Claude, On Average.
**Question:** What is an LLM exactly?
**Slug:** `claude-on-average` · Wagwan: 4 → hello pick: **"Annyeong, Bear"** (Korean)
**Premise:** An LLM is a distribution over outputs, not a database of answers.
Every response is a draw. Same prompt, different draw — that's not a bug, it's
the definition. This is WHY everything else in the series exists: scripts pin
the exact, skills bias the draw, gates catch the bad draws.
**Cold-open command:** `why did I get a different answer this time?`
**Thesis line:** "You're not querying a database. You're sampling a distribution."
**Beat sketch:** ASK → not-a-database (same question, three answers, all
plausible) → what it actually does (next-token prediction, plainly — no math
wall; one Manim fragment allowed for the distribution picture) → why temp-0
isn't a hex code (frozen ≠ specified — a persona steers, it doesn't name) →
what this buys you (creativity IS the variance) → what it costs you (never
certify one draw as "the" answer) → VERDICT artifact: "The distribution rules —
one page" → outro.
**Caution:** keep claims mechanistic and verifiable; no benchmark talk, no
"understanding" debates. This is the episode most likely to attract pedants —
the pedagogy audit should fact-check hardest here.

## E8 — Claude, Steered.
**Question:** Are we shaping the output of an LLM?
**Slug:** `claude-steered` · Wagwan: 5 → hello pick: **"Bula, Bear"** (Fijian)
**Premise:** Yes — and the shaping stacks. Three layers of conditioning text,
each biasing the distribution a different way: method persona = WHAT
(script-writer, explainer), voice register = HOW IT SOUNDS (teardown, wonder),
brand = WHOSE VOICE (nbb, hai, medhavy). One writer, many costumes — a register
is a parameter, not a person.
**Cold-open command:** `same facts — make it sound like Medhavy this time`
**Thesis line:** "You can't name the output. You can load the dice."
**Beat sketch:** ASK → the stack (what × how × whose — show the same beat
narrated in two registers, side by side) → why stacking works (each layer
narrows the distribution) → the limit (steering never becomes specifying — the
callback to E7) → the practical payoff (one pipeline, four channels — the
claude brand itself as evidence) → VERDICT artifact: "The conditioning stack —
one page" → outro.
**Ties back:** the channels table in CLAUDE-BRAND.md is this episode's living demo.

## E9 — Claude, Judged. (season finale)
**Question:** the one nobody asked but everything implies — who checks what?
**Slug:** `claude-judged` · Wagwan: 4 → hello pick: **"Vanakkam, Bear"** (Tamil)
**Premise:** The thesis of the whole system. Agents verify the DETERMINABLE
(schema valid, durations match, beats filled). Humans judge the JUDGEABLE
(interesting, funny, worth watching) — and that never delegates. Gates are a
cheap taste-check on the plan before the expensive taste-check on the video.
The determinism boundary IS the human-judgment boundary.
**Cold-open command:** `can you tell me if this video is good?`
**Thesis line:** "Maximally informed, minimally autonomous."
**Beat sketch:** ASK (and the honest answer: no — Claude can check everything
about the video except whether it's worth watching) → determinable vs judgeable →
gates as cheap taste-checks (GATE P shown literally — the PEDAGOGY.md that
blocked the audio spend in this very series) → what agents check (QC stills,
ffprobe, schema) → what never delegates → the season recap (empty routed the
models, unsupervised scoped the risk, taught froze the judgment, scripted
pinned the exact, on-average explained the draw, steered loaded the dice —
judged says who signs) → VERDICT artifact: "Who checks what — one page" →
title-restate outro.
**Why last:** it recaps every prior episode as evidence for one slogan.

---

## Sequencing rationale

taught → scripted → on-average → steered → judged runs DOWN the input stack and
then names the rule that governs it. Practical first (skills and scripts extend
what the audience just watched you do), theory second (the LLM episodes explain
why the practice works), thesis last. Alternative order (on-average first) is
more logical but colder — the audience earns the theory by feeling the practice.

## Also in the drawer (not this run)

- **"Claude, still oversimplified."** — the v2 poster promised on-screen in E1's
  verdict beat; six missing truths as its own reel. Cheap to make (assets exist).
- The pending **nbb vox-explainer** of the full taxonomy ("What is inside the
  Brutalist agentic system exactly?") — same material, different brand and
  depth; the claude-explainer episodes are the short-form cuts of it.
- The four repo gaps (fat orchestrators, forked belt, folklore reuse law,
  persona-swap ≠ sub-agent) are E6's B-roll — auditing REFACTOR-BRIEF.md against
  them would hand E6 its receipts.
