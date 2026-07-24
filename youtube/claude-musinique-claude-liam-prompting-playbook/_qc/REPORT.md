# QC REPORT — claude-musinique-claude-liam-prompting-playbook
Run: 2026-07-21 | Cut: review (314.6s, 13/13 filled) | Variant of: claude-liam-prompting-playbook

## Beat-by-beat visual audit

| Beat | Pattern | Status | Visual result | Issues |
|---|---|---|---|---|
| YTV01 | ClaudeVerdictArtifact | VIDEO | ✓ "Four moves, one discipline" — 4 lines, cream bg | None |
| B00 | ClaudeComposerAsk | VIDEO | ✓ @Musinique greeting, @Musinique folderLabel | None |
| B01 | B01_TwoScenarios (Manim) | MANIM | ✓ two-lane diagram, clean | None |
| B02 | B02_EvalSuite (Manim) | MANIM | ✓ three-column eval grid | None |
| B03 | ClaudeCodeBeat | VIDEO | ✓ "Prompt hygiene — the diff", BEFORE/AFTER XML | MINOR slow-mo 3.1× |
| B04 | B04_PatchDebt (Manim) | MANIM | ✓ patch debt timeline | None |
| B05 | ClaudeCodeBeat | VIDEO | ✓ "Instructions vs. tools" code blocks | MINOR slow-mo 3.1× |
| B06 | ClaudeWindow | VIDEO | ✓ cost function artifact view | MINOR slow-mo 2.6× |
| B07 | ClaudeWindow | VIDEO | ✓ "Model × Prompt × Harness" rows | MINOR slow-mo 2.2× |
| B08 | B08_GenEvalRepair (Manim) | MANIM | ✓ Gen→Eval→Repair loop | None |
| B09 | ClaudeComposerAsk | VIDEO | ✓ "Your turn." greeting, @Musinique folderLabel | None |
| B10 | ClaudeTitleOutro | VIDEO | ✓ "The Prompting Playbook", @Musinique handle | None |
| B11 | LogoOutro | VIDEO | ✓ Musinique M-mark logo, trailEcho, black bg | None |

## 9-point rubric

| Check | Result |
|---|---|
| Edge bleed | PASS — no content bleeds to frame edge |
| Title-safe | PASS — all text within safe margins |
| Overflow | PASS — no truncated text observed |
| Collision | PASS — no element overlap |
| Offscreen anchors | PASS |
| Legibility | PASS — code beats readable at slow-mo, Manim clean |
| Brand / palette | PASS — cream bg throughout, @Musinique routing on B00/B09/B10/B11 |
| Aspect ratio | PASS — 16:9 on all beats |
| Canvas fill | PASS — no bare gaps |

## Issues

### BLOCKER
None.

### MAJOR
None.

### MINOR
- **B03, B05 slow-motion**: Remotion clips are 10s; am_puck narrations are 31s+; compile stretches ~3.1×. Same issue as source reel. Fix on final compile by re-rendering with `durationInFrames` matched to am_puck durations.
- **B06, B07 slow-motion**: 12s clips stretched 2.2–2.6× to match 26–31s narrations. Readable but not ideal.

## Summary
Review cut: **PASS for review**. Zero blockers, zero majors. Voice is am_puck throughout. @Musinique routing (B00/B09/B10/B11) all rendering correctly. Musinique logo M-mark (trailEcho, musinique-logo-2.svg, musinique-1.mp3, 12.3s) looks clean. 4 MINOR slow-mo beats — same pattern as source reel; fix on final compile pass.
