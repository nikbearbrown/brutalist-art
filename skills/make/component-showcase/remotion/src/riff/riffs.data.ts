// The riff scripts — NikBearBrown / Teardown register. Seeded from each onda
// component's meta.json (description + pickWhen), sharpened into the teardown read:
// what it does, one pro, one con, and the teaching use. On-screen text for v1 (no
// ElevenLabs spend yet); these same strings become the VO script when you approve them.
export type Riff = {
  title: string;
  does: string;
  pro: string;
  con: string;
  edu: string;
};

export const DATA_RIFFS: Record<string, Riff> = {
  'bar-chart': {
    title: 'BarChart',
    does: 'Horizontal bars grow from zero on a calm spring; the biggest bar earns the one accent, the rest stay ink.',
    pro: 'Instant ranking. The eye finds the outlier before you say a word.',
    con: 'Dies past ~8 bars — it becomes a table pretending to be a chart.',
    edu: 'Best for "these are not equal." Here: how often a model fabricates by task — Citations towers, and red lands right on it.',
  },
  'line-chart': {
    title: 'LineChart',
    does: 'A single series strokes on left-to-right, drawing the trend as it goes.',
    pro: 'Shows direction and rate — the shape of change, not just endpoints.',
    con: 'One line, one story. Multi-series turns it into spaghetti fast.',
    edu: 'Best for "watch this move." Here: accuracy decaying across a long reasoning chain — the drop is the lesson.',
  },
  'pie-reveal': {
    title: 'PieReveal',
    does: 'One wedge sweeps in against the whole — a single share, revealed.',
    pro: 'Reads as "part of a whole" faster than any bar for one number.',
    con: 'Useless past one or two slices; humans can not compare wedge angles.',
    edu: 'Best for "how much of the whole." Here: the slice of confident answers that were flat wrong.',
  },
  'count-up': {
    title: 'CountUp',
    does: 'A number ticks from a start to a target and stops — one figure, earned.',
    pro: 'A rising number pulls the eye and lands an emotional beat on the value.',
    con: 'Pure spectacle with no context — it needs a label doing real work.',
    edu: 'Best for "one number that should sting." Here: fabricated citations per hundred, climbing to 34%.',
  },
  'progress-bar': {
    title: 'ProgressBar',
    does: 'A track fills to a percentage and holds — proportion as a single strip.',
    pro: 'Dead-simple "how far / how much," legible at a glance and tiny sizes.',
    con: 'Low information density — one number wearing a whole scene.',
    edu: 'Best for "a fraction of a known whole." Here: how much of a reasoning benchmark is memorized, not reasoned.',
  },
  'timeline': {
    title: 'Timeline',
    does: 'A line strokes on and anchor points pop in order, left to right.',
    pro: 'Makes sequence and order legible — first this, then that.',
    con: 'Says nothing about duration or weight; every step looks equal.',
    edu: 'Best for "the steps, in order." Here: the skeptic’s loop — Claim, Source?, Check, Verdict.',
  },
};
