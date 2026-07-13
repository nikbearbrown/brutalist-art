---
name: songbird
description: >
  Songbird vendored into Brutalist — the prompt-sequencing director and
  musical session producer. Owns THE SEQUENCING LAW (Entry–Beat–Exit with
  continuity lanes) that every generated-clip prompt chain in this toolkit
  follows, plus the engines: session notes (via the session skill), music-
  video and dance-video prompt sequencing, the plug viral hook (spoken-word
  cliffhanger for the shorts funnel), 169 outpainting prompts, and the
  parameter rule (style strings append verbatim to every prompt). Use when
  the user types `songbird`, `boogie`, `song`, `plug`, `169`, asks for a
  music/dance video prompt sequence, a viral hook line, or invokes the
  sequencing law while authoring shot prompts.
metadata:
  tags: songbird, sequencing, prompts, music-video, dance, viral-hook, session, higgsfield
---

# songbird — the sequencing director

Vendored from the Songbird GPT. The house version drops the persona secrecy
(Brutalist is explicit about its rules) and keeps the machinery.

## THE SEQUENCING LAW (applies to every generated-clip prompt chain)

Never disconnected moments — every chain is one continuous experience.
Each unit (clip, section, or beat) has:

- **Entry** — inherits motion or context from what came before
- **Beat** — one clear, readable mini-event or musical idea
- **Exit** — motion or lead-in that points at what comes next

Continuity lanes to hold across the chain:
- Visual: space, lighting, character (outfit included), camera path
- Musical: key, tempo, groove, instrument roles, motifs

Builder skills that author per-beat generation prompts — story-film,
dance-video, music-video, lyric-resync, kids-video — apply this law when
writing their shot lists: long lyrics or many images produce ONE coherent
sequence, never a grab-bag.

## Engines and their house homes

| engine | what it does | house home |
|---|---|---|
| `session` | Session Notes — direct a reading/arrangement | **skills/make/session** (already landed; ./art suno emits it for narration reels) |
| `song` | music-video prompt sequence: performance, lip-sync, emotional beats matching lyrics, seamless camera flow | authoring pass inside **music-video** / **lyric-resync** |
| `boogie` | dance sequence: consistent dancer/outfit/setting/light, camera flows between shots, movement tied to the song's feel | authoring pass inside **dance-video** |
| `plug` | ONE spoken-word cliffhanger sentence — teases the resolution, never provides it; noir / cinematic / soulful; format: "[hook]. Watch the full story below." | the SHORTS FUNNEL: a stronger rewrite target for the shortened cut's outro and for description first-lines |
| `169` | Nano outpainting prompt — expand a still's visual field | pantry fill-ins: extending stills to 16:9 / 9:16 before slotting |
| `colorful` | handheld-iPhone hypercolor wander; imperfect framing, mythic everyday | a style preset for prompt chains (audience-preset sibling) |
| `Xmas` | lyric→visual prompts with THE PARAMETER RULE | seasonal preset; the rule generalizes (below) |

## THE PARAMETER RULE (generalized)

When a prompt chain carries a style string (`--p …`, aspect flags, model
params), it appends to EVERY prompt line EXACTLY as written — never altered,
never dropped mid-chain. This is how a chain stays one look end to end.

## Session-state logic (how a build session tracks context)

lyrics/song name = the core material; `style:` swaps style only; `remix` =
variation KEEPING continuity; `new song` = full reset. A session never mixes
material from two songs without an explicit reset.

## plug, worked

Input: the piece's central conflict or mystery. Output: one sentence that
tightens it without resolving, then the CTA. For a Brutalist short:
"The machine posted every video in this series — except the one it got
wrong. Watch the full story below." Tone options: noir, cinematic, soulful.
Never summarize; never answer the question the hook raises.
