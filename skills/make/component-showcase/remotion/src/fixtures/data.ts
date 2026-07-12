import { staticFile } from 'remotion';

// Themed-educational fixtures for the DATA pilot. Theme: COMPUTATIONAL SKEPTICISM —
// "an AI model's confidence is not its accuracy." Each fixture overrides ONLY the
// content prop(s); onda's schema defaults fill everything else. Swap these numbers to
// re-theme the reel without touching the harness.
export const DATA_FIXTURES: Record<string, Record<string, unknown>> = {
  // FABRICATION rate by task (higher = worse). Citations is the MAX, so onda paints it with
  // the accent (red) — red lands on the exact bar the riff points at. Conformed timing
  // (duration/stagger slowed from onda's defaults) so the predict->event->resolve has room.
  'bar-chart': {
    data: [
      { label: 'Code', value: 18 },
      { label: 'Arithmetic', value: 29 },
      { label: 'Dates', value: 42 },
      { label: 'Citations', value: 66 },
    ],
    max: 100,
    duration: 60, // conform: slower than onda's 24f so events are seconds apart (RIFFING: flexible holds)
    stagger: 24,
  },
  // Accuracy drifts DOWN over a long chain of reasoning steps.
  'line-chart': { data: [61, 58, 60, 54, 49, 44, 39, 34] },
  // Share of confidently-stated answers that were actually wrong.
  'pie-reveal': { value: 38 },
  // Fabricated citations per 100 — counts up to the uncomfortable number.
  'count-up': { from: 0, to: 34, suffix: '%' },
  // How much of a "reasoning" benchmark is memorized, not reasoned.
  'progress-bar': { value: 42 },
  // The skeptic's loop — the four moves you run on any confident claim.
  'timeline': {
    points: [{ label: 'Claim' }, { label: 'Source?' }, { label: 'Check' }, { label: 'Verdict' }],
  },
  // VideoClip: use a local sample; the Onda default points to a GCS URL that returns 403.
  'video-clip': { src: staticFile('sample-clip.mp4'), startAt: 0, endAt: '5s', loop: true },
  // AudioClip / AudioVisualizer: external w3schools URL fails CORS during render; use local narration mp3.
  'audio-clip': { src: staticFile('audio/audio-clip-0.mp3'), loop: true },
  'audio-visualizer': { src: staticFile('audio/audio-visualizer-0.mp3') },
};
