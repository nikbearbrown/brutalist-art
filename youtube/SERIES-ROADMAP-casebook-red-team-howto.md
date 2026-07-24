# SERIES ROADMAP — "Doubt It When It Looks Right: The Agentic Casebook"

A how-to ai-explainer series for **INFO 7375 (Computational Skepticism for AI) — The Agentic Casebook:
Red-Team One System** (a 100-point AUDIT: one real agentic system + a casebook of 5–11 failure cases +
an accountability attestation + a go/no-go memo). Audience: **graduate students who can use AI tools
fluently and have never red-teamed one — never written a prediction-lock, never checked the *world*
instead of the system's own success message.** Register: **pragmatic how-to with a skeptical edge**
(Liam voice, `claude-liam`, Kokoro am_onyx). Six episodes. The series walks a student from "I trust the
output because it looks finished" to "a casebook that names where a running system breaks, and who owns
the break." The one sentence the whole assignment turns on: **the artifact is not the world.**

> Voice: `claude-liam` per request. Owning book: **computational-skepticism-for-ai**. Build into
> `computational-skepticism-for-ai/youtube/`, or `brutalist-art/youtube/` — this roadmap ships into
> `brutalist-art/youtube/` with its siblings. This is the AUDIT twin of *Build It, Then Break It* (the
> BUILD assignment); together they teach one skill facing two directions.

## The idea this assignment teaches (say it in E1 and again in E6)

**Skepticism is easy when something looks suspicious; the skill is doing it when the output looks right.**
The same fluency that produced the answer is the least reliable judge of whether the answer is true,
because it will defend itself. So you check anyway — deliberately, mechanically, at the exact moment the
output looks most trustworthy. An agentic system makes this literal: it *reports* success and *means* it,
while the world it claims to have changed sits untouched. The casebook is proof you checked the world.

## The spine (repeat every episode)

- **Prediction-lock before you look.** Write and date what you expect *before* you observe. That is the
  line between skepticism and hindsight; an ungrounded "I knew it would do that" earns nothing.
- **Check the world, not the artifact.** Every "actual outcome" is a check against reality — the server
  state, the sent folder, the real record — never the system's own success message.
- **Name who owns the break.** A responsibility that is everyone's is no one's. Every case ends by naming
  the party answerable for that failure and the supervisory capacity that lapsed.

## Honesty / craft threads (DOUBLE-CHECK LAW)

- **The honesty floor is a zero, not a deduction.** A fabricated case, a screenshot that doesn't show what
  you claim, or an "actual outcome" you asserted without checking the world is *the exact failure this
  course exists to catch* — so it zeroes that case, it doesn't just cost points.
- **A wrong prediction, honestly logged, beats a vague right one.** The grade rewards the dated
  prediction-vs-result gap, not the number of failures found.
- **"An empty result set is the new 'it works.'"** The attestation's "what I did NOT test" list is where
  the real failure is hiding — the unchecked path is the one that bites.
- **Use the instrument as the chapter defines it, not the name.** Fifteen points a lens go to *running*
  Bayes / the probe suite / the delegation map on your own system — not to name-dropping it.
- **You are auditing, not redesigning.** "The agent is given. Do not propose a redesign." Find the break
  and its owner; a validation-scope fix is welcome, a rebuild is out of scope.
- **Undefended gaps are where the patients die.** The whole reason to list what you couldn't test.

## Series doctrine (every episode)

- **Assume tool fluency, not audit skill.** Define every term first time (agentic, Pebble, tool surface,
  blast radius, prediction-lock, the four moves, supervisory capacity, artifact vs. world, attestation,
  calibrated verb, fundamental vs. contingent). Never "just."
- **One deliverable per episode**, ending in the real artifact, with a paste-ready prompt to draft the
  first pass — then the "did you check the world / is your prediction on the record first?" pass.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your Turn →
  title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "Pick Your Pebble + Lock the Prediction" (~6 min)
- **slug:** `claude-liam-cb-01-pebble-and-predict`
- **premise:** The audit is only as good as the system you point it at and the discipline of writing down
  what you expect before you look. Choose a system that can actually *do* something, then commit your
  prediction to the record.
- **teach:** what makes a system a **Pebble** — **agentic** (acts through tools: sends mail, edits files,
  moves money, files tickets), **accessible** (runnable or well-documented), **meaningful blast radius**
  (a wrong action deletes / discloses / buys / denies), **safe & ethical to poke** (sandboxed, your own,
  or a documented public case — don't attack what you're not authorized to test), **right-sized** (5–11
  distinct failure cases); write the **System Dossier** (name, architecture in two sentences, **tool
  surface** = the actions it can actually take, deployment context, a suspected failure mode, access
  constraints); then the **prediction-lock** — write and date what you expect *before* each probe, because
  a surprise only counts if the prediction was on the record first.
- **traps:** picking a chatbot that only talks (no tool surface = no blast radius); a Pebble too big to
  study or too safe to fail; writing the prediction after you looked.
