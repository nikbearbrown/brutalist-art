import React from 'react';
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { TD } from '../teardown';
import { CHANNEL } from './channel';
import type { Beat } from '../schedule/schedule';

// Caption stand-in for the voice (pre-ElevenLabs) — burns each beat's text over the live
// scene at its pinned frame, so you can watch the words land on the events. Color by type:
// predict/resolve carry the red accent (the friction + the payoff); reactive is ink; analytic
// is gray; outro beats center as a card. Type tag makes the beat structure visible.
const RED_TYPES = new Set(['predict', 'resolve']);
const CENTER_TYPES = new Set(['outro-topic', 'outro-channel']);

// overlay=true: white text + drop-shadow for caption-over-video contexts (RiffMp4 clip scenes).
// overlay=false (default): dark ink on white ground for Onda / card-backed scenes.
export const BeatCaption: React.FC<{ beat: Beat; overlay?: boolean }> = ({ beat, overlay = false }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const inS = spring({ frame, fps, config: { damping: 30, stiffness: 140, mass: 1 } });
  const out = spring({ frame: frame - (durationInFrames - 8), fps, config: { damping: 40, stiffness: 200, mass: 1 } });
  const opacity = inS * (1 - out);
  const accent = RED_TYPES.has(beat.type) ? TD.red : overlay ? 'rgba(255,255,255,0.75)' : (beat.type === 'analytic' ? TD.gray : TD.ink);

  if (CENTER_TYPES.has(beat.type)) {
    const isChannel = beat.type === 'outro-channel';
    const big = isChannel ? CHANNEL.name : beat.text;
    const sub = isChannel ? `${CHANNEL.handle} · ${CHANNEL.url}` : (beat.sub ?? 'THE BRUTALIST TEMPLATE LIBRARY');
    return (
      <AbsoluteFill style={{ background: TD.ground, alignItems: 'center', justifyContent: 'center', padding: '0 120px', opacity }}>
        <div style={{ width: 90, height: 6, background: TD.red, marginBottom: 22 }} />
        <div style={{ fontFamily: TD.display, fontSize: 60, fontWeight: 700, color: TD.ink, textAlign: 'center' }}>
          {big}
        </div>
        <div style={{ fontFamily: TD.display, fontSize: 18, letterSpacing: 2, textTransform: 'uppercase', color: isChannel ? TD.red : TD.gray, marginTop: 18 }}>
          {sub}
        </div>
      </AbsoluteFill>
    );
  }

  const textColor = overlay ? '#FFFFFF' : TD.ink;
  const textShadow = overlay ? '0 2px 8px rgba(0,0,0,0.95), 0 1px 3px rgba(0,0,0,0.8)' : 'none';

  return (
    <AbsoluteFill style={{ justifyContent: 'flex-end', padding: '0 90px 90px', opacity }}>
      <div style={{ borderLeft: `6px solid ${accent}`, paddingLeft: 22 }}>
        <div style={{ fontFamily: TD.display, fontSize: 15, letterSpacing: 2, textTransform: 'uppercase', color: accent, marginBottom: 8, textShadow }}>
          {beat.type}
        </div>
        <div
          style={{
            fontFamily: TD.serif,
            fontSize: beat.type === 'analytic' ? 30 : 46,
            lineHeight: 1.25,
            color: textColor,
            textShadow,
            textDecoration: beat.deixis ? 'underline' : 'none',
            textDecorationColor: TD.red,
            textUnderlineOffset: 8,
          }}
        >
          {beat.text}
        </div>
      </div>
    </AbsoluteFill>
  );
};
