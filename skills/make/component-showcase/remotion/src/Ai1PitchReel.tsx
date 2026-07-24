import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { ClaudeComposerAsk, claudeComposerAskSchema } from '../../../../../../brutalist-art/runtime/remotion/src/scenes/ClaudeComposerAsk';
import { ClaudeWindow } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-window/ClaudeWindow';
import { claudeWindowSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-window/schema';
import { ClaudeCallout } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-callout/ClaudeCallout';
import { claudeCalloutSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/claude-callout/schema';
import { CodeBlock } from '../../../../../../vox/remotion/_bench/onda/registry/components/code-block/CodeBlock';
import { codeBlockSchema } from '../../../../../../vox/remotion/_bench/onda/registry/components/code-block/schema';
import { CLAUDE, CLAUDE_FONT } from '../../../../../../brutalist-art/runtime/remotion/src/tokens/claude';
import { DivergentFates, BinaryBranch, ScaleComparison, Threshold } from './deckPatterns';
import DATA from './ai1_data.json';

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const BG = '#F2F0E9';

const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));
const remap = (x: number, x0: number, x1: number, y0: number, y1: number) => {
  const t = clamp((x - x0) / (x1 - x0 || 1), 0, 1);
  return y0 + (y1 - y0) * t;
};

const SparkLine: React.FC<{ text: string; pos?: 'top' | 'bottom' }> = ({ text, pos = 'top' }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
  const o = remap(p, 0, 0.06, 0, 1);
  return (
    <div style={{ position: 'absolute', ...(pos === 'top' ? { top: 44 } : { bottom: 40 }), left: 0, right: 0, display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 16, opacity: o }}>
      <svg width={26} height={26} viewBox="0 0 24 24">
        {Array.from({ length: 8 }, (_, i) => (
          <line key={i} x1={12} y1={12}
            x2={12 + 10 * Math.cos((i * Math.PI) / 4 + 0.2)}
            y2={12 + 10 * Math.sin((i * Math.PI) / 4 + 0.2)}
            stroke={CLAUDE.SPARK} strokeWidth={3.2} strokeLinecap="round" />
        ))}
      </svg>
      <div style={{ fontFamily: SERIF, fontSize: 40, color: CLAUDE.INK }}>{text}</div>
    </div>
  );
};

type Item = { title: string; body: string; x: number; y: number; targetX: number; targetY: number; bend: number; delay: number };
type Beat = { id: string; kind: string; act: string; frames: number; audio: string; props: any; narration: string };
export type PitchConfig = { slug: string; compId: string; title: string; items: Item[]; beats: Beat[]; totalFrames: number };

export const AI1_VIDEOS: PitchConfig[] = DATA as PitchConfig[];

const PitchBeat: React.FC<{ items: Item[]; upTo: number; sparkLine: string; command: string }> = ({ items, upTo, sparkLine, command }) => {
  const settled = items.slice(0, upTo).map((it) => ({ ...it }));
  const active = upTo < items.length ? [{ ...items[upTo] }] : [];
  return (
    <AbsoluteFill style={{ background: '#F2F0E9' }}>
      <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
        <ClaudeWindow {...claudeWindowSchema.parse({
          view: 'composer', width: 640, height: 460, fontSize: 13,
          greeting: sparkLine, command, delay: 0, typeSpeed: 1,
          folderLabel: '@HumanitariansAI',
        })} />
      </AbsoluteFill>
      {settled.length > 0 && (
        <ClaudeCallout {...claudeCalloutSchema.parse({ items: settled, delay: -600, increment: 0, titleSize: 26, bodySize: 17, maxWidth: 260 })} />
      )}
      {active.length > 0 && (
        <ClaudeCallout {...claudeCalloutSchema.parse({ items: active, delay: 8, increment: 0, titleSize: 26, bodySize: 17, maxWidth: 260 })} />
      )}
    </AbsoluteFill>
  );
};

