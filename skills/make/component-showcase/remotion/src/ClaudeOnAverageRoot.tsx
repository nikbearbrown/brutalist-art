import React from 'react';
import { Composition } from 'remotion';
import { ClaudeOnAverage, TOTAL_FRAMES } from './ClaudeOnAverage';

export const ClaudeOnAverageRoot: React.FC = () => (
  <Composition
    id="claude-on-average"
    component={ClaudeOnAverage}
    durationInFrames={TOTAL_FRAMES}
    fps={30}
    width={1280}
    height={720}
  />
);
