# SHOPPING.md — Gate D2 manifest

Written: 2026-07-22 (after audio lock — timings sourced from mp3/timings.json)

## Pantry status: NOTHING TO SOURCE

This reel has **zero VOX beats** (no `shot.type: STILL` or `COMPOSITE` with
`shot.source: archive` or `ai`). Every beat is a **REMOTION** scene built
from registered Remotion components.

No pantry stills are needed. The machine has handled every slot.

## Locked beat durations (from mp3/timings.json)

| Beat | Locked duration | Slot type |
|---|---|---|
| B00 | 18.35 s | REMOTION — ClaudeComposerAsk |
| B01 | 26.41 s | REMOTION — SkillTeardownAnatomy |
| B02 | 33.00 s | REMOTION — SkillTeardownPipeline |
| B03 | 19.61 s | REMOTION — ClaudeComposerAsk |
| B04 | 23.30 s | REMOTION — ClaudeCodeBeat |
| B05 | 28.25 s | REMOTION — SkillTeardownMechanism |
| B06 | 29.03 s | REMOTION — SkillTeardownMechanism |
| B07 | 28.03 s | REMOTION — SkillTeardownMechanism |
| BVDT | 30.72 s | REMOTION — ClaudeVerdictArtifact |
| BHTF | 28.97 s | REMOTION — ClaudeComposerAsk |
| BOUT | 2.88 s | REMOTION — ClaudeTitleOutro |
| **Total** | **268.6 s (4:29)** | |

## Skin lint notes (intentional — log for the record)

The pipeline flags one skin warning:

- **B03**: `ClaudeComposerAsk` has an empty `sparkLine` prop (no serif kicker set).
  The `runningText` drives the action; the sparkLine slot is intentionally blank on
  this self-demo beat. SPARK-LINE LAW wants a short cue here — the beat sheet metadata
  pre-logs this in `build.skin_warnings`. Not a BLOCKER; visual is clean.

## Gate D2 status

**PASSED** — pantry is complete by design; zero entries unresolved.
The review cut may proceed once you have watched the previz.
