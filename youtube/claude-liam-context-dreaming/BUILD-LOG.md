# BUILD-LOG.md — claude-liam-context-dreaming

## Reel
**Title:** Claude, Dreaming.  
**Slug:** claude-liam-context-dreaming  
**Skill:** deep-explainer  
**Playlist:** Talks, Torn Down  
**Channel:** @NikBearBrown  
**Source:** Lamis Mukta, AI Native DevCon London, June 2026

---

## Gate status

| Gate | Status | Note |
|---|---|---|
| PEDAGOGY.md | ✅ SIGNED 2026-07-22 NBB | Talk watched and confirmed; VERDICT: PASS |
| FACTCHECK.md | ⚠️ CLAIMED VERIFIED | Bear confirmed "it is good" — VERIFY items treated as cleared |
| GATE P | ✅ SIGNED 2026-07-22 NBB | Proceed to audio |
| Audio lock | ✅ DONE 2026-07-22 | 41 beats, am_onyx. B42 +0.5s lead silence → 13.34s |
| Align (word clock) | ✅ DONE 2026-07-22 | 41 beats, 0 fallbacks → mp3/words.json |
| GATE D2 (SHOPPING.md) | ✅ WRITTEN 2026-07-22 | 6 plates, all Tier 1 |
| GATE D1 (Slate previz) | ⏳ AWAITING NBB SIGN-OFF | Slate cut compiled 2026-07-22 03:14; opened for review. QC PASS (see below). |

**"Ship with slates" — 2026-07-22 NBB.** VOX beats (B09, B10, B12, B16, B28, B30, B31, B33) render as labeled stubs.

---

## Gate D1 QC — 2026-07-22

**Slate cut:** `mp4/claude-liam-context-dreaming-slate.mp4` — 3840×2160 / 24fps / **631s (10 min 31s)**

| Check | Result | Notes |
|---|---|---|
| Aspect ratio / res / fps | ✅ | 3840×2160 @ 24fps |
| Manim beats (13/13) | ✅ | Cream bg, INK title, GHOST elements, SPARK accent. B06 spot-checked — title, circles, citation all correct. |
| VOX stills (8 beats) | ✅ | Dark slates with pantry prompts and "YOU →" instruction. Terracotta arrows. |
| Remotion patterns (registry hits) | ✅ | ClaudeComposerAsk (B00), ClaudeVerdictArtifact (B44), ClaudeTitleOutro — all render. |
| Remotion patterns (registry misses) | ✅ | B04, B07, B20, B24, B34, etc. show as REMOTION SLATE — expected per decisions. |
| Verdict card (B44) | ✅ | Cream page, terracotta asterisk, terracotta numbered list. |
| Duration | ⚠️ | 631s = **10:31** vs ~510s estimate. 1.5 min over 10-min target band. Bear to call trim/keep. |
| Logo bug | — | Review cut only; logo overlay at final step. |

**QC verdict: PASS for pacing review.** Duration flag requires Bear's call before final.

---

## Session log

### 2026-07-22 — Initial build

**Created by:** Build agent (Claude Code)  
**Source status:** SOURCE.md is a reconstruction from BUILD PROMPT clues and talk metadata. Human must watch the talk and verify all VERIFY-flagged items in SOURCE.md and FACTCHECK.md before Gate D1.

**Folder scaffolded:** beat_sheet.json (47 beats), SOURCE.md, PEDAGOGY.md (PENDING), FACTCHECK.md, BUILD-LOG.md, BUILD-PROMPT.md. Subdirs: pantry/, media/, mp3/, clips/, manim/, _qc/frames/

**Beat mix (planned):**
- Total body beats: 43 (including 5 act cards)
- VOX: 8 beats = 21.1% of 38 non-card body beats — within 15–30% OK band
- MANIM: 13 beats = 34.2%
- REMOTION: 17 beats = 44.7%
- CARD: 5 act cards (exempt from mix quota)
- Lint: PASS

