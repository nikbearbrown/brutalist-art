# Registration, reel, and render

How to wire generated scenes into the Remotion project. Mirrors the working
`chinese-room-explainer` setup. All compositions are `fps={30} width={1920} height={1080}`.

## 1. The reel sequencer — `[project]/src/[PascalName]Reel.tsx`

```tsx
import React from 'react';
import { Series } from 'remotion';
import { Scene01Hook } from './scenes/Scene-01-hook';
import { Scene02Name } from './scenes/Scene-02-name';
// ...one import per scene, in order

export const REEL_FRAMES = 240 + 360 + 420; // sum of every scene's durationInFrames

export const ConceptReel: React.FC = () => (
  <Series>
    <Series.Sequence durationInFrames={240}><Scene01Hook /></Series.Sequence>
    <Series.Sequence durationInFrames={360}><Scene02Name /></Series.Sequence>
    {/* ...one Sequence per scene; durationInFrames must match the scene's export */}
  </Series>
);
```

## 2. Register in `src/Root.tsx`

Add imports near the other demo imports, then add `<Composition>` entries inside
`RemotionRoot` — one per scene (renderable in isolation) plus the full reel:

```tsx
import { Scene01Hook } from '../demos/[slug]/src/scenes/Scene-01-hook';
import { Scene02Name } from '../demos/[slug]/src/scenes/Scene-02-name';
import { ConceptReel, REEL_FRAMES } from '../demos/[slug]/src/ConceptReel';
```

```tsx
{/* ── [Concept] explainer ─────────────────────────── */}
<Composition id="[Slug]-01-Hook" component={Scene01Hook} durationInFrames={240} fps={30} width={1920} height={1080} />
<Composition id="[Slug]-02-Name" component={Scene02Name} durationInFrames={360} fps={30} width={1920} height={1080} />
<Composition id="[Slug]Reel"     component={ConceptReel} durationInFrames={REEL_FRAMES} fps={30} width={1920} height={1080} />
```

The scene appears in Remotion Studio automatically on save.

## 3. Frame budget (30 fps)

| Beat type | Frames | Seconds |
|---|---|---|
| Silent caption beat | 120–210 | 4–7s |
| Voiced beat | `ceil(words ÷ 2.5 × 30) + 60` | narration + ~2s |

Audio starts at `from={30}` (a 1s visual lead-in). A voiced scene's
`durationInFrames` must be **≥** its narration length, or speech is cut off.


## 5. Studio organization — the default layout

`import { Composition, Folder } from "remotion";`

Register so the **newest video is alone at the top** and everything older is collapsed
under one `archive` folder. Do this by default; reorganize only if asked.

```tsx
export const RemotionRoot: React.FC = () => (
  <>
    {/* newest video — alone at the top */}
    <Folder name="[slug]">
      <Composition id="[Slug]Reel" component={ConceptReel} durationInFrames={REEL_FRAMES} fps={30} width={1920} height={1080} />
      <Composition id="[Slug]-01-Hook" component={Scene01Hook} durationInFrames={240} fps={30} width={1920} height={1080} />
      {/* ...the rest of its scenes */}
    </Folder>

    {/* everything older — collapsed, never deleted */}
    <Folder name="archive">
      <Folder name="[previous-slug]">{/* its compositions */}</Folder>
      {/* ...one subfolder per older project */}
    </Folder>
  </>
);
```

When you add the next video, move the current top folder into `archive` and put the new
one first. `<Folder>` only nests the sidebar; every composition still renders by id.

## 4. Hand-off commands (the skill stops here; the user runs these)

```bash
# preview
npx remotion studio

# one-frame sanity check (zero-based frame; 30 = the 1s mark)
npx remotion still [Slug]Reel --scale=0.25 --frame=30

# optional voice (needs ELEVENLABS_API_KEY + ELEVENLABS_VOICE_ID; see KEYS.md)
npx tsx scripts/generate-audio.ts demos/[slug]/blueprint.md public/[slug]

# full render
npx remotion render [Slug]Reel out/[slug].mp4
```
