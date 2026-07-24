import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, interpolate } from 'remotion';
import TIMING from './claude-on-empty-timing.json';
import { ClaudeComposerAsk, claudeComposerAskSchema } from '../../../../../../brutalist-art/runtime/remotion/src/scenes/ClaudeComposerAsk';
import { ClaudeWindow } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-window/ClaudeWindow';
import { claudeWindowSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-window/schema';
import { ClaudeCallout } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-callout/ClaudeCallout';
import { claudeCalloutSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-callout/schema';
import { CLAUDE, CLAUDE_FONT } from '../../../../../../brutalist-art/runtime/remotion/src/tokens/claude';

const SERIF = CLAUDE_FONT.serif;
const COMMAND = 'why am I out of usage until Friday?';

const ITEMS = [
  { title: 'the real cost', body: 'run dry Tuesday.\nwork returns at reset.\nthe wait is the price.', x: 0.78, y: 0.42, targetX: 0.56, targetY: 0.52, bend: -0.2, delay: 0 },
  { title: 'one chip, all the blame', body: 'Fable 5 + High\non everything —\nemail drafts included.', x: 0.78, y: 0.66, targetX: 0.688, targetY: 0.632, bend: -0.15, delay: 0 },
  { title: 'judgment on chores', body: "the architecture model\ndoesn’t need to\nrename your files.", x: 0.22, y: 0.42, targetX: 0.34, targetY: 0.52, bend: 0.2, delay: 0 },
  { title: 'opus takes the bulk', body: "skill runs, batches,\nlong refactors —\nClaude Code’s lane.", x: 0.78, y: 0.2, targetX: 0.548, targetY: 0.242, bend: -0.2, delay: 0 },
  { title: 'author high, run low', body: 'your best model writes\nthe skill once.\nquality freezes in.', x: 0.22, y: 0.2, targetX: 0.49, targetY: 0.242, bend: 0.2, delay: 0 },
];

type Beat = { id: string; frames: number; kind: string; calloutIndex?: number; sparkLine?: string; audio: string };
const BEATS_DEF = [
  { id: 'B00', kind: 'ask' },
  { id: 'B01', kind: 'claim', calloutIndex: 0, sparkLine: 'The wait is the price.' },
  { id: 'B02', kind: 'claim', calloutIndex: 1, sparkLine: 'High on everything.' },
  { id: 'B03', kind: 'claim', calloutIndex: 2, sparkLine: 'Judgment spent on chores.' },
  { id: 'B04', kind: 'claim', calloutIndex: 3, sparkLine: 'Opus takes the bulk.' },
  { id: 'B05', kind: 'claim', calloutIndex: 4, sparkLine: 'Author high, run low.' },
  { id: 'B06', kind: 'breathe', sparkLine: 'There when it counts.' },
  { id: 'B07', kind: 'verdict' },
  { id: 'B08', kind: 'outro' },
];

type TimingEntry = { id: string; frames: number; audio: string; duration_s: number };
const TIMED: Beat[] = BEATS_DEF.map((b, i) => ({
  ...b,
  frames: (TIMING as TimingEntry[])[i].frames,
  audio: (TIMING as TimingEntry[])[i].audio,
}));
export const TOTAL_FRAMES = TIMED.reduce((a, b) => a + b.frames, 0);

// Inner beat: centered window + spark line (SPARK-LINE LAW) + accumulated callouts.
// command is pre-typed (delay:0, typeSpeed:1) — typing is B00-only.
const UsageBeat: React.FC<{ upTo: number; sparkLine: string }> = ({ upTo, sparkLine }) => {
  const settled = upTo > 0 ? ITEMS.slice(0, upTo) : [];
  const active = upTo >= 0 && upTo < ITEMS.length ? [{ ...ITEMS[upTo] }] : [];
  const allSettled = upTo < 0 ? ITEMS.map((it) => ({ ...it })) : [];
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
      {active.length > 0 && (
        <ClaudeCallout {...claudeCalloutSchema.parse({ items: active, delay: 8, increment: 0, titleSize: 26, bodySize: 17, maxWidth: 260 })} />
      )}
      {allSettled.length > 0 && (
        <ClaudeCallout {...claudeCalloutSchema.parse({ items: allSettled, delay: -600, increment: 0, titleSize: 26, bodySize: 17, maxWidth: 260 })} />
      )}
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
      artifactTitle: 'The Routing — one page',
      artifactHeading: 'Who does what',
      artifactLines: [
        'Fable 5 — skills, plans, the tricky calls. Words that get reused.',
        'Opus + Claude Code — runs, batches, refactors. The long haul.',
        'Effort Medium — the everyday default.',
        'Effort High — only when the problem earns it.',
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
        Claude, on empty<span style={{ color: CLAUDE.SEND }}>.</span>
      </div>
      <div style={{ fontFamily: SERIF, fontSize: 40, color: CLAUDE.INK, marginTop: 30 }}>@NikBearBrown</div>
      <div style={{ fontFamily: CLAUDE_FONT.ui, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 12 }}>subscribe · spend it where it counts</div>
    </AbsoluteFill>
  );
};

export const ClaudeOnEmpty: React.FC = () => {
  let at = 0;
  const seqs = TIMED.map((b) => {
    const from = at;
    at += b.frames;
    let content: React.ReactNode = null;
    if (b.kind === 'ask') {
      content = (
        <ClaudeComposerAsk {...claudeComposerAskSchema.parse({
          greeting: 'Sawubona, Bear',
          topic: 'COWORK · USAGE',
          segment: 'Claude, On Empty',
          command: COMMAND,
          runningText: 'checking the spend…',
        })} />
      );
    } else if (b.kind === 'claim') {
      content = <UsageBeat upTo={b.calloutIndex!} sparkLine={b.sparkLine!} />;
    } else if (b.kind === 'breathe') {
      content = <UsageBeat upTo={-1} sparkLine={b.sparkLine!} />;
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
