#!/usr/bin/env python3
"""
suno_export.py — export a beat sheet's narration for Suno voice generation.

THE SUNO PATH (the cheap voice): instead of one ElevenLabs call per beat,
the whole narration goes to Suno (Bear's uploaded voice) as spoken word, the
human downloads the VOCAL-ONLY stem into pantry/, and suno_slice.py cuts it
into the same mp3/beat-<BID>.mp3 slots generate_audio.py would have filled.
Whether the voice-over came from Suno or ElevenLabs, THE REST OF THE
PIPELINE IS IDENTICAL — mp3 per beat + measured actual_duration_s is the
interface, and the beat sheet stays the single source of truth.

What this writes, next to beat_sheet.json:

  <slug>.suno.style.txt  SESSION NOTES for Suno's STYLE box — the Songbird
                         `session` pattern: global setup (spoken word, voice,
                         tempo, register), form direction, and the production
                         note that matters most to the slicer: A FULL BREATH
                         OF SILENCE BETWEEN SECTIONS.
  <slug>.suno.1.txt      the narration, beat by beat, each beat preceded by a
  <slug>.suno.2.txt      DIRECTION TAG — [spoken word — <delivery>] — that
  ...                    directs the reading of that beat (Suno drifts into
                         singing without the spoken-word anchor, even when the
                         style note says spoken word). Delivery derives from
                         the beat's act (hook / body / hero / close) or from an
                         optional "delivery" field on the beat in the sheet.
                         A new file starts whenever the next beat would push
                         the current file past --limit (default 4000 chars,
                         Suno's lyrics box cap). Beats are never split.
                         --plain reverts to the bare [spoken word] tag.

The human loop:
  1. Paste <slug>.suno.style.txt into Suno's STYLE box.
  2. Paste <slug>.suno.N.txt into the LYRICS box. Generate with your voice.
  3. Download the VOCAL-ONLY stem (no music bed).
  4. Save it as pantry/<slug>-vocals-N.wav (or .mp3/.m4a/.flac).
  5. When every stem is in the pantry: python3 runtime/scripts/suno_slice.py <reel>

GATE P applies exactly as it does to generate_audio.py: PEDAGOGY.md must
carry VERDICT: PASS before narration leaves the building (--no-gate to
override deliberately).

Usage:
    python3 suno_export.py path/to/<slug>
    python3 suno_export.py path/to/<slug> --limit 4000 --tag "[spoken word]"
"""
import argparse
import re
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_audio import normalize_for_tts   # same spoken-form safety net

DEFAULT_LIMIT = 4000
DEFAULT_TAG = "[spoken word]"


def narrated_beats(sheet):
    return [b for b in sheet["beats"] if (b.get("narration_text") or "").strip()]


def delivery_for(b, beats):
    """Per-beat reading direction (the Songbird `session` pattern): an explicit
    "delivery" field on the beat wins; otherwise derive from its role."""
    if (b.get("delivery") or "").strip():
        return b["delivery"].strip()
    act = (b.get("act") or "").upper()
    mech = json.dumps(b.get("graphic") or {}).lower()
    if b is beats[0] or act == "INTRO":
        return "open direct, unhurried, a half-smile"
    if "hero" in mech:
        return "slower, weighted — let each line land"
    if act == "OUTRO":
        return "warm, conclusive, an easy close"
    return "steady, plainspoken, dry"


def beat_block(b, tag, beats=None, plain=False):
    text = normalize_for_tts(b["narration_text"].strip())
    # the TTS map turns em-dashes into " , " for pause timing — tidy the
    # spacing so the pasted lyrics read clean (", " not " ,  ")
    text = re.sub(r"\s+,\s+", ", ", text)
    if plain or beats is None:
        return f"{tag}\n{text}"
    return f"[spoken word — {delivery_for(b, beats)}]\n{text}"


def session_notes(sheet, tag=DEFAULT_TAG):
    """The STYLE-box paste — Songbird `session` mode applied to narration:
    global setup + form direction + the production note the slicer depends on."""
    title = sheet["metadata"].get("title", sheet["metadata"].get("slug", ""))
    n = len(narrated_beats(sheet))
    return (
        f"Spoken word. A single male voice reading a technical essay aloud — "
        f"dry, wry, unhurried, plainspoken. No singing, no melody, no rap "
        f"cadence, no harmonies. Conversational tempo, about 140 words a "
        f"minute. The piece is '{title}': {n} short sections, each marked "
        f"[spoken word — direction] in the lyrics; follow each section's "
        f"direction. LEAVE A FULL BREATH OF SILENCE BETWEEN SECTIONS — a "
        f"clear pause at every section break. Keep any music bed sparse and "
        f"far under the voice so the spoken stem separates cleanly. Clean "
        f"close-mic studio vocal, no reverb tail.\n")


