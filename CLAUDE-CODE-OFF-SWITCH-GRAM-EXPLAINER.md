# Claude Code Prompt — An Off Switch for Dual-Use Knowledge (GRAM) — 16:9, claude-liam

Source: Anthropic, "An off switch for dual-use knowledge in AI models"
(Jul 8, 2026) — research by AE Studio in collaboration with Anthropic.
anthropic.com/research/off-switch-dual-use ·
alignment.anthropic.com/2026/modular-pretraining/

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. All facts and figure
specs are embedded — no web access needed.

```text
Build one 16:9 claude-explainer video on Anthropic + AE Studio's "An off
switch for dual-use knowledge in AI models" (July 2026) — the GRAM method,
which gives a model deletable compartments for dangerous knowledge. All
figures REBUILT as native animated graphics — never screenshots — and the
NikBearBrown (NBB) logo present throughout. claude-liam channel. Free pipeline
only: Kokoro voice, no ElevenLabs, no higgsfield, no publishing, no git commit
or push. Run without approval pauses (no paid spend is possible under these
constraints).

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md
- skills/make/explainer/SKILL.md (and the MOTION.md / REMOTION.md it points to)
- skills/make/nbb/SKILL.md            (for the NBB brand mark / logo asset)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts

FORMAT

- 1920x1080 (16:9), 30 fps.
- Channel claude-liam: persona Liam (in for Bear), voice Kokoro am_onyx,
  register Teardown. Do not use ElevenLabs. Folder chip @NikBearBrown.
- NBB LOGO: place the NikBearBrown logo as a small persistent corner bug in
  every beat (low-opacity, lower-right, never covering content) AND full-size
  on the outro brand card. Use the NBB brand mark from the nbb skill / runtime
  assets (e.g. NikBearBrownOpen/Outro scene assets); if no logo file exists,
  render a clean "@NikBearBrown" wordmark in the Claude serif as the mark.
- Audio-first: narration generated and measured per beat FIRST; every beat
  conforms to its audio. Length derives from the beats — expect 4–6 minutes.

THE STORY (Teardown register)

Hook: a frontier model is, among other things, a giant store of knowledge —
and some of it is dual-use. Virology can build a vaccine or design a pathogen.
Cybersecurity can patch a hole or exploit it. You want three things at once:
lock the dangerous stuff surgically, still let trusted users reach it for good,
and don't dent the model on everything else.
Act 1 — Why today's locks leak: refusal training and input/output classifiers
guard the OUTPUT, but they don't change what the model KNOWS. A determined
jailbreak can still reach the knowledge underneath. The more robust move is to
control what the model knows in the first place.
Act 2 — The blunt version, and its cost: you can filter dual-use data out of
pretraining — but filtering makes ONE model with ONE fixed set of abilities.
Want a virology-capable version for a vetted biosecurity lab AND a version that
can't? You'd train two whole models. At frontier scale that's prohibitively
expensive.
Act 3 — GRAM (Gradient-Routed Auxiliary Modules): the benefits of many
filtered models for the price of ONE. Add extra neurons to every Transformer
layer, grouped into a "module" per dual-use category. On general text the whole
model learns normally. On dual-use text — say virology — only the virology
module is allowed to learn; the general weights are temporarily frozen. So the
dangerous knowledge ACCUMULATES in its module instead of diffusing across the
network. After training: delete the module and the capability goes with it —
or leave it in for a trusted deployment. Four categories → one training run
that can be configured 16 different ways (on/off per category).
Act 4 — Does it work? Three tests of rising realism:
  1. Synthetic children's stories tagged by topic — a small GRAM model could be
     reconfigured to "forget" any topic, each config nearly identical to a
     model trained from scratch with that topic filtered out.
  2. A larger model on web text + code + science papers, four real domains —
     virology, cybersecurity, nuclear physics, and a niche programming
     language (proxy for specialized dual-use code). Deleting a module removed
     that capability about as well as never training on it — WITHOUT degrading
     general performance. And it resisted an attacker retraining on a little
     malicious data about as well as filtering did; a post-hoc "unlearning"
     baseline only suppressed the knowledge and was easily restored with a bit
     of fine-tuning.
  3. Seven model sizes, 50 million → 5 billion parameters. GRAM matched data
     filtering at every size, and the gap between "module on" and "module off"
     GREW as models scaled — bypassing the protection got relatively harder and
     more expensive with scale.
Landing: as models get more capable, controlling access to dual-use ability
matters more, and today's classifiers-and-refusals are hard to harden without
hurting harmless use. GRAM points at a more robust off switch. State the
honesty plainly: this is early, preliminary research — NOT applied to any
production Claude model and maybe never will be; tested only up to 5B params
and measured by next-token prediction, not real downstream tasks; and some
dual-use knowledge may be so entangled with general knowledge that no method
separates it cleanly.

STRUCTURE (claude-explainer skeleton)

- Beat 0 — ClaudeComposerAsk cold open. Liam: "A model knows things that can
  heal or harm. What if you could give it an off switch for the dangerous
  half — without lobotomizing the rest?"
- Middle — the four acts, carried by the rebuilt figures below.
- Second-to-last — Your Turn composer beat, suggested prompt typed in:
  "Explain the difference between hiding knowledge and removing it."
- Last — @NikBearBrown brand card (full NBB logo) + title restated + a small
  "Research: AE Studio × Anthropic" credit chip.

FIGURE REBUILD HONESTY RULE

The post has no data charts with exact coordinates; rebuild every figure as a
clean animated conceptual diagram. On-screen numbers are limited to: 4
categories, 16 configurations, 3 test settings, 7 model sizes, 50 million and
5 billion parameters. No invented statistics. Caption the GRAM diagrams small,
once: "After Anthropic × AE Studio, GRAM / modular pretraining (2026)".

FIG 1 — THE THREE GOALS (opening tension)
  Three balancing icons that must hold at once: a scalpel ("limit dual-use
  surgically"), a key ("let trusted users in"), and an untouched gauge ("don't
  hurt anything else"). Animate them into a three-way balance. Terracotta
  moment: all three holding level at once.

FIG 2 — WHY TODAY'S LOCKS LEAK
  A model as a glowing knowledge-blob. Refusal + classifier layers draw as
  gates on the OUTPUT side. A "jailbreak" arrow snakes past the gates and
  touches the still-intact knowledge underneath. Point: the gates guard the
  door, not the room. Contrast with the GRAM idea to come: change the room.

FIG 3 — FILTERING IS BLUNT (the cost)
  One filtered dataset → ONE model with fixed abilities. To get a
  virology-ON and a virology-OFF version you must train TWO whole models —
  animate two expensive model-stacks building in parallel, a big cost tag on
  each. This sets up GRAM's payoff.

FIG 4 — HOW GRAM WORKS (centerpiece)
  A stack of Transformer layers. Add a strip of EXTRA neurons to each layer,
  color-grouped into four modules (virology, cybersecurity, nuclear physics,
  niche-code). Then the gradient-routing rule, animated as two passes:
   • General text flows in → the WHOLE network lights up and updates (normal).
   • Virology text flows in → the general weights FREEZE (dim/locked) and ONLY
     the virology module updates and brightens.
  Show knowledge visibly pooling into the virology module over repeated passes.
  Then the payoff: DELETE the virology module (it slides out) → the virology
  capability goes dark, the rest of the model unchanged. Or leave it in for a
  trusted deployment (key icon from FIG 1). Terracotta moment: the module
  sliding out and the capability winking off.

FIG 5 — ONE RUN, 16 CONFIGURATIONS
  Four toggle switches (the four modules), each ON/OFF, animating through the
  2×2×2×2 = 16 combinations as a compact grid that fills in. Caption: one
  training run, sixteen deployable models. Terracotta accent on the count "16".

FIG 6 — THE THREE TESTS (escalating realism)
  Three stacked panels that build in sequence:
   1. Children's stories, tagged by topic → "forget any topic," each config ≈
      a from-scratch filtered model.
   2. Web+code+science, four real domains → delete a module, capability gone,
      general performance intact; then the attacker beat: retrain on a little
      malicious data — GRAM holds (like filtering), while "unlearning" (shown
      as knowledge merely greyed-out, not removed) snaps back with light
      fine-tuning. Make the removed-vs-suppressed contrast the visual point.
   3. Scale: a line/step from 50M to 5B params where the "module on" vs
      "module off" GAP visibly WIDENS as size grows. Terracotta on the widening
      gap.

FIG 7 — THE HONEST LIMITS
  Three plainly-stated caveat cards stamp onto the GRAM diagram: "not in any
  production Claude model," "tested only to 5B params / next-token metric," and
  "some knowledge may be inseparable from general knowledge." End on the third
  — the deepest open problem.

RULES

- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. EB Garamond segment titles, Title Case.
  Modules distinguished by ink tints, accent reserved for each beat's focal
  element. The NBB logo bug is the one persistent brand element on every beat.
- Transform-don't-cut: the module neurons, the freeze/learn passes, and the
  scale gap all MOVE rather than hard-cutting.
- No number on screen beyond the allowed list. GRAM is presented as early
  research, exactly as the post frames it.

OUTPUTS

- youtube/claude-liam-off-switch-gram/
  - beat_sheet.json
  - claude-liam-off-switch-gram.mp4 (1920x1080)
  - SOURCES.md — every on-screen fact/number tied to the post, plus the
    AE Studio × Anthropic credit and the NBB logo asset used.
- Verify the mp4 exists and plays (probe duration + frame count) before
  reporting done, and end with the beat → timestamp table.
- If a figure animation fails to render after two attempts, replace that beat
  with a slate card naming it and log the failure — never silently drop it.
```
