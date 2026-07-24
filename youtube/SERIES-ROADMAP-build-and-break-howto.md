# SERIES ROADMAP — "Break Your Own Build: A Skeptic's Portfolio"

A how-to ai-explainer series for **INFO 7375 (Computational Skepticism for AI) — Build It, Then Break It:
A Skeptic's Portfolio** (a 100-point BUILD: one small real artifact + two of the book's skeptical
instruments turned on *your own work* + a confession of where you let the mistake in). Audience:
**graduate students who can build a small model / dataset / dashboard / tool and have never audited their
own work — never plotted their own reliability diagram, never gone looking for the join that silently
dropped a subgroup.** Register: **pragmatic how-to with a skeptical edge** (Liam voice, `claude-liam`,
Kokoro am_onyx). Six episodes. The series walks a student from "I made it, so I know it's right" to "a
portfolio that names the mistake I let into my own build, and proves I found it." The one sentence the
whole assignment turns on: **you will defend your own fluency — break it anyway.**

> Voice: `claude-liam` per request. Owning book: **computational-skepticism-for-ai**. Build into
> `computational-skepticism-for-ai/youtube/`, or `brutalist-art/youtube/` — this roadmap ships into
> `brutalist-art/youtube/` with its siblings. This is the BUILD twin of *The Agentic Casebook* (the AUDIT
> assignment); the instruments are the same, the direction is inward, and inward is harder.

## The idea this assignment teaches (say it in E1 and again in E5)

**A builder is the least reliable auditor of their own build — exactly the way a model is the least
reliable judge of its own output.** The model you trained, the chart you made, the dataset you cleaned:
each arrives looking right *to you*, because you made it. Skepticism turned outward is a comfortable
hostile-reader posture. Turned inward, the instruments find things you would rather not have found. That
discomfort is the assignment. The professional skill this certifies is not "can you criticize an AI
system" — it is "can you doubt your **own** output at the moment it looks most finished."

## The spine (repeat every episode)

- **Pre-register the suspect.** Before you probe, name the one decision you were least sure of while
  building. That decision is usually where the mistake is; you are marking it on the record first.
- **Prediction-lock, turned inward.** Write and date what you expect the instrument to reveal *before* you
  run it — precisely because you made the thing and think you already know. That confidence is what the
  lock is testing.
- **Run the instrument as the chapter defines it — on your own build.** 25 points an instrument go to an
  *actual* reliability diagram / probe suite / leverage graph on your artifact, not a paragraph about the
  concept.

## Honesty / craft threads (DOUBLE-CHECK LAW)

- **"No mistakes found" is graded as not-looking.** Every real build has one; the skill is finding yours.
  A submission with a clean confession is either not honest or not done probing.
- **The honesty floor is a zero, not a deduction.** Fabricated results, a "reliability diagram" that isn't
  computed from real predictions, or a misleading chart built by *changing the numbers* rather than the
  encoding — each zeroes that component. The misleading-viz exercise's entire point is that **the deception
  comes only from design choices on honest data.**
- **A surprise you predicted against beats a confirmation you assumed.** The grade rewards the dated
  prediction-vs-result gap; surprises get reported as surprises, not quietly rewritten.
- **Name the fluency you were defending.** The confession isn't "I found a bug" — it's *why you wanted to
  believe the version that contained it.* That's the irreducibly-human part the course is training.
- **Small and understood beats big and gestured-at.** A toy classifier you fully understand lets you run
  the instruments end to end; a large model you can only wave at does not.
- **Residual risk is honest, not a failure.** Every fix leaves something unclosed; say what.

## Series doctrine (every episode)

- **Assume the student can build, not audit.** Define every term first time (artifact, build note,
  pre-registered suspect, prediction-lock, reliability diagram, ECE, Brier, temperature scaling, probe
  suite, features-not-bugs, epistemic frame, MNAR, leverage graph, fairness impossibility, verb taxonomy,
  three-layer document, the four moves, residual risk). Never "just."
