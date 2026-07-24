import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, interpolate } from 'remotion';
import TIMING from './claude-oversimplified-timing.json';
import { ClaudeComposerAsk, claudeComposerAskSchema } from '../../../../../../brutalist-art/runtime/remotion/src/scenes/ClaudeComposerAsk';
import { ClaudeWindow } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-window/ClaudeWindow';
import { claudeWindowSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-window/schema';
import { ClaudeCallout } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-callout/ClaudeCallout';
import { claudeCalloutSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-callout/schema';
import { CLAUDE, CLAUDE_FONT } from '../../../../../../brutalist-art/runtime/remotion/src/tokens/claude';

const FPS = 30;
const SERIF = CLAUDE_FONT.serif;

// Six poster claims — canvas fractions match the poster layout
const ITEMS = [
  { title: 'no more copy-paste', body: 'point claude at 1 folder.\nthe real Excel, the real PDF,\nsaved on your computer.', x: 0.22, y: 0.2, targetX: 0.49, targetY: 0.242, bend: 0.2, delay: 0 },
  { title: 'make an app tonight', body: 'describe it in english.\n4 minutes later it exists.\n0 lines of code.', x: 0.78, y: 0.2, targetX: 0.548, targetY: 0.242, bend: -0.2, delay: 0 },
  { title: 'teach it once', body: 'a skill = a saved playbook.\n/skill-creator teaches claude\nyour way of working.', x: 0.22, y: 0.42, targetX: 0.34, targetY: 0.52, bend: 0.2, delay: 0 },
  { title: 'claude prompts YOU', body: 'end every request with\nthis word. it asks the questions.\nyou click the answers.', x: 0.78, y: 0.42, targetX: 0.56, targetY: 0.52, bend: -0.2, delay: 0 },
  { title: 'drop in anything', body: 'a messy doc, an old proposal,\nlast month’s numbers.\nit reads it all.', x: 0.22, y: 0.66, targetX: 0.3, targetY: 0.635, bend: 0.15, delay: 0 },
  { title: 'the smartest AI on earth', body: 'Fable 5. effort on High.\nthat’s the whole setup.', x: 0.78, y: 0.66, targetX: 0.688, targetY: 0.632, bend: -0.15, delay: 0 },
];

const V2_ITEMS = [
  { title: 'it keeps working when you leave', body: 'cowork runs in the cloud.\nclose the laptop — the task\nfinishes without you.', x: 0.22, y: 0.2, targetX: 0.49, targetY: 0.242, bend: 0.2, delay: 0 },
  { title: 'schedule it', body: 'tasks can run on a clock.\n“every monday, prep my week”\nis a real thing.', x: 0.78, y: 0.2, targetX: 0.55, targetY: 0.5, bend: -0.2, delay: 0 },
  { title: 'it asks before it acts', body: 'folder access is scoped.\nrisky commands need\nyour click first.', x: 0.22, y: 0.78, targetX: 0.3125, targetY: 0.694, bend: 0.15, delay: 0 },
  { title: 'answers become files', body: 'reports, decks, spreadsheets —\nreal files saved back\nto your folder.', x: 0.78, y: 0.42, targetX: 0.56, targetY: 0.52, bend: -0.2, delay: 0 },
  { title: 'watch it think', body: 'a live task list shows\nevery step — audit it,\ndon’t trust it blindly.', x: 0.22, y: 0.52, targetX: 0.45, targetY: 0.6, bend: 0.2, delay: 0 },
  { title: 'effort is a dial, not magic', body: 'High burns usage faster.\nMedium is right for\nmost work.', x: 0.78, y: 0.66, targetX: 0.688, targetY: 0.632, bend: -0.15, delay: 0 },
];

// SPARK-LINE LAW: inner beats never show a lonely asterisk — one short serif
// line next to the spark summarises the beat. Shown via greeting prop on
// ClaudeWindow (delay:0, typeSpeed:1 = already typed, no animation).
const SPARK_LINES = [
  'Holds. Real files.',           // B01 no more copy-paste
  'The code exists.',             // B02 make an app tonight
  'Steal this one.',              // B03 teach it once
  'Cowork already asks.',         // B04 claude prompts YOU
  'Librarian, not scanner.',      // B05 drop in anything
  'Marketing, not measurement.',  // B06 smartest AI
];
const V2_SPARK_LINE = 'Five of six hold.';

type Beat = { id: string; frames: number; kind: string; calloutIndex?: number };
const BEATS: Beat[] = [
  { id: 'B00', frames: 10 * FPS, kind: 'ask' },
  { id: 'B01', frames: 11 * FPS, kind: 'claim', calloutIndex: 0 },
  { id: 'B02', frames: 12 * FPS, kind: 'claim', calloutIndex: 1 },
  { id: 'B03', frames: 9 * FPS, kind: 'claim', calloutIndex: 2 },
  { id: 'B04', frames: 12 * FPS, kind: 'claim', calloutIndex: 3 },
  { id: 'B05', frames: Math.round(11.5 * FPS), kind: 'claim', calloutIndex: 4 },
  { id: 'B06', frames: 13 * FPS, kind: 'claim', calloutIndex: 5 },
  { id: 'B07', frames: 13 * FPS, kind: 'verdict' },
  { id: 'B08', frames: 4 * FPS, kind: 'outro' },
];

type TimingEntry = { id: string; frames: number; audio: string; duration_s: number };
const TIMED = BEATS.map((b, i) => ({
  ...b,
  frames: (TIMING as TimingEntry[])[i].frames,
  audio: (TIMING as TimingEntry[])[i].audio,
}));
export const TOTAL_FRAMES = TIMED.reduce((a, b) => a + b.frames, 0);

// PosterBeat: poster title + ClaudeWindow (spark line in greeting) +
// settled callouts (pre-drawn, negative delay) + active callout (draws in).
const PosterBeat: React.FC<{ upTo: number }> = ({ upTo }) => {
  const sparkLine = SPARK_LINES[upTo];
  const settled = ITEMS.slice(0, upTo);
  const active = [{ ...ITEMS[upTo] }];
  return (
    <AbsoluteFill style={{ background: '#F2F0E9' }}>
      <div style={{ position: 'absolute', top: 22, width: '100%', textAlign: 'center', fontFamily: SERIF, fontWeight: 700, fontSize: 44, lineHeight: 1.02, color: '#111', letterSpacing: '-0.02em' }}>
        Claude, oversimplified<span style={{ color: CLAUDE.SEND }}>.</span>
      </div>
      <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
        <div style={{ marginTop: 44 }}>
          <ClaudeWindow {...claudeWindowSchema.parse({
            view: 'composer',
            width: 640,
            height: 460,
            fontSize: 13,
            greeting: sparkLine,
            delay: 0,
            typeSpeed: 1,
          })} />
        </div>
      </AbsoluteFill>
      {settled.length > 0 && (
        <ClaudeCallout {...claudeCalloutSchema.parse({ items: settled, delay: -600, increment: 0, titleSize: 26, bodySize: 17, maxWidth: 260 })} />
      )}
      <ClaudeCallout {...claudeCalloutSchema.parse({ items: active, delay: 8, increment: 0, titleSize: 26, bodySize: 17, maxWidth: 260, arrowColor: '#161511' })} />
    </AbsoluteFill>
  );
};

// V2Beat: verdict poster — "still oversimplified." + all six v2 callouts
// staggered in. Spark line "Five of six hold." in window greeting.
const V2Beat: React.FC = () => (
  <AbsoluteFill style={{ background: '#F2F0E9' }}>
    <div style={{ position: 'absolute', top: 22, width: '100%', textAlign: 'center', fontFamily: SERIF, fontWeight: 700, fontSize: 44, lineHeight: 1.02, color: '#111', letterSpacing: '-0.02em' }}>
      Claude, still oversimplified<span style={{ color: CLAUDE.SEND }}>.</span>
    </div>
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ marginTop: 44 }}>
        <ClaudeWindow {...claudeWindowSchema.parse({
          view: 'composer',
          width: 640,
          height: 460,
          fontSize: 13,
          greeting: V2_SPARK_LINE,
          delay: 0,
          typeSpeed: 1,
        })} />
      </div>
    </AbsoluteFill>
    <ClaudeCallout {...claudeCalloutSchema.parse({ items: V2_ITEMS, delay: 10, increment: 14, titleSize: 26, bodySize: 17, maxWidth: 260 })} />
  </AbsoluteFill>
);

