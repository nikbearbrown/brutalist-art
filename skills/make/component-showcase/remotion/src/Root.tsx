import React from 'react';
import { Composition } from 'remotion';
import { ONDA_DATA } from './harness/registry';
import { OndaScene } from './harness/OndaScene';
import { RiffReel, FPS, REEL_FRAMES, SCENE_FRAMES } from './riff/RiffReel';
import { BeatPreviz, PREVIZ_FPS, PREVIZ_FRAMES } from './riff/BeatPreviz';
import { RiffTour, TOUR_FPS, TOUR_FRAMES } from './riff/RiffTour';
import { RiffMp4, MP4_FPS, MP4_FRAMES } from './riff/RiffMp4';
import { RiffManim, MANIM_FPS, MANIM_FRAMES } from './riff/RiffManim';

// Compositions:
//  - tour-data        : THE SLATE CUT — the full 68s data-viz belt-tour (captioned, silent)
//  - previz-bar-chart : the RIFFING proving unit — bar-chart with beat captions timed to it
//  - RiffData         : the earlier card-first cut (superseded by the tour)
//  - onda-<slug>      : each scene alone, to verify one component renders before the reel
export const RemotionRoot: React.FC = () => (
  <>
    <Composition
      id="tour-data"
      component={RiffTour}
      durationInFrames={TOUR_FRAMES}
      fps={TOUR_FPS}
      width={1920}
      height={1080}
    />
    <Composition
      id="riff-soul-tuzi"
      component={RiffMp4}
      durationInFrames={MP4_FRAMES}
      fps={MP4_FPS}
      width={1920}
      height={1080}
    />
    <Composition
      id="riff-manim"
      component={RiffManim}
      durationInFrames={MANIM_FRAMES}
      fps={MANIM_FPS}
      width={1920}
      height={1080}
    />
    <Composition
      id="previz-bar-chart"
      component={BeatPreviz}
      durationInFrames={PREVIZ_FRAMES}
      fps={PREVIZ_FPS}
      width={1920}
      height={1080}
    />
    <Composition
      id="RiffData"
      component={RiffReel}
      durationInFrames={REEL_FRAMES}
      fps={FPS}
      width={1920}
      height={1080}
    />
    {ONDA_DATA.map((e) => (
      <Composition
        key={e.slug}
        id={`onda-${e.slug}`}
        component={OndaScene as React.FC<Record<string, unknown>>}
        defaultProps={{ slug: e.slug }}
        durationInFrames={SCENE_FRAMES}
        fps={FPS}
        width={1920}
        height={1080}
      />
    ))}
  </>
);
