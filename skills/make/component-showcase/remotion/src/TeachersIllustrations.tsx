import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from 'remotion';
import { CLAUDE, CLAUDE_FONT } from '../../../../../../brutalist-art/runtime/remotion/src/tokens/claude';

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const STAGE = '#F2F0E9';
const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));
const remap = (x: number, x0: number, x1: number, y0: number, y1: number) => {
  const t = clamp((x - x0) / (x1 - x0 || 1), 0, 1);
  return y0 + (y1 - y0) * t;
};
const ease = (t: number) => 1 - Math.pow(1 - clamp(t, 0, 1), 3);
const useP = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  return clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
};

export const SparkLine: React.FC<{ text: string; pos?: 'top' | 'bottom' }> = ({ text, pos = 'top' }) => {
  const p = useP();
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

export const IlluStage: React.FC<{ spark: string; children: React.ReactNode }> = ({ spark, children }) => (
  <AbsoluteFill style={{ background: STAGE }}>
    {children}
    <SparkLine text={spark} />
  </AbsoluteFill>
);

export const PredictCard: React.FC<{ question: string; commit: string }> = ({ question, commit }) => {
  const p = useP();
  const qo = remap(p, 0.05, 0.15, 0, 1);
  const lo = ease(remap(p, 0.3, 0.5, 0, 1));
  const co = remap(p, 0.55, 0.65, 0, 1);
  return (
    <>
      <div style={{ position: 'absolute', top: 250, left: 0, right: 0, textAlign: 'center', fontFamily: SERIF, fontSize: 62, color: CLAUDE.INK, opacity: qo, padding: '0 140px', lineHeight: 1.2 }}>
        {question}
      </div>
      <svg width={1280} height={720} style={{ position: 'absolute', inset: 0 }}>
        <line x1={440} y1={450} x2={440 + 400 * lo} y2={450} stroke={CLAUDE.SPARK} strokeWidth={5} strokeLinecap="round" />
      </svg>
      <div style={{ position: 'absolute', top: 480, left: 0, right: 0, textAlign: 'center', fontFamily: SANS, fontSize: 26, color: CLAUDE.INK_SOFT, opacity: co }}>
        {commit}
      </div>
    </>
  );
};