const PatternBeat: React.FC<{ type: string; data: any; spark: string }> = ({ type, data, spark }) => (
  <AbsoluteFill style={{ background: BG }}>
    {type === 'DivergentFates' && <DivergentFates data={data} />}
    {type === 'BinaryBranch' && <BinaryBranch data={data} />}
    {type === 'ScaleComparison' && <ScaleComparison data={data} />}
    {type === 'Threshold' && <Threshold data={data} />}
    <SparkLine text={spark} pos={type === 'Threshold' ? 'top' : 'bottom'} />
  </AbsoluteFill>
);

const CodeBlockBeat: React.FC<{ spark: string; code: string; codeTitle: string }> = ({ spark, code, codeTitle }) => (
  <AbsoluteFill style={{ background: BG }}>
    <SparkLine text={spark} />
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center', paddingTop: 40 }}>
      <div style={{ background: '#17171C', borderRadius: 18, boxShadow: '0 14px 40px rgba(61,57,41,0.25)', overflow: 'hidden' }}>
        <CodeBlock {...codeBlockSchema.parse({ code, title: codeTitle, fontSize: 24, width: 860, delay: 6, lineDelay: 4 })} />
      </div>
    </AbsoluteFill>
  </AbsoluteFill>
);

const VerdictBeat: React.FC<{ props: any }> = ({ props }) => (
  <AbsoluteFill style={{ background: '#F2F0E9', alignItems: 'center', justifyContent: 'center' }}>
    <ClaudeWindow {...claudeWindowSchema.parse({
      view: 'artifact', width: 960, height: 580, fontSize: 16,
      artifactTitle: props.artifactTitle,
      artifactHeading: props.artifactHeading,
      artifactLines: props.artifactLines,
    })} />
  </AbsoluteFill>
);

const OutroCard: React.FC<{ props: any }> = ({ props }) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 12], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, alignItems: 'center', justifyContent: 'center', opacity: o }}>
      <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 68, color: '#111', letterSpacing: '-0.02em', textAlign: 'center', lineHeight: 1.05, maxWidth: 1050 }}>
        {String(props.title).replace(/\.$/, '')}<span style={{ color: CLAUDE.SEND }}>.</span>
      </div>
      <div style={{ fontFamily: SERIF, fontSize: 38, color: CLAUDE.INK, marginTop: 28 }}>{props.handle}</div>
      <div style={{ fontFamily: SANS, fontSize: 23, color: CLAUDE.INK_SOFT, marginTop: 12 }}>{props.subline}</div>
    </AbsoluteFill>
  );
};

export const Ai1PitchReel: React.FC<{ slug: string }> = ({ slug }) => {
  const cfg = AI1_VIDEOS.find((v) => v.slug === slug)!;
  const askProps = cfg.beats[0].props;
  let at = 0;
  const seqs = cfg.beats.map((b) => {
    const from = at;
    at += b.frames;
    let content: React.ReactNode = null;
    if (b.kind === 'ClaudeComposerAsk') {
      content = <ClaudeComposerAsk {...claudeComposerAskSchema.parse(b.props)} />;
    } else if (b.kind === 'ClaudePitchBeat') {
      content = <PitchBeat items={cfg.items} upTo={b.props.calloutIndex} sparkLine={b.props.sparkLine} command={askProps.command} />;
    } else if (b.kind === 'ClaudeVerdictArtifact') {
      content = <VerdictBeat props={b.props} />;
    } else if (b.kind === 'IlluPattern') {
      content = <PatternBeat type={b.props.patternType} data={b.props.patternData} spark={b.props.spark} />;
    } else if (b.kind === 'OndaCodeBlock') {
      content = <CodeBlockBeat spark={b.props.spark} code={b.props.code} codeTitle={b.props.codeTitle || 'decisions.json'} />;
    } else {
      content = <OutroCard props={b.props} />;
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
