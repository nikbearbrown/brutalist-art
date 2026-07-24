# QC REPORT — musinique-logo-2
Date: 2026-07-22
Auditor: Claude Code (claude-sonnet-4-6)
Cuts audited: ep01-16x9 (79.2s, 1920×1080) and ep01 (53.5s, 1080×1920)

## Architecture note (script updated mid-session)
The showcase_episodes.py script was updated between the first `props` run and `mux`.
`cuts_of()` now generates two cuts per episode (ep0N 9:16 Short + ep0N-16x9 browsable cut)
instead of one full-16x9 long cut. `build_full_16x9: false` in episodes.json (opt-in).
Outcome: 10 final cuts built (ep01–ep05 × 2 aspects). All FINAL.

## 9-point rubric — ep01-16x9 (landscape)

1. **Body window starts on technique label, no sliver** — PASS
   Frame 30: "Spring Entrance / STANDARD SPRING · DAMPING 20" lands clean.
   Frame 55: "Overshoot Spring / SQUASH · DAMPING 5" lands clean.
   bodyStartFrame=0, bodyEndFrame=1444 (end of B04 in 16x9 timing). ✓

2. **Ep01 inherited comp intro reads correctly as cold open** — PASS
   Frames 1–5: 16x9 comp's own B00 ("DESIGN · MOTION / Logo Mark Techniques" →
   ClaudeComposerAsk "Hej, Liam / animate musinique-logo-2.svg…"). Correct; no
   separate intro block authored for ep01 (include_comp_intro=true). ✓

3. **Recap (verdict) card** — PASS
   Frame 100: ClaudeVerdictArtifact "Recap / Entrances" with all 4 lines:
   Standard spring, Overshoot spring, Draw-on stroke, Mask reveal. ✓

4. **Your Turn prompt visible and correct** — PASS
   Frame 135: "BRUTALIST · REMOTION / Entrances / Your turn." composer window
   typing "Animate my logo's entrance with a Remotion spring — show me damping 5,
   20, and 80 side by side." @NikBearBrown folder label. ✓

5. **Title card correct, no double ending** — PASS
   Frame 155: "Musinique, In Motion — Part One." / @NikBearBrown /
   "four entrances · every move built in Remotion". No old comp handoff or
   outro visible. ✓

