import React from 'react';
import { Composition } from 'remotion';
import { HaiReel } from './HaiReel';
import dataH1 from './hai-claude-allowed-data.json';
import dataH2 from './hai-not-your-answer-data.json';
import dataH3 from './hai-your-quizmaster-data.json';
import dataH4 from './hai-on-the-job-data.json';
import dataH5 from './hai-when-not-data.json';

export const HaiRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="hai-claude-allowed"
        component={HaiReel}
        durationInFrames={(dataH1 as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataH1 }}
      />
      <Composition
        id="hai-not-your-answer"
        component={HaiReel}
        durationInFrames={(dataH2 as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataH2 }}
      />
      <Composition
        id="hai-your-quizmaster"
        component={HaiReel}
        durationInFrames={(dataH3 as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataH3 }}
      />
      <Composition
        id="hai-on-the-job"
        component={HaiReel}
        durationInFrames={(dataH4 as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataH4 }}
      />
      <Composition
        id="hai-when-not"
        component={HaiReel}
        durationInFrames={(dataH5 as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataH5 }}
      />
    </>
  );
};
