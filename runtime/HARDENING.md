# Video pipeline hardening — enforced rules (deep-explainer + shared runtime)

Applied 2026-07-21. These turn the prose "laws" into gates that actually run in
`scripts/run.sh`. Env: `ART_QC=1` (gates on), `ART_STRICT=1` (BLOCKER+MAJOR stop
the build; `ART_STRICT=0` = legacy warn-and-slot).

| # | Rule | Enforced by | Status |
|---|------|-------------|--------|
| 1 | Gates block, don't warn | `run.sh` Gate A/W/B strict + Gate L/V | **live** |
| 2 | Frame-level visual QC on every beat | `qc/final_frame_check.py` (Gate V) | **live, tested** |
| 3 | No single-sentence Remotion slide | `qc/beat_lint.py` (Gate L) | **live, tested** |
| 4 | Two placeholder types (STILL / VOX-ANIM) | `beat_lint.py` + `compile.py` slate | **live** |
| 5 | Root-cause layout: wrap + fill | `layout.ts` `fitToSafe` + Gate V | **driver added; scenes need the wrap** |
| 6 | Factcheck = verification | Gate F (paperwork) — verification step | **paperwork gate only (unchanged)** |
| 7 | Fixed per-channel branding | `beat_lint.py` + `qc/brand_labels.json` | **live, tested** |
| 8 | Canvas fill, no negative space | Gate V underfill + `fitToSafe` | **live, tested** |

## What runs, and when (`scripts/run.sh`)
1. **Gate F** — paperwork exists (unchanged).
2. **Gate L** (new) — `beat_lint.py`: flags single-sentence-Remotion beats, stray
   text cards, and branding mismatches. Blocks under `ART_STRICT`.
3. **Gate A / W / B** — Manim static / WCAG / layout. Gate B no longer
   "slots anyway" on a warning under `ART_STRICT` — it blocks.
4. compile → **Gate V** (new) — `final_frame_check.py` samples the compiled mp4
   and audits every beat: edge-bleed/clipping (BLOCKER), canvas underfill and
   low contrast (MAJOR). Writes `_qc/REPORT.md` + `_qc/contact_sheet.png`.
   Blocks under `ART_STRICT`; soft-skips if Pillow/numpy/ffmpeg missing.

## Verified on real footage
- `beat_lint` on the live epistemology sheet → correctly flagged **B03, B36**
  (remotion beats that fell back to `SlateCard`) and the branding kicker.
- `final_frame_check` swept the finished epistemology film (41 frames) →
  **3 BLOCKER + 19 MAJOR** (clipping + underfill). The defects were real and
  pervasive; the gate catches them.

## The two placeholder types (rules 3–4)
- **① STILL** — `lane:vox`, `type:STILL|COMPOSITE`. "Drop an image / gen-AI clip
  in the pantry." Ken-Burns / cutout. (Unchanged; your B02/B22 slates.)
- **② VOX-ANIM** — mark a beat `shot.placeholder:"vox-anim"` (or
  `shot.scene_type:"vox-anim"`). `compile.py` renders a distinct request card:
  *"VOX-ANIM · YOU → pantry media, animated vox-style with Remotion."* This is
  where every would-be single-sentence Remotion beat goes.

## The one remaining hand-step (rule 5 scene wrap)
`layout.ts` now exports `fitToSafe(contentW, contentH)` — the positive fill
driver. Gate V *catches* underfill; `fitToSafe` *prevents* it, but each Remotion
scene has to wrap its content group:

```tsx
import { fitToSafe, safeCenterX, safeCenterY } from '../tokens/layout';
const s = fitToSafe(measuredW, measuredH);
<div style={{ transform: `scale(${s})`, transformOrigin: 'center' }}>…</div>
```

This is the only change that needs a local render to tune per scene — Gate V
tells you which scenes still fail, so you can apply the wrap where it flags.

## Branding table — edit freely
`qc/brand_labels.json` is data, not code. Change a kicker, fix a handle, or add
a channel there; `beat_lint` enforces it. Current:
claude-liam/claude → "Computational Skepticism" · @NikBearBrown ·
medhavy → "Medhavy" · @MedhavyAI · hai → "Irreducibly Human" · @HumanitariansAI ·
musinique → "Tools for Indie Artists" · @Musinique.

## Not changed (be honest)
Rule 6 factcheck is still the paperwork-existence Gate F — turning it into real
claim-vs-source verification is the next piece and was left out here to keep
this change reviewable.
