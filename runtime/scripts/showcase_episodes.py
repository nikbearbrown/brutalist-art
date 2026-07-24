#!/usr/bin/env python3
"""
showcase_episodes.py — the Brutalist meta-series builder for the logo
showcase reels: standardized 16:9 endings (verdict -> Your Turn -> title
re-read) and 9:16 one-minute episode series, both rendered through the
ShowcaseWrap composition (runtime/remotion/src/ShowcaseWrap.tsx) WITHOUT
touching the monolithic showcase comps.

Audio-first: bookend narration lives in per-episode mini beat sheets, Kokoro
generates mp3s, THEN `props` measures them and emits render props. Body audio
is reassembled from the source reel's existing per-technique mp3s padded to
the comp's own timing.json frames — the same contract that timed the visuals.

Commands (run from brutalist-art/):
  python3 runtime/scripts/showcase_episodes.py scaffold <mark>   # mini beat sheets for Kokoro
  python3 runtime/scripts/showcase_episodes.py props    <mark>   # measure mp3s -> props.json per cut
  python3 runtime/scripts/showcase_episodes.py mux      <mark>   # episode audio + final mp4 mux
  python3 runtime/scripts/showcase_episodes.py status   <mark>

Between scaffold and props:
  python3 runtime/scripts/generate_audio_kokoro.py youtube/showcase-series/<mark>/<cut>
for every cut folder scaffold reports (free, local).

Between props and mux: render each cut FOREGROUND, one at a time
(the props step prints the exact `npx remotion render ... --concurrency=1`
commands; never background them, never poll ps — standing rule #3 spirit).

Config: youtube/showcase-series/<mark>/episodes.json — see the
musinique-logo-2 pilot for the authored exemplar (GATE: the human approves
that file's narration before audio is generated for a mark).
"""
from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path

ART = Path(__file__).resolve().parents[2]          # brutalist-art/
REMOTION = ART / "runtime" / "remotion"
SERIES = ART / "youtube" / "showcase-series"
FPS = 30
PAD_F = 8            # breathing frames appended after each bookend narration
FFMPEG = "ffmpeg"

# mark -> comp timing jsons (in runtime/remotion/src/) + source reel folders
MARKS = {
    "musinique-logo-2": {
        "timing_16x9": "musinique-logo-2-timing.json",
        "timing_916": "musinique-logo-2-remotion-showcase-timing.json",
        "reel_16x9": "claude-liam-musinique-logo-2-remotion-showcase-16x9",
        "reel_916": "claude-liam-musinique-logo-2-remotion-showcase",
    },
    "musinique-logo": {
        "timing_16x9": "musinique-logo-remotion-showcase-timing.json",  # comp imports same file for both aspects
        "timing_916": "musinique-logo-remotion-showcase-timing.json",
        "reel_16x9": "claude-liam-musinique-logo-remotion-showcase-16x9",
        "reel_916": "claude-liam-musinique-logo-remotion-showcase",
    },
    "bear-brown-logo": {
        "timing_16x9": "bear-brown-logo-remotion-showcase-16x9-timing.json",
        "timing_916": "bear-brown-logo-remotion-showcase-timing.json",
        "reel_16x9": "claude-liam-bear-brown-logo-remotion-showcase-16x9",
        "reel_916": "claude-liam-bear-brown-logo-remotion-showcase",
    },
    "bear-brown-initials": {
        "timing_16x9": "bear-brown-initials-remotion-showcase-timing.json",
        "timing_916": "bear-brown-initials-timing.json",
        "reel_16x9": "claude-liam-bear-brown-initials-remotion-showcase-16x9",
        "reel_916": "claude-liam-bear-brown-initials-remotion-showcase",
    },
    "h-logo": {
        "timing_16x9": "h-logo-remotion-showcase-timing.json",
        "timing_916": "h-logo-remotion-showcase-timing.json",
        "reel_16x9": "claude-liam-h-logo-remotion-showcase",  # 16x9 folder has 0 mp3s; use 9:16 reel audio
        "reel_916": "claude-liam-h-logo-remotion-showcase",
    },
    "hai-wordmark": {
        "timing_16x9": "hai-wordmark-timing.json",
        "timing_916": "hai-wordmark-timing.json",
        "reel_16x9": "claude-liam-hai-wordmark-remotion-showcase-16x9",
        "reel_916": "claude-liam-hai-wordmark-remotion-showcase",
    },
}

