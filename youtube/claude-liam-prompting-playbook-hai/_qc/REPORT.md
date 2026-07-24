# QC REPORT — claude-liam-prompting-playbook-hai
Run: 2026-07-21 | Cut: review (280.3s, 13/13 filled) | Variant of: claude-liam-prompting-playbook

## Beat-by-beat visual audit

| Beat | Pattern | Status | Visual result | Issues |
|---|---|---|---|---|
| YTV01 | ClaudeVerdictArtifact | VIDEO | ✓ "Four moves, one discipline" — 4 lines, cream bg, terracotta asterisk | None |
| B00 | ClaudeComposerAsk | VIDEO | ✓ "Merhaba, Liam" greeting, @HumanitariansAI folderLabel, "loading the playbook…" | None |
| B01 | B01_TwoScenarios (Manim) | MANIM | ✓ copied from source — two-lane diagram, clean | None |
| B02 | B02_EvalSuite (Manim) | MANIM | ✓ copied from source — three-column eval grid | None |
| B03 | ClaudeCodeBeat | VIDEO | ✓ "Prompt hygiene — the diff", BEFORE/AFTER XML, stop_sequences — slow-mo 2.7× | MINOR |
| B04 | B04_PatchDebt (Manim) | MANIM | ✓ copied from source — patch debt timeline | None |
| B05 | ClaudeCodeBeat | VIDEO | ✓ "Instructions vs. tools", both code blocks visible — slow-mo 2.8× | MINOR |
| B06 | ClaudeWindow | VIDEO | ✓ artifact view, one-sided/two-sided cost function — slow-mo 2.1× | MINOR |
| B07 | ClaudeWindow | VIDEO | ✓ "Model × Prompt × Harness", 4 approach rows — slow-mo 1.9× | MINOR |
| B08 | B08_GenEvalRepair (Manim) | MANIM | ✓ copied from source — Gen→Eval→Repair loop | None |
| B09 | ClaudeComposerAsk | VIDEO | ✓ "Your turn." greeting, @HumanitariansAI folderLabel, eval-suite prompt | None |
| B10 | ClaudeTitleOutro | VIDEO | ✓ "The Prompting Playbook", @HumanitariansAI handle, "Debug the prompt like code." | None |
| B11 | LogoOutro | VIDEO | ✓ H-HAI logo kinetic grid, cream bg (#F3EBDD), @HumanitariansAI handle | Slow-mo 3.5× — MINOR |

## 9-point rubric

| Check | Result |
|---|---|
| Edge bleed | PASS — no content bleeds to frame edge |
| Title-safe | PASS — all text within safe margins |
| Overflow | PASS — no truncated text observed |
| Collision | PASS — no element overlap |
| Offscreen anchors | PASS |
| Legibility | PASS — code beats readable at slow-mo, Manim clean |
| Brand / palette | PASS — cream #FAF9F5 / #F3EBDD on logo, ink #3D3929, terracotta accent throughout |
| Aspect ratio | PASS — 16:9 on all beats |
| Canvas fill | PASS — no bare gaps |

## Issues

### BLOCKER
None.

### MAJOR
None.

### MINOR
- **B03, B05, B06, B07 slow-motion**: Remotion clips were 10–12s; HAI narrations are 25–28s; compile stretches 2–2.8×. Content is readable — same issue as source reel. Fix on final compile pass by re-rendering with explicit `durationInFrames` matched to HAI audio durations.
- **B11 slow-motion**: LogoOutro renders 4s, beat is 14s → 3.5× stretch. Expected; fix by generating a longer logo clip or trimming the silent tail.

## Summary
Review cut: **PASS for review**. Zero blockers, zero majors. HAI channel routing (Merhaba/Your turn/B10 @HumanitariansAI/B11 H-HAI logo grid) all rendering correctly. 4 MINOR slow-mo issues on Remotion beats — same pattern as source reel; fix on final compile pass.
