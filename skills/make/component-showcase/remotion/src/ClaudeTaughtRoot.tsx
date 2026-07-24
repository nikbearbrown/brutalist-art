import React from 'react';
import { Composition } from 'remotion';
import { ClaudeTaught, TOTAL_FRAMES } from './ClaudeTaught';

export const ClaudeTaughtRoot: React.FC = () => (
  <Composition
    id="claude-taught"
    component={ClaudeTaught}
    durationInFrames={TOTAL_FRAMES}
    fps={30}
    width={1280}
    height={720}
  />
);
