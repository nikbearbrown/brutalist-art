# BUILD-PROMPT — the Brutalist showcase meta-series

Paste-ready orchestration for Claude Code on the Mac, run from `books/`.
Everything here is free (Kokoro + local renders) — no GATE P spend, but the
**narration gate is real**: never generate audio for a mark whose
`episodes.json` the human has not approved.

## What this series is

Every logo showcase comp (6 marks × 2 aspects) already exists with Liam
narration per technique. This series adds the ai-explainer bookends WITHOUT
touching those comps, via `ShowcaseWrap` (see
`runtime/remotion/src/ShowcaseWrap.tsx`):

- **16:9 series** per mark (the browsable cut — viewers jump straight to the
  group they care about): each logical group of 4 techniques becomes its own
  episode — intro (`ClaudeComposerAsk`; episode 1 keeps the comp's own
  composer cold open) → the 4 techniques → RECAP (ClaudeVerdictArtifact,
  per-group verdict lines) → YOUR TURN (prompt read verbatim + discussed,
  HANDOFF LAW) → TITLE re-read (ClaudeTitleOutro). Cut folders: `ep0N-16x9`.
- **9:16 series** per mark: the same groups as ~1-minute Shorts (`ep0N`) —
  intro + 4 techniques + Your Turn + title card; no recap beat, Shorts stay
  tight.
- **16:9 single long cut** (`full-16x9`): OPT-IN via `"build_full_16x9": true`
  in episodes.json — off by default now that the series is the primary cut.

Driver: `runtime/scripts/showcase_episodes.py` (scaffold → audio → props →
render → mux). Config per mark: `youtube/showcase-series/<mark>/episodes.json`.

## Pilot first: musinique-logo-2 (config already authored + approved path)

```bash
cd brutalist-art
# 1. mini beat sheets for the bookend narration
python3 runtime/scripts/showcase_episodes.py scaffold musinique-logo-2
# 2. Kokoro audio (free) for every cut folder scaffold printed
for d in youtube/showcase-series/musinique-logo-2/*/; do
  python3 runtime/scripts/generate_audio_kokoro.py "$d" --no-gate
done
# --no-gate: GATE P's PEDAGOGY.md check targets teaching reels; these cuts are
# 2-3 line bookend clips whose narration gate is the episodes.json approval.
# 3. measure audio -> per-cut props.json + the exact render commands
python3 runtime/scripts/showcase_episodes.py props musinique-logo-2
# 4. run each printed `npx remotion render ... --concurrency=1` FOREGROUND,
#    one at a time (standing rule #3: no backgrounding, no ps-polling)
# 5. episode audio assembly + final mux
python3 runtime/scripts/showcase_episodes.py mux musinique-logo-2
```

**QC (VISUAL QC LAW, mandatory):** for every final mp4, sample frames
(`ffmpeg -i <mp4> -vf fps=2 _qc/frames/%05d.png`), READ the PNGs, audit the
9-point rubric — especially: body window starts exactly on a technique label
(no half-beat slivers from a wrong offset), bookend audio ends before the
next segment starts, episode 1's inherited comp intro reads correctly as a
cold open, and the 16:9 cut drops the comp's OLD handoff/title completely
(no double ending). Log defects in `_qc/REPORT.md`, fix, re-render.

Known first-run risk, checked deliberately: several marks share a timing json
filename between aspects in `showcase_episodes.py MARKS` — if a body window
lands mid-technique, the comp's actual `import TIMING from './…'` line names
the right file; fix the table and re-run `props`.

**STOP after the pilot.** Show Bear one 16:9 episode (`ep0N-16x9`) and one
Short (`ep0N`). Only after approval, continue to the batch.

## Batch: the other five marks

For each of `musinique-logo`, `bear-brown-logo`, `bear-brown-initials`,
`h-logo`, `hai-wordmark`:

1. Author `youtube/showcase-series/<mark>/episodes.json` by following the
   musinique-logo-2 exemplar EXACTLY in structure, but with mark-specific
   narration: pull each mark's technique names from its source reel's
   `beat_sheet.json` (B01–B20 first sentences), group 4 per episode in comp
   order (hai-wordmark has 19 → 4/4/4/4/3), write fresh Teardown-register
   intro/your-turn lines per episode — never copy the pilot's lines with the
   mark name swapped. Rotate the world-language hellos (don't repeat within
   a mark; Wagwan stays Bear's — Liam never takes it). Every your_turn
   narration READS the prompt verbatim then discusses it in one line
   (HANDOFF LAW). Series titles: `<Mark>, In Motion — Part N.` with the
   right handle (`@HumanitariansAI` for hai-wordmark; `@Musinique` optional
   for the musinique marks if Bear says so — default `@NikBearBrown`).
2. **GATE: present the episodes.json narration table to Bear. Do not
   generate audio until approved.**
3. Run the same scaffold → audio → props → render → mux → QC loop as the
   pilot.

## Ledger

Log every command + defect + fix in `youtube/showcase-series/BUILD-LOG.md`
(append-only). `MISSING:` lines per the report-and-add contract if anything
isn't in the folder. Never publish — uploads are a separate human-triggered
step.
