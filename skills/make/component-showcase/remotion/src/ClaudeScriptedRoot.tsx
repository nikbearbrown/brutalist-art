import React from 'react';
import { Composition } from 'remotion';
import { ClaudeScripted, TOTAL_FRAMES } from './ClaudeScripted';

export const ClaudeScriptedRoot: React.FC = () => (
  <Composition
    id="claude-scripted"
    component={ClaudeScripted}
    durationInFrames={TOTAL_FRAMES}
    fps={30}
    width={1280}
    height={720}
  />
);
