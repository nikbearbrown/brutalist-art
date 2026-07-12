import React from 'react';
import { Series } from 'remotion';
import { ONDA_DATA } from '../harness/registry';
import { OndaScene } from '../harness/OndaScene';
import { RiffCard } from './RiffCard';
import { DATA_RIFFS } from './riffs.data';

// Reel timing @ 30fps: each scene = a riff card, then the live scene retinted to teardown.
export const FPS = 30;
export const CARD_FRAMES = 5 * FPS; // 5s of riff card
export const SCENE_FRAMES = 6 * FPS; // 6s of the scene playing
export const BLOCK_FRAMES = CARD_FRAMES + SCENE_FRAMES;
export const REEL_FRAMES = ONDA_DATA.length * BLOCK_FRAMES;

export const RiffReel: React.FC = () => (
  <Series>
    {ONDA_DATA.flatMap((e) => [
      <Series.Sequence key={`${e.slug}-card`} durationInFrames={CARD_FRAMES}>
        <RiffCard riff={DATA_RIFFS[e.slug]} />
      </Series.Sequence>,
      <Series.Sequence key={`${e.slug}-scene`} durationInFrames={SCENE_FRAMES}>
        <OndaScene slug={e.slug} />
      </Series.Sequence>,
    ])}
  </Series>
);
