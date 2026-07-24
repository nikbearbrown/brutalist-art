import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from 'remotion';

const SERIF = 'Georgia, "Times New Roman", serif';
const SANS = '-apple-system, "SF Pro Display", "Helvetica Neue", "Segoe UI", sans-serif';
const STAGE = '#F2F0E9';
const INK = '#3D3929';
const SPARK = '#D97757';

const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));
const remap = (x: number, x0: number, x1: number, y0: number, y1: number) => {
  const t = clamp((x - x0) / (x1 - x0 || 1), 0, 1);
  return y0 + (y1 - y0) * t;
};
const ease = (t: number) => 1 - Math.pow(1 - clamp(t, 0, 1), 3);

export const SparkLine: React.FC<{ text: string; pos?: 'top' | 'bottom' }> = ({ text, pos = 'top' }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
  const o = ease(remap(p, 0, 0.06, 0, 1));
  return (
    <div style={{
      position: 'absolute',
      ...(pos === 'top' ? { top: 44 } : { bottom: 40 }),
      left: 0, right: 0, display: 'flex',
      justifyContent: 'center', alignItems: 'center', gap: 16, opacity: o,
    }}>
      <svg width={26} height={26} viewBox="0 0 24 24">
        {Array.from({ length: 8 }, (_, i) => (
          <line key={i} x1={12} y1={12}
            x2={12 + 10 * Math.cos(i * Math.PI / 4 + 0.2)}
            y2={12 + 10 * Math.sin(i * Math.PI / 4 + 0.2)}
            stroke={SPARK} strokeWidth={3.2} strokeLinecap="round" />
        ))}
      </svg>
      <div style={{ fontFamily: SERIF, fontSize: 40, color: INK }}>{text}</div>
    </div>
  );
};

export const IlluStage: React.FC<{ spark?: string; children: React.ReactNode }> = ({ spark, children }) => (
  <AbsoluteFill style={{ background: STAGE }}>
    {children}
    {spark && <SparkLine text={spark} />}
  </AbsoluteFill>
);

export const PredictCard: React.FC<{ question: string; commit: string }> = ({ question, commit }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
  const qOp = ease(remap(p, 0.04, 0.18, 0, 1));
  const cOp = ease(remap(p, 0.18, 0.30, 0, 1));
  return (
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ maxWidth: 900, padding: '0 60px', textAlign: 'center' }}>
        <div style={{
          fontFamily: SERIF, fontSize: 54, fontWeight: 700, color: INK,
          lineHeight: 1.2, marginBottom: 44, opacity: qOp,
          transform: `translateY(${(1 - qOp) * 16}px)`,
        }}>
          {question}
        </div>
        <div style={{
          fontFamily: SANS, fontSize: 26, color: SPARK, opacity: cOp,
          transform: `translateY(${(1 - cOp) * 10}px)`,
          border: `2px solid ${SPARK}`, borderRadius: 8,
          padding: '14px 32px', display: 'inline-block',
        }}>
          {commit}
        </div>
      </div>
    </AbsoluteFill>
  );
};
