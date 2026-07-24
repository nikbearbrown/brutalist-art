# Claude Code Prompt — H-HAI Logo Remotion Showcase (9:16, claude-liam)

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace.

```text
Build one long-form 9:16 vertical Remotion video that animates logos/H-HAI-Logo.svg
every way Remotion can — a technique-showcase reel in the Claude explainer skin,
claude-liam channel. The purpose is REVIEW: I need to SEE each move to judge which
ones work. Free pipeline only: Kokoro voice, no ElevenLabs, no higgsfield, no
publishing, no git commit or push. Run without approval pauses (no paid spend is
possible under these constraints).

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md
- skills/make/explainer/SKILL.md (and the MOTION.md / REMOTION.md it points to)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts

FORMAT

- 1080x1920 (9:16), 30 fps.
- Channel claude-liam: persona Liam (in for Bear), folder chip @NikBearBrown,
  voice Kokoro am_onyx, register Teardown. Do not use ElevenLabs.
- Audio-first: generate and measure Liam's narration per beat FIRST; conform
  every beat's duration to its audio.
- Length is derived from the beat count, not a fixed clock. Expect roughly
  2.5–4 minutes.

SUBJECT

- logos/H-HAI-Logo.svg — the Humanitarians AI "H" ligature mark: two <path>
  elements, fill #171717, on a 340x368 viewBox.
- Before animating, extract the two path d-strings and drive them directly with
  @remotion/paths. Drop the SVG's soft-edge <filter>; if a beat wants a shadow,
  re-implement it as a cheap offset/opacity layer. Never depend on SVG filters
  in the render path.
- The logo is the subject. Its ink stays #171717 on the Claude cream page in
  every beat except ones explicitly labeled as color treatments.

STRUCTURE (claude-explainer skeleton)

- Beat 0 — ClaudeComposerAsk cold open. Liam frames the question: one logo,
  every move Remotion knows — which ones deserve to live?
- Middle — ONE TECHNIQUE PER BEAT. Every technique beat must show:
  1. the technique name on screen as a Title Case segment label (EB Garamond,
     terracotta underline — the one accent),
  2. the H mark actually performing the technique,
  3. one short Liam line naming the move and what to judge it by.
- Second-to-last — Your Turn composer beat with a suggested prompt typed in.
- Last — @NikBearBrown brand card, title restated.

TECHNIQUE CATALOG (minimum one beat each; add more only if they render cleanly)

1. Spring Entrance — default spring() pop-in.
2. Overshoot Spring — high-bounce config with squash-and-stretch on landing.
3. Draw-On Stroke — evolvePath() outline trace, then fill flood.
4. Per-Path Stagger — H arrives first, the A diagonal follows in an offset Sequence.
5. Mask Reveal — clip-path wipe left-to-right, then a radial iris.
6. Scale Zoom — camera push from 8x down to fit; contrast linear vs bezier easing.
7. Rotation — pivot entrance, then a slow continuous rotate hold.
8. Skew And Shear — italic lean-in and release.
9. Opacity Through Blur — fade-through-blur entrance.
10. Color Interpolation — interpolateColors ink → terracotta → ink (labeled as a
    treatment beat, not brand law).
11. Kinetic Grid — the mark tiled across the frame, rippling on staggered delays.
12. Glitch Slices — horizontal slice offsets for ~8 frames, then snap clean.
13. Trail Echo — low-opacity motion-trail copies on a fast slide.
14. Noise Wobble — noise-driven micro-jitter that settles to stillness.
15. Elastic Physics — drop-in with scaleY squash and rebound.
16. Orbit Parts — the two paths separate, orbit each other, reunite into the mark.
17. Card Flip — perspective + rotateY, the logo on both faces.
18. Shadow Play — the shadow animates independently, then rejoins the mark.
19. Composer Summon — the mark "sent" from the Claude composer, terracotta spark
    on send (the one beat where the Claude UI is the subject).
20. Exit Family — three quick exits back-to-back: shrink-spin, blur-out, mask-close.

RULES

- Claude fidelity brand: cream #FAF9F5 page, warm ink #3D3929 text, terracotta
  #D97757 as the ONE accent per beat. Segment titles Title Case, never all caps.
- Every beat is motion, not text — no bullet slides.
- Reuse existing scene chrome (ClaudeComposerAsk, ClaudeTitleOutro) for the
  bookends; build technique beats as new composable scenes following the repo's
  existing showcase-video convention.

OUTPUTS

- youtube/claude-liam-h-logo-remotion-showcase/
  - beat_sheet.json
  - claude-liam-h-logo-remotion-showcase.mp4 (1080x1920)
  - TECHNIQUES.md — one row per beat: number, technique, start timestamp,
    scene file, and an empty keep/kill checkbox column for my review pass.
- Verify the mp4 exists and plays (probe duration and frame count) before
  reporting done, and end with the beat → timestamp table.
- If a technique fails to render after two attempts, replace its beat with a
  slate card naming the technique and log the failure in TECHNIQUES.md —
  never silently drop a technique.
```
