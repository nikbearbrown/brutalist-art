# SERIES ROADMAP — "What Is Gru?" (a helper series)

A companion ai-explainer series that teaches students the **Gru** tool — the software-design-
documentation consultant behind the Boondoggle assignments in **INFO 7375 (Computational
Skepticism for AI)**. Audience: **students who have to use Gru (for the Boondoggle Report and
beyond) and have never seen a phase-gated SDD tool or a Boondoggle Score.** Register: **pragmatic
how-to with a skeptical edge** (Liam voice, `claude-liam`, Kokoro am_onyx). Six episodes. This is a
*helper* series — explain the tool, then **use Gru to demo Gru** on screen (the signature move).

> Voice: `claude-liam` per request. Build into `computational-skepticism-for-ai/youtube/`, or
> `brutalist-art/youtube/` — tell me the owning book slug. Pairs with the Boondoggle Report (Week 1)
> and the Reallocation Engine assignment roadmaps.

## The one idea Gru exists to teach

**Programming as conducting.** You are Gru; Claude is the minions. The minions are excellent and
enthusiastic — they execute exactly what they understood you to mean. **The gap between what you
meant and what they understood is where all the damage lives.** Gru's job is not to help you type
less; it's to help you **decide more precisely** — which task is Claude's, which is yours, in what
order, with what handoff condition. Under it all is the **solve-verify asymmetry**: Claude solves
faster than any human and that won't change; what won't change either is that Claude can't verify
its own output against domain reality, can't reframe a bad problem, can't supply accountability.

## Meta-resonance (the session's throughline, made a tool)

Gru is the **delegation map + hard-stop + human-owns-the-truth** discipline formalized. The
Boondoggle Score's Claude/human split with named handoff conditions is the delegation map; the
five supervisory-capacity labels are the human-judgment gates; and Gru's `/recipe` TODO taxonomy
(DATA SOURCE / DEFINE / DEV / APPROVE / REPORT FIELD) is **the same taxonomy** as the recipe
framework in the branding course's A5B. One line on that in E1 ties the whole curriculum together.

## Honesty / craft threads (the tool's own philosophy) — DOUBLE-CHECK LAW

- **A sophisticated document built on an unformulated problem is worse than no document.** It looks
  like rigor. It teaches that rigor is a format, not a practice. Gru holds the line at `/v0` for
  exactly this reason.
- **The pushback protects your thinking, not the document's quality.** Don't route around it.
- **Silent mode is for when you already know**, not for skipping the thinking.
- **Every Claude prompt is a complete specification, not a delegation.** "Follow the SDD" fails —
  Claude has no memory between prompts; the constraints must be pasted in.
- **Boondoggling is deciding more precisely, not typing less.**

## Series doctrine (every episode)

- **Assume no exposure to Gru or SDDs.** Define every term first time (SDD, boondoggle, phase gate,
  supervisory capacity, handoff condition, minion brief, silent mode, solve-verify asymmetry). Never "just."
- **Show it running.** Every episode ends by demoing the actual commands on a small example app —
  Gru demoing Gru. The Onda code-block / composer shows the real command and Gru's real pushback.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your Turn
  → title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "What Is Gru? Programming as Conducting" (~6 min)
- **slug:** `claude-liam-gru-01-what-is-gru`
- **premise:** Gru is a senior software architect that does one thing no other tool does — it tells
  you which parts of a build belong to Claude and which belong only to you, and produces a score
  that separates them.
- **teach:** the conductor metaphor (Gru designs the mission, assigns the minions, checks the work,
  decides what the mission IS, takes responsibility — the meant-vs-understood gap is where the
  damage lives); the **solve-verify asymmetry** (Claude solves fast; can't verify domain-grounded,
  can't reframe a bad problem, can't supply accountability); why it exists (the Irreducibly Human
  curriculum, Tier 4); the two modes (interactive default with pushback + phase gates; `/silent`);
  demo: type `/help`, read the Welcome Menu, meet the command families.
- **traps:** expecting a code generator; treating Gru as autocomplete; skipping straight to output.
- **deliverable:** understanding + a running Gru session. Your Turn = "set up Gru (Claude Project or
  paste the system prompt), type `/help`, and read the menu before you touch a command."

### E2 — "The Five Supervisory Capacities: What Only You Can Do" (~5 min)
- **slug:** `claude-liam-gru-02-five-capacities`
- **premise:** Gru labels every human step in the score with one of five capacities — the
  irreducibly human parts of a build. Learn them and you can read any Boondoggle Score.
- **teach:** **[PA] Plausibility Auditing** (hearing the wrong note before verification); **[PF]
  Problem Formulation** (deciding what the mission is before Claude sees it); **[TO] Tool
  Orchestration** (which Claude task, what order, what trust); **[IJ] Interpretive Judgment**
  (supplying meaning and accountability Claude can't); **[EI] Executive Integration** (holding all
  four toward one goal). These are where you supervise, not delegate.
- **traps:** treating the labels as jargon; assuming Claude can do any of the five.
- **deliverable:** fluency in the five labels. Your Turn = "for a build you know, name one moment
  that needed each of the five capacities — the ones you can't name are your blind spots."

### E3 — "Start Here: The /v0 Problem-Formulation Gate" (~6 min)
- **slug:** `claude-liam-gru-03-v0-gate`
- **premise:** Gru won't write a word of your SDD until you can name the thing you're building in one
  sentence. If `/v0` stops you cold, that's the tool working.
- **teach:** why the gate exists (most weak input is a *problem-formulation* gap, not laziness — you
  haven't separated the problem from the thing from the ecosystem); the **three questions** (the
  ecosystem in two sentences; the existing components it touches; **in one sentence, what are you
  ADDING** — the thing, not the problem); the format **"[THING] is a [WHAT] inserted [WHERE] that
  produces [OUTPUT]"**; weak vs. strong ("improve signal reliability" = a goal, not a thing →
  "the Coherence Layer is a stateless audit component inserted between … that produces …"). Demo
  `/v0` live, including Gru holding the line.
