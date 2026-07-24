import React from 'react';
import { Composition } from 'remotion';
import { ClaudeUnsupervised, TOTAL_FRAMES } from './ClaudeUnsupervised';

export const ClaudeUnsupervisedRoot: React.FC = () => (
  <Composition
    id="claude-unsupervised"
    component={ClaudeUnsupervised}
    durationInFrames={TOTAL_FRAMES}
    fps={30}
    width={1280}
    height={720}
  />
);
