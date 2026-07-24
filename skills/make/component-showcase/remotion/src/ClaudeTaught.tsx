import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, interpolate } from 'remotion';
import TIMING from './claude-taught-timing.json';
import { ClaudeComposerAsk, claudeComposerAskSchema } from '../../../../../../brutalist-art/runtime/remotion/src/scenes/ClaudeComposerAsk';
import { ClaudeWindow } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-window/ClaudeWindow';
import { claudeWindowSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-window/schema';
import { ClaudeCallout } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-callout/ClaudeCallout';
import { claudeCalloutSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-callout/schema';
import { CodeBlock } from '../../../../../../vox/remotion/_bench/onda/registry/components/code-block/CodeBlock';
import { codeBlockSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/code-block/schema';
import { CLAUDE, CLAUDE_FONT } from '../../../../../../brutalist-art/runtime/remotion/src/tokens/claude';

const SERIF = CLAUDE_FONT.serif;
const COMMAND = '/skill-creator teach claude my way of making videos';

const ITEMS = [
  { title: 'the influence half', body: 'register, pickWhen, taste —\njudgment written once\nso runners never guess.', x: 0.22, y: 0.42, targetX: 0.49, targetY: 0.242, bend: 0.2, delay: 0 },
  { title: 'the specify half', body: 'file contracts, gates, laws.\nexact enough to run\nwithout asking anything.', x: 0.78, y: 0.66, targetX: 0.688, targetY: 0.632, bend: -0.15, delay: 0 },
  { title: 'authored once', body: 'Fable writes it once.\nOpus runs it forever.\nquality freezes in.', x: 0.78, y: 0.2, targetX: 0.548, targetY: 0.242, bend: -0.2, delay: 0 },
  { title: 'the vague skill', body: '"match my tone."\n"be thorough." —\nthe runner improvises.', x: 0.78, y: 0.42, targetX: 0.56, targetY: 0.52, bend: -0.2, delay: 0 },
  { title: 'author high, run low', body: 'the expensive part:\nthe authoring.\nthe cheap part: forever.', x: 0.22, y: 0.2, targetX: 0.34, targetY: 0.52, bend: 0.15, delay: 0 },
];

type BeatDef = { id: string; kind: string; calloutIndex?: number; sparkLine?: string };
const BEATS_DEF: BeatDef[] = [
  { id: 'B00', kind: 'ask' },
  { id: 'B01', kind: 'code' },
  { id: 'B02', kind: 'claim', calloutIndex: 0, sparkLine: 'Judgment, frozen.' },
  { id: 'B03', kind: 'claim', calloutIndex: 1, sparkLine: 'Laws, not vibes.' },
  { id: 'B04', kind: 'claim', calloutIndex: 2, sparkLine: 'Written once.' },
  { id: 'B05', kind: 'claim', calloutIndex: 3, sparkLine: "Runners don't improvise." },
  { id: 'B06', kind: 'claim', calloutIndex: 4, sparkLine: 'Author high, run low.' },
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

// B01 — dark glass Onda code-block on blank ClaudeWindow (never re-skinned).
const CodeBeat: React.FC = () => (
  <AbsoluteFill style={{ background: '#F2F0E9' }}>
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <ClaudeWindow {...claudeWindowSchema.parse({ view: 'blank', width: 860, height: 540, fontSize: 15 })} />
    </AbsoluteFill>
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <CodeBlock {...codeBlockSchema.parse({
        title: 'SKILL.md — the anatomy',
        code: '---\nname: claude-explainer\npickWhen: user asks for a claude reel\nregister: Teardown\n---\n\n## Laws\n- GATE P before any audio spend\n- Cold open: always ClaudeComposerAsk\n- Spark line on every inner beat\n- Outro restates the episode title',
        fontSize: 18,
        width: 720,
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
      artifactTitle: 'Anatomy of a skill — one page',
      artifactHeading: 'What goes where',
      artifactLines: [
        'pickWhen + register — the influence half. When to load it and how to sound.',
        'Laws — the rules the runner never breaks, no matter what.',
        'Gates — what must pass before any money is spent.',
        'File contracts — where outputs land and what they\'re named.',
        'Author in Fable once. Run in Opus forever. The cheap part is the part that runs.',
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
        Claude, taught<span style={{ color: CLAUDE.SEND }}>.</span>
      </div>
      <div style={{ fontFamily: SERIF, fontSize: 40, color: CLAUDE.INK, marginTop: 30 }}>@NikBearBrown</div>
      <div style={{ fontFamily: CLAUDE_FONT.ui, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 12 }}>subscribe · judgment, written down</div>
    </AbsoluteFill>
  );
};

export const ClaudeTaught: React.FC = () => {
  let at = 0;
  const seqs = TIMED.map((b) => {
    const from = at;
    at += b.frames;
    let content: React.ReactNode = null;
    if (b.kind === 'ask') {
      content = (
        <ClaudeComposerAsk {...claudeComposerAskSchema.parse({
          greeting: 'Wagwan, Bear',
          topic: 'COWORK · SKILLS',
          segment: 'Claude, Taught',
          command: COMMAND,
          runningText: 'reading the playbook…',
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
