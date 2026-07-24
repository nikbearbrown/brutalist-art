# CAMPAIGN-FEEDBACK — build-driven findings for the refactor

Each example build appends a `## REFACTOR FEEDBACK` block here (see EXAMPLES-CAMPAIGN.md).
The refactor session consumes this: MISSING → vendor list · FIXED → regressions closed · DEPS →
INSTALL/doctor · STILL BLOCKED → open gates.


## REFACTOR FEEDBACK — suno-vs-11-labs-cost-test — 2026-07-13 (human review)
LAYOUT DEFECTS caught by human eye that layout_audit missed:

  (1) B02_TheChallenger — stamp overflow, invisible to overlap check:
      stamp_bg was a fixed Rectangle(width=3.6) marked _qc_intentional=True, which
      suppressed the audit entirely on that object. stamp_txt "ONE GENERATION ≈ ONE
      VIDEO'S NARRATION" is wider than 3.6 units — white text spilled onto the near-white
      card and rendered as clipped garbage ("NERATION ≈ ONE VIDEO'S NAR"). Two blind spots:
        (a) _qc_intentional on a background must not exempt the text it carries.
        (b) White-on-white spill is invisible to a text-vs-text overlap check.
      Fix: build stamp_bg from the text, not a guessed size — size Rectangle from stamp_txt.width.

  (2) B05_PantryDrop — box-vs-text collision:
      pantry_path auto_box at RIGHT*2.6+UP*0.2 overlapped step-2 head text "generate + download"
      at LEFT*2.0+UP*0.18. The audit checks text-vs-text but not box-vs-text, so it missed
      the box's left edge intruding on the text zone.
      Fix: move pantry_path to RIGHT*3.2+DOWN*0.55 and reduce font_size.

AUDIT BLIND SPOTS logged:
  - _qc_intentional suppresses ALL sub-object checks, including text the bg carries.
    Future: _qc_intentional should suppress stroke/position checks but NOT carried text.
  - box-vs-text collision: auto_box extent is not compared against nearby text centroids.
    Future: add box-extent (bounding_box) into the overlap manifest alongside text centroids.

