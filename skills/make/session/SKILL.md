---
name: session
description: >
  Session Notes for voice generation — direct a READING, don't just label it.
  The Songbird `session` pattern applied to the toolkit: turn narration or a
  poem into (1) a STYLE-box paste for Suno (global setup: voice, register,
  tempo, the breath rule, bed guidance) and (2) direction-tagged lyrics
  ([spoken word — [delivery]] above every section). Use when the user types
  `session`, asks for session notes, wants to direct a Suno reading of a poem
  or narration, or the bare [spoken word] tag isn't enough. Output is text to
  paste — the human generates in Suno; the stem comes back through pantry/ to
  suno-slice (narration reels) or recitation-film (poems).
metadata:
  tags: suno, session-notes, spoken-word, voice, songbird, poem, recitation
---

# session — direct the reading

The lesson from the [spoken word] era: a single style label keeps Suno from
singing, but it doesn't tell the voice HOW to read. Session Notes do. The
pattern (from Songbird's `session` engine): global setup → form map →
per-section direction → production notes. No visuals, structured text only.

## Two paths

### A. Narration reels (automated)

`./art suno [reel]` already emits the whole package from beat_sheet.json:

- `[slug].suno.style.txt` — the session notes for Suno's STYLE box:
  voice + register, ~140 wpm, "no singing", the SLICER'S RULE ("leave a full
  breath of silence between sections"), sparse-bed guidance for stem
  separation.
- `[slug].suno.N.txt` — lyrics with a direction tag above every beat:
  `[spoken word — steady, plainspoken, dry]`. The delivery derives from the
  beat's role (hook / body / hero / close), or set it per beat with a
  `"delivery"` field in the sheet — that field is this skill's authoring
  surface: write direction like a producer ("slower, weighted — let each
  line land"), not like a style label.
- `[slug].suno.map.json` — which beats each lyric file carries (the slicer
  trusts this over recomputation).

### B. Poems / recitations (authored)

For a poem the human writes the session notes — the form IS the direction.
Author two pastes into the reel's folder:

1. STYLE box — global setup: whose voice, the register ("measured, intimate,
   no melodrama"), tempo, what the music bed may do (or "no bed"), and the
   breath rule between stanzas.
2. LYRICS box — the poem with a direction tag above each stanza:
   `[spoken word — hushed, rising through the third line]`. Keep the poem's
   own text EXACT (any adaptation is content — voxlit's ADAPTATION MARKER
   law applies downstream).

The performance comes back as a mastered stem into `pantry/`, and the reel
builds with `recitation-film` (the performance is the master clock, forced
alignment of the KNOWN text — GATE 0) — or, for beat-sheet reels, with
`./art suno-slice`.

## The worked example

`youtube/she-walks-in-beauty/pantry/` — Byron (1814, public domain), read in
Bear's Suno voice under session-notes direction:
`SheWalksinBeautybyLordByron1814NateSpoken-mastered.wav` + `song.txt`.
Note its stanza breaks differ from Byron's printed 6/6/6 — downstream films
must carry the adaptation marker.

## Rules

- Session notes direct, never transcribe: no bar counts read aloud, no meta.
- The breath rule is non-negotiable for anything the slicer will cut.
- Style box ≤ ~1000 chars; lyrics files ≤ 4000 chars (the exporter enforces).
- The human generates; the machine never claims to have produced the audio.
