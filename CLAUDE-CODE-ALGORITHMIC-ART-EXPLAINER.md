# Claude Code Prompt — The Algorithmic Art Skill (16:9, claude-liam)

Source: Anthropic's `algorithmic-art` skill (SKILL.md) — the instruction
folder that turns "make me generative art" into a two-step pipeline:
algorithmic philosophy (manifesto) → seeded p5.js implementation.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. The skill's full text is
summarized in the beats — quotes marked as verbatim are exact from SKILL.md.
No web access needed.

```text
Build one 16:9 claude-explainer video on Anthropic's algorithmic-art skill —
the shipped instruction folder that teaches Claude to make generative art by
first founding an aesthetic MOVEMENT (a written manifesto) and only then
writing the code. The reel's visuals are the argument: every major beat is a
LIVING generative system rendered natively, deterministic and seeded — the
video literally runs the kind of art the skill produces. claude-liam channel.
Free pipeline only: Kokoro voice, no ElevenLabs, no higgsfield, no
publishing, no git commit or push. Run without approval pauses (no paid
spend is possible under these constraints).

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
- Suggested title: "Claude, Seeded" (series style: Claude Taught, Claude
  Scripted, Claude Unsupervised). Restate the skill name in the description.

THE STORY (Teardown register)

Hook: when you ask Claude for art, it doesn't paint. It founds an art
movement, writes the manifesto, and then writes an algorithm that has to
live up to it. That's not a metaphor — it's literally the instruction file.
Act 1 — What a skill is: a folder of instructions Claude reads before
working (SKILL.md, templates, licenses). This one rewires "draw me
something" into a pipeline: philosophy first, code second. Outputs: a .md
manifesto and a single self-contained HTML artifact.
Act 2 — The manifesto step: Claude must invent a named movement — the
skill's own examples: "Organic Turbulence," "Quantum Harmonics," "Recursive
Whispers," "Field Dynamics," "Stochastic Crystallization" — and write 4–6
paragraphs of computational aesthetics: noise fields, particle behaviors,
emergence, parametric variation. The twist worth naming: the manifesto is a
prompt Claude writes FOR ITSELF. Phase one Claude briefs phase two Claude.
Act 3 — The conceptual seed: the skill demands a hidden reference — the
user's actual subject woven invisibly into parameters and behaviors.
Verbatim: "Think like a jazz musician quoting another song through
algorithmic harmony - only those who know will catch it, but everyone
appreciates the generative beauty." Sophistication as a design requirement.
Act 4 — The code step: p5.js, and the Art Blocks pattern — randomSeed(seed),
noiseSeed(seed) — same seed, identical output, forever. Parameters must
emerge from the philosophy ("how to express this philosophy through code?"),
never from a pattern menu. And a strict template contract: the viewer's
chrome is FIXED (sidebar, seed navigation, Anthropic branding, Poppins/Lora),
the algorithm inside is FREE. Brand consistency outside, creative anarchy
inside — the same law this very video runs on.
Act 5 — The craftsmanship tell (the Teardown moment): the skill orders
itself to repeat, over and over, that the result must feel "meticulously
crafted," "the product of deep computational expertise," "master-level
implementation." Why repeat it? Because repetition steers a language model's
quality register. This is prompt engineering pointed at Claude's own
standards dial — Anthropic prompting Claude the way power users prompt
Claude. Honest caveat: framing isn't competence; the algorithm still has to
earn it — which is why the skill also bans random RGB, demands color
harmony, composition, and performance.
Landing: process over product. "This is like creating a series of prints
from the same plate" (verbatim) — the algorithm is the plate, the seed is
the print. Beauty lives in the process, not the final frame.

STRUCTURE (claude-explainer skeleton + your-turn closing)

- Beat 0 — ClaudeComposerAsk cold open. Liam: "Ask Claude for art, and the
  first thing it writes… is a manifesto. Let me show you the strangest,
  smartest instruction file Anthropic ships."
- Middle — the five acts, carried by the living figures below.
- Closing per your-turn: VERDICT recap card → Your Turn composer beat →
  title re-read on the @NikBearBrown brand card.
- Your Turn suggested prompt (Liam reads it in full): "Create algorithmic
  art about something I love. First write me the manifesto for a new
  generative art movement, then build it as an interactive sketch — and
  hide one reference in the algorithm only I would catch."

LIVING FIGURES — the reel's visuals ARE generative systems

Implement each as a native, deterministic animated scene (Remotion canvas or
an offline-rendered port of the p5 algorithm — reproducible from a fixed
seed; never a screen recording, never a screenshot). Keep each system's
palette inside the Claude fidelity palette: ink strokes on cream, terracotta
as the single accent per beat. Seed values must be logged in SOURCES.md.

FIGURE 1 — ORGANIC TURBULENCE (Act 2 opener; the showpiece)
  A flow field driven by layered Perlin noise: thousands of particles
  following vector forces, trails accumulating into organic density maps —
  fast particles brighten toward terracotta, slow ones fade to ink shadow
  (the skill's own description, made real). Run it live behind the
  manifesto's name card: "Organic Turbulence — chaos constrained by natural
  law, order emerging from disorder."

FIGURE 2 — THE MOVEMENT GALLERY (Act 2; four quick vignettes)
  Four living thumbnails, each ~6–8 seconds, name-carded like gallery
  plaques, cycling while Liam reads the skill's condensed philosophies:
    Quantum Harmonics — gridded particles with evolving phase; interference
    makes bright nodes and voids; emergent mandalas.
    Recursive Whispers — recursive branching constrained by golden ratios,
    noise-perturbed asymmetry, line weight thinning per recursion level.
    Field Dynamics — particles born at edges flowing along invisible vector
    fields, dying at equilibrium; only the traces remain.
    Stochastic Crystallization — random points relaxing into Voronoi cells;
    color by cell size; random yet inevitable tiling.
  Transform-don't-cut between vignettes (one system dissolves into the
  next's initial conditions).

FIGURE 3 — THE PIPELINE (Act 1; diagram beat)
  A three-node flow in house style: USER REQUEST → ALGORITHMIC PHILOSOPHY
  (.md manifesto) → EXPRESSION (.html artifact, p5.js inline). Chips under
  node two: "4–6 paragraphs · a named movement · written by Claude, for
  Claude." Terracotta on the arrow between the two Claude phases —
  narration: the handoff is the invention.

FIGURE 4 — THE HIDDEN SEED (Act 3; concept beat)
  One flow field runs; a terracotta annotation ring circles a region where
  the field's angles subtly trace a motif (build a real example: e.g. the
  field's rotation constant derived from a chosen reference number).
  On-screen serif quote, verbatim: "Think like a jazz musician quoting
  another song through algorithmic harmony." Narration: the subject is in
  the parameters, not on the canvas.

FIGURE 5 — SAME PLATE, DIFFERENT PRINTS (Act 4; the seed grid)
  Onda code-block beat first (mono, small): randomSeed(seed);
  noiseSeed(seed); — labeled "the Art Blocks pattern." Then one algorithm
  rendered as a 3x3 grid of seeds (log the nine seed values), tiles
  materializing one by one — visibly the same species, visibly different
  individuals. Terracotta ring lands on one tile; caption verbatim: "a
  series of prints from the same plate." Then re-run tile #1 with its same
  seed — pixel-identical — caption: "Same seed ALWAYS produces identical
  output."

FIGURE 6 — FIXED VS VARIABLE (Act 4; UI-as-subject beat — the ONE beat
  where an interface may appear, per the ILLUSTRATE LAW, because the
  artifact viewer IS the subject)
  Rebuild the skill's viewer as a native Remotion mock (never a
  screenshot): canvas left, sidebar right — Seed (display, prev/next,
  random, jump) → Parameters (sliders) → Colors → Actions (regenerate,
  reset, download). Ink-line the FIXED chrome and hold it steady while the
  VARIABLE interior (algorithm + sliders) hot-swaps twice between two of
  the movement systems. Narration: brand consistency outside, creative
  anarchy inside.

FIGURE 7 — THE QUALITY DIAL (Act 5; typographic beat)
  The craftsmanship phrases stack in serif, each stamped like a spec:
  "meticulously crafted algorithm" · "the product of deep computational
  expertise" · "painstaking optimization" · "master-level implementation."
  A terracotta counter ticks how many times the skill repeats the
  instruction. Narration makes the Teardown point (repetition steers the
  register) and the honest caveat (framing isn't competence — the skill
  also bans random RGB and demands balance, harmony, hierarchy, and
  reproducibility).

FIGURE RULES

- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. EB Garamond segment titles, Title
  Case. The generative systems obey the same palette — ink-weight strokes
  on cream, terracotta reserved for each beat's focal element.
- Every generative beat must be deterministic: fixed seed, fixed frame
  count, reproducible render. Log every seed in SOURCES.md.
- Transform-don't-cut within figure beats.
- Verbatim quotes on screen must match SKILL.md exactly. Cite once per
  figure, small: "Source: Anthropic, algorithmic-art SKILL.md".

OUTPUTS

- youtube/claude-liam-algorithmic-art/
  - beat_sheet.json
  - claude-liam-algorithmic-art.mp4 (1920x1080)
  - SOURCES.md — every verbatim quote with its SKILL.md line, and every
    seed value used by every generative beat.
- Verify the mp4 exists and plays (probe duration and frame count) before
  reporting done, and end with the beat → timestamp table.
- If a generative system fails to render after two attempts, replace that
  beat with a slate card naming it and log the failure — never silently
  drop it.
```
