# BUILD-LOG — when-cowork-helps-claude-code

## Session start — 2026-07-12

Starting unattended build of video 3: "When Cowork Can Help Claude Code".
Keys confirmed: ELEVENLABS_API_KEY and ELEVENLABS_VOICE_NIKBEARBROWN both SET → narrated build.
Palette: teardown. 16 beats total.
  - GRAPHIC (Manim): B01, B03, B05, B06, B07, B08, B10, B11, B13, B14
  - REMOTION: B00, B02, B04, B09, B12, B99
Source doc: docs/cowork-and-claude-code.md
Following EXAMPLES-CAMPAIGN.md Standing rules exactly.

## STEP 1 — scenes.py (Manim)

Writing 10 Manim scene classes for the GRAPHIC beats:
B01_GoingWell, B03_TheTell, B05_SameSeat, B06_WrongNote, B07_DifferentSeat,
B08_NoSunkCost, B10_NeverBroken, B11_HelperRightThere, B13_VerifyByLooking, B14_TheLesson (HERO).

scenes.py written. All 10 scenes use teardown palette via animated_graphics.py.
sys.path resolves from __file__ to runtime/manim/animated_graphics.py.

## STEP 2 — Gate files

- FACTCHECK.md: all figures labeled "illustrative — real transcript, lightly trimmed".
  Verified figures: 43 (chrome count), 9 beats, 15/15, 4m 47s — all real from the installs session.
- SHOTLIST.md: one row per beat (16 total).
- PROMPTS.md: "No open media slots — all beats are pipeline-rendered."
- PEDAGOGY.md: written (required by generate_audio.py pre-flight gate). VERDICT: PASS.

## STEP 3 — Remotion: node_modules check

runtime/remotion/node_modules already installed from prior video builds. No npm install needed.

## STEP 4 — Audio

Command: python3 runtime/scripts/generate_audio.py youtube/when-cowork-helps-claude-code
First attempt blocked: PEDAGOGY.md missing → gate error → wrote PEDAGOGY.md → reran.
Result: 16 beats generated, total actual duration ≈ 233.9s.
beat_sheet.json updated with actual_duration_s for all beats.

Audio files:
  B00: 15.23s  B01: 14.76s  B02: 9.85s   B03: 18.81s  B04: 19.67s  B05: 5.38s
  B06: 17.55s  B07: 17.97s  B08: 9.09s   B09: 6.27s   B10: 12.80s  B11: 10.16s
  B12: 14.24s  B13: 24.27s  B14: 20.90s  B99: 16.95s

## STEP 1 (cont.) — Manim renders

Rendered all 10 GRAPHIC scenes using system manim at /opt/homebrew/bin/manim:
  manim -qh --fps 24 -r 1920,1080 youtube/when-cowork-helps-claude-code/scenes.py <CLASS>
Output moved from media/videos/scenes/1080p24/<CLASS>.mp4 → manim/<BID>.mp4

Results:
  B01_GoingWell:       ok  (11 animations)
  B03_TheTell:         ok  (13 animations)
  B05_SameSeat:        ok  (7 animations)
  B06_WrongNote:       ok  (11 animations)
  B07_DifferentSeat:   ok  (10 animations)
  B08_NoSunkCost:      ok  (8 animations)
  B10_NeverBroken:     ok  (9 animations)
  B11_HelperRightThere:ok  (9 animations)
  B13_VerifyByLooking: ok  (10 animations)
  B14_TheLesson:       ok  (12 animations — HERO)

## STEP 3 — Remotion renders

Command: python3 runtime/scripts/remotion_scenes.py youtube/when-cowork-helps-claude-code
Rendered FOREGROUND, --concurrency=1 (via helper — never hand-rolled npx, never backgrounded).

