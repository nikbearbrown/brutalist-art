#!/usr/bin/env python3
"""song_prompts.py — song mode scaffold: lyrics + character tokens -> beat sheet + PROMPTS.md.

Inputs (in the episode folder):
  lyrics.txt        TITLE:/ARTIST: header lines, then one lyric line per line
  characters.json   token registry: {"STAR": {"descriptor": "...", "ref": "https://raw.githubusercontent.com/...",
                    "oref_weight": 300, "anchors": "..."}, ...}
  style.json        {"suffix": "...", "ar": "16:9", "profile": "...", "version": "7"}

Pass 1 (no scenes yet): segments the lyric into beats (~<=16 words each),
writes beat_sheet.json skeleton (V01..Vnn, lyric_text per beat, shot STILL/ai)
and PROMPTS.md with <SCENE — write me> placeholders.
Pass 2 (after the builder authors beat["scene"] in beat_sheet.json): rerun —
PROMPTS.md regenerates with real scenes. Idempotent; never overwrites scenes.

Prompt shape (one fenced block per beat, beat id FIRST per the prompt law):
  <ref-urls> B##, <scene>, <style suffix> --ar 16:9 --oref <url> --ow N --profile X --v 7
Character tokens in scenes ([STAR]) expand to the registry descriptor.
"""
import json, re, sys
from pathlib import Path

MAX_WORDS = 16

def main():
    folder = Path(sys.argv[1]).resolve()
    lyr = (folder / "lyrics.txt").read_text(encoding="utf-8").strip().split("\n")
    chars = json.loads((folder / "characters.json").read_text())
    style = json.loads((folder / "style.json").read_text()) if (folder / "style.json").exists() else {}
    title = artist = ""
    lines = []
    for ln in lyr:
        s = ln.strip()
        if s.upper().startswith("TITLE:"): title = s[6:].strip()
        elif s.upper().startswith("ARTIST:"): artist = s[7:].strip()
        elif s: lines.append(s)

    # segment: greedy chunks <= MAX_WORDS, at least 1 line
    beats, cur, wc = [], [], 0
    for ln in lines:
        w = len(ln.split())
        if cur and wc + w > MAX_WORDS:
            beats.append(cur); cur, wc = [], 0
        cur.append(ln); wc += w
    if cur: beats.append(cur)

    sheet_path = folder / "beat_sheet.json"
    old = json.loads(sheet_path.read_text()) if sheet_path.exists() else None
    old_scenes = {b["beat_id"]: b.get("scene") for b in (old or {}).get("beats", [])} if old else {}

    bs = []
    for i, chunk in enumerate(beats, 1):
        bid = f"V{i:02d}"
        bs.append({
            "beat_id": bid,
            "lyric_text": " / ".join(chunk),
            "scene": old_scenes.get(bid),          # authored by the builder; preserved on rerun
            "shot": {"type": "STILL", "source": "ai", "motion": "mjvideo"},
        })
    sheet = {"metadata": {"slug": folder.name, "title": title, "artist": artist,
                          "mode": "song", "style": style, "characters": sorted(chars)},
             "beats": bs}
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False))

    # PROMPTS.md — per beat, include ONLY the refs for tokens the scene uses
    suffix = style.get("suffix", "")

    def build(scene, bid):
        used = [(t, c) for t, c in chars.items() if f"[{t}]" in scene]
        for t, c in used:
            scene = scene.replace(f"[{t}]", c["descriptor"])
        refs = " ".join(c["ref"] for _, c in used)
        tail = f'--ar {style.get("ar","16:9")}'
        for _, c in used:
            tail += f' --oref {c["ref"]} --ow {c.get("oref_weight",300)}'
        if style.get("profile"): tail += f' --profile {style["profile"]}'
        tail += f' --v {style.get("version","7")}'
        head = (refs + " ") if refs else ""
        return f"{head}{bid}, {scene}, {suffix} {tail}"

    out = [f"# PROMPTS — {folder.name}",
           f"{title} · {artist}" if title else "",
           "",
           "One block per beat — paste into Midjourney as-is. Generate a grid,",
           "REJECT anything failing the identity anchors (characters.json), pick",
           "the best, animate the keeper (image-to-video), download, rename",
           "`V##-<anything>.mp4`, drop in pantry/. Audio is stripped at intake —",
           "the song is the only track.", ""]
    todo = 0
    for b in sheet["beats"]:
        out.append(f"## {b['beat_id']} — {b['lyric_text'][:70]}")
        scene = b.get("scene")
        if scene:
            out.append("```")
            out.append(build(scene, b["beat_id"]))
            out.append("```")
        else:
            todo += 1
            out.append("```")
            out.append(f"<SCENE — write me, then rerun song_prompts.py>")
            out.append("```")
        out.append("")
    (folder / "PROMPTS.md").write_text("\n".join(out))
    print(f"[song] {len(bs)} beats | {len(bs)-todo} scenes authored, {todo} to write | {folder/'PROMPTS.md'}")

if __name__ == "__main__":
    main()
