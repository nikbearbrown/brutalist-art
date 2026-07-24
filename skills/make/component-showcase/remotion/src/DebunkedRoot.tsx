import React from 'react';
import { Composition } from 'remotion';
import { DebunkedReel, DEBUNKED_TOTAL_FRAMES } from './DebunkedReel';

export const DebunkedRoot: React.FC = () => (
  <Composition
    id="ClaudeDebunked"
    component={DebunkedReel}
    durationInFrames={DEBUNKED_TOTAL_FRAMES}
    fps={30}
    width={1280}
    height={720}
  />
);
