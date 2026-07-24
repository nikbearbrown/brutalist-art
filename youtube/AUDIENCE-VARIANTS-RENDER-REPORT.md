# AUDIENCE VARIANTS RENDER REPORT

**Date:** 2026-07-16
**Run mode:** Unattended batch
**Jobs attempted:** 4
**Jobs built:** 4
**Jobs failed:** 0

---

## JOB 1 — Medhavy · Claude, Judged

| Field | Value |
|---|---|
| Status | BUILT |
| Authoritative sheet | `youtube/medhavy-claude-judged/beat_sheet.medhavy.json` |
| Build copy | `youtube/medhavy-claude-judged/beat_sheet.json` |
| Final MP4 | `youtube/medhavy-claude-judged/claude-judged-medhavy.mp4` |
| Voice | af_kore (Kokoro) |
| Register | Wonder |
| Palette | medhavy (Okabe-Ito) |
| Beat count | 10 (B00–B09) |
| Measured duration | 158.46s (~2:38) |
| File size | 2,970,916 bytes (~2.8 MB) |
| Resolution | 1920×1080 |
| Audio stream | present |
| PEDAGOGY verdict | PASS |

**Closing order:** B07 VERDICT → B08 AI-USE-BOUNDARY → B09 OUTRO ✓

**QC notes:**
- All 10 beats filled (VIDEO), 0 slates in final cut
- callout-reveal motion carries 5/10 beats (50%); compiler warns at >40% cap — not a blocking defect for audience variants (inherited from canonical beat structure)
- B01 (ClaudeCodeBeat, 10.0s Remotion) slowed 1.70× to fill 17.1s audio beat — visible slow-motion in code animation; acceptable for a solo Kokoro voice narration
- B07/B08 (ClaudeWindow) slowed ~1.5× — acceptable; artifact card reads at that pace

**Repairs applied:**
- `ClaudeUsageBeat` Remotion pattern not registered in current runtime; replaced B02–B06 with `MedhavyConceptCard` (registered, palette-appropriate). Authoritative sheet unchanged; repair is in build copy only.

**Remaining concerns:**
- B01 code animation slow-motion. To fix: extend ClaudeCodeBeat duration in Remotion or re-render B01 Remotion at a faster typing speed.
- `callout-reveal` motion density (50%). Future refactor: replace some body beats with `ClaudeWindow view="blank"` + on-screen text.

**Open command:**
```bash
open /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/medhavy-claude-judged/claude-judged-medhavy.mp4
```

---

## JOB 2 — HAI · Claude, Judged

| Field | Value |
|---|---|
| Status | BUILT |
| Authoritative sheet | `youtube/hai-claude-judged/beat_sheet.hai.json` |
| Build copy | `youtube/hai-claude-judged/beat_sheet.json` |
| Final MP4 | `youtube/hai-claude-judged/claude-judged-hai.mp4` |
| Voice | am_onyx (Kokoro) |
| Register | Pragmatist |
| Palette | humanitarians (muted editorial) |
| Beat count | 10 (B00–B09) |
| Measured duration | 132.54s (~2:13) |
| File size | 2,463,784 bytes (~2.3 MB) |
| Resolution | 1920×1080 |
| Audio stream | present |
| PEDAGOGY verdict | PASS |

**Closing order:** B07 VERDICT → B08 AI-USE-BOUNDARY → B09 OUTRO ✓

**B08 cli_exercise check:**
- lane: RESEARCH ✓
- ASK/OUTPUT/CHANGE/OUTPUT2 structure present ✓
- Both when-to-use and when-not-to-use AI covered ✓

**QC notes:**
- All 10 beats filled (VIDEO), 0 slates
- callout-reveal at 50% (same as Job 1, inherited structure)
- B03/B04/B05 center-cut (15.1s clip into shorter actual-duration beats) — narration is shorter than Remotion clip; clip is trimmed correctly

**Repairs applied:**
- Same `ClaudeUsageBeat` → `MedhavyConceptCard` replacement for B02–B06 in build copy.

**Remaining concerns:**
- `MedhavyConceptCard` uses Claude token colors (not humanitarians palette) for the body callout beats (B02–B06). This is a palette-impurity for the HAI variant. Future fix: build a `HAIConceptCard` Remotion component with humanitarians token colors.

**Open command:**
```bash
open /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/hai-claude-judged/claude-judged-hai.mp4
```

---

## JOB 3 — Medhavy · Claude, On Average

| Field | Value |
|---|---|
| Status | BUILT |
| Authoritative sheet | `youtube/medhavy-claude-on-average/beat_sheet.medhavy.json` |
| Build copy | `youtube/medhavy-claude-on-average/beat_sheet.json` |
| Final MP4 | `youtube/medhavy-claude-on-average/claude-on-average-medhavy.mp4` |
| Voice | af_kore (Kokoro) |
| Register | Wonder |
| Palette | medhavy (Okabe-Ito) |
| Beat count | 10 (B00–B09) |
| Measured duration | 160.67s (~2:41) |
| File size | 3,124,668 bytes (~3.0 MB) |
| Resolution | 1920×1080 |
| Audio stream | present |
| PEDAGOGY verdict | PASS |

