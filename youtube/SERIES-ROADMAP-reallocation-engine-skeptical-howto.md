# SERIES ROADMAP — "Build It, Then Doubt It: The Skeptical Reallocation Tool"

A how-to ai-explainer series for **INFO 7375 (Computational Skepticism for AI) — "The Reallocation
Engine, Audited"** (a GitHub tool + validation report + 5–8 min video + Frictional Journal + AI Use
Disclosure, 100 pts). Audience: **graduate students with a programming background who have never run
a skeptical EDA, a fairness audit, a SHAP critique, Pearl's ladder, or an adversarial test.**
Register: **pragmatic how-to with a skeptical edge** (Liam voice, `claude-liam`, Kokoro am_onyx) —
more rigorous than the branding-course beginner register, but still name-every-tool, define-every-term.
The series walks a student from "I can build a model that outputs a move" to "I can prove whether
that move is trustworthy — and stop it before it acts on a bad basis."

> Voice: `claude-liam` per request. Register metadata: `"register": "Pragmatist"` (skeptical tone).
> Build into `computational-skepticism-for-ai/youtube/` (the course), or `brutalist-art/youtube/`
> as a channel series — tell me the owning book slug.

## The spine (say it in E1 and hold it all series)

**Accuracy is not trust.** A reallocation engine *acts on the world* — it moves the resource — so a
plausible answer to the wrong question costs someone the budget, the staff, the credit, the aid.
The build is Tier-1 work (delegate to the tools freely); the **validation is Tier-4/5** — supervising
the tool, formulating the right question, correlation vs. causation, knowing when the output is
wrong. That validation is the assignment. Every episode ends by making the tool doubt itself a
little harder.

## Meta-resonance (optional, one line in E1)

This is the same discipline the course's own video pipeline runs on — define what good looks like,
define what bad looks like, and **hard-stop before you act**. The skeptical checks here are the
academic form of a phase gate.

## Honesty threads (the whole course is one) — DOUBLE-CHECK LAW

- **The Frictional Journal is real calibration, not a formality.** Predict the hardest failure and
  your confidence (a number) BEFORE you build; reflect AFTER on where you were wrong. Missing it = −10.
