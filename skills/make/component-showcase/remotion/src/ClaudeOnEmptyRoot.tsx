import React from 'react';
import { Composition } from 'remotion';
import { ClaudeOnEmpty, TOTAL_FRAMES } from './ClaudeOnEmpty';

export const ClaudeOnEmptyRoot: React.FC = () => (
  <Composition
    id="claude-on-empty"
    component={ClaudeOnEmpty}
    durationInFrames={TOTAL_FRAMES}
    fps={30}
    width={1280}
    height={720}
  />
);
