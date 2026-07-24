#!/usr/bin/env python3
"""_align.py — forced alignment for she-walks-in-beauty (GATE 0).

faster-whisper word timestamps on the mastered WAV, DP-matched to the known
poem lines → align/words.json + align/lines.json + align/REPORT.txt.

  python3 youtube/she-walks-in-beauty/_align.py

Output:
  align/words.json — [{w, start, end}, ...]
  align/lines.json — {breath_ms, lines:[{i,text,start,end,matched}], breaths:[...]}
  align/REPORT.txt — 5 random spot-checks for GATE 0 sign-off
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WAV  = HERE / "pantry" / "SheWalksinBeautybyLordByron1814NateSpoken-mastered.wav"
SONG = HERE / "pantry" / "song.txt"
OUT  = HERE / "align"
OUT.mkdir(exist_ok=True)

BREATH_MS = 350  # inter-line gap (ms) that counts as a breath

def norm(w):
    return re.sub(r"[^a-z']", "", w.lower())

def load_lines():
    lines = []
    for ln in SONG.read_text().splitlines():
        ln = ln.strip()
        if ln and not ln.startswith(("TITLE", "ARTIST")):
            lines.append(ln)
    return lines

def main():
    from faster_whisper import WhisperModel
    import numpy as np

    if not WAV.exists():
        sys.exit(f"[align] WAV not found: {WAV}")

    LINES = load_lines()
    print(f"[align] {len(LINES)} lines to align")
    print(f"[align] running faster-whisper small.en on {WAV.name} ...")

    model = WhisperModel("small.en", device="auto", compute_type="int8")
    segs, _ = model.transcribe(str(WAV), word_timestamps=True,
                               vad_filter=True, beam_size=5)
    words = [{"w": w.word.strip(), "start": round(w.start, 3),
              "end": round(w.end, 3)}
             for s in segs for w in (s.words or [])]
    (OUT / "words.json").write_text(json.dumps({"words": words}, indent=0))
    print(f"[align] {len(words)} words transcribed -> align/words.json")

    # DP alignment: known line-words → transcribed words (monotonic)
    try:
        from rapidfuzz.distance import Levenshtein
        sim = lambda a, b: 1 - Levenshtein.normalized_distance(a, b)
    except ImportError:
        sim = lambda a, b: 1.0 if a == b else (0.6 if a[:3] == b[:3] else 0.0)

    flat, line_of = [], []
    for i, line in enumerate(LINES):
        for w in line.split():
            flat.append(norm(w)); line_of.append(i)
    tw = [norm(x["w"]) for x in words]
    n, m = len(flat), len(tw)
    S = np.full((n + 1, m + 1), -1e9)
    S[0, :] = 0
    P = np.zeros((n + 1, m + 1), dtype=np.int8)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match  = S[i-1, j-1] + sim(flat[i-1], tw[j-1])
            skip_t = S[i,   j-1] - 0.05   # extra transcribed word
            skip_k = S[i-1, j  ] - 0.4    # missed known word
            S[i, j] = max(match, skip_t, skip_k)
            P[i, j] = [match, skip_t, skip_k].index(S[i, j])

    # backtrack
    j = int(S[n].argmax()); i = n
    hit = [None] * n
    while i > 0 and j > 0:
        p = P[i, j]
        if p == 0:
            hit[i-1] = j-1; i -= 1; j -= 1
        elif p == 1:
            j -= 1
        else:
            i -= 1

    lines_out, k = [], 0
    for li, line in enumerate(LINES):
        wds = line.split()
        idx = [hit[k + q] for q in range(len(wds)) if hit[k + q] is not None]
        k += len(wds)
        if idx:
            lines_out.append({"i": li + 1, "text": line,
                              "start": words[idx[0]]["start"],
                              "end":   words[idx[-1]]["end"],
                              "matched": len(idx)})
        else:
            lines_out.append({"i": li + 1, "text": line,
                              "start": None, "end": None, "matched": 0})

    # interpolate unmatched lines, enforce monotonic
    for q, L in enumerate(lines_out):
        if L["start"] is None:
            prev_end = next((lines_out[r]["end"] for r in range(q-1, -1, -1)
                             if lines_out[r]["end"]), 0.0)
            nxt = next((lines_out[r]["start"] for r in range(q+1, len(lines_out))
                        if lines_out[r]["start"]), prev_end + 3.0)
            L["start"] = prev_end
            L["end"]   = max(prev_end + 0.5, nxt)
            L["interpolated"] = True

    breaths = []
    for a, b in zip(lines_out, lines_out[1:]):
        gap = b["start"] - a["end"]
        if gap * 1000 >= BREATH_MS:
            breaths.append({"after_line": a["i"], "t": a["end"],
                            "gap_s": round(gap, 3)})

    (OUT / "lines.json").write_text(json.dumps(
        {"breath_ms": BREATH_MS, "lines": lines_out, "breaths": breaths},
        indent=2))
    print(f"[align] -> align/lines.json  ({len(lines_out)} lines, {len(breaths)} breaths)")

    bad = [L["i"] for L in lines_out if L["matched"] == 0]
    import random
    random.seed(42)
    spot = random.sample([L for L in lines_out if L["matched"]], min(5, len(lines_out)))
    rep = [
        f"lines matched: {len(LINES) - len(bad)}/{len(LINES)}",
        f"breaths (>= {BREATH_MS}ms): {len(breaths)}",
        f"unmatched (interpolated): {bad}",
        "",
        "SPOT-CHECK 5 (GATE 0 — alignment lock):",
    ]
    for L in spot:
        rep.append(f"  {L['start']:7.2f}-{L['end']:7.2f}  {L['text']}")
    (OUT / "REPORT.txt").write_text("\n".join(rep))
    print("\n".join(rep))
    print("\n[align] GATE 0: scrub the 5 spot-checks above before trusting word timing.")
    print("[align] done — align/words.json  align/lines.json  align/REPORT.txt")

if __name__ == "__main__":
    sys.exit(main())
