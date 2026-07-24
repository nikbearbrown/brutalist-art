import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, interpolate } from 'remotion';
import TIMING from './claude-on-average-timing.json';
import { ClaudeComposerAsk, claudeComposerAskSchema } from '../../../../../../brutalist-art/runtime/remotion/src/scenes/ClaudeComposerAsk';
import { ClaudeWindow } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-window/ClaudeWindow';
import { claudeWindowSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-window/schema';
import { ClaudeCallout } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-callout/ClaudeCallout';
import { claudeCalloutSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-callout/schema';
import { CodeBlock } from '../../../../../../vox/remotion/_bench/onda/registry/components/code-block/CodeBlock';
import { codeBlockSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/code-block/schema';
import { CLAUDE, CLAUDE_FONT } from '../../../../../../brutalist-art/runtime/remotion/src/tokens/claude';

const SERIF = CLAUDE_FONT.serif;
const COMMAND = 'why did I get a different answer this time?';

const ITEMS = [
  { title: 'not a database', body: 'same question,\nthree answers,\nall plausible.', x: 0.78, y: 0.42, targetX: 0.56, targetY: 0.52, bend: -0.2, delay: 0 },
  { title: 'a draw, not a lookup', body: 'next token,\nmost likely\ngiven all context.', x: 0.78, y: 0.66, targetX: 0.688, targetY: 0.632, bend: -0.15, delay: 0 },
  { title: 'temp-zero steers', body: "frozen ≠ specified.\na persona shifts\nwhat is most likely.", x: 0.78, y: 0.2, targetX: 0.548, targetY: 0.242, bend: -0.2, delay: 0 },
  { title: 'variance is the feature', body: 'creativity lives\nin the tails.\nuse it.', x: 0.22, y: 0.66, targetX: 0.3, targetY: 0.66, bend: 0.15, delay: 0 },
  { title: 'one draw ≠ the answer', body: 'certify with a gate.\nnever trust\na single sample.', x: 0.22, y: 0.2, targetX: 0.49, targetY: 0.242, bend: 0.2, delay: 0 },
];

type BeatDef = { id: string; kind: string; calloutIndex?: number; sparkLine?: string };
const BEATS_DEF: BeatDef[] = [
  { id: 'B00', kind: 'ask' },
  { id: 'B01', kind: 'code' },
  { id: 'B02', kind: 'claim', calloutIndex: 0, sparkLine: 'Not a database.' },
  { id: 'B03', kind: 'claim', calloutIndex: 1, sparkLine: 'A draw, not a lookup.' },
  { id: 'B04', kind: 'claim', calloutIndex: 2, sparkLine: 'Temp-zero steers.' },
  { id: 'B05', kind: 'claim', calloutIndex: 3, sparkLine: 'Variance is the feature.' },
  { id: 'B06', kind: 'claim', calloutIndex: 4, sparkLine: 'One draw is not the answer.' },
  { id: 'B07', kind: 'verdict' },
  { id: 'B08', kind: 'outro' },
];

type TimingEntry = { id: string; frames: number; audio: string; duration_s: number };
type Beat = BeatDef & { frames: number; audio: string };
const TIMED: Beat[] = BEATS_DEF.map((b, i) => ({
  ...b,
  frames: (TIMING as TimingEntry[])[i].frames,
  audio: (TIMING as TimingEntry[])[i].audio,
}));
export const TOTAL_FRAMES = TIMED.reduce((a, b) => a + b.frames, 0);

const CodeBeat: React.FC = () => (
  <AbsoluteFill style={{ background: '#F2F0E9' }}>
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <ClaudeWindow {...claudeWindowSchema.parse({ view: 'blank', width: 860, height: 540, fontSize: 15 })} />
    </AbsoluteFill>
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <CodeBlock {...codeBlockSchema.parse({
        title: 'same prompt, three draws',
        code: '$ claude -p "write one line about focus"\n▸ Focus is the art of saying no.\n\n$ claude -p "write one line about focus"\n▸ Attention narrows. That\'s how you get anywhere.\n\n$ claude -p "write one line about focus"\n▸ What you choose not to do is the strategy.',
        fontSize: 17,
        width: 740,
        lineDelay: 8,
      })} />
    </AbsoluteFill>
  </AbsoluteFill>
);

const UsageBeat: React.FC<{ upTo: number; sparkLine: string }> = ({ upTo, sparkLine }) => {
  const settled = upTo > 0 ? ITEMS.slice(0, upTo) : [];
  const active = [{ ...ITEMS[upTo] }];
  return (
    <AbsoluteFill style={{ background: '#F2F0E9' }}>
      <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
        <ClaudeWindow {...claudeWindowSchema.parse({
          view: 'composer',
          width: 640,
          height: 460,
          fontSize: 13,
          greeting: sparkLine,
          command: COMMAND,
          delay: 0,
          typeSpeed: 1,
        })} />
      </AbsoluteFill>
      {settled.length > 0 && (
        <ClaudeCallout {...claudeCalloutSchema.parse({ items: settled, delay: -600, increment: 0, titleSize: 26, bodySize: 17, maxWidth: 260 })} />
      )}
      <ClaudeCallout {...claudeCalloutSchema.parse({ items: active, delay: 8, increment: 0, titleSize: 26, bodySize: 17, maxWidth: 260 })} />
    </AbsoluteFill>
  );
};

const VerdictBeat: React.FC = () => (
  <AbsoluteFill style={{ background: '#F2F0E9', alignItems: 'center', justifyContent: 'center' }}>
    <ClaudeWindow {...claudeWindowSchema.parse({
      view: 'artifact',
      width: 900,
      height: 560,
      fontSize: 17,
      artifactTitle: 'The distribution rules — one page',
      artifactHeading: 'What Claude actually is',
      artifactLines: [
        "You're not querying a database. You're sampling a distribution.",
        "Same prompt, different draw — that's not a bug, that's the definition.",
        'Temperature zero steers toward most likely; it does not specify an output.',
        'Variance is the creativity. Certify draws with gates, not with faith.',
        'Scripts pin the exact. Skills bias the draw. Gates catch the bad draws.',
      ],
    })} />
  </AbsoluteFill>
);

const OutroCard: React.FC = () => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 12], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, alignItems: 'center', justifyContent: 'center', opacity: o }}>
      <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 76, color: '#111', letterSpacing: '-0.02em', textAlign: 'center', lineHeight: 1.05 }}>
        Claude, on average<span style={{ color: CLAUDE.SEND }}>.</span>
      </div>
      <div style={{ fontFamily: SERIF, fontSize: 40, color: CLAUDE.INK, marginTop: 30 }}>@NikBearBrown</div>
      <div style={{ fontFamily: CLAUDE_FONT.ui, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 12 }}>subscribe · sample deliberately</div>
    </AbsoluteFill>
  );
};

export const ClaudeOnAverage: React.FC = () => {
  let at = 0;
  const seqs = TIMED.map((b) => {
    const from = at;
    at += b.frames;
    let content: React.ReactNode = null;
    if (b.kind === 'ask') {
      content = (
        <ClaudeComposerAsk {...claudeComposerAskSchema.parse({
          greeting: 'Annyeong, Bear',
          topic: 'COWORK · LLMs',
          segment: 'Claude, On Average',
          command: COMMAND,
          runningText: 'sampling the distribution…',
        })} />
      );
    } else if (b.kind === 'code') {
      content = <CodeBeat />;
    } else if (b.kind === 'claim') {
      content = <UsageBeat upTo={b.calloutIndex!} sparkLine={b.sparkLine!} />;
    } else if (b.kind === 'verdict') {
      content = <VerdictBeat />;
    } else {
      content = <OutroCard />;
    }
    return (
      <Sequence key={b.id} from={from} durationInFrames={b.frames}>
        {content}
        <Audio src={staticFile(b.audio)} />
      </Sequence>
    );
  });
  return <AbsoluteFill style={{ background: CLAUDE.PAGE }}>{seqs}</AbsoluteFill>;
};