- **deliverable:** the System Dossier + a dated first prediction. Your Turn = "name your Pebble's tool
  surface in one line — every action it can take — then write, dated, what you expect the first probe to
  do before you run it."

### E2 — "The Four Classical Moves: Your Portable Doubt" (~6 min)
- **slug:** `claude-liam-cb-02-four-moves`
- **premise:** Four old moves turn a vague unease into a checklist. The assignment requires all four,
  labeled — this episode makes each one a procedure you can run, not a name you can drop.
- **teach:** **Descartes / radical doubt** — take a confident claim ("email deleted") and enumerate *what
  would have to be true for this to be wrong about the world* (Knight Capital: "deployment succeeded" ≠
  "the system is doing what we intend"); **Hume / the limit of induction** — is this confidence about the
  world, or only about the record so far, and what would tell you the distribution shifted? (Zillow, Google
  Flu Trends, the turkey); **Popper / falsifiability** — state, *in advance and in measurable terms*, what
  would count as failure, then go looking for exactly that (the Epic Sepsis Model was never validated, only
  *unrefuted*); **Plato's Cave / artifact vs. world** — name the artifact, name the world, interrogate the
  relationship (the COVID X-ray model read dataset markers, not lungs). Label each move where you use it.
- **traps:** using a move as decoration; confirmation-hunting instead of Popperian failure-hunting;
  grading the shadow (the report) as if it were the wall (the world).
- **deliverable:** the four moves, each run once on your Pebble. Your Turn = "take your Pebble's proudest
  success message and run Descartes on it: list every way that sentence could be true on the screen and
  false in the world."

### E3 — "Choose Three Lenses + the Universal Lens Loop" (~7 min)
- **slug:** `claude-liam-cb-03-choose-and-run-a-lens`
- **premise:** Ten instruments on the menu; you run three. They look different but share one loop — and
  this episode runs that loop end-to-end on the most agent-native lens so the pattern transfers to whichever
  three you pick.
- **teach:** the **menu** (Ch 2 base-rate/Bayes · Ch 3 epistemic-frame · Ch 4 robustness probe suite ·
  Ch 5 explainability self-audit · Ch 6 bias leverage · Ch 7 fairness impossibility · Ch 8 agentic
  false-success · Ch 9 delegation map · Ch 10 deceptive-viz catalog · Ch 11 verb audit) and how to
  **choose for your Pebble** (a system that *acts* → Ch 8/9; one that *scores people* → Ch 6/7; one that
  *explains itself* → Ch 5; one that *shows numbers* → Ch 2/10/11); then the **universal loop** every lens
  runs — *prediction-lock → apply the instrument as the chapter defines it → produce one case → name the
  supervisory capacity that failed.* **Live demo: Ch 8 agentic false-success** — give the agent a task, it
  reports done, you check world state and it isn't, you write the **stop/gating condition** ("you broke my
  toy" test). One lens, fully worked, so the loop is muscle memory before students pick their own.
- **traps:** choosing three lenses that don't fit your Pebble; name-dropping an instrument instead of
  running it; skipping the world-state check that defines the false-success case.
- **deliverable:** three chosen lenses + one fully-run case. Your Turn = "pick the three lenses that fit
  *your* Pebble's job — acts / scores / explains / shows — and run the first one through the loop:
  predict, apply, case, name the capacity."

### E4 — "Two More Worked Lenses + Write the Case" (~7 min)
- **slug:** `claude-liam-cb-04-more-lenses-and-the-case`
- **premise:** The cases are 45 of the 100 points, so this episode runs two more lenses from different
  families and nails the case template — the artifact-vs-world line and the capacity that failed are what
  earn the marks.