// OutroCard: OUTRO LAW — restates the episode title in poster-style serif
// with terracotta period, @NikBearBrown handle beneath.
const OutroCard: React.FC = () => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 12], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, alignItems: 'center', justifyContent: 'center', opacity: o }}>
      <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 76, color: '#111', letterSpacing: '-0.02em', textAlign: 'center', lineHeight: 1.05 }}>
        Claude, oversimplified<span style={{ color: CLAUDE.SEND }}>.</span>
      </div>
      <div style={{ fontFamily: SERIF, fontSize: 40, color: CLAUDE.INK, marginTop: 30 }}>@NikBearBrown</div>
      <div style={{ fontFamily: CLAUDE_FONT.ui, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 12 }}>subscribe · the poster, taken apart</div>
    </AbsoluteFill>
  );
};

export const ClaudeOversimplified: React.FC = () => {
  let at = 0;
  const seqs = TIMED.map((b) => {
    const from = at;
    at += b.frames;
    let content: React.ReactNode = null;
    if (b.kind === 'ask') {
      content = (
        <ClaudeComposerAsk {...claudeComposerAskSchema.parse({
          greeting: 'Jambo, Bear',
          topic: 'COWORK · THE POSTER',
          segment: 'Claude, Oversimplified',
          command: '/how-to help me do [X]. AskUserQuestion.',
          runningText: 'grading six claims…',
        })} />
      );
    } else if (b.kind === 'claim') {
      content = <PosterBeat upTo={b.calloutIndex!} />;
    } else if (b.kind === 'verdict') {
      content = <V2Beat />;
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
