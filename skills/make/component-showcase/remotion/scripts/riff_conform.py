#!/usr/bin/env python3
"""riff_conform.py — re-flow a riff beat sheet to the MEASURED audio (RIFFING.md two-pass).

Audio-first: after riff_audio.py has written `actual_duration_s` into every beat, this lays
the beats end-to-end at their real spoken lengths, injects a short observational silence at
each `event` beat, and then CONFORMS each template so its key event (the settle/reveal) lands
under that event beat. Emits <sheet>.conformed.json — the render's single source of truth.

  sacred: the event SEQUENCE + the spoken durations.  free variable: the visual holds.

Usage:  python3 scripts/riff_conform.py beats/onda-data-tour.beats.json
"""
import argparse, json, sys
from pathlib import Path

PAD = 4       # frames of breath between spoken beats
OBSERVE = 12  # frames of observational silence at an `event` beat (the settle lands here)
INTER_SEG = 10  # frames between segments


def conform_props(slug, props, event_local):
    """Set the template's timing so its key event lands at `event_local` frames into the
    segment. bar-chart: the accent (largest) bar is index 3, staggered; single-event
    templates (count-up/line-chart/pie-reveal) settle at `duration`."""
    p = {k: v for k, v in (props or {}).items() if k != "note"}
    if slug == "bar-chart":
        stagger, accent = 24, 3
        duration = event_local - accent * stagger
        if duration < 12:  # not enough room — tighten the stagger
            stagger = max(4, (event_local - 12) // accent)
            duration = event_local - accent * stagger
        p["stagger"] = stagger
        p["duration"] = max(12, duration)
    else:
        p["duration"] = max(12, event_local)
    return p


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("beatsheet", type=Path)
    a = ap.parse_args()
    sheet = json.loads(a.beatsheet.read_text())
    fps = sheet.get("fps", 30)

    cursor = 0
    for seg in sheet["segments"]:
        seg["start_frame"] = cursor
        for beat in seg["beats"]:
            beat["frame"] = cursor
            if beat.get("type") == "event":
                beat["hold"] = OBSERVE
                cursor += OBSERVE
            else:
                d = max(1, round(float(beat.get("actual_duration_s", 0)) * fps))
                beat["hold"] = d
                cursor += d + PAD
        # conform the template to seat its event under the `event` beat
        if seg.get("template"):
            ev = next((b for b in seg["beats"] if b.get("type") == "event"), None)
            if ev is not None:
                slug = seg["template"].replace("onda:", "")
                seg["props"] = conform_props(slug, seg.get("props"), ev["frame"] - seg["start_frame"])
        cursor += INTER_SEG

    sheet["total_frames"] = cursor
    sheet["conformed"] = True
    out = a.beatsheet.with_suffix("").with_suffix(".conformed.json")
    out.write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
    print(f"[ok] conformed → {out.name}  ·  {cursor} frames = {cursor/fps:.1f}s")
    for seg in sheet["segments"]:
        tp = seg.get("props", {})
        extra = f"  dur={tp.get('duration')} stagger={tp.get('stagger')}" if seg.get("template") else ""
        print(f"   {seg['id']:<11} start={seg['start_frame']:>5}{extra}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
