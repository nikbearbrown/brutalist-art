import React from 'react';
import { Composition } from 'remotion';
import { ClaudeJudged, TOTAL_FRAMES } from './ClaudeJudged';

export const ClaudeJudgedRoot: React.FC = () => (
  <Composition
    id="claude-judged"
    component={ClaudeJudged}
    durationInFrames={TOTAL_FRAMES}
    fps={30}
    width={1280}
    height={720}
  />
);
