import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile } from 'remotion';
import { ClaudeComposerAsk, claudeComposerAskSchema } from '../../../../../../brutalist-art/runtime/remotion/src/scenes/ClaudeComposerAsk';
import { ClaudeVerdictArtifact, claudeVerdictArtifactSchema } from '../../../../../../brutalist-art/runtime/remotion/src/scenes/ClaudeVerdictArtifact';
import { ClaudeTitleOutro, claudeTitleOutroSchema } from '../../../../../../brutalist-art/runtime/remotion/src/scenes/ClaudeTitleOutro';
import { PredictCard, IlluStage } from './TeachersIllustrations';
import {
  TwoColumnCard, ThreeCardFlow, ContrastBoxes, ConceptCard,
  ListCard, PairRuleCard, TimelineCard, SeasonDeckCard,
  TierDiagram, DivergentFatesBeat,
} from './SeriesIllustrations';

export const HaiReel: React.FC<{ data: any }> = ({ data }) => {
  let at = 0;
  const seqs = (data.beats as any[]).map((b) => {
    const from = at;
    at += b.frames;
    let content: React.ReactNode = null;

    switch (b.kind) {
      case 'ClaudeComposerAsk':
        content = <ClaudeComposerAsk {...claudeComposerAskSchema.parse(b.props)} />;
        break;
      case 'ClaudeVerdictArtifact':
        content = <ClaudeVerdictArtifact {...claudeVerdictArtifactSchema.parse(b.props)} />;
        break;
      case 'ClaudeTitleOutro':
        content = <ClaudeTitleOutro {...claudeTitleOutroSchema.parse(b.props)} />;
        break;

      // Two-column cards — covered/open, banned/open, scaffold/crutch, etc.
      case 'HaiBanCoverageCard':
        content = <TwoColumnCard
          sparkLine={b.props.sparkLine}
          leftHeader={b.props.leftHeader ?? 'the ban covers'}
          rightHeader={b.props.rightHeader ?? 'still open to you'}
          coveredItems={b.props.coveredItems}
          openItems={b.props.openItems}
          evidenceNote={b.props.evidenceNote}
        />;
        break;
      case 'HaiOpenZoneGrid':
        content = <TwoColumnCard
          sparkLine={b.props.sparkLine}
          leftHeader={b.props.leftHeader ?? 'banned zone'}
          rightHeader={b.props.rightHeader ?? 'open to you'}
          bannedItems={b.props.bannedItems}
          openItems={b.props.openItems}
          evidenceNote={b.props.evidenceNote}
        />;
        break;
      case 'HaiTwoColumnCard':
      case 'MedhavyTwoColumnCard':
        content = <TwoColumnCard {...b.props} />;
        break;

      // Three-step card flow (exemption trap, sequential reasoning)
      case 'HaiExemptionTrap':
      case 'HaiThreeCardFlow':
      case 'MedhavyThreeCardFlow':
        content = <ThreeCardFlow {...b.props} />;
        break;

      // Predict beat
      case 'HaiPredictCard':
      case 'MedhavyPredictCard':
        content = (
          <IlluStage spark={b.props.sparkLine}>
            <PredictCard question={b.props.question} commit={b.props.commit} />
          </IlluStage>
        );
        break;

      // Two-box contrast (reveal beats)
      case 'HaiRevealContrast':
      case 'MedhavyContrastBoxes':
        content = <ContrastBoxes {...b.props} />;
        break;

      // Single concept card
      case 'HaiConceptCard':
      case 'MedhavyConceptCard':
        content = <ConceptCard {...b.props} />;
        break;

      // List card
      case 'HaiListCard':
      case 'MedhavyListCard':
        content = <ListCard {...b.props} />;
        break;

      // AI-yes / not-AI-here pair rule
      case 'HaiPairRule':
      case 'HaiPairRuleCard':
      case 'MedhavyPairRuleCard':
        content = <PairRuleCard {...b.props} />;
        break;

      // Spaced-repetition timeline
      case 'HaiTimelineCard':
      case 'MedhavyTimelineCard':
        content = <TimelineCard {...b.props} />;
        break;

      // Episode recap deck
      case 'HaiSeasonDeck':
      case 'HaiSeasonDeckCard':
      case 'MedhavySeasonDeckCard':
        content = <SeasonDeckCard {...b.props} />;
        break;

      // 4-tier taxonomy diagram
      case 'HaiTierDiagram':
      case 'MedhavyTierDiagram':
        content = <TierDiagram {...b.props} />;
        break;

      // Divergent fates (Bastani data in H2/M episodes)
      case 'HaiDivergentFates':
      case 'MedhavyDivergentFates':
        content = <DivergentFatesBeat {...b.props} />;
        break;

      default:
        content = null;
    }

    return (
      <Sequence key={b.id} from={from} durationInFrames={b.frames}>
        {content}
        <Audio src={staticFile(b.audio)} />
      </Sequence>
    );
  });

  return <AbsoluteFill style={{ background: '#F2F0E9' }}>{seqs}</AbsoluteFill>;
};
