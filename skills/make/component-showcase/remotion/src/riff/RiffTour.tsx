import React from 'react';
import { AbsoluteFill, Sequence, Audio, staticFile } from 'remotion';
import { OndaScene } from '../harness/OndaScene';
import { BeatCaption } from './BeatCaption';
import { TD } from '../teardown';
import tour from '../../beats/templates-onda.conformed.json';

// THE CATALOG CUT (with sound): the Brutalist Template Library video, timing CONFORMED to the
// measured NBB audio (riff_audio.py -> riff_conform.py). Non-template segments render a card
// (intro / library credit with link / outro) from `segment.card`; template segments render the
// live Onda component with a persistent number+name label from `segment.label`. Each beat plays
// its mp3 at its conformed frame; captions ride along as CC.
export const TOUR_FPS = tour.fps as number;
export const TOUR_FRAMES = tour.total_frames as number;

const Card: React.FC<{ title: string; sub?: string; link?: string }> = ({ title, sub, link }) => (
  <AbsoluteFill style={{ background: TD.ground, alignItems: 'center', justifyContent: 'center', flexDirection: 'column' }}>
    <div style={{ width: 110, height: 7, background: TD.red, marginBottom: 28 }} />
    <div style={{ fontFamily: TD.display, fontWeight: 700, fontSize: 84, color: TD.ink, textAlign: 'center', letterSpacing: -1 }}>
      {title}
    </div>
    {sub ? (
      <div style={{ fontFamily: TD.display, fontSize: 24, letterSpacing: 2, textTransform: 'uppercase', color: TD.gray, marginTop: 22 }}>
        {sub}
      </div>
    ) : null}
    {link ? (
      <div style={{ fontFamily: TD.serif, fontSize: 30, color: TD.red, marginTop: 30 }}>{link}</div>
    ) : null}
  </AbsoluteFill>
);

// Persistent catalog label — TOP-left, clear of the bottom caption band (no text-on-text).
const TemplateLabel: React.FC<{ label: string }> = ({ label }) => (
  <AbsoluteFill style={{ justifyContent: 'flex-start', alignItems: 'flex-start', padding: '56px 0 0 90px' }}>
    <div style={{ background: TD.ink, color: TD.ground, fontFamily: TD.display, fontWeight: 600, fontSize: 22, letterSpacing: 1, padding: '10px 20px' }}>
      {label}
    </div>
  </AbsoluteFill>
);

const segs = tour.segments as any[];
const segDuration = (i: number) =>
  (i + 1 < segs.length ? segs[i + 1].start_frame : TOUR_FRAMES) - segs[i].start_frame;

export const RiffTour: React.FC = () => (
  <AbsoluteFill style={{ background: TD.ground }}>
    {segs.map((s, i) => {
      const body = s.template ? (
        <>
          <OndaScene slug={String(s.template).replace('onda:', '')} propsOverride={s.props} />
          {s.label ? <TemplateLabel label={s.label} /> : null}
        </>
      ) : (
        <Card title={s.card?.title ?? ''} sub={s.card?.sub} link={s.card?.link} />
      );
      return (
        <Sequence key={s.id} from={s.start_frame} durationInFrames={segDuration(i)}>
          {body}
        </Sequence>
      );
    })}
    {/* the NBB voice — each spoken beat's mp3 at its conformed frame */}
    {segs.flatMap((s) =>
      (s.beats as any[])
        .filter((b) => b.audio_file && b.text)
        .map((b, j) => (
          <Sequence key={`aud-${s.id}-${j}`} from={b.frame}>
            <Audio src={staticFile(b.audio_file)} />
          </Sequence>
        )),
    )}
    {/* captions as karaoke CC, aligned to the same conformed frames */}
    {segs.flatMap((s) =>
      (s.beats as any[])
        .filter((b) => b.text)
        .map((b, j) => (
          <Sequence key={`cap-${s.id}-${j}`} from={b.frame} durationInFrames={Math.max(1, b.hold || 1)}>
            <BeatCaption beat={b} />
          </Sequence>
        )),
    )}
  </AbsoluteFill>
);