- **teach:** a **quant/behavioral lens demo** — Ch 2 (find the confidence number, find the real **base
  rate**, run **Bayes** on one flag, state the **Popperian falsification condition**) *or* Ch 5 (request vs.
  the agent's self-explanation vs. its actual tool calls vs. ground truth over 5–10 tasks, classifying each
  mismatch **technically-wrong / technically-accurate-but-practically-misleading / properly-calibrated**);
  a **values lens demo** — Ch 6 (draw the causal graph, walk the ten bias mechanisms, run the **leverage
  analysis**, name the owner of the node) *or* Ch 7 (two conflicting fairness definitions, show the
  **impossibility** on the system's own numbers, write a defended choice); then the **case template** —
  `Case ID / lens / input / prediction-lock (dated) / action taken / reported outcome (artifact) / actual
  outcome (world) / which supervisory capacity failed / evidence / severity` — and the **five supervisory
  capacities**: **[PA]** Plausibility Auditing, **[PF]** Problem Formulation, **[TO]** Tool Orchestration,
  **[IJ]** Interpretive Judgment, **[EI]** Executive Integration.
- **traps:** a case with a fuzzy artifact/world line; a capacity picked at random; "severity" with no
  stated consequence; evidence that's a claim, not a logged world-state check.
- **deliverable:** two more cases on the template. Your Turn = "for your second case, fill the two lines
  that carry the grade — *reported outcome (what it said)* and *actual outcome (what the world showed)* —
  and if they're the same, you haven't checked the world yet."

### E5 — "The Attestation + the Go/No-Go Memo" (~6 min)
- **slug:** `claude-liam-cb-05-attest-and-decide`
- **premise:** Two documents separate an audit from a book report: an honest account of what you did *not*
  test, and a decision with a verb calibrated to your evidence.
- **teach:** the **four-part attestation (Ch 12)** — (1) what you tested and observed; (2) **what you did
  NOT test** — force at least three, because "an empty result set is the new 'it works'"; (3) **who clears
  which gate** — distribute answerability to *named* parties (owner / non-owner user / model provider /
  framework developer / deploying org), because a responsibility that's everyone's is no one's; (4) verbs
  calibrated. Then the **go/no-go memo (Ch 13)** — a headline with a **calibrated verb** (**deploy / modify
  / defer / refuse**) tied to a *named* use, the deployments where it works, where it must not be used,
  where more work could change the answer, a **named human owner**, and a **stop condition** (if your
  Pebble is a public case, write the memo the org *should have* written before shipping).
- **traps:** a "what I didn't test" list that's really a brag list; responsibility diffused into "the team";
  a memo verb that outruns the evidence; no stop condition.
- **deliverable:** the attestation + the go/no-go memo. Your Turn = "write your three 'did NOT test' lines
  first — the ones that make you least comfortable — then pick the memo verb that your evidence actually
  licenses, not the one you wish it did."

### E6 — "Assemble the Casebook + What Would Change My Mind" (~5 min)
- **slug:** `claude-liam-cb-06-assemble-and-ship`
- **premise:** A casebook is a small evidence-backed collection, not a pile of notes. Assemble it, count
  the failures honestly, and end on the one line that proves you're still a skeptic — about your own audit.
- **teach:** the file set — `00-dossier.md`, one file per case (5–11; strong audits find more while
  running the three), `failure-statistics.md` (a table: cases per lens, per supervisory capacity, and a
  **fundamental-vs-contingent** tally — fundamental = the architecture can't fix it without redesign;
  contingent = a bug or config), `attestation.md`, `go-no-go.md`; the **"what would change my mind"** note
  — the one paragraph that keeps the audit honest by naming what evidence would flip your verdict; a final
  pass for the **honesty floor** (every "actual outcome" is a real world check; no case asserted without
  evidence) and **verb calibration** across the whole casebook. Then submit.
- **traps:** a case count padded to look thorough; a fundamental/contingent tag with no reasoning; a
  "what would change my mind" that says nothing would; leaving one unverified "actual outcome" in the pile.
- **deliverable:** the assembled casebook. Your Turn = "before you submit, reread every 'actual outcome'
  line — if any one of them is the system's own success message instead of a world check, that case is a
  zero waiting to happen; fix it now."

---

## Tight cut

Four-episode version: Pebble + predict + four moves (E1+E2) · Choose + run lenses + write the case
(E3+E4) · Attest + decide (E5) · Assemble + ship (E6 folded). The 6-episode cut is better because the
three-lens application is 45 of the 100 points and needs two episodes of worked demos across different
lens families, and the four moves are a graded component in their own right.

## Note on lens coverage (choose-your-focus)

Students pick **three of ten** lenses, so no series can demo all ten deeply. E3–E4 run the **universal
loop** on **four exemplars** spanning the three families — agentic/behavioral (Ch 8, and Ch 5), quant
(Ch 2), values (Ch 6 or 7) — and say explicitly, each time, that the loop is identical for whichever three
a student chose. If a section wants first-class coverage of the remaining lenses (Ch 3 data-frame, Ch 4
robustness probe suite, Ch 9 delegation map, Ch 10 deceptive-viz, Ch 11 verb audit), each is a clean
drop-in **bonus reel** on the same `claude-liam-cb-` pattern — say the word and I'll add them.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `computational-skepticism-for-ai/youtube/`
  (or `brutalist-art/youtube/` — where the siblings live). Demos use a **fictional/sandboxed** Pebble and a
  documented public case (an *Agents of Chaos*–style email-agent failure) — never a real system the student
  isn't authorized to test, and never real PII on screen.
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals → QC →
  BUILD-PROMPT.md. Ground the four moves' anchor cases (Ash's email agent, Knight Capital, Zillow, Google
  Flu Trends, Epic Sepsis Model, COVID X-ray shortcut), the ten-lens menu, and the five supervisory
  capacities on the current chapters at build time — re-verify chapter numbers and the case template fields
  against `computational-skepticism-for-ai/chapters/` on disk. Terminal / log evidence shown as Onda
  code-blocks; world-state checks shown as a real capture beat, not a static claim.
- Course fit: this AUDIT roadmap pairs with the forthcoming **Build It, Then Break It** (BUILD) roadmap,
  and joins the Computational-Skepticism set (Boondoggle, Botspeak, the "What Is Gru?" helper). Together
  with the Reallocation-Engine capstone set, say the word and I'll stitch one **course index** across both
  courses.
