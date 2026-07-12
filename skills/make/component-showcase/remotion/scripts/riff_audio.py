#!/usr/bin/env python3
"""riff_audio.py — audio-first TTS for a riff beat sheet (the NikBearBrown voice).

Reads a riff beat sheet (segments[].beats[] with `text`), generates ONE ElevenLabs MP3
per spoken beat, measures the real duration with mutagen, and writes:

  public/audio/<segment>-<i>.mp3
  public/audio/timings.json         {"intro-0": 2.9, "bar-chart-1": 1.4, ...}

It also writes `actual_duration_s` + `audio_file` back into each beat in the beat sheet, so
the sheet is the single source of truth. That measured duration is GROUND TRUTH for the
conform pass — never estimate timing from word count.

Reuses vox's ElevenLabs call verbatim (model eleven_multilingual_v2, mp3_44100_128).
Voice + key are read from the environment, then --env, then ../../vox/.env by default.

Requires:  pip install mutagen   ·   ffmpeg on PATH (for `event` silences)
Usage:
    python3 scripts/riff_audio.py beats/onda-data-tour.beats.json
    python3 scripts/riff_audio.py beats/onda-data-tour.beats.json --dry-run     # plan, no calls
    python3 scripts/riff_audio.py beats/onda-data-tour.beats.json --only bar-chart-1
"""
import argparse, json, os, re, subprocess, sys, urllib.request, urllib.error
from pathlib import Path

API_URL = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
HERE = Path(__file__).resolve().parents[1]  # brutalist/remotion/

SYMBOLS = {"—": ", ", "–": ", ", "…": "...", "%": " percent", "·": ", "}


def normalize(t: str) -> str:
    for s, spoken in SYMBOLS.items():
        t = t.replace(s, spoken)
    return re.sub(r"\s+", " ", t).strip()


def measure(path: Path) -> float:
    from mutagen.mp3 import MP3
    return round(MP3(str(path)).info.length, 2)


def load_env(explicit: str | None) -> dict:
    """Parse a .env for keys. Order: current env wins; then explicit; then ../../vox/.env."""
    vals = {}
    candidates = [Path(explicit)] if explicit else [HERE / ".env", HERE.parents[1] / "vox" / ".env"]
    for env in candidates:
        if env and env.exists():
            for line in env.read_text().splitlines():
                m = re.match(r"\s*([A-Z_]+)\s*=\s*(.+)\s*$", line)
                if m and m.group(1) not in vals:
                    vals[m.group(1)] = m.group(2).strip().strip("'\"")
    return vals


def generate_one(text, voice_id, api_key, out_path):
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "output_format": "mp3_44100_128",
        "voice_settings": {"stability": 0.80, "similarity_boost": 0.75, "style": 0.0, "use_speaker_boost": False, "speed": 0.85},
    }
    req = urllib.request.Request(
        API_URL.format(voice_id=voice_id),
        data=json.dumps(payload).encode("utf-8"),
        headers={"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": api_key},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            out_path.write_bytes(resp.read())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"[err] ElevenLabs HTTP {e.code}: {e.read().decode('utf-8', 'ignore')[:400]}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("beatsheet", type=Path)
    ap.add_argument("--api-key", default=os.getenv("ELEVENLABS_API_KEY"))
    ap.add_argument("--voice", default=os.getenv("ELEVENLABS_VOICE_NIKBEARBROWN"))
    ap.add_argument("--env", default=None)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", nargs="*", default=None)
    a = ap.parse_args()

    env = load_env(a.env)
    api_key = a.api_key or env.get("ELEVENLABS_API_KEY")
    voice = a.voice or env.get("ELEVENLABS_VOICE_NIKBEARBROWN")
    if not a.dry_run and not api_key:
        print("[err] no ELEVENLABS_API_KEY (env, --api-key, or ../../vox/.env)", file=sys.stderr); return 1
    if not a.dry_run and not voice:
        print("[err] no NBB voice id (ELEVENLABS_VOICE_NIKBEARBROWN)", file=sys.stderr); return 1

    sheet = json.loads(a.beatsheet.read_text())
    fps = sheet.get("fps", 30)
    audio_dir = HERE / "public" / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    timings, total = {}, 0.0

    for seg in sheet["segments"]:
        for i, beat in enumerate(seg["beats"]):
            text = (beat.get("text") or "").strip()
            key = f"{seg['id']}-{i}"
            if not text:
                # `event` beats: a real silence so the visual settle has room (ground truth too).
                secs = round((beat.get("hold", 15)) / fps, 2)
                out = audio_dir / f"{key}.mp3"
                if not a.dry_run:
                    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
                                    "-t", f"{secs:.3f}", "-q:a", "9", "-acodec", "libmp3lame", str(out)],
                                   check=True, capture_output=True)
                beat["actual_duration_s"] = secs; beat["audio_file"] = f"audio/{key}.mp3"
                timings[key] = secs; total += secs
                continue
            if a.only and key not in a.only:
                continue
            out = audio_dir / f"{key}.mp3"
            # voice reads `tts` if present (e.g. spoken URLs), else the display `text`
            spoken = normalize(beat.get("tts") or text)
            print(f"[{key}] {'(dry) ' if a.dry_run else ''}{spoken[:70]}")
            if not a.dry_run:
                generate_one(spoken, voice, api_key, out)
                dur = measure(out)
                beat["actual_duration_s"] = dur; beat["audio_file"] = f"audio/{key}.mp3"
                timings[key] = dur; total += dur

    if not a.dry_run:
        (audio_dir / "timings.json").write_text(json.dumps(timings, indent=1))
        a.beatsheet.write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
        print(f"\n[ok] {len(timings)} clips · {total:.1f}s spoken · durations written back to {a.beatsheet.name}")
        print("[next] conform the timing to these durations, then render the sound slate.")
    else:
        print(f"\n[dry] {sum(1 for s in sheet['segments'] for b in s['beats'] if (b.get('text') or '').strip())} beats would be voiced.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