# NOTE: several 16:9/9:16 comps share a timing json on disk; the offsets are
# computed from whichever file the COMP actually imports (verify the comp's
# `import TIMING from './...'` line if a body window ever looks misaligned,
# and fix the table above — that check is part of the mark's first QC pass).


def die(msg: str) -> None:
    sys.exit(f"[showcase] {msg}")


def load_timing(name: str) -> list[dict]:
    p = REMOTION / "src" / name
    if not p.exists():
        die(f"timing json missing: {p}")
    return json.loads(p.read_text())


def offsets(timing: list[dict]) -> dict[str, tuple[int, int]]:
    """beat id -> (startFrame, endFrame)."""
    out, acc = {}, 0
    for t in timing:
        out[t["id"]] = (acc, acc + t["frames"])
        acc += t["frames"]
    return out


def mp3_seconds(p: Path) -> float:
    try:
        from mutagen.mp3 import MP3  # type: ignore
        return float(MP3(str(p)).info.length)
    except Exception:
        r = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(p)],
            capture_output=True, text=True)
        return float(r.stdout.strip())


def bookend_frames(cut_dir: Path, beat_id: str) -> int:
    mp3 = cut_dir / "mp3" / f"beat-{beat_id}.mp3"
    if not mp3.exists():
        die(f"missing audio {mp3} — run generate_audio_kokoro.py {cut_dir} first")
    return math.ceil(mp3_seconds(mp3) * FPS) + PAD_F


def cfg_for(mark: str) -> dict:
    p = SERIES / mark / "episodes.json"
    if not p.exists():
        die(f"no config at {p} — author it (see musinique-logo-2 exemplar)")
    return json.loads(p.read_text())


def ask_props(block: dict, handle: str) -> dict:
    return {
        "greeting": block.get("greeting", ""),
        "command": block.get("prompt", block.get("command", "")),
        "topic": block.get("topic", ""),
        "segment": block.get("segment", ""),
        "runningText": block.get("runningText", ""),
        "output": block.get("output", []),
        "folderLabel": handle,
    }


def cuts_of(mark: str, cfg: dict) -> list[tuple[str, dict, str]]:
    """(cut folder name, cut config, kind) — kind: full | ep916 | ep169.

    Every episode builds in BOTH aspects: ep<N> is the 9:16 one-minute Short
    (no recap — Shorts stay tight); ep<N>-16x9 is the browsable 16:9 series
    cut WITH the recap (verdict card), so viewers jump straight to the group
    they care about. The single long 16:9 cut is opt-in via build_full_16x9.
    """
    cuts: list[tuple[str, dict, str]] = []
    if cfg.get("build_full_16x9"):
        cuts.append(("full-16x9", cfg["ending_16x9"], "full"))
    for ep in cfg["episodes"]:
        cuts.append((f"ep{ep['n']:02d}", ep, "ep916"))
        cuts.append((f"ep{ep['n']:02d}-16x9", ep, "ep169"))
    return cuts


