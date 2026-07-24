# Claude Code Prompt — ai-explainer for EVERY skill in anthropics/ (batch, claude-liam, 16:9)

Unattended ledger loop: one ai-explainer skill-teardown video per unique
SKILL.md under `../anthropics`, Liam voice (Kokoro am_onyx), 16:9 only.
Resumable — safe to stop and re-paste; finished videos are skipped. Each
video AUTO-OPENS in the default player when it passes QC.

Scale, honestly: ~635 SKILL.md files, ~400 unique after dedupe. This runs
for as long as you let it. The ledger is the state; kill it whenever.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace.

```text
Build one ai-explainer video (16:9, claude-liam, skill-teardown modifier)
for EVERY unique skill under ../anthropics, one after another, until the
list is exhausted or I stop you. This is an unattended batch LOOP. Free
pipeline only: Kokoro voice am_onyx, no ElevenLabs, no higgsfield, no
publishing, no git commit or push. Run without approval pauses (no paid
spend is possible under these constraints). 16:9 ONLY — never build 9:16
variants or shorts in this run.

READ COMPLETELY BEFORE ACTING (once, then apply to every video)

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md — the skill-teardown modifier section
  is the law for every video in this batch
- skills/make/explainer/SKILL.md (and its MOTION.md / REMOTION.md)
- skills/make/your-turn/SKILL.md (closing block contract)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts and tokens/layout.ts
- youtube/claude-liam-theme-factory/ and youtube/claude-liam-algorithmic-art/
  — the two exemplars built under this modifier. Copy their beat-sheet
  schema, remotion-src composition pattern, PEDAGOGY/SOURCES/BUILD-PROMPT
  discipline, and per-beat media/ flow.

THE WORK LIST (build it first, then loop)

1. Find every SKILL.md: find ../anthropics -name "SKILL.md" -not -path
   "*/node_modules/*" — exclude template/ skills, _to_delete/, archive/.
2. DEDUPE by frontmatter name: the enterprise packs (claude-for-legal,
   financial-services, knowledge-work-plugins, …) repeat skills like
   cold-start-interview / customize / matter-workspace across plugins.
   One video per unique skill name — build from the first/canonical copy,
   record the other paths as duplicates in the ledger row.
3. ORDER the queue best-first:
   a. ../anthropics/skills/skills/* (the canonical showcase repo)
   b. claude-code/plugins/*, claude-plugins-official, claude-tag-plugins
   c. k12-teacher-skills, cwc-workshops, claude-cookbooks,
      claude-agent-sdk-demos, launch-your-agent, claude-quickstarts
   d. the enterprise packs (claude-for-legal, financial-services,
      knowledge-work-plugins, healthcare, life-sciences), community
      plugins, everything else
4. SKIP already built: algorithmic-art and theme-factory exist in
   brutalist-art/youtube/ — mark them "built (exemplar)" and move on.
   Also skip any queue entry whose target mp4 already exists and probes
   valid (this is what makes the loop resumable).
5. Write the ledger BEFORE building: ../anthropics/SKILL-EXPLAINERS-BATCH-LOG.md
   — one row per unique skill: name | source path | duplicates | status
   (pending/built/failed/skipped) | mp4 path | runtime | notes. Update it
   after every video. The ledger is the single source of truth for resume.

PER VIDEO (the contract — identical for every skill)

- OWNERSHIP RULE: build INTO the owning repo's folder:
  ../anthropics/<repo>/youtube/claude-liam-<skill-name>/ (create youtube/
  if absent). Never build inside brutalist-art.
- Read the WHOLE skill first: SKILL.md plus every file it references
  (templates, references/, scripts, themes, licenses). The teardown
  explains the actual mechanism, not the description blurb.
- Author beat_sheet.json on the theme-factory schema: metadata
  (brand claude-liam, persona "Liam (in for Bear)", voice/voice_kokoro
  am_onyx, engine kokoro, palette claude, modifier skill-teardown,
  source_skill path), 9–12 beats: ClaudeComposerAsk cold open (Liam
  introduces himself in the first breath — IN-FOR-BEAR LAW; rotate the
  world-language hello, never repeat within this batch run day) → the
  modifier's act spine (what-a-skill-is compressed, the pipeline, 2–4
  mechanism acts, the design tell) → ClaudeVerdictArtifact →
  ClaudeComposerAsk handoff (Your Turn prompt that INVOKES the skill on
  the viewer's own material, read aloud verbatim and discussed) →
  ClaudeTitleOutro. Series-style title when it fits ("Claude, <word>.").
- SELF-DEMO LAW: execute the skill's own instructions where the free
  pipeline can (docx/pptx/pdf/xlsx: generate a real tiny artifact and
  rebuild its anatomy natively; design skills: render real output;
  workflow/enterprise skills that need external services or credentials:
  labeled PIPELINE slate + REBUILD-LAW illustrations of documented
  outputs, logged in BUILD-LOG.md). Never fake output. Never screenshot.
- VERBATIM QUOTE LAW: on-screen quotes exact, cited once per figure
  ("Source: Anthropic, <skill> SKILL.md" — or the actual publisher for
  community/tag plugins; check the repo).
- PEDAGOGY.md audit (honest, rewrite until it passes, end "VERDICT: PASS")
  BEFORE audio. Then Kokoro audio via
  python3 runtime/scripts/generate_audio_kokoro.py <reel> — durations are
  the locked clock. SOURCES.md: every quote with its line, every number
  computed not invented. BUILD-PROMPT.md: the standalone rebuild prompt.
- Visuals per the ai-explainer laws (ILLUSTRATE LAW — UI only in
  bookends/ask beats; SHOW-DON'T-TELL; FILL-THE-CANVAS; SPARK-LINE ≤4
  words; LOGO LAW; one terracotta accent — with the true-hex exception
  when the skill's own colors/output ARE the data, logged in SOURCES.md).
  Render Remotion only via runtime/scripts/remotion_scenes.py, foreground,
  --concurrency=1. Assemble with runtime/scripts/compile.py.
- QC per VISUAL QC LAW: frames at 2 fps + each beat at ~15/50/85%, READ
  the PNGs, 9-point rubric, _qc/REPORT.md, re-render until zero
  BLOCKER/MAJOR. Then ffprobe the mp4 (audio present, duration sane).
- AUTO-OPEN: the moment a video passes QC and probes valid, run
  open "<absolute path to the final mp4>" so it plays for the human.
  Open ONLY the final QC-passed cut, once per video — never intermediate
  renders.

THE LOOP

1. Take the next pending row in the ledger. If its mp4 exists and probes
   valid, mark built and continue.
2. Build it end to end per the contract. Update the ledger row.
3. A beat that fails twice → labeled PIPELINE slate, logged, keep going.
   A video that fails after a genuine attempt → status "failed" with the
   reason, continue to the next — one failure never halts the batch.
4. Every 10 videos, append a one-line progress summary to the ledger
   (built/failed/remaining counts).
5. Stop only when every row is built, failed, or skipped. Then print the
   final ledger table.

Begin now: build the work list, write the ledger, then start with the
first pending skill and work down. Do not ask for confirmation between
videos.
```
