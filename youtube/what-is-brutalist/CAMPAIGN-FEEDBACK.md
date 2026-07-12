# CAMPAIGN-FEEDBACK — what-is-brutalist
# append-only log of human-feedback iterations after initial build

---

## 2026-07-12 — Box overflow + conductor-loop beat

### Feedback (verbatim)
> "Fix the boxes — make them wider to properly hold the text. Keep the bad (too-narrow) frame in
> this video, and add a new beat after B08 where my voice clone tells you to fix the boxes and you
> do it, on screen. Log my feedback."

### Root cause
B08_ScoreAndPlaying tool cards used `Rectangle(width=2.4, height=0.6)` — a fixed box that
overflowed when the VGroup(tool_name + role_name) exceeded 2.4 units wide. Same pattern in B03.

### Fix applied (general toolkit, not one-off)
- `runtime/manim/animated_graphics.py`: added `auto_box(content, h_pad, v_pad, …)` — measures
  content mob at render time and sizes the Rectangle to fit.
- `youtube/what-is-brutalist/scenes.py`: B08 and B03 updated to call `auto_box()`.

### Artifacts
- `media/box-before.png` + `media/box-before.mp4` — B08 frame at 3s (narrow box, visible overflow)

### New beat B08B (conductor loop, live)
- Position: immediately after B08
- narration: "Here's that loop — live, from building this very video…"
- Scene: BEFORE narrow box → INSTRUCTION chip → AFTER auto_box (Teardown palette)
- Audio: 17.5s (ElevenLabs NikBearBrown)
- Result: manim/B08B.mp4 ✓

### Recompile
- 17/17 beats filled · 191.9s narrated cut
- Deliverable: `what-is-brutalist-review.mp4`

### Toolkit fix promoted
`auto_box()` is now part of `runtime/manim/animated_graphics.py` — available to all future scenes
in this repo. Any card/label helper should call it instead of hardcoding a Rectangle size.

---
