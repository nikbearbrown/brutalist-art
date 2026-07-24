import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, interpolate } from 'remotion';
import TIMING from './claude-unsupervised-timing.json';
import { ClaudeComposerAsk, claudeComposerAskSchema } from '../../../../../../brutalist-art/runtime/remotion/src/scenes/ClaudeComposerAsk';
import { ClaudeWindow } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-window/ClaudeWindow';
import { claudeWindowSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-window/schema';
import { ClaudeCallout } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-callout/ClaudeCallout';
import { claudeCalloutSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-callout/schema';
import { CodeBlock } from '../../../../../../vox/remotion/_bench/onda/registry/components/code-block/CodeBlock';
import { codeBlockSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/code-block/schema';
import { CLAUDE, CLAUDE_FONT } from '../../../../../../brutalist-art/runtime/remotion/src/tokens/claude';

const SERIF = CLAUDE_FONT.serif;
const COMMAND = 'is --dangerously-skip-permissions ever a good idea?';

const ITEMS = [
  { title: 'no more may-I?', body: 'writes, deletes, installs —\nanything in reach,\nno questions asked.', x: 0.78, y: 0.42, targetX: 0.56, targetY: 0.52, bend: -0.2, delay: 0 },
  { title: 'risk = blast radius', body: 'the danger lives in\nwhat the folder holds,\nnot in the flag.', x: 0.2, y: 0.66, targetX: 0.3, targetY: 0.66, bend: 0.15, delay: 0 },
  { title: 'worst case: re-render', body: 'a bad beat is a file.\nregenerate it.\nkeep the rest.', x: 0.78, y: 0.66, targetX: 0.7, targetY: 0.632, bend: -0.15, delay: 0 },
  { title: 'run. check. redo.', body: "it runs until done.\nyou review the cut —\nan editor, not a babysitter.", x: 0.78, y: 0.2, targetX: 0.548, targetY: 0.242, bend: -0.2, delay: 0 },
  { title: 'opus runs the loop', body: 'fable wrote the skill.\nopus grinds it out.\nauthor high, run low.', x: 0.22, y: 0.2, targetX: 0.49, targetY: 0.242, bend: 0.2, delay: 0 },
];

type BeatDef = { id: string; kind: string; calloutIndex?: number; sparkLine?: string };
const BEATS_DEF: BeatDef[] = [
  { id: 'B00', kind: 'ask' },
  { id: 'B01', kind: 'code' },
  { id: 'B02', kind: 'claim', calloutIndex: 0, sparkLine: 'It means it.' },
  { id: 'B03', kind: 'claim', calloutIndex: 1, sparkLine: 'Risk = blast radius.' },
  { id: 'B04', kind: 'claim', calloutIndex: 2, sparkLine: 'Worst case: re-render.' },
  { id: 'B05', kind: 'claim', calloutIndex: 3, sparkLine: 'Run. Check. Redo.' },
  { id: 'B06', kind: 'claim', calloutIndex: 4, sparkLine: 'Opus runs the loop.' },
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

// B01 — dark glass code block (Onda, never re-skinned) on claude-window blank stage.
const CodeBeat: React.FC = () => (
  <AbsoluteFill style={{ background: '#F2F0E9' }}>
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <ClaudeWindow {...claudeWindowSchema.parse({ view: 'blank', width: 860, height: 540, fontSize: 15 })} />
    </AbsoluteFill>
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <CodeBlock {...codeBlockSchema.parse({
        title: 'zsh — unsupervised',
        code: 'claude --dangerously-skip-permissions \\\n  "build the reel: audio, conform, render, QC"',
        fontSize: 20,
        width: 720,
        lineDelay: 10,
      })} />
    </AbsoluteFill>
  </AbsoluteFill>
);

// Inner beat: composer window + spark line (SPARK-LINE LAW) + accumulating callouts.
// command pre-typed (delay:0, typeSpeed:1) — typing is B00-only.
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
      artifactTitle: 'The Seatbelt Rules — one page',
      artifactHeading: 'When to skip the prompts',
      artifactLines: [
        'Git-tracked folder — every change reversible.',
        'Regenerable outputs — the worst case is a re-render.',
        'Nothing secret in reach — no credentials, no prod, nothing unique.',
        'Gates inside the pipeline — audio spend and publishing still need a human.',
        "Fail any one? Keep the permission prompts. They're the seatbelt.",
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
        Claude, unsupervised<span style={{ color: CLAUDE.SEND }}>.</span>
      </div>
      <div style={{ fontFamily: SERIF, fontSize: 40, color: CLAUDE.INK, marginTop: 30 }}>@NikBearBrown</div>
      <div style={{ fontFamily: CLAUDE_FONT.ui, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 12 }}>subscribe · know your blast radius</div>
    </AbsoluteFill>
  );
};

export const ClaudeUnsupervised: React.FC = () => {
  let at = 0;
  const seqs = TIMED.map((b) => {
    const from = at;
    at += b.frames;
    let content: React.ReactNode = null;
    if (b.kind === 'ask') {
      content = (
        <ClaudeComposerAsk {...claudeComposerAskSchema.parse({
          greeting: 'Merhaba, Bear',
          topic: 'CLAUDE CODE · YOLO MODE',
          segment: 'Claude, Unsupervised',
          command: COMMAND,
          runningText: 'weighing the blast radius…',
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
