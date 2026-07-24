import React from 'react';
import { Composition } from 'remotion';
import { ClaudeSteered, TOTAL_FRAMES } from './ClaudeSteered';

export const ClaudeSteeredRoot: React.FC = () => (
  <Composition
    id="claude-steered"
    component={ClaudeSteered}
    durationInFrames={TOTAL_FRAMES}
    fps={30}
    width={1280}
    height={720}
  />
);
