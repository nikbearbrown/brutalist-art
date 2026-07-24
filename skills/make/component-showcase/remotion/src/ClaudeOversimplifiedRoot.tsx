import React from 'react';
import { Composition } from 'remotion';
import { ClaudeOversimplified, TOTAL_FRAMES } from './ClaudeOversimplified';

export const ClaudeOversimplifiedRoot: React.FC = () => (
  <Composition
    id="claude-oversimplified"
    component={ClaudeOversimplified}
    durationInFrames={TOTAL_FRAMES}
    fps={30}
    width={1280}
    height={720}
  />
);
