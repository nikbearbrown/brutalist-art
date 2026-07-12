# [STAR] tokens — character references in generated prompts

The prompt generator never writes a character description ad hoc. Characters
are TOKENS with a registry entry; the generator expands the token, so every
prompt in a series carries the identical descriptor + the identical reference
image. Identity lives in ONE place.

## Registry (one block per character)

```
[STAR]
  name:        Star
  descriptor:  adorable black and white penguin
  ref:         https://raw.githubusercontent.com/nikbearbrown/vox/main/aspects/kids/host/refs/star.png
  oref_weight: 300
  anchors:     round body, white belly panel, small orange beak and feet,
               no accessories  (the identity checklist volunteers reject against)
```

Rules for the ref image itself:
- ONE canonical image per character (front-facing, plain background, flat
  even light, full body). It lives in this repo under
  `aspects/kids/host/refs/` — committed and pushed, so the raw URL works.
  Updating the character = committing a new ref = every future prompt shifts
  together. Never hotlink an image that can move.
- Optional second ref (three-quarter view) for pose-heavy beats.

## Prompt expansion (the generator's template)

Input: the song/beat analysis (timings + per-beat scene notes). Output: one
fenced, paste-ready block per beat in PROMPTS.md — beat id first, per the
prompt law:

```
<ref-url> B01, large uppercase letter P prominently displayed, [STAR-DESC] standing beside the letter, preschool educational illustration, felt-paper diorama, layered paper cutout style, snowy background, soft pastel colors --ar 16:9 --oref <ref-url> --ow 300 --profile unwh2g4 --v 7
```

How the three reference mechanisms divide (don't conflate them):
- **URL at the front** = image prompt: loose influence on content/composition.
- **`--oref <url> --ow ~200-400`** = omni-reference: the CHARACTER lock (v7's
  replacement for --cref). This is what holds identity. Lower --ow lets pose
  and expression vary; higher freezes the look. Start ~300 for a host.
- **`--profile` / `--sref`** = the STYLE (felt-paper diorama look). Style and
  character are separate dials — keep them separate so a style tweak never
  redesigns the character.
- 9:16 variants: same prompt, `--ar 9:16`, "empty lower third" if captions land there.

## The pick gate (volunteers)

Generation is cheap; SELECTION is the QC. Per beat: generate a grid, volunteers
reject anything failing the identity anchors (silhouette, proportions, palette,
inventory — from the registry entry) or the scene requirement, pick the best.
Nothing auto-accepts. The keeper is renamed `B##-<token>.png`, dropped in the
episode's `pantry/` — normal intake takes it from there. Rejections cost
nothing; a wrong-eared penguin that ships costs the series.

## Identity law (identity-stable, not pixel-identical)

Recognizably-the-same beats byte-identical: the imperfection is the medium
(felt reads handmade). What must hold every generation: silhouette, proportion
ratios, palette, design inventory. What may drift: texture, grain, micro-pose.
Boil-cycle technique: 2-3 keepers of the SAME pose cycled at 6-8fps during
long holds — continuous handmade shimmer instead of a recast at each cut.
Overlay test = tolerance bands on the anchors, applied by the volunteers' eyes
first and the drift script second.

## Song-driven episodes

When the episode IS a song (alphabet song, color song): the song analysis is
the master clock (lyric-match discipline — per-line beats, forced alignment),
the generator writes one prompt per line with the [TOKEN]s, and Gate K's
pacing laws still govern the CUTTING (no sub-2s cuts, one new stimulus per
beat) even though music runs continuously — a song episode is the one place
continuous music is the design, not a violation.
