/**
 * Scene template for a muybridge beat.
 * Copy to: [project]/src/scenes/Scene-NN-kebab.tsx
 * Rename the component to SceneNNName and set durationInFrames from the frame budget.
 *
 * Silent-first: the animated key phrase below IS the caption. Leave <Audio> OUT
 * until MP3s exist (then uncomment the line marked VOICE).
 *
 * Modeled on demos/chinese-room-explainer/src/scenes/*. 30 fps, 1920x1080.
 */
import React from 'react';
import {
  AbsoluteFill,
  Sequence,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
  Easing,
  staticFile,
  Audio,
  Img,
} from 'remotion';
import { loadFont } from '@remotion/google-fonts/Inter';

const { fontFamily } = loadFont();

// Pull from brand/[BRAND]/[BRAND].md when a brand is named; these are NBB defaults.
const COLORS = {
  bg: '#FFFFFF',
  ink: '#1A1A1A',
  accent: '#D13B3B',
};

// Frame budget: silent caption beat ≈ 120–210. Voiced ≈ ceil(words/2.5*30)+60.
export const durationInFrames = 180;

export const SceneNNName: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const bgOpacity = interpolate(frame, [0, 18], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });

  // Key phrase reveal (this is the on-screen caption).
  const phrase = ['ONE', 'IDEA', 'PER', 'SCENE'];
  const wordOpacity = phrase.map((_, i) =>
    interpolate(frame, [24 + i * 10, 36 + i * 10], [0, 1], {
      extrapolateLeft: 'clamp',
      extrapolateRight: 'clamp',
      easing: Easing.out(Easing.cubic),
    })
  );

  // Example diagram element rising in (replace with the beat's real visual).
  const figureSpring = spring({ frame: frame - 18, fps, config: { stiffness: 120, damping: 18 } });
  const figureY = interpolate(figureSpring, [0, 1], [40, 0]);

  return (
    <AbsoluteFill style={{ backgroundColor: COLORS.bg, opacity: bgOpacity, fontFamily }}>
      {/* VOICE (opt-in): uncomment once public/[slug]/audio/slide-NN.mp3 exists */}
      {/* <Sequence from={30}><Audio src={staticFile('[slug]/audio/slide-NN.mp3')} /></Sequence> */}

      {/* Reuse a cajal figure instead of redrawing, when one exists:
      <Img src={staticFile('[slug]/figure-NN.png')} style={{ position:'absolute', left:1100, top:300, width:680 }} /> */}

      <div
        style={{
          position: 'absolute',
          left: 160,
          top: 420,
          display: 'flex',
          gap: 24,
          fontSize: 96,
          fontWeight: 900,
          letterSpacing: '-0.03em',
          color: COLORS.ink,
          lineHeight: 1,
          flexWrap: 'wrap',
          maxWidth: 1100,
          transform: `translateY(${figureY}px)`,
        }}
      >
        {phrase.map((word, i) => (
          <span key={word} style={{ opacity: wordOpacity[i] }}>
            {word}
          </span>
        ))}
      </div>
    </AbsoluteFill>
  );
};
