# CAMPAIGN-FEEDBACK — build-driven findings for the refactor

Each example build appends a `## REFACTOR FEEDBACK` block here (see EXAMPLES-CAMPAIGN.md).
The refactor session consumes this: MISSING → vendor list · FIXED → regressions closed · DEPS →
INSTALL/doctor · STILL BLOCKED → open gates.


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
