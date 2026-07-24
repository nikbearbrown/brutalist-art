# Claude Code Prompt — ai-explainer for EVERY brutalist-art skill (meta-series, claude-liam, 16:9)

Unattended ledger loop: one ai-explainer skill-teardown video per skill in
the toolkit's own `art list`, Liam voice (Kokoro am_onyx), 16:9. These are
videos ABOUT the toolkit, so per the ownership rule they build INTO
`brutalist-art/youtube/` (the Brutalist meta-series exception — NOT into a
book). Resumable; each finished video auto-opens.

~46 skills. This runs a while. The ledger is the state; stop and re-paste
any time.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace.

```text
Build one ai-explainer video (16:9, claude-liam, skill-teardown modifier)
for EVERY skill in this toolkit's own `skills/make/` directory, one after
another, until the list is exhausted or I stop you. This is the Brutalist
META-SERIES: the videos are ABOUT the toolkit, so per the ownership rule
they build INTO brutalist-art/youtube/, NOT into any book. Unattended batch
LOOP. Free pipeline only: Kokoro voice am_onyx, no ElevenLabs, no
higgsfield, no publishing, no git commit or push. Run without approval
pauses (no paid spend possible). 16:9 ONLY — no 9:16, no shorts.

READ COMPLETELY BEFORE ACTING (once, then apply to every video)

- AGENTS.md, CLAUDE.md (the ownership rule), CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md — the skill-teardown modifier section
  is the law for every video in this batch
- skills/make/explainer/SKILL.md (and its MOTION.md / REMOTION.md)
- skills/make/your-turn/SKILL.md, docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts and tokens/layout.ts
- GLOSSARY.md (old→new names — use the NEW name as the slug; keep the old
  name as a trigger-word mention where it helps a viewer)
- youtube/claude-liam-theme-factory/ and youtube/claude-liam-algorithmic-art/
  — the two skill-teardown exemplars. Copy their beat-sheet schema,
  remotion-src composition pattern, PEDAGOGY/SOURCES/BUILD-PROMPT
  discipline, and per-beat media/ flow.

THE WORK LIST (build it first, then loop)

1. Enumerate skills: every directory under skills/make/ that contains a
   SKILL.md. Confirm against `bash art --list`. Each skill's SKILL.md is
   the source; the slug is claude-liam-<skill-name> (the NEW name).
2. SKIP already built: any skill whose youtube/claude-liam-<skill>/ mp4
   already exists and probes valid (resume). No toolkit-skill exemplars
   exist yet, so none are pre-skipped — theme-factory and algorithmic-art
   are ANTHROPIC skills, a different series, leave them alone.
3. ORDER the queue best-first (most-used builders first, ops/reference
   last):
   a. The explainer builders people reach for daily: ai-explainer,
      sketch-explainer, math-explainer, explainer, remotion-explainer,
      code-walkthrough, cli-explainer, explainer-deepen.
   b. Ideas + script: scout, claude-scout, cli-scout, sim-scout,
      script-writer, shot-planner, duration-planner.
   c. Story / music / bio / kids: story-film, bio, music-video, songbird,
      lyric-resync, lyric-overlay, dance-video, recitation-film,
      kids-video, collage-ads.
   d. Branding / audience / assets: audience-preset, nbb, hai, medhavy,
      brutalist-medhavy, logo, ai-asset-gen, ai-character-id,
      diagram-redraw, line-art-vectorizer, figure-planner, component-showcase.
   e. Ops / closing / publish: your-turn, slate-filler, reel-updater,
      video-inventory, claude-refactor, session, youtube-publisher.
   f. Parked/unlisted last (mark LOW in the ledger, still build unless I
      say skip): listing-cards, product-photos.
4. Write the ledger BEFORE building: youtube/META-SERIES-BATCH-LOG.md —
   one row per skill: name | old name | source SKILL.md | tier(a–f) |
   status (pending/built/failed/skipped) | mp4 path | runtime | notes.
   Update after every video. The ledger is the single source of truth for
   resume.

PER VIDEO (skill-teardown contract — identical for every skill)

- Build INTO brutalist-art/youtube/claude-liam-<skill-name>/ (meta-series).
- Read the WHOLE skill first: SKILL.md + everything it references
  (reference files, scripts, templates). The teardown explains the actual
  mechanism, not the description blurb.
- Author beat_sheet.json on the theme-factory schema: metadata (brand
  claude-liam, persona "Liam (in for Bear)", voice/voice_kokoro am_onyx,
  engine kokoro, palette claude, modifier skill-teardown, source_skill
  path), 9–12 beats: ClaudeComposerAsk cold open (Liam introduces himself
  first breath — IN-FOR-BEAR LAW; rotate the world-language hello, NEVER
  repeat a hello within this run) → the modifier's act spine
  (what-a-skill-is compressed after the first few episodes, the pipeline,
  2–4 mechanism acts, the design tell) → ClaudeVerdictArtifact →
  ClaudeComposerAsk handoff (Your Turn prompt that INVOKES the skill on
  the viewer's OWN material — e.g. "run sketch-explainer on your hardest
  chapter concept"; read aloud verbatim + discussed) → ClaudeTitleOutro.
  Series title "Claude, <participle>." when it fits; restate the skill
  name in the description.
- SELF-DEMO LAW (mandatory when feasible): these skills MAKE things, so
  the demo is the skill's own output rebuilt natively — a sketch-explainer
  beat shows a real progressive-disclosure doodle fragment; math-explainer
  shows a Manim fragment; script-writer shows a real beat_sheet.json being
  emitted; duration-planner shows a real content→length computation;
  scout shows a real candidate card. Where actually running the skill
  needs paid APIs or another render pass, that demo beat is a labeled
  PIPELINE slate naming what's needed + REBUILD-LAW illustrations of the
  documented output, logged in BUILD-LOG.md. Never fake output, never
  screenshot. (Meta note: ai-explainer's own episode may use the mirror
  move — this very video is the skill demoing itself.)
- VERBATIM QUOTE LAW: on-screen quotes exact, cited once per figure
  "Source: brutalist-art/skills/make/<skill>/SKILL.md".
- PEDAGOGY.md audit (honest, rewrite until it passes, end "VERDICT: PASS")
  BEFORE audio. Kokoro audio via
  python3 runtime/scripts/generate_audio_kokoro.py <reel> — durations are
  the locked clock. SOURCES.md: every quote with its line, numbers
  computed not invented. BUILD-PROMPT.md: the standalone rebuild prompt.
- Visuals per the ai-explainer laws (ILLUSTRATE LAW — UI only in
  bookends/ask beats; SHOW-DON'T-TELL; FILL-THE-CANVAS; SPARK-LINE ≤4
  words; LOGO LAW; one terracotta accent). Render Remotion only via
  runtime/scripts/remotion_scenes.py, foreground, --concurrency=1.
  Assemble with runtime/scripts/compile.py.
- QC per VISUAL QC LAW: frames at 2 fps + each beat ~15/50/85%, READ the
  PNGs, 9-point rubric, _qc/REPORT.md, re-render until zero BLOCKER/MAJOR.
  Then ffprobe (audio present, duration sane).
- AUTO-OPEN: the moment a video passes QC and probes valid, run
  open "<absolute path to the final mp4>" so it plays for the human. Only
  the final QC-passed cut, once per video.

THE LOOP

1. Next pending ledger row. If its mp4 exists and probes valid, mark built
   and continue.
2. Build end to end per the contract. Update the ledger row.
3. A beat failing twice → labeled PIPELINE slate, logged, keep going. A
   video failing after a genuine attempt → status "failed" + reason,
   continue — one failure never halts the batch.
4. Every 10 videos, append a one-line progress summary to the ledger.
5. Stop only when every row is built, failed, or skipped. Print the final
   ledger table.

Begin now: enumerate skills/make/, write youtube/META-SERIES-BATCH-LOG.md,
then start with tier (a) and work down. Do not ask for confirmation between
videos — run the list.
```