CONTENT CHANGES:
  (3) New B00A announce beat added to both variants: ElevenLabs voiced in both ("This is
      the Suno/ElevenLabs version…"). Announcer is the constant; body voice is the experiment.
  (4) Variant labeling: topic string "SUNO VS 11 LABS" suffixed per folder — "(SUNO)" and
      "(11 LABS)" — so analytics and Remotion props distinguish the two published videos.


## REFACTOR FEEDBACK — posting-to-youtube — 2026-07-13
MISSING (vendor into brutalist-art):
  - none — all assets resolved within brutalist-art/
FIXED (toolkit bugs this build surfaced):
  - No new toolkit bugs. Standing rules #3/#4 followed exactly. Build completed without deviations.
  - Graphic-to-motion warning fires at 9/15 = 60% > 40% cap. Correct for a technical-process reel.
    No code change needed; the guideline may want a per-genre override flag.
DEPS (must be installed to build this type):
  - manim — system dep (/opt/homebrew/bin/manim), not in .venv — for GRAPHIC beat rendering
  - remotion node_modules — cd runtime/remotion && npm install (already installed from video 1/2)
  - ElevenLabs key — ELEVENLABS_API_KEY + ELEVENLABS_VOICE_NIKBEARBROWN in .env — for narration
STILL BLOCKED: none.
RESULT: 15/15 beats rendered (235.8s, narrated). 0 slates. 0 beats need human review.
  Standing rules #3 and #4 followed exactly — Remotion rendered via remotion_scenes.py (foreground),
  props matched to schema, verified by looking at qc-sheet.png. No placeholder text found.
  B12 HERO confirmed: dark bg, "THE MACHINE POSTS." / "YOU OWN WHAT SHIPS.", machine/human split.


## REFACTOR FEEDBACK — installs — 2026-07-13
RESULT: 15/15 beats compiled (224.7s, narrated). All 9 Manim beats clean incl. hero B11 (CLONE YOUR VOICE).
FIXED (toolkit, standing rules #3/#4 in EXAMPLES-CAMPAIGN.md):
  - Remotion render discipline: the build agent hand-rolled `npx remotion render` in the BACKGROUND and
    polled `ps|grep chrome` to detect completion → invented a phantom "43 stale Chrome" problem (the
    user's real Chrome + Spotify) and stalled for hours. Fix: render ONLY via
    `runtime/scripts/remotion_scenes.py` (foreground, --concurrency=1). Rule #3.
  - Remotion prop/schema mismatch: 6 REMOTION beats (B00 B02 B05 B08 B13 B99) rendered Root.tsx
    defaultProps (cancer-biology, photoelectric-effect) because beat_sheet `shot.remotion.props` used
    keys not in each component's zod schema. Fix: props patched to real names (topic/segment/
    runningText/filename/code/variant); added Rule #4 (match schema, verify on qc-sheet). Needs --force re-render.
DEPS: none new (remotion node_modules already installed by video 1).
STILL BLOCKED: none. Watch item — center-cut trims long terminal compositions to audio; verify type-on head survives.
DEEPER TODO (optional): give Root.tsx compositions neutral defaultProps, or have remotion_scenes.py warn on
  unknown prop keys, so a schema mismatch fails loud instead of silently rendering another video's demo.


## REFACTOR FEEDBACK — when-cowork-helps-claude-code — 2026-07-12
MISSING (vendor into brutalist-art):
  - none — all assets resolved within brutalist-art/
FIXED (toolkit bugs this build surfaced):
  - PEDAGOGY.md gate: generate_audio.py gated on PEDAGOGY.md; gate was not documented in BUILD-PROMPT.md.
    Added PEDAGOGY.md (VERDICT: PASS) before audio spend. Not a bug — the gate works correctly.
    BUILD-PROMPT.md for future videos should mention this pre-flight step explicitly.
  - ART_VENV path: .venv/bin/manim does not exist (venv doesn't bundle manim); system manim at
    /opt/homebrew/bin/manim works. BUILD-PROMPT.md should document `manim` as a system-level dep,
    not a venv dep. No code changed; documented here.
  - Graphic-to-motion ratio warning: 10/16 beats (62%) are MANIM graphic type, over the 40% pantry cap.
    This is intentional for a concept-heavy narrative video; the warning fires correctly. The cap
    guideline may need a per-genre override flag for case-study / pure-narrative videos.
DEPS (must be installed to build this type):
  - manim — system dep (/opt/homebrew/bin/manim), not in .venv — for GRAPHIC beat rendering
  - remotion node_modules — cd runtime/remotion && npm install (already done from video 1/2)
  - ElevenLabs key — ELEVENLABS_API_KEY + ELEVENLABS_VOICE_NIKBEARBROWN in .env — for narration
STILL BLOCKED: none.
RESULT: 16/16 beats rendered (233.9s, narrated). 0 slates. 0 beats need human review.
  Standing rules #3 and #4 followed exactly — Remotion rendered via remotion_scenes.py (foreground),
  props matched to schema, verified by looking at qc-sheet.png. No placeholder text found.

## HUMAN FEEDBACK — posting-to-youtube rev 2 — 2026-07-13

- "The video explains the tool and CC upload is an important feature — clients want their captions
  right." → video 4 gets a rev 2: B03 becomes "four things" (adds the `.srt` line); new beat B04A
  "captions ship with the post". Publisher caption parity restored in `c3cac9b` (force-ssl scope,
  `captions.insert`, `.srt` emission — the vendored `publish_playlist.py` had dropped what the
  ancestor `youtube_publish.py` had).
- Toolkit lesson: **vendoring a script is a refactor — diff features against the ancestor before
  first use.** The caption gap only surfaced because a human asked where the CC went.


## REFACTOR FEEDBACK — posting-to-youtube REV 2 — 2026-07-13
MISSING (vendor into brutalist-art):
  - none
FIXED (toolkit bugs this build surfaced):
  - publish_playlist.py hardcoded `--playlist` default to "Quantum Mechanics Volume 1 (NotebookLM)"
    (a stale default from another project). Running without `--playlist` created a wrong playlist and
    added the video there instead of the Brutalist playlist. Fix: default now reads $ART_PLAYLIST env
    var (empty fallback), with a runtime guard that fails fast if the value is empty.
    File: skills/upload/youtube-publisher/scripts/publish_playlist.py.
  - The REV 2 BUILD-PROMPT section did not include `--playlist "Brutalist"` in the publish command.
    Future BUILD-PROMPTs must always include `--playlist` explicitly (or set ART_PLAYLIST in .env).
DEPS: same as original build (manim, remotion node_modules, ElevenLabs key).
STILL BLOCKED:
  - Human: delete accidentally-created playlist "Quantum Mechanics Volume 1 (NotebookLM)"
    (PLaOEYdBvYAog) in YouTube Studio.
  - Human: delete superseded video https://youtu.be/5iadw1MET3Q (unlisted) in YouTube Studio.
RESULT: 16/16 beats rendered (262.1s, narrated). 0 slates.
  B03 re-rendered (Remotion, foreground, --force): shows `installs.srt ← the caption track (CC)`.
  B04A_CaptionsRight new Manim scene: srt cue card, auto-caption strikethrough, captions.insert caption.
  SRT regenerated: 16 cues, 262s. Caption track uploaded via captions.insert. ✓
  Rev-2 video: https://youtu.be/PE2Zv8hBDzc (unlisted, in Brutalist playlist).
  Standing rules #1–#4 followed exactly.

## REFACTOR FEEDBACK — four-shorts build — 2026-07-13
FIXED (toolkit bugs this build surfaced):

  - RULE #4 VIOLATION — Remotion defaultProps silently override missing beat props:
    Remotion MERGES --props JSON with Root.tsx defaultProps on a per-field basis.
    If a beat's shot.remotion.props omits a schema field (e.g. `topic`), Remotion
    uses the composition's defaultProps value — not the schema's .default() — so
    "CANCER BIOLOGY" (the demo topic set in Root.tsx) appeared in every render that
    was missing `topic`. Fix: what-is-brutalist beat props patched to include all
    schema fields (topic, segment, runningText, filename). Future guard: remotion_scenes.py
    should warn when props keys don't cover all schema-required fields, so a mismatch
    fails loud rather than silently rendering another video's demo content.

  - PORTRAIT TEXT CLIP — `whiteSpace: 'pre'` clips output/code lines in 9:16:
    All four Onda components (BrutalistTerminalOpen, NikBearBrownTerminalAsk,
    NikBearBrownCodeBlock, BrutalistCommentCTA) used `whiteSpace: 'pre'` on checklist,
    output, and code lines. In 16:9 (1920px wide) all lines fit. In portrait (1080px wide
    terminal body ≈ 800px), lines longer than ~24 monospace chars clipped mid-word.
    Fix: changed to `whiteSpace: 'pre-wrap'` + `overflowWrap: 'break-word'` +
    `paddingLeft: '2ch' / textIndent: '-2ch'` (hanging indent). Applies to both 16:9
    and 916 renders — non-breaking since landscape lines are short enough never to wrap.

  - MISSING 916 COMPOSITIONS — BrutalistTerminalOpen916 and BrutalistCommentCTA916
    not in Root.tsx at start of session. Without them the ONDA CHECK flagged B00 and
    B99 as BLOCKED across all four shorts. Added both as identical-component entries
    with width=1080, height=1920 (same schema and props type as their 16:9 parents).
    Rule: whenever a new Onda component is added for 16:9, a 916 entry must be added
    to Root.tsx immediately — the ONDA CHECK requires it for any short derivative.

  - STALE CENTER-CUT FILES — pre-patch shorts.py created <reel>/media/<bid>-916.mp4
    for REMOTION beats (actual Remotion renders cropped 16:9→9:16). These are
    auto-deleted garbage: delete any media/<bid>-916.mp4 whose beat has shot.type=REMOTION
    before re-running shorts.py and remotion_scenes.py.

  - surround_box() is TEXTISH in Gate A — the static-check stub adds positional Mob
    args as submobjects; SurroundingRectangle(text_stack) causes the resulting rectangle
    to be "textish" (invisible to the shape snapshot). Fix in scenes.py: replace
    surround_box() with auto_box() (safe — uses explicit width/height kwargs) or a plain
    Rectangle(width=..., height=...) for heart/highlight boxes.

  - _qc_intentional must go on the STROKE, not on text — in Gate B the _collect_strokes()
    walker checks for `_qc_intentional` on Lines/Arrows/curves. Setting the flag on the
    adjacent Text object (the label) doesn't suppress the "label on line" detection.
    Fix: `strikethrough._qc_intentional = True` on the Line object itself.

  - PORTRAIT SAFE ZONE LESSONS — portrait frame is ±2.25 x / ±4.0 y but safe area
    is ±1.95 x / ±3.4 y. Key patterns to avoid:
    * Balance-scale pans at ±2.0 → rescale to ±1.5 for safe zone
    * `to_edge(DOWN, buff=0.42)` puts bottom captions at y≈-3.58 (outside safe area);
      use buff≥0.6 or accept the warning if intentional
    * `next_to(stroke, DIRECTION, small_buff)` often triggers Gate B "label on curve";
      prefer `move_to(explicit_coords)` that's clearly away from the stroke body

STILL BLOCKED:
  - ElevenLabs API key invalid (HTTP 401). B99 outro for all four shorts is a 16s
    silence placeholder. Human must fix ELEVENLABS_API_KEY in .env, then run:
    `python3 runtime/scripts/generate_audio.py brutalist-art/youtube/<reel>/short --only B99`
    for all four reels before final compile and publish.

RESULT: Four 9:16 review cuts compiled. 0 Gate B errors. ONDA CHECK: 0 BLOCKED.
  All REMOTION beats render real beat content with portrait pre-wrap layout.

## REFACTOR FEEDBACK — four-shorts publish — 2026-07-13
FIXED (toolkit bugs this publish surfaced):
  - generate_audio.py HTTP 404 from ElevenLabs: `output_format: "mp3_44100_128"` was
    in the JSON body. ElevenLabs v1 API requires it as a QUERY PARAMETER, not a body
    field. Fix: moved to URL — `API_URL = ".../text-to-speech/{voice_id}?output_format=mp3_44100_128"`.
    Direct urllib test with same body (no output_format field) returned 200; adding the
    field to the body caused the 404. File: runtime/scripts/generate_audio.py.
  - Publisher expects mp4 at `<folder>/mp4/<slug>.mp4`; `art final` writes `<slug>-cut.mp4`
    to the folder root. Fix: copy `<slug>-cut.mp4` → `mp4/<slug>.mp4` before publish.
    Future: `art final` should write directly to `mp4/<slug>.mp4` or stage_publish.py
    should be run as part of the shorts publish flow to create the symlink.
  - Shorts had no SRT files. Publisher uploads `<slug>.srt` if present (CC ships with
    every post per CLAUDE.md). Fix: generate SRTs from beat sheet `actual_duration_s`
    + `narration_text` using same write_srt() logic as stage_publish.py.
    Future: `art final` or `art publish` for shorts should auto-generate the SRT.
DEPS: same as prior build.
STILL BLOCKED: none.
RESULT: Four 9:16 shorts published to "Shorts" playlist (unlisted).
  what-is-brutalist-short → https://youtu.be/_3rOaPmqvok (unlisted)
  installs-short          → https://youtu.be/igVBV4I2sBw (unlisted)
  when-cowork-helps-claude-code-short → https://youtu.be/NTD76WPrMfU (unlisted)
  posting-to-youtube-short → https://youtu.be/tb88NXJwWzs (unlisted)
  All four: CC caption tracks uploaded. Public flip is manual Studio decision.
  Standing rules #1–#4 followed exactly.

## HUMAN FEEDBACK — first shorts run — 2026-07-13

- "Every time it uses Onda terminal or Onda code it is not reformatting the Onda
  properly … if it did that for any MP4 it generated with Remotion, the Remotion
  needs to be redone." → THE ONDA CHECK added to shorts.py: REMOTION beats are
  detected BY THE SHEET (shot.type), never by folder — Remotion renders live in
  media/ and were being treated as croppable captured footage, center-cutting
  terminal/code text mid-word. Now: pantry/<bid>-916.* wins; else the short's
  sheet is rewired to the <pattern>916 portrait composition from Root.tsx and the
  beat re-renders portrait via remotion_scenes.py on short/; no 916 composition →
  loud BLOCKED line (add the composition or a pantry file). Stale center-cut
  -916 files of Remotion output are ignored and should be deleted.
- Toolkit lesson: media type is a property of the BEAT (sheet), not of the file's
  folder. Any rule keyed on directory ("media/ = croppable") breaks the moment
  two generators share an output directory.

## FIRST SUNO STEM — suno-vs-11-labs-cost-test — 2026-07-13

- Real stem (3:33, Bear's uploaded voice, vocal-only) over-split under silence
  detection: 27 segments for 13 beats — Suno pauses mid-beat as long as it
  pauses between beats. The refuse-gate worked as designed.
- Fix shipped: the EXPECTED-DURATION MERGE in suno_slice.py — beats' narration
  lengths give expected duration shares; a DP groups consecutive segments into
  one window per beat (bonus for cutting at bigger silences); windows off by
  > max(3s, 25%) still refuse. Model-like, no new deps. --strict disables.
- This stem sliced clean: 13 windows, worst Δ −4.0s (pacing), boundaries on
  the biggest gaps. Slices + measured durations written back; the sheet now
  records voice_engine.
- Backlog: a --align mode (faster-whisper forced alignment of the KNOWN
  narration text, voxlit's recitation-clock pattern) as the gold path where
  faster-whisper is installed.

## HUMAN FEEDBACK — she-walks-in-beauty — 2026-07-13 (karaoke tail cutoff)

Karaoke film cuts "innocent!" mid-word — the B99 outro hits before the last word
fully decays into silence. Fix: extend source.mp4 by 3s of music tail (WAV has
~32s of music after the speech ends at ~82s); re-render Remotion project; reassemble
review cut with the extra breathing room before B99.
Lesson: always let the final word resolve to silence before the next beat.

## HUMAN FEEDBACK — she-walks-in-beauty — 2026-07-13 (wrong build path)

Review cut failed: video was built as a generic graphic-card reel — the mastered
performance WAV was beat-sliced into mp3/beat-*.mp3, stanzas rendered as static
Manim text cards with guessed timing, no align/ folder, no karaoke, no audiogram.

Correct build path: recitation-film + lyric-overlay (continuous WAV master clock,
forced alignment → align/words.json + align/lines.json, karaoke + audiogram burned in).
Both skills exist in this repo and neither was used.

Lesson: the build path is chosen by the video's declared skill/purpose, not by the
default pipeline. The folder's stated purpose (worked example for session-karaoke-audiogram,
video 19b) and the presence of the mastered continuous WAV were both on record — the
build session still defaulted to the beat-slice/Manim-card pipeline.

Required rebuild:
  1. MASTER CLOCK: use the continuous WAV (SheWalksinBeautybyLordByron1814NateSpoken-mastered.wav)
     as the clock, not per-beat slices.
  2. GATE 0: forced alignment via align.py (or lyric-overlay's align step) → align/words.json
     + align/lines.json.
  3. FOREGROUND: karaoke overlay + audiogram burned into picture via lyric-overlay skill.
  4. NEW INTRO BEAT B00: ElevenLabs voiced; explains the clip is a Suno voice clone, directed
     with the session command, and that the karaoke proves word-sync.
  5. SRT CC track from line-level alignment.

Actions: retire mp3/beat-*.mp3 slices and scenes.py (wrong architecture); rebuild from
continuous WAV + forced alignment + overlay_new.py.
