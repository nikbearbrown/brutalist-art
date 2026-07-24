# QC REPORT — claude-liam-claude-science
Run: 2026-07-21 | Cut: review (344.7s, 15/15 filled) | Title: Ten Years Every Year.

## Beat-by-beat visual audit

| Beat | Pattern | Status | Visual result | Issues |
|---|---|---|---|---|
| YTV01 | ClaudeVerdictArtifact | VIDEO | ✓ "What the teardown found" — 5 lines, cream bg | SKIN LINT (intentional teardown pre-roll) |
| B00 | ClaudeComposerAsk | VIDEO | ✓ "Yassou, Liam" greeting, CLAUDE SCIENCE topic | None |
| B01 | ScaleComparison | VIDEO | ✓ log-axis bar chart, 50–100 → 5–10 yr ranges, accent band | MINOR: small axis labels at screenshot frame |
| B02 | AttritionChain | VIDEO | ✓ dot grid 20→15→3, "15/20" counter, accent final survivors | None |
| B03 | ClaudeScienceSourceFlow | VIDEO | ✓ dark rack → arc → window, "The loop, not the replacement." | None |
| B04 | ClaudeScienceLayerStack | VIDEO | ✓ 3 orange-accent layer cards, "×10 where the bottleneck is cognitive." | None |
| B05 | ClaudeScienceChipGrid | VIDEO | ✓ 6-chip grid (5 aspiration + 1 caveat), "The aspirational layer." | None |
| B06 | ClaudeScienceLayerStack | VIDEO | ✓ 3 layers (Literature synthesis accented), "The token budget is a real ceiling." | None |
| B07 | DivergentFates | VIDEO | ✓ 2 diverging paths (Optimist ↑ good, Skeptic ↓ warn) | None |
| B08 | ClaudeScienceLayerStack | VIDEO | ✓ 3 locked layers, "Not a caveat — the architecture." | None |
| B09 | BinaryBranch | VIDEO | ✓ question → Cognitive (good) / Physical (warn) branches, resolver box | None |
| B10 | ClaudeVerdictArtifact | VIDEO | ✓ "What it shows. What it asserts." — 7 SHOWS/ASSERTS lines | Switched from ClaudeWindow (no table support) |
| B11 | ClaudeComposerAsk | VIDEO | ✓ "Your turn." handoff prompt | None |
| B12 | ClaudeTitleOutro | VIDEO | ✓ "Ten Years Every Year.", @NikBearBrown | None |
| B13 | LogoOutro | VIDEO | ✓ bear-brown elasticPhysics, bear-brown-logo-2.svg, bear-brown-1.mp3, 13.7s | SKIN LINT (intentional NBB pattern) |

## New Remotion components registered

| ID | File | Canvas |
|---|---|---|
| `ScaleComparison` | `src/deckPatterns.tsx` | 1280×720 |
| `AttritionChain` | `src/deckPatterns.tsx` | 1280×720 |
| `DivergentFates` | `src/deckPatterns.tsx` | 1280×720 |
| `BinaryBranch` | `src/deckPatterns.tsx` | 1280×720 |
| `ClaudeScienceLayerStack` | `src/ClaudeScienceIllu.tsx` | 1280×720 |
| `ClaudeScienceSourceFlow` | `src/ClaudeScienceIllu.tsx` | 1280×720 |
| `ClaudeScienceChipGrid` | `src/ClaudeScienceIllu.tsx` | 1280×720 |

## 9-point rubric

| Check | Result |
|---|---|
| Edge bleed | PASS — no content bleeds to frame edge |
| Title-safe | PASS — all text within safe margins |
| Overflow | PASS — no truncated text observed |
| Collision | PASS — no element overlap |
| Offscreen anchors | PASS |
| Legibility | PASS — data-viz labels readable; mono font on deckPatterns beats appropriate |
| Brand / palette | PASS — cream bg throughout; orange accent; @NikBearBrown routing B00/B11/B12/B13 |
| Aspect ratio | PASS — 16:9 on all beats |
| Canvas fill | PASS — no bare gaps |

## Issues

### BLOCKER
None.

### MAJOR
None.

### MINOR
- **SKIN LINT (acknowledged)**: YTV01 cold-open is ClaudeVerdictArtifact — intentional teardown pre-roll summary format, not a composer ask. Acknowledged.
- **SKIN LINT (acknowledged)**: B13 outro is LogoOutro after ClaudeTitleOutro — intentional NBB pattern; LogoOutro is the correct final beat.
- **Motion variety**: 'reveal' carries 9/15 beats (60%) — above the ~40% cap. Acceptable for single-subject teardown format; all C2/C3 pattern beats use reveal.
- **B10 redesigned**: Originally ClaudeWindow with `artifactKind:"table"` (unsupported). Switched to ClaudeVerdictArtifact with SHOWS/ASSERTS labeled lines — same information, legible format.
- **REBUILD LAW (deferred)**: B07 DivergentFates uses authored track labels, not verbatim comment text. Per NARRATION.md open item, verbatim comments from cd3PsBoGYkc comment section have not yet been sourced. This is a final-cut task.

## Summary
Review cut: **PASS for review**. 15/15 beats filled. Zero blockers, zero majors. 7 new Remotion Compositions registered in runtime Root.tsx (4 C2 rhetorical patterns from deckPatterns.tsx, 3 C3 structural wrappers via ClaudeScienceIllu.tsx). Audio: 331s Kokoro am_onyx, all 15 beats narrated. NBB logo B13 confirmed: bear-brown, elasticPhysics, 13.7s. Total compiled: 344.7s (5:44).