- **One deliverable per episode**, ending in the real artifact, with a paste-ready prompt to draft the
  first pass — then the "did you run it on your *own* build, and is your prediction on the record first?"
  pass.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your Turn →
  title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "Build It Small + Pre-Register the Suspect" (~6 min)
- **slug:** `claude-liam-bnb-01-build-and-suspect`
- **premise:** The whole assignment depends on a build small enough to actually probe and honest enough to
  name what you were unsure of while making it. Pick it, build it, and mark the suspect before you defend it.
- **teach:** the five build options (**a small model/classifier** with predictions *and* confidence; **a
  dataset you assemble** with joins a reader can't see; **a dashboard/visualization** of a real finding;
  **an agent recipe/small tool** that acts and reports; **a prompt-based system** that decides or
  classifies) and the rule — small, real, yours, fully understood; then the **build note** (what it does,
  what data/inputs, and **the one decision you were least sure about** — the pre-registered suspect, because
  that's usually where the mistake is); then the **inward prediction-lock** (write and date what each
  instrument will reveal *before* you run it, since "I made it, I know" is exactly the confidence under test).
- **traps:** a build too big to probe end-to-end; a build note that hides the shaky decision instead of
  naming it; skipping the prediction because you think you already know.
- **deliverable:** the working artifact + a build note that names the suspect. Your Turn = "write your
  build note's last line first: the one decision you were least sure of while building — a label, a join,
  a threshold, a feature — because that's the suspect your instruments are going to convict."

### E2 — "Break Your Own Build: the Loop + Calibration" (~7 min)
- **slug:** `claude-liam-bnb-02-loop-and-calibration`
- **premise:** Every instrument shares one inward loop — predict, run it on your own work, report what it
  exposed *especially what you didn't want to find*. This episode runs that loop fully on the most
  transferable instrument: does your build's confidence mean anything?
- **teach:** the **break-your-own-build loop** (pre-registered prediction-lock → run the instrument as the
  chapter defines it → report the exposure, including the unwelcome one → note the fix + residual risk);
  then **Calibration (Ch 2 + Ch 11)** worked end-to-end — make your artifact **emit its own confidence**,
  **bin predictions by stated confidence**, plot the **reliability diagram** against the diagonal, compute
  **Brier score** and **ECE**, fit **temperature scaling**, then **re-plot on a shifted slice** of data and
  report what moved — catching the *decorative* confidence number that looked meaningful and wasn't. Weave
  in the first **classical moves** inward: Descartes (how could my "90% confident" be false?), Hume (is that
  confidence about the world or only about my sample?).
- **traps:** a sentence about calibration instead of a computed diagram; skipping the shifted-distribution
  re-plot (where the decorative number is exposed); reading a good in-sample curve as proof.
- **deliverable:** a real reliability diagram + ECE/Brier + a shifted re-plot on your build. Your Turn =
  "predict your model's ECE before you compute it — write the number down — then compute it; the gap
  between your guess and the truth is the first thing calibration taught you about your own confidence."

### E3 — "Probe the Model and Its Data: Robustness + the Data-Frame" (~7 min)
- **slug:** `claude-liam-bnb-03-robustness-and-data-frame`
- **premise:** Two instruments that attack the two places a build hides its mistakes — the model's learned
  shortcuts, and the data it never questioned. Run whichever fits your artifact; the loop is identical.
