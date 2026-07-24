# QC REPORT — claude-liam-prompting-playbook
Run: 2026-07-20 | Cut: review (334.6s, 9/13 filled)

## Beat-by-beat visual audit

| Beat | Pattern | Status | Visual result | Issues |
|---|---|---|---|---|
| YTV01 | ClaudeVerdictArtifact | VIDEO | ✓ Cream bg, terracotta asterisk, "Four moves, one discipline" — all 4 lines rendering, clean numbered list | None |
| B00 | ClaudeComposerAsk | VIDEO | ✓ "Bonjour, Liam" greeting, full prompt text in composer, @NikBearBrown chip, "loading the playbook…" | None |
| B01 | SLATE | SLATE | Pipeline slate: "B01 / PIPELINE → render animated_graphics.py scene B01_*" | Awaiting Manim |
| B02 | SLATE | SLATE | Pipeline slate: "B02 / PIPELINE → render animated_graphics.py scene B02_*" | Awaiting Manim |
| B03 | ClaudeCodeBeat | VIDEO | ✓ macOS code window, BEFORE/AFTER XML diff, stop_sequences harness line, spark: "If you can't tell policy from guidelines, neither can the model." | Slow-mo 3.3× (render short) — MINOR |
| B04 | SLATE | SLATE | Pipeline slate: "B04 / PIPELINE → render animated_graphics.py scene B04_*" | Awaiting Manim |
| B05 | ClaudeCodeBeat | VIDEO | ✓ "Instructions vs. tools", both code blocks visible, spark: "Instructions don't add capability. Tools do." | Slow-mo 3.2× — MINOR |
| B06 | ClaudeWindow | VIDEO | ✓ Artifact view, "One-sided vs. two-sided cost function", 5 lines, spark: "An incomplete cost function produces the wrong optimization." | None |
| B07 | ClaudeWindow | VIDEO | ✓ "Model × Prompt × Harness", 4 approach rows + lesson row, spark clear | None |
| B08 | SLATE | SLATE | Pipeline slate: "B08 / PIPELINE → render animated_graphics.py scene B08_*" | Awaiting Manim |
| B09 | ClaudeComposerAsk | VIDEO | ✓ "Your turn." greeting, full eval-suite paste prompt, @NikBearBrown chip, "paste this into Claude…" | None |
| B10 | ClaudeTitleOutro | VIDEO | ✓ Title "The Prompting Playbook", @NikBearBrown handle, subline "Debug the prompt like code." | None |
| B11 | LogoOutro | VIDEO | ✓ NBB kinetic grid logo, @NikBearBrown handle, cream/ink palette | Slow-mo 3.5× — MINOR |

## 9-point rubric

| Check | Result |
|---|---|
| Edge bleed | PASS — no content bleeds to frame edge |
| Title-safe | PASS — all text within safe margins |
| Overflow | PASS — no truncated text observed |
| Collision | PASS — no element overlap |
| Offscreen anchors | PASS |
| Legibility | PASS — code beats readable, artifact lines clear |
| Brand / palette | PASS — cream #FAF9F5, ink #3D3929, terracotta accent throughout |
| Aspect ratio | PASS — 16:9 on all beats |
| Canvas fill | PASS — no bare grey/black gaps |

## Issues

### BLOCKER
None.

### MAJOR
None.

### MINOR
- **B03, B05, B11 slow-motion**: Remotion renders are 10s/4s; compile stretches 3–3.5×. Frames are fully readable and content is correct — no blurring observed at this render quality. Will re-render with explicit `durationInFrames` once Manim slates are filled and final compile is run. Not blocking review cut.

### Slates pending Manim (expected)
- B01: `B01_TwoScenarios` — two-scenario lane diagram
- B02: `B02_EvalSuite` — three-column eval type diagram
- B04: `B04_PatchDebt` — instruction lifecycle / patch debt timeline
- B08: `B08_GenEvalRepair` — generate-evaluate-repair loop diagram

## Summary
Review cut: **PASS for review**. Zero blockers, zero majors. 4 Manim slates awaiting human-supplied media or Manim scene authoring. 3 minor slow-mo issues on Remotion code/logo beats — fix on final compile pass after Manim fill.
