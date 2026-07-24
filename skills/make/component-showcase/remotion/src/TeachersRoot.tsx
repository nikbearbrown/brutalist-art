import React from 'react';
import { Composition } from 'remotion';
import { TeachersReel, TEACHERS_TOTAL_FRAMES } from './TeachersReel';

export const TeachersRoot: React.FC = () => (
  <Composition
    id="ClaudeForTeachers"
    component={TeachersReel}
    durationInFrames={TEACHERS_TOTAL_FRAMES}
    fps={30}
    width={1280}
    height={720}
  />
);