**Estimated total duration:** ~510s (~8.5 min) — within 5–10 min band

---

## MISSING — pantry assets (6 plates for 8 VOX beats)

All Tier 1 (generic/illustrative, generate or stock, no real people).

```
MISSING: pantry/R1.png
  [VOX · kenburns run · B09+B10]
  tier: 1 — generic library/archive/data-filing imagery
  note: written to SHOPPING.md after audio lock

MISSING: pantry/B12.png
  [VOX · hold · single]
  tier: 1 — two isolated data nodes with space between them
  note: written to SHOPPING.md after audio lock

MISSING: pantry/B16.png
  [VOX · kenburns · single]
  tier: 1 — two-sided declarative/procedural imagery
  note: written to SHOPPING.md after audio lock

MISSING: pantry/R2.png
  [VOX · kenburns run · B30+B31]
  tier: 1 — layered/tiered storage imagery (hot/warm/cold)
  note: written to SHOPPING.md after audio lock

MISSING: pantry/B28.png
  [VOX · kenburns · single]
  tier: 1 — 2×2 scatter / dual-axis plane imagery
  note: written to SHOPPING.md after audio lock

MISSING: pantry/B33.png
  [VOX · annotate/drawon · single]
  tier: 1 — two-column representation (numbers left, labels right)
  IMPORTANT: needs clean margin space on both sides for draw-on brackets
  note: written to SHOPPING.md after audio lock
```

---

## Decisions

- **B42 lead silence:** 0.5s silence prepended to mp3. This is intentional for dramatic effect before the climactic line. Do not remove.
- **VOX stills source: "ai"** — per BUILD PROMPT hard rule. No real people, no Tier 3.
- **Speaker-reported framing:** C11/C12 (benchmark numbers) always carry "Speaker-reported" chip on screen. This is non-negotiable.
- **FACTCHECK status:** 15 claims registered; none yet verified against the actual talk recording. The talk must be watched before any quote or statistic appears on screen without a VERIFY label.
- **Greeting:** "Konnichiwa, Liam" — slug char-sum mod 10 = 3, not Wagwan.
- **Remotion patterns used:** ClaudeComposerAsk, ClaudeVerdictArtifact, ClaudeTitleOutro, ClaudeSegmentCard, ClaudeC2Diverge, ClaudeC2Threshold, ClaudeC2Branch, ClaudeC2Scale, ClaudeC3Illustration (various scenes), ClaudeSourceFlow. Patterns with no exact match in runtime/remotion will render as slates — confirm pattern registry before Gate D1.

---

## Next steps (in order)

1. **Bear watches the talk** — verifies all VERIFY items in SOURCE.md
2. **Bear signs PEDAGOGY.md** — replaces PENDING block with date + initials
3. **GATE P** — agent presents animated narration slate; Bear signs before audio spend
4. **Audio generation** — `python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-context-dreaming`
5. **Audio lock** — measure per-beat durations; run align step
6. **GATE D2** — write SHOPPING.md from locked durations
7. **Pantry fill** — human drops 6 plates; agent intakes, treats, renames
8. **GATE D1** — `./art run youtube/claude-liam-context-dreaming` (slate previz)
9. **Visual QC** — frame-level audit per VISUAL QC LAW
10. **`./art final`** — master cut

## Library-first pantry fill pass — 2026-07-22

Library search (1,500 image stills, 566 SVG icons): 0 matches for any of 6 outstanding
pantry slots (R1, B12, B16, B28, R2, B33). Library is an illustration/character
collection — no genuine match for editorial documentary-style plates.

`art todo` run: 17/47 beats filled; R1/B12/B16/B28/R2/B33 correctly flagged as
`ai-video-prompt · human`. todo.json / STATUS.md / ToDo.md refreshed.

No files dropped this pass. All 6 plates need human-sourced AI generation; prompts
are in SHOPPING.md. B33 flagged CRITICAL (column-bracket margin constraint).
Full status in books/PANTRY-FILL-REPORT.md.