def scaffold(mark: str) -> None:
    cfg = cfg_for(mark)
    for cut, block, kind in cuts_of(mark, cfg):
        d = SERIES / mark / cut
        d.mkdir(parents=True, exist_ok=True)
        beats = []
        if kind in ("ep916", "ep169") and block.get("intro"):
            beats.append(("E00", block["intro"]["narration"]))
        if kind == "full" and block.get("verdict"):
            beats.append(("E90", block["verdict"]["narration"]))
        if kind == "ep169" and block.get("recap"):
            beats.append(("E90", block["recap"]["narration"]))
        beats.append(("E91", block["your_turn"]["narration"]))
        beats.append(("E92", block["title_out"]["narration"]))
        sheet = {
            "metadata": {
                "slug": f"{mark}-{cut}",
                "title": cfg.get("series_title", mark),
                "engine": "kokoro",
                "voice_kokoro": "am_onyx",
                "clock": "narration",
                "purpose": "showcase-series bookend audio",
            },
            "beats": [
                {"beat_id": bid, "narration_text": txt,
                 "shot": {"type": "REMOTION", "source": "own"}}
                for bid, txt in beats
            ],
        }
        (d / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
        print(f"[showcase] scaffolded {d.relative_to(ART)} ({len(beats)} bookend beats)")
    print(f"[showcase] next: generate_audio_kokoro.py each cut folder, then `props {mark}`")


def props(mark: str) -> None:
    cfg = cfg_for(mark)
    m = MARKS[mark]
    handle = cfg.get("handle", "@NikBearBrown")
    t169 = load_timing(m["timing_16x9"])
    t916 = load_timing(m["timing_916"])
    off169, off916 = offsets(t169), offsets(t916)
    render_cmds = []

    for cut, block, kind in cuts_of(mark, cfg):
        d = SERIES / mark / cut
        common = {
            "yourTurn": {**ask_props(block["your_turn"], handle),
                         "durationF": bookend_frames(d, "E91")},
            "titleOut": {"title": block["title_out"]["title"],
                         "handle": handle,
                         "subline": block["title_out"].get("subline", ""),
                         "durationF": bookend_frames(d, "E92")},
        }
        if kind == "full":
            comp_id = "ShowcaseWrap16x9"
            # body = everything up to the comp's OLD handoff (last two entries)
            p: dict = {
                "mark": mark,
                "bodyStartFrame": 0,
                "bodyEndFrame": off169[t169[-2]["id"]][0],
                "intro": None,
                "verdict": {**{k: block["verdict"][k] for k in
                              ("artifactTitle", "artifactHeading", "artifactLines")},
                            "durationF": bookend_frames(d, "E90")},
                **common,
            }
        else:
            comp_id = "ShowcaseWrap916" if kind == "ep916" else "ShowcaseWrap16x9"
            off = off916 if kind == "ep916" else off169
            first, last = block["techniques"]
            recap = block.get("recap") if kind == "ep169" else None
            p = {
                "mark": mark,
                "bodyStartFrame": 0 if block.get("include_comp_intro") else off[first][0],
                "bodyEndFrame": off[last][1],
                "intro": ({**ask_props(block["intro"], handle),
                           "durationF": bookend_frames(d, "E00")}
                          if block.get("intro") else None),
                "verdict": ({**{k: recap[k] for k in
                               ("artifactTitle", "artifactHeading", "artifactLines")},
                             "durationF": bookend_frames(d, "E90")}
                            if recap else None),
                **common,
            }
        (d / "props.json").write_text(json.dumps(p, indent=1, ensure_ascii=False))
        out = d / "video-silent.mp4"
        render_cmds.append(
            f"(cd {REMOTION} && npx remotion render src/index.ts {comp_id} "
            f"{out} --props={d / 'props.json'} --concurrency=1 --scale=2 --crf=16 --image-format=png)"
        )
        total = (
            (p["intro"]["durationF"] if p["intro"] else 0)
            + (p["bodyEndFrame"] - p["bodyStartFrame"])
            + (p["verdict"]["durationF"] if p["verdict"] else 0)
            + p["yourTurn"]["durationF"] + p["titleOut"]["durationF"]
        )
        print(f"[showcase] {cut}: {total} frames = {total / FPS:.1f}s -> props.json")

    print("\n[showcase] render each cut FOREGROUND, one at a time:")
    for c in render_cmds:
        print("  " + c)
    print(f"[showcase] then: `mux {mark}`")


def _piece(src: Path, frames: int, tmp: Path, idx: int) -> Path:
    """Pad/trim one mp3 to an exact frame count -> wav piece."""
    out = tmp / f"p{idx:03d}.wav"
    secs = frames / FPS
    subprocess.run(
        [FFMPEG, "-y", "-i", str(src),
         "-af", f"aresample=48000,apad=whole_dur={secs:.5f},atrim=0:{secs:.5f}",
         "-ac", "2", str(out)],
        check=True, capture_output=True)
    return out


def mux(mark: str) -> None:
    cfg = cfg_for(mark)
    m = MARKS[mark]
    t169, t916 = load_timing(m["timing_16x9"]), load_timing(m["timing_916"])
    off916 = offsets(t916)

    for cut, block, kind in cuts_of(mark, cfg):
        d = SERIES / mark / cut
        silent = d / "video-silent.mp4"
        propsf = d / "props.json"
        if not silent.exists() or not propsf.exists():
            print(f"[showcase] {cut}: skip (render or props missing)")
            continue
        p = json.loads(propsf.read_text())
        tmp = d / "_audio"
        tmp.mkdir(exist_ok=True)
        pieces: list[Path] = []
        i = 0

        def add(src: Path, frames: int) -> None:
            nonlocal i
            pieces.append(_piece(src, frames, tmp, i))
            i += 1

        if p["intro"]:
            add(d / "mp3" / "beat-E00.mp3", p["intro"]["durationF"])
        # body: source reel technique mp3s padded to the comp's own timing
        landscape = kind in ("full", "ep169")
        timing = t169 if landscape else t916
        reel = ART / "youtube" / (m["reel_16x9"] if landscape else m["reel_916"])
        acc = 0
        for t in timing:
            s, e = acc, acc + t["frames"]
            acc = e
            if e <= p["bodyStartFrame"] or s >= p["bodyEndFrame"]:
                continue
            add(reel / "mp3" / f"beat-{t['id']}.mp3", t["frames"])
        if p["verdict"]:
            add(d / "mp3" / "beat-E90.mp3", p["verdict"]["durationF"])
        add(d / "mp3" / "beat-E91.mp3", p["yourTurn"]["durationF"])
        add(d / "mp3" / "beat-E92.mp3", p["titleOut"]["durationF"])

        concat = tmp / "concat.txt"
        concat.write_text("".join(f"file '{w.name}'\n" for w in pieces))
        track = tmp / "track.wav"
        subprocess.run([FFMPEG, "-y", "-f", "concat", "-safe", "0",
                        "-i", str(concat), "-c", "copy", str(track)],
                       check=True, capture_output=True, cwd=tmp)
        final = d / f"{mark}-{cut}.mp4"
        subprocess.run([FFMPEG, "-y", "-i", str(silent), "-i", str(track),
                        "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                        "-c:a", "aac", "-b:a", "192k", "-shortest", str(final)],
                       check=True, capture_output=True)
        print(f"[showcase] {cut}: -> {final.relative_to(ART)}")
    print("[showcase] done — VISUAL QC LAW: sample frames of every cut and LOOK before calling it built")


def status(mark: str) -> None:
    cfg = cfg_for(mark)
    for cut, _, _kind in cuts_of(mark, cfg):
        d = SERIES / mark / cut
        have = {x: (d / x).exists() for x in ("beat_sheet.json", "mp3", "props.json", "video-silent.mp4")}
        final = list(d.glob(f"{mark}-{cut}.mp4"))
        print(f"  {cut:10} " + " ".join(f"{k}:{'Y' if v else '-'}" for k, v in have.items())
              + (" FINAL" if final else ""))


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] not in ("scaffold", "props", "mux", "status"):
        die("usage: showcase_episodes.py scaffold|props|mux|status <mark>")
    cmd, mark = sys.argv[1], sys.argv[2]
    if mark not in MARKS:
        die(f"unknown mark {mark} — one of {', '.join(MARKS)}")
    {"scaffold": scaffold, "props": props, "mux": mux, "status": status}[cmd](mark)


if __name__ == "__main__":
    main()
