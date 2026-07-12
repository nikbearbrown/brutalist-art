import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame, spring, useVideoConfig } from 'remotion';
import { TD } from '../teardown';
import type { Riff } from './riffs.data';

// The riff card — teardown chrome: white ground, ink text, one red accent. Shown before
// each scene; the register (what/pro/con/teaching) reads as on-screen text in v1 and
// becomes the ElevenLabs VO script once approved.
const Row: React.FC<{ tag: string; text: string; accent?: boolean; delay: number }> = ({
  tag,
  text,
  accent,
  delay,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame: frame - delay, fps, config: { damping: 30, stiffness: 110, mass: 1 } });
  const y = interpolate(s, [0, 1], [16, 0]);
  return (
    <div style={{ opacity: s, transform: `translateY(${y}px)`, marginBottom: 22, maxWidth: 1180 }}>
      <div
        style={{
          fontFamily: TD.display,
          fontSize: 17,
          letterSpacing: 2,
          textTransform: 'uppercase',
          color: accent ? TD.red : TD.gray,
          marginBottom: 6,
        }}
      >
        {tag}
      </div>
      <div style={{ fontFamily: TD.serif, fontSize: 34, lineHeight: 1.3, color: TD.ink }}>{text}</div>
    </div>
  );
};

export const RiffCard: React.FC<{ riff: Riff }> = ({ riff }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = spring({ frame, fps, config: { damping: 30, stiffness: 110, mass: 1 } });
  return (
    <AbsoluteFill
      style={{
        background: TD.ground,
        padding: '90px 120px',
        justifyContent: 'center',
      }}
    >
      {/* red rule + title */}
      <div style={{ opacity: t, marginBottom: 34 }}>
        <div style={{ width: 90, height: 6, background: TD.red, marginBottom: 20 }} />
        <div style={{ fontFamily: TD.display, fontSize: 76, fontWeight: 700, color: TD.ink }}>
          {riff.title}
        </div>
      </div>
      <Row tag="What it does" text={riff.does} delay={6} />
      <Row tag="Pro" text={riff.pro} delay={12} />
      <Row tag="Con" text={riff.con} delay={18} />
      <Row tag="In teaching" text={riff.edu} accent delay={24} />
    </AbsoluteFill>
  );
};
