import React from 'react';
import { Composition } from 'remotion';
import { MedPitchReel, PITCH_VIDEOS } from './MedPitchReel';

export const MedPitchRoot: React.FC = () => (
  <>
    {PITCH_VIDEOS.map((v) => (
      <Composition
        key={v.slug}
        id={v.compId}
        component={MedPitchReel as any}
        defaultProps={{ slug: v.slug }}
        durationInFrames={v.totalFrames}
        fps={30}
        width={1280}
        height={720}
      />
    ))}
  </>
);