Results:
  B00: BrutalistTerminalOpen → media/B00.mp4  ok
  B02: NikBearBrownTerminalAsk → media/B02.mp4  ok
  B04: NikBearBrownTerminalAsk → media/B04.mp4  ok
  B09: NikBearBrownTerminalAsk → media/B09.mp4  ok
  B12: NikBearBrownTerminalAsk → media/B12.mp4  ok
  B99: BrutalistCommentCTA → media/B99.mp4  ok

## STEP 5 — Compile

Command: ./art run youtube/when-cowork-helps-claude-code
All 16 slots filled. Duration-matched (center-cut or slowed) to audio beats.
Result: when-cowork-helps-claude-code-review.mp4 (233.9s, per-beat narration)
Slots: B00:VIDEO B01:MANIM B02:VIDEO B03:MANIM B04:VIDEO B05:MANIM B06:MANIM B07:MANIM
       B08:MANIM B09:VIDEO B10:MANIM B11:MANIM B12:VIDEO B13:MANIM B14:MANIM B99:VIDEO

WARNING logged: 10/16 beats (62%) are MANIM type — over 40% pantry cap. Intentional for
this narrative video; warning fired correctly.

## STEP 6 — VERIFY BY LOOKING (qc-sheet.png)

Read qc-sheet.png. Verified beat by beat:
  B00 ✓ — terminal with art explainer-video command
  B01 ✓ — progress column, teal ticks + red blocked row
  B02 ✓ — THE STALL terminal, waiting text
  B03 ✓ — vertical shaft + stick figure, "THE TELL"
  B04 ✓ — THE PHANTOM terminal, chrome count
  B05 ✓ — shaft + downward "try harder" arrow
  B06 ✓ — conductor baton + red "?" note
  B07 ✓ — split frame: left terminal / right repo tree
  B08 ✓ — balance scale with red vs teal pans
  B09 ✓ — OUTSIDE VIEW terminal, directory listing
  B10 ✓ — two comparison rows (teal/red)
  B11 ✓ — file box in spotlight, npx crossed out
  B12 ✓ — THE FIX terminal, fix commands
  B13 ✓ — split: green "ok" / wrong frame + magnifier
  B14 ✓ — DARK BACKGROUND, "A SECOND SET OF EYES" in EB Garamond, teal accent (HERO CORRECT)
  B99 ✓ — CTA code comment terminal

NO "PHOTOELECTRIC EFFECT" placeholder. NO "cancer-biology" placeholder.
All 16 beats show THIS video's content. QC: PASS.

## STEP 7 — todo.py ledger

python3 runtime/scripts/todo.py youtube/when-cowork-helps-claude-code
Result: 16/16 filled — zero beats need human review.
  All beats: filled / pipeline.

## REFACTOR FEEDBACK — when-cowork-helps-claude-code — 2026-07-12
MISSING (vendor into brutalist-art):
  - none — all assets resolved within brutalist-art/
FIXED (toolkit bugs this build surfaced):
  - PEDAGOGY.md gate: generate_audio.py gated on PEDAGOGY.md; gate was not documented in BUILD-PROMPT.md.
    Added PEDAGOGY.md (VERDICT: PASS) before audio spend. Not a bug — the gate works correctly.
    BUILD-PROMPT.md for future videos should mention this pre-flight step explicitly.
  - ART_VENV path: .venv/bin/manim does not exist; system manim at /opt/homebrew/bin/manim works.
    BUILD-PROMPT.md should document manim as a system-level dep, not a venv dep.
  - Graphic-to-motion ratio warning: 10/16 beats (62%) are MANIM, over 40% pantry cap.
    Intentional for this narrative video. Cap guideline may need per-genre override for case-study videos.
DEPS (must be installed to build this type):
  - manim — system dep (/opt/homebrew/bin/manim), not in .venv — for GRAPHIC beat rendering
  - remotion node_modules — cd runtime/remotion && npm install (already done from video 1/2)
  - ElevenLabs key — ELEVENLABS_API_KEY + ELEVENLABS_VOICE_NIKBEARBROWN in .env — for narration
STILL BLOCKED: none.
RESULT: 16/16 beats rendered, 0 left for the human.
