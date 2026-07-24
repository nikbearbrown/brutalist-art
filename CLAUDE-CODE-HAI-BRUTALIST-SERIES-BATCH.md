# Claude Code Prompt — "Using Brutalist" HAI Fellows Series (batch, claude-liam)

Builds the full Humanitarians AI Fellows onboarding series (E01–E12) as
claude-liam / @HumanitariansAI explainers, one after another, until all are
done — every video carried by native animated visualizations and infographics.

Series map (read it — it holds the per-episode capsules):
`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/HAI-FELLOWS-BRUTALIST-SERIES-MAP.md`

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. Resumable LOOP: builds
every episode, skips any already rendered, never stops until each is built or
logged failed. Toolkit meta-series → builds into `brutalist-art/youtube/`.
Free pipeline only — Kokoro voice, no ElevenLabs, no higgsfield, no
publishing, no git commit or push.

```text
Build the full "Using Brutalist" Humanitarians AI Fellows onboarding series —
episodes E01 through E12 in HAI-FELLOWS-BRUTALIST-SERIES-MAP.md — as
claude-explainer videos (16:9, claude-liam voice, @HumanitariansAI branding),
and keep going until all are built. This is a batch LOOP (12 videos), not one
video. Free pipeline only: Kokoro voice, no ElevenLabs, no higgsfield, no
publishing, no git commit or push. Run start-to-finish without approval pauses
— the human reviews the finished mp4s at the end.

READ COMPLETELY BEFORE ACTING (once, then apply to every episode)

- AGENTS.md
- CLAUDE-BRAND.md
- youtube/HAI-FELLOWS-BRUTALIST-SERIES-MAP.md  (the series map — episode list,
  slugs, theses, and the centerpiece each episode animates)
- skills/make/ai-explainer/SKILL.md  (incl. the Student/Fellow profile mode,
  used by E12)
- skills/make/explainer/SKILL.md (and MOTION.md / REMOTION.md)
- skills/make/your-turn/SKILL.md
- skills/make/cli-explainer/SKILL.md (for the command/terminal beats in
  E03 / E05 / E06)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts
- For accuracy, the existing topic builds you're rebranding: what-is-brutalist/,
  installs/, posting-to-youtube/, cowork-setup/ (reuse their FACTS — commands,
  steps, file names — do NOT copy their @NikBearBrown branding).

SHARED RULES (every episode)

- Channel claude-liam: persona Liam (Kokoro am_onyx), IN-FOR-BEAR LAW — Liam
  says "Liam, in for Bear" on the cold open and outro. Folder chip
  @HumanitariansAI; HAI logo bug per LOGO LAW; full-size HAI mark on the outro.
  Register Teardown-warm — this is a welcome to Fellows, not a takedown.
- Format 1920x1080 (16:9), 30 fps. Audio-first: narration generated and
  measured per beat FIRST; every beat conforms to its audio. Expect 2–4 min
  each; length from beats.
- AUDIENCE = Humanitarians AI Fellows learning to turn a week of their research
  into a published explainer. Every episode teaches ONE step of that loop and
  ends pointing at the next.
- VISUALIZE EVERYTHING YOU CAN — every step, command, pipeline, comparison, or
  mechanism is a NATIVE animated Manim/Remotion beat (infographic or diagram)
  in the Claude palette, never a screenshot, never a static bullet list. Build
  each episode's "centerpiece" from the series map exactly. ASK→RESULT law
  applies wherever a generated visual appears. Follow the dataviz discipline,
  recolored to the Claude fidelity palette.
- Claude fidelity palette: cream #FAF9F5, warm ink #3D3929, terracotta #D97757
  as the ONE accent per beat. EB Garamond segment titles, Title Case. Onda
  code-block for every command/code line (real commands, never prose as code).
  Claude UI (composer) only in the bookends per ILLUSTRATE LAW; the terminal
  appears where the terminal IS the subject (E03/E05/E06).
- FACTS THAT MUST APPEAR EXACTLY where the episode calls for them:
  * contact: hr@humanitarians.ai
  * run command: caffeinate claude --dangerously-skip-permissions
  * setup: cp .env.example .env  ·  ./setup --install  ·  ./art keys
  * the generic prompt seed (E06): "claude code prompt to create claude
    explainer liam voice for every one of these video ideas — it should create
    animation visualizations and infographics"
  * the per-Fellow line (E06): "Liam, for [your name] and Humanitarians AI"
  * publish target (E11): youtube.com/@humanitariansai, "Fellows Research"
    playlist, via Gaurav's script (from hr@humanitarians.ai)
  Invent no other commands, flags, or numbers. If a detail isn't in the map or
  the existing builds, keep it qualitative.

EPISODE CONTRACT (apply to each E01–E12 from the map)

- Slug + folder: hai-brutalist-<slug> from the map → build into
  youtube/hai-brutalist-<slug>/. (Do NOT overwrite the existing
  what-is-brutalist/, installs/, posting-to-youtube/ folders — the HAI
  episodes are new folders.)
- Beat 0 — ClaudeComposerAsk cold open: Liam states the episode's thesis as a
  hook + "Liam, in for Bear."
- Middle — teach the one step, centerpiece animated per the map's capsule.
- Closing per your-turn: VERDICT recap card (the thesis, one line) → Your Turn
  composer beat (the HANDOFF prompt = the next action; e.g. E03 → the install
  command, E06 → the generic prompt seed, E11 → "publish this to Fellows
  Research") read in full by Liam → title re-read on the @HumanitariansAI card.
- E12 uses the Student/Fellow profile mode (see SKILL.md) as its subject —
  teach HOW to profile a Fellow, with a short worked mini-example.
- Cross-link: each episode's narration names the next one in a closing line so
  the series reads as a course (E00, the existing
  claude-liam-hai-how-to-explainer-videos, is the trailer/index — reference it
  in E01's open).

THE LOOP

1. Parse the map's E01–E12 into an ordered work list. Write a ledger at
   youtube/HAI-BRUTALIST-SERIES-BATCH-LOG.md: episode | slug | status
   (pending/built/failed/skipped) | mp4 path | notes.
2. For each episode in order, SKIP if
   youtube/hai-brutalist-<slug>/mp4/hai-brutalist-<slug>.mp4 already exists and
   probes valid (idempotent/resumable). Else build end to end into
   youtube/hai-brutalist-<slug>/:
     - beat_sheet.json (persona Liam, folderLabel @HumanitariansAI)
     - mp4/hai-brutalist-<slug>.mp4 (1920x1080)
     - SOURCES.md — every exact command/email/URL/playlist verbatim for QC.
3. Verify each mp4 exists and plays (probe duration + frame count); run the
   VISUAL QC LAW frame pass. Mark built, update the ledger, MOVE ON.
4. A beat that won't render after two attempts → slate card naming it + log;
   never silently drop a beat, never let one bad beat stop the episode.
5. A whole episode that fails after a genuine attempt → mark "failed" with the
   reason and CONTINUE — one failure must not halt the series.
6. Stop only when every episode is built/failed/skipped. Print the final ledger
   and, per built episode, its beat → timestamp table.

Begin with E01 and work through E12. Do not ask for confirmation between
episodes — run the whole series, then report.
```