- **traps:** describing the problem instead of the thing; accepting a sentence that could describe
  ten systems; routing around the gate.
- **deliverable:** a passed `/v0` sentence. Your Turn = "run `/v0`; if you can't name the thing,
  don't fill in more context — separate the thing from the problem it solves."

### E4 — "Build the SDD: The Command Library + Phase Gates" (~7 min)
- **slug:** `claude-liam-gru-04-command-library`
- **premise:** Gru builds the SDD in a fixed, gated sequence — and pushes back at every step. The
  gates aren't friction; they're where the thinking happens.
- **teach:** the families — **Problem & Vision** (`/v1` intake → `/v2` principles → `/v3` flows →
  `/v4` needs), **Systems** (`/s1`–`/s4`), **Domain & API** (`/d1`–`/d3`), **Scope & Production**
  (`/p1`–`/p5`), **compile** (`/g1`) and audits (`/g2` the 7 failure modes, `/g4` the new-engineer
  test); the **phase gates** between them (Gru won't proceed until you confirm); **interactive vs
  `/silent`** (silent = clean output when you already know; default = pushback + gates); the
  **pushback layer** (constructive skeptic — flags weak input, names assumptions, disagrees when a
  decision contradicts a principle). Demo `/v1`→`/s1` on the small app, including one real pushback.
- **traps:** silent-moding to skip the thinking; overriding a principle collision; a component that
  maps to no Need.
- **deliverable:** an SDD `/v1`→`/s1`. Your Turn = "run the sequence in interactive mode; when Gru
  pushes back, resolve it — don't `/silent` your way past the gate."

### E5 — "The Boondoggle Score (/claude): Who Builds What, and the Handoff" (~7 min)
- **slug:** `claude-liam-gru-05-boondoggle-score`
- **premise:** The payoff command. `/claude` turns your SDD into a conductor's score — every step
  labeled Claude or human, in dependency order, with an explicit handoff condition between each.
- **teach:** the two parts (the **MINION part** = complete copy-pasteable Claude prompts; the **GRU
  part** = human tasks each labeled with a supervisory capacity + a precise action); every Claude
  step carries **CONTEXT REQUIRED → PROMPT → EXPECTED OUTPUT → HANDOFF CONDITION → DEPENDENCY**; the
  **prompt-writing principle** — every prompt is a *complete specification*, not "help me with X"
  ("follow the SDD" fails; Claude has no memory, paste the constraints in); the **score summary**
  (critical path, highest-risk handoffs, the supervisory-capacity distribution — and Gru *flags* any
  capacity that appears zero times as "a boondoggle that assumes Claude is always right"); it's
  available at **any** stage. Demo `/claude`, then the **Minion Brief**.
- **traps:** a vague prompt ("write the User model"); a handoff condition that says "looks good"
  instead of a testable check; no plausibility-auditing steps.
- **deliverable:** a Boondoggle Score. Your Turn = "run `/claude`; find the one Claude step whose
  handoff condition you couldn't test — that's the step most likely to ship a silent failure."

### E6 — "Bonus: The Recipe Pipeline (/recipe · /snickerdoodle)" (~6 min) — for pipeline builds
- **slug:** `claude-liam-gru-06-recipe-pipeline`
- **premise:** For students building runnable pipelines, `/recipe` generates a Claude Code agent that
  hardens your recipes to a standard until they're RUNNABLE — then you bring them back for a score.
- **teach:** what `/recipe` produces (a customized **Claude Code agent prompt**, not an interactive
  audit); the **four intake questions** (pipeline name + one-sentence purpose for a domain expert;
  origin — n8n / spec-first / unknown; which governing files exist; known gaps); the **five TODO
  types** (DATA SOURCE / DEFINE / DEV / APPROVE / REPORT FIELD — *the same taxonomy as the recipe
  framework*); the **graduation ladder** (DRAFT → RUNNABLE IN SAMPLE MODE → RUNNABLE LIVE); the flow
  (Gru → agent prompt → Claude Code audits recipes one at a time → you close the TODOs → back to Gru
  for `/claude`). Gru won't score a recipe with open TODOs — close them first.
- **traps:** asking for a Boondoggle Score before the recipe is RUNNABLE; a purpose written for a
  developer instead of a domain expert; a report step missing one of its three required elements.
- **deliverable:** a generated agent prompt (for pipeline students). Your Turn = "run `/recipe` with
  your one-sentence purpose; if you can't write that sentence for a domain expert, that's a
  problem-formulation gap, not a tooling gap."

---

## Tight cut

Four-episode version: What is Gru + the five capacities (E1+E2) · `/v0` gate (E3) · Command library +
Boondoggle Score (E4+E5) · `/recipe` bonus (E6, optional). The 6-episode cut is better because the
five capacities and the `/v0` gate are the two conceptual keys students most often skip.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `computational-skepticism-for-ai/
  youtube/` (or `brutalist-art/youtube/` — tell me the owning book slug). Signature move: **use Gru
  to demo Gru** — run the real commands on a small example app and show the real pushback.
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals → QC →
  BUILD-PROMPT.md. Ground the demos on the Gru system prompt provided; re-verify the command set
  against the current course materials at build time.
- Course fit: this helper series is the on-ramp for the **Boondoggle Report** (Week 1) and feeds the
  **Reallocation Engine** and **Botspeak Prompt Adaptation** assignments. Together with those three,
  the Computational-Skepticism course now has a coherent starter set — say the word and I'll map the
  remaining weekly validation exercises + the research-project milestones into one course index.
