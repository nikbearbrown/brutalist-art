# Claude Code Prompt — Scout the anthropics/ repo for explainer video ideas

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

The source to mine is the sibling folder `../anthropics` (a large collection
of Anthropic SDKs, tools, quickstarts, demos, and research papers — e.g.
claude-agent-sdk-*, claude-cookbooks, claude-quickstarts, skills,
prompt-eng-interactive-tutorial, model-cards, plus papers like
ConstitutionalHarmlessnessPaper, DecompositionFaithfulnessPaper,
sleeper-agents-paper, sycophancy-to-subterfuge-paper,
toy-models-of-superposition, attribution-graphs-frontend,
political-neutrality-eval, and more).

Paste the complete prompt below. Nothing to replace. This is a SCOUT pass —
it produces reviewable candidate cards only. It writes no videos, renders
nothing, spends nothing, and does not git commit or push.

```text
Scout the sibling repo ../anthropics for explainer-video candidates and write
reviewable candidate cards. This is a discovery pass ONLY: propose ideas, rank
them, never build. No rendering, no audio, no paid services, no git commit or
push. Run without approval pauses.

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- skills/make/scout/SKILL.md
- skills/make/claude-scout/SKILL.md
- skills/make/cli-scout/SKILL.md
- skills/make/sim-scout/SKILL.md
- skills/make/duration-planner/SKILL.md   (for length guidance per candidate)
- CLAUDE-BRAND.md and skills/make/ai-explainer/SKILL.md  (so cards target
  the claude-explainer builder correctly)

Follow the scout skills' candidate-card FORMAT exactly (the same format the
bears-doodles / claude-explainer builder consumes). Do not invent a new
schema — match what those SKILL.md files specify. If the scouts disagree on
minor fields, prefer the format in skills/make/scout/SKILL.md and note the
choice at the top of the index file.

SURVEY FIRST, THEN ROUTE

1. Walk ../anthropics one level deep (and one more level only where a folder's
   purpose isn't obvious from its name + README). Do NOT read entire codebases
   — read each repo's README.md / top-of-file docs / paper abstract + section
   headings. Build a short internal inventory: for each folder, one line on
   what it is and whether it carries a teachable idea.
2. Classify every folder into one of four buckets and route it to the matching
   scout lens:
   - RESEARCH / PAPERS (ConstitutionalHarmlessnessPaper,
     DecompositionFaithfulnessPaper, sleeper-agents-paper,
     sycophancy-to-subterfuge-paper, toy-models-of-superposition,
     attribution-graphs-frontend, political-neutrality-eval, model-cards,
     evals, ...) -> scout / claude-scout lens. These are concept explainers:
     one surprising, provable idea per candidate.
   - INTERPRETABILITY / VISUAL-MATH (toy-models-of-superposition,
     attribution-graphs-frontend, jacobian-lens, PySvelte, headvis, ...) ->
     sim-scout lens (Manim / interactive-dataviz candidates), because the idea
     is carried by a moving diagram.
   - BUILD-WITH-CLAUDE / SDK / TOOLS (claude-agent-sdk-*, claude-quickstarts,
     claude-cookbooks, claude-code*, skills, launch-your-agent,
     prompt-eng-interactive-tutorial, anthropic-sdk-*, maestro, apitools, ...)
     -> cli-scout lens ("build/research X with Claude" candidates).
   - SKIP: pure infra / vendored deps with no teachable Anthropic idea
     (httpcore, hypercorn, orjson, tokio, triton, rclone, s5cmd, redis-py,
     blobfile, terragrunt, argo-cd, nix-*, cargo-nix-plugin, swift-markdown*,
     leptos-chartistry, sse-starlette, python-tblib, riegeli-rs, beam, and the
     like). List these under a "Skipped (no distinctive teachable idea)"
     section with a one-line reason each — never silently drop them, so the
     human can override.

CANDIDATE CARDS

- One card per video idea, in the scout builder-card format. A single rich
  repo may yield 1-3 cards; most yield 0-1. Aim for QUALITY: a card should
  name ONE concrete, teachable, ideally counterintuitive idea — not "explain
  the whole SDK."
- Every card must include, at minimum (in addition to whatever the SKILL.md
  format requires): source folder path under ../anthropics; the one-sentence
  teachable claim; suggested builder (claude-explainer / math-explainer /
  claude-cli per the routing above); suggested channel (default claude-liam,
  since that's the free Kokoro pipeline — flag any that clearly want a
  different audience, e.g. claude-hai for teaching/ethics angles); a
  derived runtime estimate via duration-planner (not a fixed clock); and 2-4
  concrete visual beats a builder could start from.
- Prefer ideas that VISUALIZE well (a mechanism, a before/after, a
  counterintuitive result, a build-loop) over ideas that are just API surface.

RANK

- Score every candidate on a simple, stated rubric: teachability (is there one
  clear idea?), visual potential (does it move?), audience pull (would a
  channel viewer click?), and freshness (is this a story people haven't seen
  explained). Put the ranked list at the top of the index.

OUTPUTS

- Write everything under ../anthropics/vids/ (create it if absent):
  - ../anthropics/vids/INDEX.md — the ranked candidate list with scores, the
    bucket routing summary, and the "Skipped" section.
  - ../anthropics/vids/<kebab-slug>.md — one candidate card per idea, in the
    scout format, named by the idea (not the repo).
- End your run with: total folders surveyed, counts per bucket, number of
  candidate cards written, and the top 5 ranked ideas as a quick list.
- Do NOT modify anything inside ../anthropics except by adding files under
  ../anthropics/vids/. Treat every source repo as read-only.
```
