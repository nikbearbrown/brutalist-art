// Root.tsx — composition registration for the Strange Brothers overlay.
//
// width/height match the SOURCE video (1920x1080) so there is no rescale; fps and
// durationInFrames come from beat_data.json so the timeline ends exactly with the
// track. Default composition "MusicVideo" is lyrics-only (no audiogram); opt into
// the waveform with "MusicVideo-Wave".

import { Composition } from "remotion";
import { MusicVideo } from "./MusicVideo";
import beatData from "./beat_data.json";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* default look: karaoke lyrics only, no waveform */}
      <Composition
        id="MusicVideo"
        component={MusicVideo}
        durationInFrames={beatData.durationInFrames}
        fps={beatData.fps}
        width={1920}
        height={1080}
        defaultProps={{ showWaveform: false }}
      />
      {/* opt-in variant: same timing + the audiogram waveform */}
      <Composition
        id="MusicVideo-Wave"
        component={MusicVideo}
        durationInFrames={beatData.durationInFrames}
        fps={beatData.fps}
        width={1920}
        height={1080}
        defaultProps={{ showWaveform: true }}
      />
      {/* portrait 9:16 with waveform — for Shorts */}
      <Composition
        id="MusicVideo-Wave-Portrait"
        component={MusicVideo}
        durationInFrames={beatData.durationInFrames}
        fps={beatData.fps}
        width={1080}
        height={1920}
        defaultProps={{ showWaveform: true }}
      />
    </>
  );
};
