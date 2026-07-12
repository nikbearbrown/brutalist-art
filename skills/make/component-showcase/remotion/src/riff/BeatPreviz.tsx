import React from 'react';
import { AbsoluteFill, Sequence } from 'remotion';
import { OndaScene } from '../harness/OndaScene';
import { DATA_FIXTURES } from '../fixtures/data';
import { DATA_RIFFS } from './riffs.data';
import { barChartSchedule, barChartBeats, type BarDatum } from '../schedule/schedule';
import { BeatCaption } from './BeatCaption';

// Timing previz: the live bar-chart (conformed timing) with the beat captions burned in at
// their computed frames — captions stand in for the NBB voice so you can verify the words
// land on the events BEFORE any ElevenLabs spend. predict fires ~0.9s before Citations
// settles (E3); event is silence at E3; resolve lands ~0.3s after.
export const PREVIZ_FPS = 30;

const fx = DATA_FIXTURES['bar-chart'] as { data: BarDatum[]; duration: number; stagger: number };
const SCHED = barChartSchedule(fx.data, { duration: fx.duration, stagger: fx.stagger });
const BEATS = barChartBeats(SCHED, DATA_RIFFS['bar-chart'], PREVIZ_FPS);
// last visible frame across all beats, + a small tail
export const PREVIZ_FRAMES =
  Math.max(...BEATS.map((b) => b.frame + (b.hold || 0))) + 20;

export const BeatPreviz: React.FC = () => (
  <AbsoluteFill>
    <OndaScene slug="bar-chart" />
    {BEATS.filter((b) => b.text).map((b, i) => (
      <Sequence key={i} from={Math.max(0, b.frame)} durationInFrames={b.hold || 1}>
        <BeatCaption beat={b} />
      </Sequence>
    ))}
  </AbsoluteFill>
);