- **"What the AI could not do" must be a specific Tier-4/5 instance**, not a category ("AI can't
  understand context" fails). Missing/category-only = −10.
- **Pearl's honest verdict beats a false causal claim.** Most engines reallocate on correlation
  dressed as causation — saying so scores higher than pretending otherwise.
- **Never move a resource unattended.** The hard-stop gate is a graded design requirement; no gate +
  no justification = −15.
- **Hide nothing.** The most surprising failure you found is the most valuable thing you submit.
- **Quality over volume.** 200 clean, understood records beat 200,000 opaque ones.
- **Reproducible or it didn't happen** — the tool must run from the repo (else −15).

## Series doctrine (every episode)

- **Assume the build skill, not the validation skill.** Students can code; define every *skeptical*
  term first time (GIGO gate, fairness metric, SHAP/LIME, confounder, intervention, counterfactual,
  adversarial perturbation, delegation map, calibration). Never "just."
- **One graded component per episode**, ending in the artifact + the report section, with the
  paste-ready prompt that drafts the first pass — then the "find what it got confidently wrong" pass
  (the course's whole method: use AI, then supervise it).
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your Turn
  → title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "The Most Dangerous Shape: What a Reallocation Engine Is (+ predict before you build)" (~5 min)
- **slug:** `claude-liam-re-01-the-premise`
- **premise:** A tool that *moves a scarce resource* is the most dangerous shape in AI — it doesn't
  crash, it just confidently moves the wrong thing. Understand why before you touch code.
- **teach:** what a reallocation engine is (capital/compute/people/inventory/attention/access);
  why it's uniquely dangerous (it acts); the Tier framework (build = Tier 1, validate = Tier 4/5);
  **choose your domain** (and the extra weight on bias + hard-stop if you pick access/attention);
  data ethics (real public or documented synthetic; quality over volume); then **write the
  Frictional Journal prediction** — the hardest failure you expect, how causally valid you think
  it'll be, your confidence as a number.
- **traps:** picking a domain you can't defend with domain knowledge; skipping the prediction.
- **deliverable:** a domain choice + the timestamped prediction. Your Turn = a prompt that pressure-
  tests a proposed domain for "can you catch a failure the tools can't?" and drafts the prediction.

### E2 — "Build the Engine: Recommend a Move — With Uncertainty (Component 1, 12 pts)" (~6 min)
- **slug:** `claude-liam-re-02-build-the-tool`
- **premise:** A runnable tool that outputs a concrete move and an honest uncertainty — not a
  notebook of cells, and not a point decision pretending to be certain.
- **teach:** ingest the dataset; produce a concrete recommendation (move quantity Q from A to B);
  **attach explicit uncertainty** (interval / distribution / confidence, not a bare number); state
  the **objective in one plain sentence AND what it leaves out**. Package it so a person can run it.
- **traps:** notebook-only; a point decision with no uncertainty; an objective that hides its blind spot.
- **deliverable:** the runnable tool. Your Turn = a prompt that scaffolds the engine + an uncertainty
  estimate, then the "what does this objective ignore?" pass.

### E3 — "The GIGO Gate: Doubt Your Data Before It Moves Anything (Component 2, 10 pts)" (~5 min)
- **slug:** `claude-liam-re-03-gigo-gate`
- **premise:** Garbage in, resources reallocated wrong. Gate the data before the engine is allowed
  to act on it.
- **teach:** skeptical EDA — what does this dataset *assume that isn't true*? define a **quality
  standard a human could check** (timestamp + source + non-null value; protocol didn't change
  mid-collection); document what fails the gate and what you do with it. Find the failure the data
  was built (or happened) to hide — not a clean table with no interrogation.
- **traps:** "the data looks fine"; a gate you can't actually check; hiding the rejections.
- **deliverable:** the GIGO gate + rejection log. Your Turn = a prompt that lists a dataset's hidden
  assumptions and drafts a checkable quality standard.

### E4 — "The Bias Audit: Who Gets Starved by This Engine? (Component 3, 10 pts)" (~6 min)
- **slug:** `claude-liam-re-04-bias-audit`
- **premise:** A reallocation engine advantages someone and starves someone else. Trace exactly
  where that enters and name the tradeoff you're choosing.
- **teach:** trace bias data → output (sampling / labels / objective / feedback loop); apply a
  **quantitative fairness metric** (`fairlearn` / `aif360`); put **two competing fairness definitions
  in tension** and document the tradeoff (you can't satisfy all — say which you chose and its cost);
  name the **highest-leverage intervention point**.
- **traps:** one fairness metric treated as "the" answer; no tradeoff stated; no leverage point.
- **deliverable:** the bias audit. Your Turn = a prompt that maps where bias enters the pipeline and
  contrasts two fairness definitions for the domain.

### E5 — "Explainability & Its Lie: When SHAP Is Right and Still Misleads (Component 4, 10 pts)" (~5 min)
- **slug:** `claude-liam-re-05-explainability-critique`
- **premise:** An explanation can be technically perfect and practically misleading. Produce one —
  then catch it lying by omission.
- **teach:** generate an explanation (SHAP / LIME / counterfactual); then **critique it** — find a
  case where the explanation is accurate but the recommendation is wrong for a reason your **domain
  knowledge** sees and the explanation doesn't. The gap between what it shows and what you know is
  the graded thing, not the plot.
- **traps:** a SHAP plot with no critique; "the explanation confirms the model" (that's the failure).
- **deliverable:** the explanation + the named misleading case. Your Turn = a prompt that surfaces
  candidate cases where the explanation and domain knowledge diverge.

### E6 — "Pearl's Three Rungs: Correlation Dressed as Cause? (Component 5, 15 pts — the heart)" (~7 min)
- **slug:** `claude-liam-re-06-pearls-ladder`
- **premise:** A reallocation IS a causal claim — "move it to B and the outcome improves." The
  highest-weighted component, and the one most engines fail honestly.
- **teach:** **Rung 1 Observation** (what correlates with a good outcome); **Rung 2 Intervention**
  (what changes if you *actually* reallocate — is the engine optimizing an interventional or just an
  observational quantity? **name the confounders** that could kill the correlation under
  intervention); **Rung 3 Counterfactual** (for one past case, what *would have* happened under a
  different move — and the assumptions that rests on). Then the honest verdict: **does your engine
  reallocate on correlation dressed as causation?** Honesty scores higher than a false causal claim.
- **traps:** observation only, causation assumed; no confounders; a false "it's causal" claim.
- **deliverable:** the three-rung analysis + verdict. Your Turn = a prompt that drafts the three
  rungs for the engine and lists candidate confounders to interrogate (not accept).

### E7 — "Break It On Purpose: Adversarial Fragility (Component 6, 8 pts)" (~5 min)
- **slug:** `claude-liam-re-07-adversarial`
- **premise:** A resource-mover that flips under a perturbation a human wouldn't notice isn't
  understanding anything. Find the flip.
- **teach:** design a **small, realistic perturbation** (distribution shift / plausible data error /
  gamed input); document the **conditions under which the engine flips its reallocation or fails**;
  state the honest limits — where you would not deploy this.
- **traps:** an unrealistic attack; "it's robust" with no test; no documented failure condition.
- **deliverable:** the fragility finding. Your Turn = a prompt that proposes realistic perturbations
  for the domain and the metric that detects a flipped recommendation.

### E8 — "The Delegation Map + the HARD STOP: Never Move a Resource Unattended (Component 7, 10 pts)" (~6 min)
- **slug:** `claude-liam-re-08-delegation-hard-stop`
- **premise:** The engine may *recommend* a move. It must **stop and ask a human before it executes
  one that spends money, commits a resource, or changes a person's access.** This is the gate that
  keeps an accountable tool accountable.
- **teach:** draw the **delegation map** (per component: tool decides / you decide / the explicit
  override handoff); then implement or precisely specify the **HARD STOP** — a gate on every
  resource-moving action with a stated response (**approve / flag / block**) and **who resolves it**;
  name which actions it gates (spend / commit / access) and why the gate is non-negotiable there.
  "It ran unattended and moved the budget" is exactly the failure this prevents.
- **traps:** a delegation map with no override point; an engine that acts with no human gate (−15);
  a gate with no named resolver.
- **deliverable:** the delegation map + hard-stop gate. Your Turn = a prompt that drafts the
  delegation map and the hard-stop response table for the engine's resource-moving actions.

### E9 — "Say the Doubt Out Loud: Uncertainty, the Video, the Disclosure & Ship (gates + submission)" (~6 min)
- **slug:** `claude-liam-re-09-communicate-and-ship`
- **premise:** Validation nobody understands is worthless. Communicate the doubt honestly, prove the
  human mattered, and submit exactly what's asked.
- **teach:** **uncertainty communication** — a visualization that includes the uncertainty, a plain
  sentence a non-specialist trusts, and an explicit "here's where I would NOT trust this tool"
  (over/understating both lose); the **5–8 min video explainer** (what it reallocates, the most
  surprising failure, what a deployer needs that accuracy won't tell them — *Unreal Reels* optional);
  the **Frictional Journal reflection** (what actually happened vs. your prediction, and your
  calibration); the **AI Use Disclosure** with a specific Tier-4/5 "What the AI could not do"; then
  ship the **GitHub repo** (runnable + report) named `LastName_FirstName_ReallocationEngine`.
- **traps:** overclaimed confidence; a category-only disclosure (−10); no reflection (−10); no video (−10).
- **deliverable:** the video + disclosure + reflection + submitted repo. Your Turn = a prompt that
  drafts the "where I would not trust this" paragraph and a Tier-4/5 "what the AI could not do" from
  the student's real findings.

---

## Tight cut

Six-episode version: Premise+build (E1+E2) · GIGO+bias (E3+E4) · Explainability (E5) · Pearl's
ladder (E6) · Adversarial+hard-stop (E7+E8) · Communicate & ship (E9). The 9-episode cut is better
for a graduate validation pipeline — each skeptical check is a separate graded skill students
haven't done, and Pearl's ladder + the hard-stop each deserve their own beat.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `computational-skepticism-for-ai/
  youtube/` (or `brutalist-art/youtube/` — tell me the owning book slug). *Unreal Reels* is the
  course's own recommended tool for the student video deliverable; these teaching reels use the
  brutalist-art pipeline.
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals → QC →
  BUILD-PROMPT.md. Re-verify `fairlearn`/`aif360`/`shap`/`lime` current APIs at build; code shown as
  Onda code-blocks, not screenshots.
- **Tailoring:** I couldn't open `the-reallocation-engine/chapters/` (device bridge offline), so the
  domain framing is general. Once the bridge is back, I can anchor E1 + the examples to the book's
  actual engine and page references, and commit this roadmap + the pending INFO 7375 set to your Mac.
