import React from 'react';
import { Composition } from 'remotion';
import { Ai1PitchReel, AI1_VIDEOS } from './Ai1PitchReel';

export const Ai1PitchRoot: React.FC = () => (
  <>
    {AI1_VIDEOS.map((v) => (
      <Composition
        key={v.slug}
        id={v.compId}
        component={Ai1PitchReel as any}
        defaultProps={{ slug: v.slug }}
        durationInFrames={v.totalFrames}
        fps={30}
        width={1280}
        height={720}
      />
    ))}
  </>
);