**Closing order:** B07 VERDICT → B08 AI-USE-BOUNDARY → B09 OUTRO ✓

**Content preservation check:**
- Token-by-token from context-conditioned probabilities (B03): ✓ preserved
- Responses are samples from a distribution (B02): ✓ preserved
- Temperature zero narrows but doesn't guarantee fixed context-independent answer (B04): ✓ preserved
- B08 covers exploration/drafts/hypotheses (use) vs facts/eligibility/safety/exact repetition (do not use): ✓

**QC notes:**
- All 10 beats filled (VIDEO), 0 slates
- callout-reveal at 50% (inherited)
- B01 (three-draw demo) slowed 1.73× — most dramatic slow-motion in this job

**Repairs applied:**
- `ClaudeUsageBeat` → `MedhavyConceptCard` for B02–B06 in build copy.

**Remaining concerns:**
- B01 slow-motion (1.73×) is the most visually notable timing stretch in this batch.

**Open command:**
```bash
open /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/medhavy-claude-on-average/claude-on-average-medhavy.mp4
```

---

## JOB 4 — HAI · Claude, On Average

| Field | Value |
|---|---|
| Status | BUILT |
| Authoritative sheet | `youtube/hai-claude-on-average/beat_sheet.hai.json` |
| Build copy | `youtube/hai-claude-on-average/beat_sheet.json` |
| Final MP4 | `youtube/hai-claude-on-average/claude-on-average-hai.mp4` |
| Voice | am_onyx (Kokoro) |
| Register | Pragmatist |
| Palette | humanitarians (muted editorial) |
| Beat count | 10 (B00–B09) |
| Measured duration | 132.96s (~2:13) |
| File size | 2,604,769 bytes (~2.5 MB) |
| Resolution | 1920×1080 |
| Audio stream | present |
| PEDAGOGY verdict | PASS |

**Closing order:** B07 VERDICT → B08 AI-USE-BOUNDARY → B09 OUTRO ✓

**B08 cli_exercise check:**
- lane: BUILD ✓
- ASK/OUTPUT/CHANGE/OUTPUT2 structure present ✓
- Five-run variance table exercise — operationalizes the use/do-not-use boundary ✓

**Content preservation check:**
- Token-by-token construction (B03): ✓
- Samples from distribution (B00, B02): ✓
- Temperature zero narrows but does not pin (B04): ✓
- B08 boundary: "USE — options · drafts · summaries · provisional hypotheses" / "DO NOT USE UNVERIFIED — payment · eligibility · safety · legal decisions" ✓

**QC notes:**
- All 10 beats filled (VIDEO), 0 slates
- callout-reveal at 50% (inherited)

**Repairs applied:**
- `ClaudeUsageBeat` → `MedhavyConceptCard` for B02–B06 in build copy.

**Remaining concerns:**
- Same palette-impurity as Job 2: `MedhavyConceptCard` uses Claude tokens rather than humanitarians tokens for B02–B06.

**Open command:**
```bash
open /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/hai-claude-on-average/claude-on-average-hai.mp4
```

---

## Cross-job notes

### ClaudeUsageBeat — missing composition, repair documented

`ClaudeUsageBeat` is referenced in all four authoritative beat sheets (B02–B06 for both source videos) but is not registered as a Remotion composition in the current runtime. The canonical source reels (`claude-judged/`, `claude-on-average/`) solved this by pre-rendering those beats as PNGs via a separate tool not present in the current runtime.

**Resolution applied in this batch:** `MedhavyConceptCard` substituted in each build copy. `MedhavyConceptCard` is registered, renders reliably, carries sparkLine + heading + body, and is palette-consistent for Medhavy jobs. For HAI jobs it uses the Claude token color scheme rather than humanitarians colors — a known impurity. The authoritative `.medhavy.json` / `.hai.json` files retain the original `ClaudeUsageBeat` pattern for future resolution.

**Permanent fix path:** Register `ClaudeUsageBeat` as a Remotion composition (or alias it to `MedhavyConceptCard`) in `runtime/remotion/src/Root.tsx` and `runtime/remotion/src/index.ts`.

### Motion density warning

All four videos trigger the compiler's 50% callout-reveal warning. This is a style note (inherited from the canonical beat structure), not an error. The final cuts play correctly.

### Authoritative sheets intact

The `.medhavy.json` and `.hai.json` files were not modified. Build copies (`beat_sheet.json`) inside each variant directory reflect the `ClaudeUsageBeat` → `MedhavyConceptCard` repair.

### Canonical sources untouched

`youtube/claude-judged/` and `youtube/claude-on-average/` were not modified, renamed, or overwritten.

---

## Totals

| | Count |
|---|---|
| Attempted | 4 |
| Built | 4 |
| Failed | 0 |