- **teach:** **Robustness probe (Ch 4)** — write a small **probe suite** (≥3: perturbation, proxy-feature,
  distribution-shift, plus authority-escalation / tool-surface for agents & prompts), run it, and for each
  break apply **features-not-bugs** framing (name the **proxy** your build learned, the **human-relevant
  feature** it *should* use, and what the gap says), delivering a **robustness profile** table (robust
  against *what* · residual risk · monitoring) — never a single number. Then **Data-frame audit (Ch 3)** —
  write a **datasheet** for your data (Gebru's questions, adapted), run the **six-step epistemic-frame
  reconstruction** ("why exactly N rows? what is *not* in the data?" — MCAR/MAR/**MNAR**), build the
  **structural-assumptions table** (sampling / time-window / label-proxy / MNAR / feature-engineering /
  boundary), trace one row end-to-end, and name a **hidden failure procedural EDA would miss** in your own
  data. Continue the four moves inward: Plato (name the artifact I made vs. the world it claims to describe).
- **traps:** a probe suite that only perturbs and never tests a proxy; a robustness *number* instead of a
  profile; a datasheet that describes the file instead of reconstructing the frame; the row-trace skipped.
- **deliverable:** a robustness profile *or* an epistemic-frame audit of your own build. Your Turn = "run
  one proxy-feature probe on your model — remove or scramble the feature you suspect it's leaning on — and
  if accuracy barely moves, you found the shortcut it actually learned."

### E4 — "Values & Honesty: Bias, Misleading Charts, Over-Reaching Verbs" (~7 min)
- **slug:** `claude-liam-bnb-04-values-and-honesty`
- **premise:** Three instruments for the mistakes that don't show up in accuracy — where bias enters, how
  a chart flatters a result, and how a verb outruns its evidence. All on your own work.
- **teach:** **Bias & fairness (Ch 6 + Ch 7)** — draw the **causal graph** from world to your artifact's
  output, run a **leverage analysis** to find where bias enters (rarely the model), then compute **≥2 of
  demographic parity / equalized odds / calibration parity** across a group in your data, show they
  **cannot all hold** (the **impossibility, on your own numbers**), and write a **defended choice** with a
  monitoring plan — or a defended "not applicable, here is why." **Honest visualization (Ch 10)** — build
  the **honest** version of your finding *and* a **deliberately misleading** version **from the same
  numbers** (deception only from encoding: truncated axes, distribution-hiding aggregation, cherry-picked
  window, color asymmetry), put them side by side, and write what each choice did (the misleading chart is
  for-your-eyes-only; the report ships the *comparison*). **Uncertainty & verbs (Ch 11)** — write your
  central finding in the **three-layer document** (plain / technical / reproducibility appendix), run a
  **verb audit** against the taxonomy (*hypothesize → suggest → observe → find → show → demonstrate →
  conclude → prove*), mark every over-reach *you* made, rewrite at the licensed verb, and state **what
  would change your mind**. Close the four moves: Popper (what did I decide, in advance, would count as my
  build failing?).
- **traps:** a fairness metric computed but no impossibility shown on your numbers; a misleading chart made
  by inventing data (a zero — the point is honest data, dishonest encoding); a verb audit that finds no
  over-reach in your own writing.
- **deliverable:** one values/honesty instrument fully run on your build. Your Turn = "take your build's
  headline sentence and find its verb on the taxonomy — if you wrote 'shows' or 'proves,' ask what result
  would license that verb, and whether you actually have it."

### E5 — "The Confession: Where I Let the Mistake In" (~6 min)
- **slug:** `claude-liam-bnb-05-the-confession`
- **premise:** The heart of the BUILD, and the hardest page to write. Not "here's a bug" — the real mistake
  you let into your own work, and the fluency you were defending when you did.
- **teach:** the four parts of the confession — **what the mistake was** (a leaked feature, an optimistic
  label, a chart choice that flattered the result, an unchecked confidence number, a join that silently
  dropped a subgroup — the *real* one your instruments surfaced, not a hypothetical); **why you wanted to
  believe the version that contained it** (the fluency you were defending — the part only you can name);
  **how an instrument caught it** (or how you caught it while running one); **what you changed and what
  residual risk remains.** Why "no mistakes found" is graded as not-looking, and why the confession — not
  the clean result — is what the course certifies.
- **traps:** a safe, cosmetic "mistake" that costs nothing to admit; skipping the *why-you-believed-it*
  part (the whole point); claiming a fix with no residual risk named.
- **deliverable:** the one-page confession. Your Turn = "write the sentence you don't want to write: the
  version of your result you were rooting for, and the reason you were rooting for it — that reason is the
  mistake's hiding place."

### E6 — "Assemble the Skeptic's Portfolio + Ship" (~5 min)
- **slug:** `claude-liam-bnb-06-assemble-and-ship`
- **premise:** A portfolio, not a pile — the artifact, two instrument reports, the confession, and a
  closing note that keeps you honest. Assembled so an employer could open it.
- **teach:** the deliverable set — the **artifact** (code / dataset / dashboard / tool / prompt system)
  with a **run/repro note** a reader can actually rerun; the **build note** with the pre-registered
  suspect; **two instrument reports**, each with its **dated prediction-lock**, method, result, and the
  **labeled classical moves**; the **confession**; a closing **"what would change my mind" / "still
  puzzling"** note; the **three-layer / reproducibility** pass (a reader can rerun the core result; claims
  pitched at licensed verbs). Then the **stretch** (a third instrument — no extra rubric points, but a
  materially stronger portfolio for an employer and for the honesty quartile), and a final **honesty-floor**
  sweep (every diagram computed from real predictions; the misleading chart built only from encoding).
- **traps:** a repro note nobody can follow; prediction-locks written after the fact; leaving an
  uncomputed figure or an invented-number chart in the pile.
- **deliverable:** the assembled skeptic's portfolio. Your Turn = "hand your repro note to a classmate and
  have them rerun your core result from it alone — the step they get stuck on is the step you left out."

---

## Tight cut

Four-episode version: Build + suspect + the loop + calibration (E1+E2) · One more instrument across
model/data/values (E3 or E4) · The confession (E5) · Assemble + ship (E6). The 6-episode cut is better
because the two instruments are 50 of the 100 points and the six-option menu needs worked demos across all
three families (quant, model/data, values/honesty), and the confession is the graded thematic core and
earns its own beat.

## Note on instrument coverage (choose-your-focus)

Students run **two of six** instruments, so E2–E4 demo the **inward loop** on all six exemplars — quant
(Ch 2+11 calibration), model/data (Ch 4 robustness, Ch 3 data-frame), values/honesty (Ch 6/7 fairness,
Ch 10 honest-viz, Ch 11 verbs) — while saying, each time, that the loop is identical for whichever two a
student picks. The four classical moves are woven across E2–E4 (Descartes/Hume in E2, Plato in E3, Popper
in E4) rather than given a standalone episode, because here they're graded *inside* the instrument work,
not as a separate component.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `computational-skepticism-for-ai/youtube/`
  (or `brutalist-art/youtube/` — where the siblings live). Demos build a **toy, fully-understood** artifact
  (a small tabular classifier + a real public dataset) so the reliability diagram, probe suite, and
  leverage graph can be shown *computed*, not gestured at — and any on-screen data is public, never real PII.
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals → QC →
  BUILD-PROMPT.md. Ground every technique on the current chapters at build time — re-verify the reliability
  diagram / ECE / temperature-scaling method (Ch 2, 11), the probe-suite + features-not-bugs framing (Ch 4),
  the six-step epistemic-frame + MNAR (Ch 3), the fairness impossibility (Ch 6, 7), the deceptive-viz
  catalog (Ch 10), and the verb taxonomy (Ch 11) against `computational-skepticism-for-ai/chapters/` on
  disk. Computed figures shown as real plot beats; code shown as Onda code-blocks.
- Course fit: this BUILD roadmap is the twin of **The Agentic Casebook** (AUDIT) roadmap — one skill facing
  two directions — and joins the Computational-Skepticism set (Boondoggle, Botspeak, the "What Is Gru?"
  helper). With the Reallocation-Engine capstone set, say the word and I'll stitch one **course index**
  across both courses.
