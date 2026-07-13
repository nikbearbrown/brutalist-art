# CAMPAIGN-FEEDBACK — build-driven findings for the refactor

Each example build appends a `## REFACTOR FEEDBACK` block here (see EXAMPLES-CAMPAIGN.md).
The refactor session consumes this: MISSING → vendor list · FIXED → regressions closed · DEPS →
INSTALL/doctor · STILL BLOCKED → open gates.


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
