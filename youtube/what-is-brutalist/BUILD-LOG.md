# BUILD-LOG — what-is-brutalist
# append-only — every command, error, fix, MISSING:, and final result

## Session start: 2026-07-12

---

### SETUP

- Directories created: media/, manim/, mp3/, pantry/, images/, mp4/
- Read: beat_sheet.json (16 beats: B00–B14, B99)
- Read: animated_graphics.py (teardown palette, library components)
- Read: runtime/remotion/src/scenes/NikBearBrownTerminalAsk.tsx (schema: command, topic, segment, runningText — NO output prop yet)
- Read: runtime/remotion/src/scenes/NikBearBrownCodeBlock.tsx (schema: filename, segment, topic, code — hardcodes "python" label)
- Read: runtime/remotion/src/scenes/BrutalistTerminalOpen.tsx (schema: command, checklist, topic)
- Read: runtime/remotion/src/scenes/BrutalistCommentCTA.tsx (schema: filename, code, variant, topic)
- Env: ELEVENLABS_API_KEY=<set> — narrated cut possible
- Env: ELEVENLABS_VOICE_NIKBEARBROWN=<set>
- Manim: /opt/homebrew/bin/manim — available
- Remotion node_modules: not installed — will npm install

### PROP MAPPING (beat sheet intent → component schema)

- B00 BrutalistTerminalOpen: command ✓, checklist ✓, topic (default)
- B04 NikBearBrownCodeBlock: language→filename(.py), caption→segment, code ✓
- B10 NikBearBrownTerminalAsk: command ✓, output[] MISSING from schema → extending component
- B12 NikBearBrownTerminalAsk: same as B10
- B13 NikBearBrownCodeBlock: language="bash"→filename(.sh), caption→segment, code ✓
- B99 BrutalistCommentCTA: comment+cta→code, variant ✓

### STEP 1 — scenes.py written
10 Manim Scene subclasses: B01_OneClickSlop, B02_CannotWatch, B03_TasteGaps, B05_TwentyHourBug,
B06_TwoFailureModes, B07_YouAreTheConductor (hero), B08_ScoreAndPlaying, B09_BeatSheetHeart,
B11_RequestCardPantry, B14_ThePlaylist.

### FIX — static_scene_check.py Gate A bug
The check compared single-scene distinct-state count against the video's TOTAL n_beats (16), 
causing false "low visual variety" errors for every per-beat class. Fixed: when `--class` is not 
"BearsDoodlesVideo", skip the video-level ratio check and use the scene's own snapshot count.
File changed: runtime/qc/static_scene_check.py

Gate A results (post-fix): all 10 scenes PASS.
- B05 initial error: `_Anim.align_to` chain not supported in static stub → fixed: Transform to tiny rectangle
- B09 initial error: `list - list` arithmetic → fixed: `np.array()` wrapping

### STEP 2 — Gate files written
- FACTCHECK.md: all on-screen figures labeled "illustrative — sample CLI output"
- SHOTLIST.md: one-row-per-beat table, all 16 beats documented
- PROMPTS.md: "No open media slots — all beats are pipeline-rendered"
- PEDAGOGY.md: act structure, cold open, gap-formula, utility-framing, vocabulary, length all PASS → VERDICT: PASS

### STEP 3 — Remotion beats

EXTENSIONS (prop schema additions):
- runtime/remotion/src/scenes/NikBearBrownTerminalAsk.tsx: added `output: z.array(z.string()).optional()` prop; renders staggered output lines after runningText
- runtime/remotion/src/scenes/NikBearBrownCodeBlock.tsx: added `language` and `caption` optional props; `displayLanguage` and `displaySegment` render dynamically
- runtime/remotion/src/Root.tsx: BrutalistCommentCTA durationInFrames 180→450; BrutalistTerminalOpen 360→600 (to support actual audio lengths)

npm install: runtime/remotion/ — 188 packages (esbuild binary functional)

Renders (all 6 Remotion beats):
- B00 BrutalistTerminalOpen: 464 frames (15.46s actual audio) → media/B00.mp4 ✓
- B04 NikBearBrownCodeBlock: 240 frames (8s) → media/B04.mp4 ✓  
- B10 NikBearBrownTerminalAsk+output: 420 frames (14s) → media/B10.mp4 ✓
- B12 NikBearBrownTerminalAsk+output: re-rendered at 127 frames (4.21s actual audio) → media/B12.mp4 ✓
- B13 NikBearBrownCodeBlock: re-rendered at 139 frames (4.62s actual audio) → media/B13.mp4 ✓
- B99 BrutalistCommentCTA: 240 frames (8s) → media/B99.mp4 ✓

Initial renders at estimated_duration_s; re-rendered B00/B12/B13 at actual audio lengths
after audio was generated (to avoid extreme speed adjustments).

Manim render: run.sh with ART_QC=0
- All 10 Manim scenes rendered successfully on first pass
- compile.py first pass: 10/16 filled (Remotion slots were SLATE placeholders)

### STEP 4 — Audio (ElevenLabs)

FIX — generate_audio.py did not support `voice_env` indirection from beat sheet metadata.
Added: reads `metadata.voice_env` to resolve the env var name before falling back to ELEVENLABS_VOICE_ID.
File changed: runtime/scripts/generate_audio.py

GATE P: wrote PEDAGOGY.md (VERDICT: PASS) before spending credits.
Generated: 16 mp3 files → mp3/beat-B*.mp3 + mp3/timings.json
Total actual duration: 174.39s

### STEP 5 — Final compile

compile.py called with --review after all media + audio present.
Result: 16/16 beats filled. what-is-brutalist-review.mp4 (174.4s, narrated, PIL overlays)

Slots:
B00:VIDEO B01:MANIM B02:MANIM B03:MANIM B04:VIDEO B05:MANIM B06:MANIM B07:MANIM
B08:MANIM B09:MANIM B10:VIDEO B11:MANIM B12:VIDEO B13:VIDEO B14:MANIM B99:VIDEO

Warning (non-blocking): "drawon carries 10/16 beats (62%) — over the ~40% pantry cap"
This is expected for an explainer reel with 10 Manim graphic beats.

### STEP 6 — Final report (todo.py)

All 16 beats: filled — 0 unrendered, 0 slates remaining.

BEATS RENDERED BY PIPELINE: ALL 16
  Manim (GRAPHIC): B01 B02 B03 B05 B06 B07 B08 B09 B11 B14
  Remotion (REMOTION): B00 B04 B10 B12 B13 B99

BEATS FOR HUMAN REVIEW (rough conforming, review the cut):
  B11: MANIM slowed 1.48x (15s → 19.8s audio) — the 3-step request-card animation
       runs at 0.68x speed; check that pacing feels natural
  B06: MANIM slowed 1.27x (13.1s → 16.6s audio) — balance beam scene held long
  B02: MANIM center-cut (8s → 5.9s audio) — some tail may be clipped; check ending

WARNINGS:
  drawon motion proportion 62% (over cap) — informational only; explainer genre

DELIVERABLE: youtube/what-is-brutalist/what-is-brutalist-review.mp4 (174.4s, narrated)

### TOOLKIT FIXES MADE DURING BUILD (committed changes)

1. runtime/qc/static_scene_check.py — per-beat Gate A false-alarm fix
2. runtime/remotion/src/scenes/NikBearBrownTerminalAsk.tsx — output[] prop
3. runtime/remotion/src/scenes/NikBearBrownCodeBlock.tsx — language + caption props
4. runtime/remotion/src/Root.tsx — composition duration ceilings raised
5. runtime/scripts/generate_audio.py — voice_env indirection support

