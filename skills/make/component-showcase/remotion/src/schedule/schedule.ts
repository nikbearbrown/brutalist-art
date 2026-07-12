// Schedule extractor + beat generator for the onda bar-chart (RIFFING.md: perception must
// yield a *schedule*). Declared-truth: a bar grows over `duration` starting at
// `delay + i*stagger`, so bar i finishes at `delay + i*stagger + duration`. onda paints the
// accent on the LARGEST-value bar — that bar is the riff's subject (the outlier we point at).
// Timing here is the CONFORMED timing (from the fixture), slowed so the beats have room.

export type BarDatum = { label: string; value: number };
export type SceneEvent = { id: string; frame: number; desc: string };
export type Schedule = { finishes: number[]; accentIndex: number; events: SceneEvent[] };

export function barChartSchedule(
  data: BarDatum[],
  opts: { delay?: number; stagger: number; duration: number },
): Schedule {
  const { delay = 0, stagger, duration } = opts;
  const finishes = data.map((_, i) => delay + i * stagger + duration);
  const accentIndex = data.reduce((m, d, i, a) => (d.value > a[m].value ? i : m), 0);
  return {
    finishes,
    accentIndex,
    events: [
      { id: 'E1', frame: 0, desc: 'bars empty, labels set' },
      { id: 'E2', frame: finishes[0], desc: 'first bar settles' },
      {
        id: 'E3',
        frame: finishes[accentIndex],
        desc: `${data[accentIndex].label} settles — the outlier, red (tallest)`,
      },
    ],
  };
}

export type Beat = {
  type: 'reactive' | 'predict' | 'event' | 'resolve' | 'analytic' | 'outro-topic' | 'outro-channel';
  frame: number; // absolute start frame
  hold: number; // frames the caption stays up (0 = silence)
  text: string;
  deixis?: boolean;
  source?: string;
  sub?: string; // outro-topic: overrides the centered card's uppercase subtitle
};

// Build the beat sheet against the schedule. lead/lag are in ms → frames at fps.
// predict→event→resolve straddles E3 (the outlier); analytic fills the held gap after;
// the two outro beats are the mandatory always-Remotion tail (RIFFING.md).
export function barChartBeats(sched: Schedule, riff: { does: string; con: string }, fps = 30): Beat[] {
  const ms = (m: number) => Math.round((m / 1000) * fps);
  const E2 = sched.events[1].frame;
  const E3 = sched.events[2].frame;
  return [
    { type: 'reactive', frame: E2 + ms(-1600), hold: 52, deixis: true, text: 'watch these fill in' },
    { type: 'predict', frame: E3 + ms(-900), hold: 30, text: 'the last one should worry you' },
    { type: 'event', frame: E3, hold: 0, text: '' }, // observational silence
    { type: 'resolve', frame: E3 + ms(300), hold: 60, deixis: true, text: 'there it is — citations. two-thirds, made up' },
    { type: 'analytic', frame: E3 + 30, hold: 100, text: `${riff.does} ${riff.con}` },
    { type: 'outro-topic', frame: E3 + 135, hold: 70, source: 'ABOUT.MD', text: 'computational skepticism — the series' },
    { type: 'outro-channel', frame: E3 + 210, hold: 70, source: 'AUTHOR.MD', text: 'Nik Bear Brown — more teardowns next' },
  ];
}
