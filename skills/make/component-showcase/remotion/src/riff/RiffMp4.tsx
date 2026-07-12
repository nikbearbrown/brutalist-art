import React from 'react';
import { AbsoluteFill, Sequence, Audio, OffthreadVideo, staticFile } from 'remotion';
import { BeatCaption } from './BeatCaption';
import { TD } from '../teardown';
import type { Beat } from '../schedule/schedule';
import riff from '../../beats/soul-tuzi.conformed.json';

// THE MP4 RIFF CUT: body segments play a Higgsfield clip (public/clips/<name>) under the
// teardown caption band; outro segments render the Remotion brutalist card. Same conformed
// beat sheet contract as the Onda tour (riff_audio -> riff_conform), so audio + captions are
// identical — only the scene body differs (OffthreadVideo instead of an Onda component).
export const MP4_FPS = (riff as { fps: number }).fps;
export const MP4_FRAMES = (riff as { total_frames: number }).total_frames;

const Card: React.FC<{ title: string; sub?: string; link?: string }> = ({ title, sub, link }) => (
  <AbsoluteFill style={{ background: TD.ground, alignItems: 'center', justifyContent: 'center', flexDirection: 'column' }}>
    <div style={{ width: 110, height: 7, background: TD.red, marginBottom: 28 }} />
    <div style={{ fontFamily: TD.display, fontWeight: 700, fontSize: 84, color: TD.ink, textAlign: 'center', letterSpacing: -1, whiteSpace: 'pre-line' }}>
      {title}
    </div>
    {sub ? (
      <div style={{ fontFamily: TD.display, fontSize: 24, letterSpacing: 2, textTransform: 'uppercase', color: TD.gray, marginTop: 22 }}>
        {sub}
      </div>
    ) : null}
    {link ? <div style={{ fontFamily: TD.serif, fontSize: 30, color: TD.red, marginTop: 30 }}>{link}</div> : null}
  </AbsoluteFill>
);

const ClipScene: React.FC<{ clip: string }> = ({ clip }) => (
  <AbsoluteFill style={{ background: TD.ink }}>
    <OffthreadVideo
      src={staticFile(`clips/${clip}`)}
      loop
      muted
      style={{ width: '100%', height: '100%', objectFit: 'cover' }}
    />
    {/* gradient scrim so white caption text pops against any clip */}
    <AbsoluteFill style={{
      background: 'linear-gradient(to top, rgba(0,0,0,0.72) 0%, rgba(0,0,0,0.35) 30%, transparent 58%)',
      pointerEvents: 'none',
    }} />
  </AbsoluteFill>
);

const segs = (riff as { segments: any[] }).segments;
const segDuration = (i: number) =>
  (i + 1 < segs.length ? segs[i + 1].start_frame : MP4_FRAMES) - segs[i].start_frame;

export const RiffMp4: React.FC = () => (
  <AbsoluteFill style={{ background: TD.ground }}>
    {segs.map((s, i) => (
      <Sequence key={s.id} from={s.start_frame} durationInFrames={Math.max(1, segDuration(i))}>
        {s.clip ? <ClipScene clip={s.clip} /> : <Card title={s.card?.title ?? ''} sub={s.card?.sub} link={s.card?.link} />}
      </Sequence>
    ))}
    {segs.flatMap((s) =>
      (s.beats as any[])
        .filter((b) => b.audio_file && b.text)
        .map((b, j) => (
          <Sequence key={`aud-${s.id}-${j}`} from={b.frame}>
            <Audio src={staticFile(b.audio_file)} />
          </Sequence>
        )),
    )}
    {segs.flatMap((s) =>
      (s.beats as any[])
        .filter((b) => b.text)
        .map((b, j) => (
          <Sequence key={`cap-${s.id}-${j}`} from={b.frame} durationInFrames={Math.max(1, b.hold || 1)}>
            <BeatCaption beat={b as Beat} overlay={!!s.clip} />
          </Sequence>
        )),
    )}
  </AbsoluteFill>
);