def chunk_beats(sheet, limit=DEFAULT_LIMIT, tag=DEFAULT_TAG, plain=False):
    """Partition narrated beats into files of <= limit chars (beats whole).
    Returns [(chunk_text, [beat, ...]), ...]. The export also writes
    <slug>.suno.map.json recording which beats each file carries —
    suno_slice.py prefers the map over recomputing, so tag style can never
    drift the partition."""
    beats = narrated_beats(sheet)
    chunks, cur_beats, cur_text = [], [], ""
    for b in beats:
        block = beat_block(b, tag, beats, plain)
        if len(block) > limit:
            raise SystemExit(f"[suno] beat {b['beat_id']} alone exceeds "
                             f"{limit} chars — split the narration in the sheet")
        cand = block if not cur_text else cur_text + "\n\n" + block
        if len(cand) > limit and cur_beats:
            chunks.append((cur_text, cur_beats))
            cur_beats, cur_text = [b], block
        else:
            cur_beats, cur_text = cur_beats + [b], cand
    if cur_beats:
        chunks.append((cur_text, cur_beats))
    return chunks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", type=Path)
    ap.add_argument("--limit", type=int, default=DEFAULT_LIMIT,
                    help="max chars per .suno.N.txt (Suno lyrics cap, default 4000)")
    ap.add_argument("--tag", default=DEFAULT_TAG,
                    help="meta tag written above EVERY beat (default '[spoken word]')")
    ap.add_argument("--no-gate", action="store_true",
                    help="skip the GATE P (PEDAGOGY VERDICT: PASS) check")
    ap.add_argument("--plain", action="store_true",
                    help="bare [spoken word] tags; skip session notes + per-beat delivery direction")
    a = ap.parse_args()
    folder = a.folder.resolve()
    sheet = json.loads((folder / "beat_sheet.json").read_text())
    slug = sheet["metadata"].get("slug", folder.name)

    if not a.no_gate:
        ped = folder / "PEDAGOGY.md"
        if not (ped.exists() and "VERDICT: PASS" in ped.read_text()):
            raise SystemExit("[suno] GATE P: PEDAGOGY.md with VERDICT: PASS required "
                             "before narration export (--no-gate to override)")

    # the stems land here — make the drop target exist before the human needs it
    (folder / "pantry").mkdir(exist_ok=True)
    (folder / "mp3").mkdir(exist_ok=True)

    if not a.plain:
        style = folder / f"{slug}.suno.style.txt"
        style.write_text(session_notes(sheet, a.tag))
        print(f"[suno] {style.name}  {len(style.read_text())} chars  → Suno STYLE box")

    chunks = chunk_beats(sheet, a.limit, a.tag, a.plain)
    chunk_map = {}
    for i, (text, beats) in enumerate(chunks, 1):
        out = folder / f"{slug}.suno.{i}.txt"
        out.write_text(text + "\n")
        chunk_map[str(i)] = [b["beat_id"] for b in beats]
        print(f"[suno] {out.name}  {len(text)} chars · {len(beats)} beats "
              f"({beats[0]['beat_id']}–{beats[-1]['beat_id']})  → Suno LYRICS box")
    (folder / f"{slug}.suno.map.json").write_text(json.dumps(chunk_map, indent=1))
    print(f"[suno] {len(chunks)} lyric file(s). For each N:")
    if not a.plain:
        print(f"[suno]   0. paste {slug}.suno.style.txt into Suno's STYLE box (session notes)")
    print('[suno]   1. paste <slug>.suno.N.txt into the LYRICS box · your voice · generate')
    print(f"[suno]   2. download the VOCAL-ONLY stem (no music bed)")
    print(f"[suno]   3. save as pantry/{slug}-vocals-N.wav  (mp3/m4a/flac also fine)")
    print(f"[suno] then: python3 runtime/scripts/suno_slice.py {folder.name}  "
          f"# fills mp3/beat-*.mp3 — no ElevenLabs calls")


if __name__ == "__main__":
    main()