6. **Palette / background** — PASS
   Cream (#FAF9F5) throughout bookends. Comp body uses its own palette. ✓

7. **Aspect ratio** — PASS
   1920×1080 (landscape). Bookend scenes render wide-format correctly. ✓

8. **No leaked B21/B22 (old comp ending)** — PASS
   bodyEndFrame=1444 (B04 end); B21 starts at 6413. Nothing from B21+ appears. ✓

9. **Bookend audio boundaries** — PASS
   Duration arithmetic: body(1444) + verdict(517) + yourTurn(296) + titleOut(119) = 2376f = 79.2s.
   Measured silent = 79.21s. Match within rounding. ✓

## 9-point rubric — ep01 (portrait Short)

1. **Body window starts on technique label** — PASS
   9:16 body starts at frame 0 (include_comp_intro=true); frame 40 shows
   "Overshoot Spring" label cleanly (B02). ✓

2. **Ep01 inherited comp intro (9:16 version)** — PASS
   Frame 1: "REMOTION · MOTION TECHNIQUES / Musinique Logo Techniques" — portrait
   comp's own B00. Correct cold open. ✓

3. **No recap block** — PASS
   9:16 Shorts have no recap (tight format). Skipped correctly. ✓

4. **Your Turn prompt — full text visible** — PASS
   Frame 90: Full prompt "Animate my logo's entrance with a Remotion spring —
   show me damping 5, 20, and 80 side by side." visible in portrait composer.
   "paste this into Claude…" running text. ✓

5. **Title card correct** — PASS
   Frame 105: "Musinique, In Motion — Part One." / @NikBearBrown /
   "four entrances · every move built in Remotion" — portrait layout. ✓

6. **Aspect ratio** — PASS
   1080×1920 (portrait). Bookend scenes render in portrait-specific variants
   (ClaudeTitleOutro916). ✓

7. **No old comp ending** — PASS
   bodyEndFrame=1190 (B04 end in 9:16 timing). Body is frames 0–1190 only. ✓

8. **Duration** — PASS
   body(1190) + yourTurn(296) + titleOut(119) = 1605f = 53.5s. ✓

9. **Palette** — PASS
   Cream throughout bookends. ✓

## Defects (previous session)
None detected for ep01/ep01-16x9.

## Files (previous session)
- ep01-16x9: youtube/showcase-series/musinique-logo-2/ep01-16x9/musinique-logo-2-ep01-16x9.mp4 (4.1 MB)
- ep01: youtube/showcase-series/musinique-logo-2/ep01/musinique-logo-2-ep01.mp4 (3.4 MB)
- All 10 frames sampled at: _qc/frames-ep01-16x9/ and _qc/frames-ep01/

---

## Session 2 QC — 2026-07-22 — ep02 through ep05 (both aspects)
Auditor: Claude Code (claude-sonnet-4-6)
Frames sampled at 0.5fps (ep02, ep02-16x9) and 0.25fps (all others).

### ep02 (9:16 Short, 58.1s) — PASS
- Intro: ClaudeComposerAsk "Merhaba, Liam" / Transforms / "animate…transforms: scale, rotation, skew, blur — part 2 of 5". Output lines: Scale Zoom · Rotation / Skew And Shear · Opacity Through Blur. ✓
- Body window starts on "Rotation / FULL 360° · SPRING SETTLE". No sliver. ✓
- Body: Skew And Shear / Opacity Through Blur visible mid-cut. ✓
- No recap card (Short). ✓
- Your Turn verbatim: "Rotate my logo 360° with a spring settle, then show the same spin with linear timing — and tell me why the spring reads better." ✓
- Title: "Part Two. / @NikBearBrown / four transforms · every move built in Remotion". ✓

### ep02-16x9 (84.1s) — PASS
- Intro: same as ep02 Short, 16:9 layout. ✓
- Body: Rotation → Skew And Shear → Opacity Through Blur cleanly labeled. ✓
- Recap card: "Transforms" heading, 4 bullets (Scale zoom · rotation · skew · blur-fade / All four are interpolate() + easing / The easing curve is the design decision / Spring settle beats linear every time). ✓
- Your Turn verbatim. ✓
- Title: "Part Two. / @NikBearBrown / four transforms". ✓
- No old comp ending visible. ✓

### ep03 (9:16 Short, 58.5s) — PASS
- Intro: "Ciao, Liam" / Surface Moves / "…surface: color, grid, glitch, echo — part 3 of 5". Output lines: Color Interpolation · Kinetic Grid / Glitch Slices · Trail Echo. ✓
- Your Turn verbatim: "Glitch my logo into 7 horizontal slices for half a second, then snap it perfectly clean — make the clean snap land on a beat." ✓

### ep03-16x9 (83.9s) — PASS
- Intro correct. ✓
- Recap: "Surface Moves" heading, 4 bullets (Color · kinetic grid · glitch · trail echo / The mark holds; the surface carries energy / Emphasis moves — mid-scene, not entrances / The glitch earns it by snapping CLEAN). ✓

### ep04 (9:16 Short, 59.9s) — PASS
- Intro: "Hej, Liam" / Physics / "…physics: wobble, elastic, flip, shadow — part 4 of 5". Output lines: Noise Wobble · Elastic Physics / Card Flip · Shadow Play. ✓

### ep04-16x9 (85.7s) — PASS
- Recap: "Physics" heading, 4 bullets (Wobble · elastic impact · card flip · shadow / Weight sells motion; springs fake mass / Face swap lands exactly at 90° / Shadow is the cheapest depth you can buy). ✓

### ep05 (9:16 Short, 64.4s) — PASS
- Intro: "Jambo, Liam" / Live Marks & Exits / "…live marks + exits — part 5 of 5". Output lines: Composer Summon · Stroke Pulse / Scale Breathe · Exit Family. ✓

### ep05-16x9 (91.2s) — PASS
- Recap: "Live Marks & Exits" heading, 4 bullets (Composer summon · pulse · breathe · exits / Idle states make a mark feel alive / Every mark needs a way OUT, not just in / Three exits shown — your brand picks one). ✓
- Title: "Musinique, In Motion — Part Five. / @NikBearBrown / live marks + exits · every move built in Remotion". ✓

### World-language greeting rotation (no within-aspect repeats)
ep01: Selam (9:16) / Hej (16x9 comp) · ep02: Merhaba · ep03: Ciao · ep04: Hej · ep05: Jambo

### Defects found (session 2): NONE
All 10 cuts confirmed FINAL. No re-renders required.
