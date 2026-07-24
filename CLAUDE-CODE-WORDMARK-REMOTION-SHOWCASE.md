# Claude Code Prompt — HAI Wordmark Remotion Showcase (9:16, claude-liam)

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace.

```text
Build one long-form 9:16 vertical Remotion video that animates
logos/HUMANITARIANS-AI-wordmark.svg every way Remotion can — a
technique-showcase reel in the Claude explainer skin, claude-liam channel. The
purpose is REVIEW: I need to SEE each move to judge which ones work. Free
pipeline only: Kokoro voice, no ElevenLabs, no higgsfield, no publishing, no
git commit or push. Run without approval pauses (no paid spend is possible
under these constraints).

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md
- skills/make/explainer/SKILL.md (and the MOTION.md / REMOTION.md it points to)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts

CRITICAL PRE-STEP — OUTLINE THE TEXT

The wordmark's letters are live <text> elements set in Arial-BoldMT. Rendering
them as-is makes the output font-environment-dependent. Before any animation:
convert every glyph to outline paths (local tooling of your choice — e.g. a
headless browser + opentype conversion, or Inkscape CLI if available) and save
the result as logos/HUMANITARIANS-AI-wordmark.outlined.svg. Verify visually
against the original (overlay diff) before proceeding. Animate ONLY the
outlined version, one path per glyph, so letters can be driven individually.
The two custom ligature marks (the leading H and the trailing AI diagonal) are
already paths — keep them as distinct elements.

FORMAT

- 1080x1920 (9:16), 30 fps.
- Channel claude-liam: persona Liam (in for Bear), folder chip @NikBearBrown,
  voice Kokoro am_onyx, register Teardown. Do not use ElevenLabs.
- Audio-first: generate and measure Liam's narration per beat FIRST; conform
  every beat's duration to its audio.
- Length is derived from the beat count, not a fixed clock. Expect roughly
  2.5–4 minutes.

THE VERTICAL PROBLEM (make it a feature)

The wordmark is ultra-wide (1060x133) and the frame is tall. Do not letterbox
it small and call it done — the layout strategies ARE showcase beats:

A. Marquee Scroll — full-size wordmark tracking horizontally through the frame.
B. Stacked Break — split to "HUMANITARIANS" over "AI", each line sized to the width.
C. Rotate Vertical — the wordmark set 90°, running up the frame like a spine.
D. Focus Crop — camera pans along the word at full scale, ending on the AI ligature.

Every other technique beat picks whichever of these layouts shows the move best,
and names it in the on-screen label's subline.

STRUCTURE (claude-explainer skeleton)

- Beat 0 — ClaudeComposerAsk cold open. Liam frames the question: one wordmark,
  every move Remotion knows — which ones deserve to live?
- Middle — ONE TECHNIQUE PER BEAT. Every technique beat must show:
  1. the technique name on screen as a Title Case segment label (EB Garamond,
     terracotta underline — the one accent),
  2. the wordmark actually performing the technique,
  3. one short Liam line naming the move and what to judge it by.
- Second-to-last — Your Turn composer beat with a suggested prompt typed in.
- Last — @NikBearBrown brand card, title restated.

TECHNIQUE CATALOG (minimum one beat each; add more only if they render cleanly)

1. Letter Cascade — per-glyph spring entrance, left to right stagger.
2. Word Slam — "HUMANITARIANS" lands, then "AI" slams in with screen shake.
3. Draw-On Glyphs — evolvePath() traces each outlined letter, then fill flood.
4. Baseline Wave — letters ride a traveling sine wave, then settle.
5. Tracking Breathe — letter-spacing expands wide and contracts to spec.
6. Typewriter — glyphs appear one per tick with a terracotta caret.
7. Mask Wipe — clip-path sweep along the word, both directions.
8. Highlight Sweep — a light band passes across the ink, one pass only.
9. Ligature Spotlight — camera isolates the leading H mark and trailing AI
   diagonal; they counter-rotate, the plain letters dim to 20%.
10. Per-Letter Flip — rotateX cards, each glyph flipping in sequence.
11. Scale Focus — push from the full word into a single glyph and back.
12. Blur Depth — front-to-back rack focus across the word (per-glyph blur).
13. Color Interpolation — interpolateColors ink → terracotta → ink, sweeping
    letter by letter (labeled as a treatment beat, not brand law).
14. Elastic Physics — the word drops in, squashes, rebounds as a unit.
15. Glitch Slices — horizontal slice offsets across the word, snap clean.
16. Kinetic Stack — the stacked-break layout ripples line against line.
17. Marquee Loop — the full-size marquee at three speeds, cut on the beat.
18. Assembly — glyphs fly in from scattered positions/rotations to their slots.
19. Exit Family — three quick exits back-to-back: letter-drop, blur-out, wipe-close.

RULES

- Claude fidelity brand: cream #FAF9F5 page, warm ink #3D3929 text, terracotta
  #D97757 as the ONE accent per beat. Wordmark ink stays #171717 except beat 13.
- Segment titles Title Case, never all caps. Every beat is motion, not text —
  no bullet slides.
- Reuse existing scene chrome (ClaudeComposerAsk, ClaudeTitleOutro) for the
  bookends; build technique beats as new composable scenes following the repo's
  existing showcase-video convention.
- Never modify logos/HUMANITARIANS-AI-wordmark.svg itself; the outlined copy is
  a new file.

OUTPUTS

- youtube/claude-liam-hai-wordmark-remotion-showcase/
  - beat_sheet.json
  - claude-liam-hai-wordmark-remotion-showcase.mp4 (1080x1920)
  - TECHNIQUES.md — one row per beat: number, technique, layout used (A/B/C/D),
    start timestamp, scene file, and an empty keep/kill checkbox column.
- logos/HUMANITARIANS-AI-wordmark.outlined.svg (the outlined conversion).
- Verify the mp4 exists and plays (probe duration and frame count) before
  reporting done, and end with the beat → timestamp table.
- If a technique fails to render after two attempts, replace its beat with a
  slate card naming the technique and log the failure in TECHNIQUES.md —
  never silently drop a technique.
```
