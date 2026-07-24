import React from 'react';
import { Composition } from 'remotion';
import { HaiReel } from './HaiReel';
import dataM1 from './medhavy-in-the-classroom-data.json';
import dataM2 from './medhavy-on-the-hinge-data.json';
import dataM3 from './medhavy-preparing-class-data.json';
import dataM4 from './medhavy-not-the-teacher-data.json';
import dataM5 from './medhavy-trained-like-doctors-data.json';

export const MedhavySeriesRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="medhavy-in-the-classroom"
        component={HaiReel}
        durationInFrames={(dataM1 as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataM1 }}
      />
      <Composition
        id="medhavy-on-the-hinge"
        component={HaiReel}
        durationInFrames={(dataM2 as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataM2 }}
      />
      <Composition
        id="medhavy-preparing-class"
        component={HaiReel}
        durationInFrames={(dataM3 as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataM3 }}
      />
      <Composition
        id="medhavy-not-the-teacher"
        component={HaiReel}
        durationInFrames={(dataM4 as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataM4 }}
      />
      <Composition
        id="medhavy-trained-like-doctors"
        component={HaiReel}
        durationInFrames={(dataM5 as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataM5 }}
      />
    </>
  );
};
