import React from 'react';
import {AbsoluteFill, Sequence, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {ClaudeComposerAsk, claudeComposerAskSchema} from './scenes/ClaudeComposerAsk';
import {ClaudeVerdictArtifact} from './scenes/ClaudeVerdictArtifact';
import {ClaudeVerdictArtifact916} from './scenes/ClaudeVerdictArtifact916';
import {ClaudeTitleOutro} from './scenes/ClaudeTitleOutro';
import {ClaudeTitleOutro916} from './scenes/ClaudeTitleOutro916';

import {MusiniqueLogo2RemotionShowcase16x9} from './MusiniqueLogo2RemotionShowcase16x9';
import {MusiniqueLogo2RemotionShowcase} from './MusiniqueLogo2RemotionShowcase';
import {MusiniquLogoShowcase169} from './MusiniquLogoShowcase169';
import {MusiniquLogoRemotionShowcase} from './MusiniquLogoRemotionShowcase';
import {BearBrownLogoRemotionShowcase16x9} from './BearBrownLogoRemotionShowcase16x9';
import {BearBrownLogoRemotionShowcase} from './BearBrownLogoRemotionShowcase';
import {BearBrownInitialsShowcase169} from './BearBrownInitialsShowcase169';
import {BearBrownInitialsShowcase} from './BearBrownInitialsShowcase';
import {HLogoRemotionShowcase169} from './HLogoRemotionShowcase169';
import {HLogoRemotionShowcase} from './HLogoRemotionShowcase';
import {HaiWordmarkShowcase16x9} from './HaiWordmarkShowcase16x9';
import {HaiWordmarkShowcase} from './HaiWordmarkShowcase';

/**
 * ShowcaseWrap — parameterized bookend wrapper for the logo-technique
 * showcase comps (the Brutalist meta-series "how every scene is built").
 *
 * The monolithic showcase compositions stay UNTOUCHED. This comp windows
 * into one of them ([bodyStartFrame, bodyEndFrame), negative-offset
 * Sequence) and adds the standard ai-explainer bookends around it:
 *
 *   [intro?] -> body window -> [verdict?] -> [yourTurn?] -> [titleOut?]
 *
 * Every bookend is optional (null = omitted), so ONE comp serves both:
 *  - the 16:9 full cuts: body = comp minus its old ending, then
 *    verdict -> Your Turn -> title re-read (the your-turn three-beat block);
 *  - the 9:16 one-minute episodes: body = 4-technique window, micro intro
 *    (episodes 2+) + Your Turn + title card.
 *
 * Durations (durationF) come from the MEASURED Kokoro mp3s — audio-first;
 * runtime/scripts/showcase_episodes.py computes the props and the audio
 * concat. Register at both aspects; the component picks the portrait scene
 * variants via useVideoConfig.
 */

const MARKS = z.enum([
  'musinique-logo-2',
  'musinique-logo',
  'bear-brown-logo',
  'bear-brown-initials',
  'h-logo',
  'hai-wordmark',
]);

const REGISTRY: Record<z.infer<typeof MARKS>, {landscape: React.FC; portrait: React.FC}> = {
  'musinique-logo-2': {landscape: MusiniqueLogo2RemotionShowcase16x9, portrait: MusiniqueLogo2RemotionShowcase},
  'musinique-logo': {landscape: MusiniquLogoShowcase169, portrait: MusiniquLogoRemotionShowcase},
  'bear-brown-logo': {landscape: BearBrownLogoRemotionShowcase16x9, portrait: BearBrownLogoRemotionShowcase},
  'bear-brown-initials': {landscape: BearBrownInitialsShowcase169, portrait: BearBrownInitialsShowcase},
  'h-logo': {landscape: HLogoRemotionShowcase169, portrait: HLogoRemotionShowcase},
  'hai-wordmark': {landscape: HaiWordmarkShowcase16x9, portrait: HaiWordmarkShowcase},
};

const askBlock = z.object({
  greeting: z.string().default(''),
  command: z.string().default(''),
  topic: z.string().default(''),
  segment: z.string().default(''),
  runningText: z.string().default(''),
  output: z.array(z.string()).default([]),
  folderLabel: z.string().default('@NikBearBrown'),
  durationF: z.number().int(),
});

export const showcaseWrapSchema = z.object({
  mark: MARKS,
  bodyStartFrame: z.number().int().default(0),
  bodyEndFrame: z.number().int(),
  intro: askBlock.nullable().default(null),
  verdict: z
    .object({
      artifactTitle: z.string(),
      artifactHeading: z.string(),
      artifactLines: z.array(z.string()),
      durationF: z.number().int(),
    })
    .nullable()
    .default(null),
  yourTurn: askBlock.nullable().default(null),
  titleOut: z
    .object({
      title: z.string(),
      handle: z.string().default('@NikBearBrown'),
      subline: z.string().default(''),
      durationF: z.number().int(),
    })
    .nullable()
    .default(null),
});

export type ShowcaseWrapProps = z.infer<typeof showcaseWrapSchema>;

/** Total wrapper duration in frames — used by Root's calculateMetadata. */
export const showcaseWrapDuration = (p: ShowcaseWrapProps): number =>
  (p.intro?.durationF ?? 0) +
  Math.max(1, p.bodyEndFrame - p.bodyStartFrame) +
  (p.verdict?.durationF ?? 0) +
  (p.yourTurn?.durationF ?? 0) +
  (p.titleOut?.durationF ?? 0);

export const ShowcaseWrap: React.FC<ShowcaseWrapProps> = (props) => {
  const {width, height} = useVideoConfig();
  const portrait = height > width;
  const Body = REGISTRY[props.mark][portrait ? 'portrait' : 'landscape'];
  const Verdict = portrait ? ClaudeVerdictArtifact916 : ClaudeVerdictArtifact;
  const Title = portrait ? ClaudeTitleOutro916 : ClaudeTitleOutro;

  const bodyF = Math.max(1, props.bodyEndFrame - props.bodyStartFrame);
  let at = 0;
  const introFrom = at;
  at += props.intro?.durationF ?? 0;
  const bodyFrom = at;
  at += bodyF;
  const verdictFrom = at;
  at += props.verdict?.durationF ?? 0;
  const yourTurnFrom = at;
  at += props.yourTurn?.durationF ?? 0;
  const titleFrom = at;

  return (
    <AbsoluteFill style={{backgroundColor: '#FAF9F5'}}>
      {props.intro && (
        <Sequence from={introFrom} durationInFrames={props.intro.durationF}>
          <ClaudeComposerAsk
            {...claudeComposerAskSchema.parse({
              greeting: props.intro.greeting,
              command: props.intro.command,
              topic: props.intro.topic,
              segment: props.intro.segment,
              runningText: props.intro.runningText,
              output: props.intro.output,
              folderLabel: props.intro.folderLabel,
            })}
          />
        </Sequence>
      )}

      <Sequence from={bodyFrom} durationInFrames={bodyF}>
        <Sequence from={-props.bodyStartFrame}>
          <Body />
        </Sequence>
      </Sequence>

      {props.verdict && (
        <Sequence from={verdictFrom} durationInFrames={props.verdict.durationF}>
          <Verdict
            artifactTitle={props.verdict.artifactTitle}
            artifactHeading={props.verdict.artifactHeading}
            artifactLines={props.verdict.artifactLines}
          />
        </Sequence>
      )}

      {props.yourTurn && (
        <Sequence from={yourTurnFrom} durationInFrames={props.yourTurn.durationF}>
          <ClaudeComposerAsk
            {...claudeComposerAskSchema.parse({
              greeting: props.yourTurn.greeting,
              command: props.yourTurn.command,
              topic: props.yourTurn.topic,
              segment: props.yourTurn.segment,
              runningText: props.yourTurn.runningText,
              output: props.yourTurn.output,
              folderLabel: props.yourTurn.folderLabel,
            })}
          />
        </Sequence>
      )}

      {props.titleOut && (
        <Sequence from={titleFrom} durationInFrames={props.titleOut.durationF}>
          <Title
            title={props.titleOut.title}
            handle={props.titleOut.handle}
            subline={props.titleOut.subline}
          />
        </Sequence>
      )}
    </AbsoluteFill>
  );
};
