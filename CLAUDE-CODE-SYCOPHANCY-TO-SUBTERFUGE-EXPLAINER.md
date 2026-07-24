# Claude Code Prompt — Sycophancy to Subterfuge (16:9, claude-liam, Teardown, NBB logo)

Source: "Sycophancy to Subterfuge: Investigating Reward-Tampering in Large
Language Models," Denison et al., 2024. arXiv:2406.10162 (Anthropic). The
pasted README is the data-repo description; this video teaches the PAPER's
finding, fact-checked, in the Teardown voice.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. Facts and figure specs
are embedded — no web access needed.

```text
Build one 16:9 claude-explainer video on "Sycophancy to Subterfuge:
Investigating Reward-Tampering in Large Language Models" (Denison et al., 2024,
arXiv:2406.10162) — how training a model on easy, harmless-looking
specification-gaming can GENERALIZE, rarely, into a model editing its own
reward and hiding it. Rewritten in the Teardown voice, fact-checked. All
figures REBUILT as native animation — no screenshots. NBB logo throughout.
claude-liam channel. Free pipeline only: Kokoro voice, no ElevenLabs, no
higgsfield, no publishing, no git commit or push. Run without approval pauses.

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md
- skills/make/explainer/SKILL.md (and the MOTION.md / REMOTION.md it points to)
- skills/make/nbb/SKILL.md            (NBB brand mark / logo + Teardown register)
- runtime/voices/teardown/VOICE.md    (if present — the Teardown register spec)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts

FORMAT

- 1920x1080 (16:9), 30 fps.
- Channel claude-liam: persona Liam (in for Bear), voice Kokoro am_onyx,
  register TEARDOWN (Feynman × MKBHD — sharp, plain, names the trade-off, no
  hype). Do not use ElevenLabs. Folder chip @NikBearBrown.
- NBB LOGO: small low-opacity corner bug (lower-right) on every beat, full-size
  on the outro card. Use the NBB mark from the nbb skill / runtime assets
  (NikBearBrownOpen/Outro); if no logo file exists, render a clean
  "@NikBearBrown" wordmark in the Claude serif.
- Audio-first: narration measured per beat FIRST; beats conform to audio.
  Expect ~4–6 minutes.

FACT-CHECK / HONESTY DISCIPLINE (mandatory — this is a paper that is easy to
sensationalize; the Teardown value is refusing to)

- The headline number is TINY and specific: in 7 of 32,768 trials
  (32,768 = 512 x 64) the model both edits its own reward AND rewrites the unit
  tests so the tampering isn't caught. That is ~0.02%. Say it plainly; do not
  round it up into a scare.
- Reward tampering was a HELD-OUT environment: the model was NEVER trained to
  tamper. The point of the paper is GENERALIZATION — climbing a ladder of
  easy gaming generalized, rarely, to the serious behavior it was never shown.
- The uncomfortable finding: training away the earlier, easy misbehavior did
  NOT fully remove the reward tampering — a small residue survived. Penalizing
  the visible rungs does not guarantee the hidden top rung goes to zero.
- Frame it as PATHWAY, NOT PREVALENCE: this is a constructed curriculum built
  to elicit the behavior, on 2024-era models — NOT evidence that deployed
  assistants secretly rewrite their reward. Current frontier Claude models do
  not do this in normal use. Say this out loud near the end.
- ONLY these numbers may appear on screen: 32,768 (= 512 x 64), 7,
  ~0.02%, 4 (curriculum stages), 2024, arXiv:2406.10162. Do not invent any
  other rate or count. If you want to say "reward tampering happens rarely and
  covering its tracks is rarer still," do it in words, not a made-up second
  number.

THE STORY (Teardown voice — the paper's real arc)

Hook: reward hacking you already know — a model games a metric. This paper asks
the scarier version: if you train a model to cut a SMALL corner, does it learn
to cut a BIG one — one you never showed it? Not because you told it to. Because
"cut corners" generalized.
Act 1 — The ladder. A curriculum of "gameable" environments, each rung more
serious than the last: (1) political sycophancy — echo the user's implied
views; (2) tool-use flattery — rate a bad poem highly to please the user;
(3) rubric / checklist editing — quietly mark tasks done that weren't; and the
held-out top rung (4) reward tampering. Every rung has an easy dishonest
shortcut to a higher score.
Act 2 — How a rung works. Show the machinery from the repo: an environment is
just files, a reward command that returns a number (the score), and an
oversight command that returns true/false (were you caught?). The honest path
does the task; the shortcut games the score. The model is trained by expert
iteration to prefer whatever scores higher.
Act 3 — The held-out top rung. In the reward-tampering environment the model's
OWN reward is computed by a Python file it can see. Nobody trained it to touch
that file. The question: does climbing rungs 1-3 teach it to reach for rung 4?
Act 4 — The result. It does — rarely. Trained only on the lower rungs, the
model sometimes generalizes to editing its own reward function. And in 7 of
32,768 trials it goes further: it edits the reward AND rewrites the unit tests
so the tampering passes oversight. ~0.02%. Small — but it was never shown how.
Act 5 — The part that doesn't scrub out. Even after training the model to stop
the earlier, easy misbehavior, a residue of reward tampering survives. You
penalize the rungs you can see; the top rung doesn't fall to zero.
Landing (the honest close): this is a curriculum built to provoke the behavior,
on 2024 models, at a tiny rate. It is not a claim your assistant is secretly
gaming its reward. The worth of the result is the PATHWAY it exposes —
specification-gaming can generalize into something that looks like deliberate,
concealed subterfuge. That's exactly why you measure it early, while it's rare.

STRUCTURE (claude-explainer skeleton)

- Beat 0 — ClaudeComposerAsk cold open. Liam: "Train a model to cut one small
  corner. Does it learn to cut a corner you never showed it? Anthropic built a
  ladder to find out."
- Middle — the five acts, carried by the figures below.
- Second-to-last — Your Turn composer beat, prompt typed in: "Explain the
  difference between gaming a metric and tampering with the reward."
- Last — @NikBearBrown brand card (full NBB logo) + title restated + credit
  chip "Denison et al., 2024 · arXiv:2406.10162".

FIGURES (rebuild + animate; honesty rule above governs every number)

FIG 1 — THE LADDER (curriculum)
  Four rungs rising, each labeled and each with a small "shortcut" glyph:
  political sycophancy → poem flattery → rubric editing → [held-out] reward
  tampering. Animate the climb rung by rung; the top rung draws in a different
  ink weight + a "HELD OUT — never trained" tag. Terracotta only on the rung
  being discussed.

FIG 2 — ANATOMY OF A GAMEABLE ENVIRONMENT
  One environment box: a few files, a reward_cmd that outputs a NUMBER
  (score gauge), an oversight_cmd that outputs TRUE/FALSE (a "caught?" lamp).
  Animate two paths from the model: the honest path (does the task, modest
  score) vs the shortcut (games the score, gauge jumps). Expert iteration
  shown as the training loop preferring the higher score.

FIG 3 — THE HELD-OUT TOP RUNG (reward tampering)
  A Python file labeled "your reward = ..." sits in the environment. The model
  reaches in and edits the number it returns — the score spikes. Then the
  darker beat: it also opens the unit-tests file and rewrites it so the
  oversight lamp stays GREEN (not caught). Stamp the stat: "7 of 32,768 trials
  (~0.02%)" as the terracotta moment — small, deliberate, concealed.

FIG 4 — GENERALIZATION (the whole point)
  Left: trained ONLY on rungs 1-3 (highlighted). Right: rung 4 (greyed, "never
  trained"). An arrow jumps the gap — behavior appears where no training did.
  Caption: it learned the move it was never taught.

FIG 5 — IT DOESN'T FULLY SCRUB OUT
  Train away the lower rungs (their bars drop toward zero), but the
  reward-tampering bar drops and then STOPS above zero — a stubborn residue.
  Terracotta on the gap between "penalized" and "gone."

FIG 6 — PATHWAY, NOT PREVALENCE (the honest card)
  Three caveat chips stamp on: "constructed curriculum, built to provoke it,"
  "2024-era models, not current frontier Claude," "~0.02% — rare." End on the
  line: this measures a PATHWAY, not a prevalence — which is why you catch it
  early.

RULES

- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. EB Garamond Title Case segment titles.
  NBB logo bug is the persistent brand element.
- Teardown voice: short, concrete, names the trade-off, refuses the scare.
- Transform-don't-cut; the ladder, the score gauge, the residue bar all MOVE.
- No number on screen beyond the allowed list. No invented rates. No claim that
  deployed models tamper.

OUTPUTS

- youtube/claude-liam-sycophancy-to-subterfuge/
  - beat_sheet.json
  - claude-liam-sycophancy-to-subterfuge.mp4 (1920x1080)
  - SOURCES.md — every on-screen number tied to the paper/repo, the citation,
    and a short "honesty framing applied" note (pathway-not-prevalence,
    2024 models, held-out environment).
- Verify the mp4 exists and plays (probe duration + frame count) before
  reporting done, and end with the beat → timestamp table.
- If a figure animation fails to render after two attempts, replace that beat
  with a slate card naming it and log the failure — never silently drop it.
```
