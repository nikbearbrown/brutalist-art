#!/usr/bin/env python3
"""riff_gate.py — the riff visual gate (layout-invariant lint). The Remotion analog of vox's
Gate W: a fast, no-render static check on a conformed beat sheet + the known layout constants.
Catches the failures that bit us — label over caption, captions too long for the safe band,
two captions on screen at once, off-palette contrast. Run after riff_conform, before render.

  exit 0 clean · 1 warnings · 2 errors

Usage:  python3 scripts/riff_gate.py beats/templates-onda.conformed.json
"""
import argparse, json, sys
from pathlib import Path

# Layout contract (must match RiffTour/BeatCaption):
LABEL_BAND = ("top", 0.0, 0.22)      # TemplateLabel lives in the top ~22%
CAPTION_BAND = ("bottom", 0.72, 1.0) # lower-third captions live in the bottom ~28%
# Text budgets (chars) before a caption crowds the safe band, by beat type:
CAP_WARN = {"analytic": 230, "default": 150}
CAP_ERR = {"analytic": 320, "default": 220}
LABEL_WARN = 30
TOKENS = {"INK": "#2A1A0E", "RED": "#C8102E", "GRAY": "#545454"}  # on white; must clear WCAG AA


def lum(h):
    r, g, b = (int(h[i:i+2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = f(r), f(g), f(b)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("beatsheet", type=Path)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    sheet = json.loads(a.beatsheet.read_text())
    errs, warns = [], []

    # L1 — band separation is structural (label top, captions bottom); assert it holds.
    if not (LABEL_BAND[2] <= CAPTION_BAND[1]):
        errs.append("L1 BAND-OVERLAP: label band and caption band intersect — they will collide")

    # L2 — no two caption beats share a frame range (two captions on screen at once).
    beats = []
    for s in sheet["segments"]:
        for b in s["beats"]:
            if (b.get("text") or "").strip():
                beats.append((b["frame"], b["frame"] + max(1, b.get("hold", 1)), s["id"], b.get("type")))
    beats.sort()
    for (s0, e0, id0, t0), (s1, e1, id1, t1) in zip(beats, beats[1:]):
        if s1 < e0:
            warns.append(f"L2 CAPTION-OVERLAP: {id0}({t0}) [{s0}-{e0}] and {id1}({t1}) start {s1} overlap")

    # L3 — caption length within the safe band.
    for s in sheet["segments"]:
        for b in s["beats"]:
            t = (b.get("text") or "").strip()
            if not t or b.get("type") in ("outro-topic", "outro-channel"):
                continue
            n = len(t)
            k = "analytic" if b.get("type") == "analytic" else "default"
            if n > CAP_ERR[k]:
                errs.append(f"L3 CAPTION-TOO-LONG {s['id']}/{b.get('type')} — {n} chars (> {CAP_ERR[k]}); will overflow the band")
            elif n > CAP_WARN[k]:
                warns.append(f"L3 CAPTION-LONG {s['id']}/{b.get('type')} — {n} chars (> {CAP_WARN[k]}); may crowd the band")

    # L4 — label chip length.
    for s in sheet["segments"]:
        lab = s.get("label")
        if lab and len(lab) > LABEL_WARN:
            warns.append(f"L4 LABEL-LONG {s['id']} — '{lab}' is {len(lab)} chars (> {LABEL_WARN}); may overrun the chip")

    # L5 — teardown text tokens clear WCAG AA (4.5) on white.
    for name, hexc in TOKENS.items():
        c = contrast(hexc, "#FFFFFF")
        if c < 4.5:
            (errs if c < 3.0 else warns).append(f"L5 CONTRAST {name} {hexc} on white = {c:.2f}:1 (< 4.5 AA)")

    tag = f"[riffGate] {a.beatsheet.name}"
    for e in errs: print(f"{tag} ERROR {e}")
    for w in warns: print(f"{tag} WARN  {w}")
    if not errs and not warns:
        print(f"{tag} clean — layout invariants hold")
    return 2 if errs else (1 if warns else 0)


if __name__ == "__main__":
    sys.exit(main())
