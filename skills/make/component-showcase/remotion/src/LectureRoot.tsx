import React from 'react';
import { Composition } from 'remotion';
import { HaiReel } from './HaiReel';
import dataAi1IntoCanvas from './ai1-into-canvas-lecture-data.json';
import dataAi1Overview from './ai1-overview-lecture-data.json';
import dataAi1TheCanon from './ai1-the-canon-lecture-data.json';
import dataAi1YourVersion from './ai1-your-version-lecture-data.json';
import dataHaiClaudeAllowed from './hai-claude-allowed-lecture-data.json';
import dataHaiNotYourAnswer from './hai-not-your-answer-lecture-data.json';
import dataHaiOnTheJob from './hai-on-the-job-lecture-data.json';
import dataHaiWhenNot from './hai-when-not-lecture-data.json';
import dataHaiYourQuizmaster from './hai-your-quizmaster-lecture-data.json';
import dataMedhavyInTheClassroom from './medhavy-in-the-classroom-lecture-data.json';
import dataMedhavyNotTheTeacher from './medhavy-not-the-teacher-lecture-data.json';
import dataMedhavyOnTheHinge from './medhavy-on-the-hinge-lecture-data.json';
import dataMedhavyPreparingClass from './medhavy-preparing-class-lecture-data.json';
import dataMedhavyTrainedLikeDoctors from './medhavy-trained-like-doctors-lecture-data.json';
import dataMcpAlreadyBuilt from './mcp-already-built-lecture-data.json';
import dataMcpByDesign from './mcp-by-design-lecture-data.json';
import dataMcpInYourHands from './mcp-in-your-hands-lecture-data.json';
import dataMcpOverview from './mcp-overview-lecture-data.json';
import dataMcpTheBusiness from './mcp-the-business-lecture-data.json';
import dataMcpTheConnector from './mcp-the-connector-lecture-data.json';
import dataMcpTheProblem from './mcp-the-problem-lecture-data.json';

export const LectureRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="ai1-into-canvas-lecture"
        component={HaiReel}
        durationInFrames={(dataAi1IntoCanvas as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataAi1IntoCanvas }}
      />
      <Composition
        id="ai1-overview-lecture"
        component={HaiReel}
        durationInFrames={(dataAi1Overview as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataAi1Overview }}
      />
      <Composition
        id="ai1-the-canon-lecture"
        component={HaiReel}
        durationInFrames={(dataAi1TheCanon as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataAi1TheCanon }}
      />
      <Composition
        id="ai1-your-version-lecture"
        component={HaiReel}
        durationInFrames={(dataAi1YourVersion as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataAi1YourVersion }}
      />
      <Composition
        id="hai-claude-allowed-lecture"
        component={HaiReel}
        durationInFrames={(dataHaiClaudeAllowed as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataHaiClaudeAllowed }}
      />
      <Composition
        id="hai-not-your-answer-lecture"
        component={HaiReel}
        durationInFrames={(dataHaiNotYourAnswer as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataHaiNotYourAnswer }}
      />
      <Composition
        id="hai-on-the-job-lecture"
        component={HaiReel}
        durationInFrames={(dataHaiOnTheJob as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataHaiOnTheJob }}
      />
      <Composition
        id="hai-when-not-lecture"
        component={HaiReel}
        durationInFrames={(dataHaiWhenNot as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataHaiWhenNot }}
      />
      <Composition
        id="hai-your-quizmaster-lecture"
        component={HaiReel}
        durationInFrames={(dataHaiYourQuizmaster as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataHaiYourQuizmaster }}
      />
      <Composition
        id="medhavy-in-the-classroom-lecture"
        component={HaiReel}
        durationInFrames={(dataMedhavyInTheClassroom as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataMedhavyInTheClassroom }}
      />
      <Composition
        id="medhavy-not-the-teacher-lecture"
        component={HaiReel}
        durationInFrames={(dataMedhavyNotTheTeacher as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataMedhavyNotTheTeacher }}
      />
      <Composition
        id="medhavy-on-the-hinge-lecture"
        component={HaiReel}
        durationInFrames={(dataMedhavyOnTheHinge as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataMedhavyOnTheHinge }}
      />
      <Composition
        id="medhavy-preparing-class-lecture"
        component={HaiReel}
        durationInFrames={(dataMedhavyPreparingClass as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataMedhavyPreparingClass }}
      />
      <Composition
        id="medhavy-trained-like-doctors-lecture"
        component={HaiReel}
        durationInFrames={(dataMedhavyTrainedLikeDoctors as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataMedhavyTrainedLikeDoctors }}
      />
      <Composition
        id="mcp-already-built-lecture"
        component={HaiReel}
        durationInFrames={(dataMcpAlreadyBuilt as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataMcpAlreadyBuilt }}
      />
      <Composition
        id="mcp-by-design-lecture"
        component={HaiReel}
        durationInFrames={(dataMcpByDesign as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataMcpByDesign }}
      />
      <Composition
        id="mcp-in-your-hands-lecture"
        component={HaiReel}
        durationInFrames={(dataMcpInYourHands as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataMcpInYourHands }}
      />
      <Composition
        id="mcp-overview-lecture"
        component={HaiReel}
        durationInFrames={(dataMcpOverview as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataMcpOverview }}
      />
      <Composition
        id="mcp-the-business-lecture"
        component={HaiReel}
        durationInFrames={(dataMcpTheBusiness as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataMcpTheBusiness }}
      />
      <Composition
        id="mcp-the-connector-lecture"
        component={HaiReel}
        durationInFrames={(dataMcpTheConnector as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataMcpTheConnector }}
      />
      <Composition
        id="mcp-the-problem-lecture"
        component={HaiReel}
        durationInFrames={(dataMcpTheProblem as any).totalFrames}
        fps={30}
        width={1280}
        height={720}
        defaultProps={{ data: dataMcpTheProblem }}
      />
    </>
  );
};
