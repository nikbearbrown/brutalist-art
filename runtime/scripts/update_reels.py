#!/usr/bin/env python3
"""update_reels.py — bring built reels up to the latest specs (outro migration).

The outro spec changed: green-screen mascot outros (outro.py rebrands the last
CARD beat) are being replaced by Remotion outros (OutroSeries from the book's ABOUT.MD,
OutroCTA from AUTHOR.MD). This reconciles an existing reel to that spec:

  1. detect drift  — old mascot outro present? padded (out-of-sync) audio? orphan mp3s?
  2. STRIP         — delete the mascot media/<bid>.mp4 (+ its compiled clip), restore
                     the pristine un-padded narration from clips/_work/outro-orig-*, reset
                     the beat's actual_duration_s. NO credits, no network — the pristine
                     narration already exists.
  3. delete orphan mp3s (audio for beats no longer in the sheet)
  4. OUTRO         — append OutroSeries + OutroCTA beats, generate audio only for those
                     (generate_audio.py --only), render via remotion_scenes.py, recompile
                     via run.sh. Only runs when --outro flag is passed.

DRY-RUN BY DEFAULT: prints the plan, changes nothing. Pass --apply to strip.
Pass --outro --apply to also append + render the new outros.
--apply deletes files, so it runs on the Mac (via Claude Code), not the Cowork sandbox.

Usage:
  python3 scripts/update_reels.py <REEL>                    # dry-run one reel
  python3 scripts/update_reels.py --all                     # dry-run every reel, write UPDATE.md at the repo root
  python3 scripts/update_reels.py <REEL> --apply             # strip this reel to spec
  python3 scripts/update_reels.py --all --apply              # strip every drifted reel
  python3 scripts/update_reels.py <REEL> --outro --apply     # strip + append + render + recut
  python3 scripts/update_reels.py --all --outro --apply      # full fleet migration
"""
import argparse, json, os, re, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]        # runtime/
FFPROBE = shutil.which("ffprobe")

# Prefer the nvm node that ships with the remotion project's node_modules
_NVM_NODE = Path.home() / ".nvm" / "versions" / "node"
def _node_env():
    """Return env dict with a working Node in PATH (nvm > system)."""
    env = dict(os.environ)
    if _NVM_NODE.is_dir():
        candidates = sorted(_NVM_NODE.iterdir(), reverse=True)
        for c in candidates:
            nb = c / "bin"
            if (nb / "node").exists():
                env["PATH"] = str(nb) + os.pathsep + env.get("PATH", "")
                break
    return env


# ---------------------------------------------------------------------------
# drift detection
# ---------------------------------------------------------------------------

def probe_dur(path):
    if not FFPROBE:
        return None
    r = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    try:
        return round(float(r.stdout.strip()), 3)
    except Exception:
        return None


def analyze(reel: Path):
    """Return a drift record for one reel (no side effects)."""
    try:
        sheet = json.loads((reel / "beat_sheet.json").read_text())
    except Exception:
        return None
    beats = sheet.get("beats", [])
    ids = [b.get("beat_id") for b in beats]
    last = beats[-1] if beats else None
    book = reel.parents[1]
    d = {"reel": reel, "sheet": sheet, "beats": beats, "ids": ids,
         "mascot": None, "orphans": [], "missing": [], "book": book}

    # old mascot outro = last CARD beat with a media mp4 AND a pristine backup
    if last and last.get("shot", {}).get("type") == "CARD":
        lid = last["beat_id"]
        mascot_mp4 = reel / "media" / f"{lid}.mp4"
        pristine = reel / "clips" / "_work" / f"outro-orig-{lid}.mp3"
        if mascot_mp4.exists() and pristine.exists():
            d["mascot"] = {"bid": lid, "mp4": mascot_mp4, "pristine": pristine,
                           "clip": reel / "clips" / f"{lid}.mp4",
                           "padded_mp3": reel / (last.get("audio_file") or f"mp3/beat-{lid}.mp3"),
                           "workfiles": list((reel / "clips" / "_work").glob("outro-*"))}

    # orphan mp3s (audio for a beat id not in the sheet)
    mp3dir = reel / "mp3"
    if mp3dir.is_dir():
        for m in mp3dir.glob("beat-*.mp3"):
            bid = m.stem.replace("beat-", "")
            if bid not in ids:
                d["orphans"].append(m)
    # missing audio (non-silent beat with no mp3)
    for b in beats:
        bid = b.get("beat_id")
        if not b.get("silent") and not (mp3dir / f"beat-{bid}.mp3").exists():
            d["missing"].append(bid)

    has_about = (book / "ABOUT.MD").exists()
    has_author = (book / "AUTHOR.MD").exists()
    d["about"], d["author"] = has_about, has_author
    d["drift"] = bool(d["mascot"] or d["orphans"] or d["missing"])

    # outro-present: check if OutroSeries/OutroCTA beats already appended
    d["outro_done"] = any(
        b.get("shot", {}).get("remotion", {}).get("pattern") in ("OutroSeries", "OutroCTA")
        for b in beats
    )
    return d


# ---------------------------------------------------------------------------
# strip phase
# ---------------------------------------------------------------------------

def strip(d, timings_note):
    """Destructively strip the mascot outro + orphans; restore pristine narration."""
    reel, sheet, beats = d["reel"], d["sheet"], d["beats"]
    actions = []
    m = d["mascot"]
    if m:
        lid = m["bid"]
        for p in (m["mp4"], m["clip"]):
            if p.exists():
                p.unlink(); actions.append(f"deleted {p.relative_to(reel)}")
        shutil.copy(m["pristine"], m["padded_mp3"])
        dur = probe_dur(m["padded_mp3"])
        for b in beats:
            if b["beat_id"] == lid and dur:
                b["actual_duration_s"] = dur
        actions.append(f"restored pristine narration {m['padded_mp3'].relative_to(reel)} ({dur}s)")
        for wf in m["workfiles"]:
            if wf.exists():
                wf.unlink()
        actions.append(f"cleaned {len(m['workfiles'])} outro work file(s)")
        man = reel / "clips" / "manifest.json"
        if man.exists():
            try:
                mj = json.loads(man.read_text()); mj.pop(lid, None)
                man.write_text(json.dumps(mj, indent=1))
            except Exception:
                pass
    for o in d["orphans"]:
        o.unlink(); actions.append(f"deleted orphan {o.relative_to(reel)}")
    (reel / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
    return actions


# ---------------------------------------------------------------------------
# outro append + render phase
# ---------------------------------------------------------------------------

def _parse_about(about_path: Path) -> dict:
    """Extract seriesTitle, tagline, githubSlug from ABOUT.MD."""
    text = about_path.read_text()
    # "# About The Reallocation Engine" → title
    m = re.search(r'^#\s+About\s+(.+)', text, re.MULTILINE)
    series_title = m.group(1).strip() if m else about_path.parents[0].name
    # GitHub slug from "[slug](https://github.com/...)" link
    m = re.search(r'\[([a-z0-9][a-z0-9-]*)\]\(https://github\.com/', text)
    github_slug = m.group(1) if m else ""
    return {"seriesTitle": series_title, "tagline": "", "githubSlug": github_slug}


def _parse_author(author_path: Path) -> dict:
    """Extract authorName and handle from AUTHOR.MD."""
    text = author_path.read_text()
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    author_name = "Nik Bear Brown"
    for i, line in enumerate(lines):
        if line.lower().startswith("# author") and i + 1 < len(lines):
            author_name = lines[i + 1]
            break
    m = re.search(r'youtube.*?@([A-Za-z0-9_]+)', text, re.IGNORECASE)
    handle = f"@{m.group(1)}" if m else "@NikBearBrown"
    return {"authorName": author_name, "handle": handle,
            "ctaText": "Like and subscribe for more."}


def _next_bids(beats: list) -> tuple:
    """Return the next two beat IDs after the current last beat."""
    if not beats:
        return "B01", "B02"
    nums = [int(re.search(r'\d+', b["beat_id"]).group()) for b in beats
            if re.search(r'\d+', b.get("beat_id", ""))]
    last_n = max(nums) if nums else 0
    return f"B{last_n+1:02d}", f"B{last_n+2:02d}"


def append_outro_beats(d: dict) -> tuple:
    """Append OutroSeries + OutroCTA beats to the beat sheet. Returns (bids, err)."""
    reel, sheet, beats, book = d["reel"], d["sheet"], d["beats"], d["book"]
    if d["outro_done"]:
        return None, "outro beats already present"

    about_props = (_parse_about(book / "ABOUT.MD") if (book / "ABOUT.MD").exists()
                   else {"seriesTitle": book.name, "tagline": "", "githubSlug": ""})
    author_props = (_parse_author(book / "AUTHOR.MD") if (book / "AUTHOR.MD").exists()
                    else {"authorName": "Nik Bear Brown", "handle": "@NikBearBrown",
                          "ctaText": "Like and subscribe for more."})

    bid_s, bid_c = _next_bids(beats)

    beats.append({
        "beat_id": bid_s,
        "act": "OUTRO",
        "type": "GRAPHIC",
        "name": "OutroSeries",
        "narration_text": f"Part of the {about_props['seriesTitle']} series.",
        "shot": {
            "type": "GRAPHIC", "source": "remotion", "motion": "fade",
            "scene_type": "outro-series",
            "remotion": {
                "pattern": "OutroSeries",
                "provenance": "proven-core/OutroSeries",
                "version": "1",
                "props": about_props,
            },
        },
        "estimated_duration_s": 6,
        "audio_file": f"mp3/beat-{bid_s}.mp3",
    })
    beats.append({
        "beat_id": bid_c,
        "act": "OUTRO",
        "type": "GRAPHIC",
        "name": "OutroCTA",
        "narration_text": author_props["ctaText"],
        "shot": {
            "type": "GRAPHIC", "source": "remotion", "motion": "fade",
            "scene_type": "outro-cta",
            "remotion": {
                "pattern": "OutroCTA",
                "provenance": "proven-core/OutroCTA",
                "version": "1",
                "props": author_props,
            },
        },
        "estimated_duration_s": 5,
        "audio_file": f"mp3/beat-{bid_c}.mp3",
    })
    (reel / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
    return [bid_s, bid_c], None


def apply_outro(d: dict) -> list:
    """Full outro pipeline: append beats, generate audio, remotion render, recut."""
    reel = d["reel"]
    acts = []

    new_bids, err = append_outro_beats(d)
    if err:
        acts.append(err)
        return acts
    acts.append(f"appended {new_bids[0]} OutroSeries + {new_bids[1]} OutroCTA")

    # Generate audio for only the two new beats
    env = _node_env()
    api_key = os.environ.get("ELEVENLABS_API_KEY", "")
    r = subprocess.run(
        [sys.executable, str(HERE / "scripts" / "generate_audio.py"),
         str(reel), "--only"] + new_bids,
        env={**env, "ELEVENLABS_API_KEY": api_key},
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        acts.append(f"AUDIO FAIL: {(r.stderr or r.stdout)[-300:]}")
        return acts
    acts.append(f"audio generated for {new_bids}")

    # Render the two Remotion beats → media/<bid>.mp4
    r = subprocess.run(
        [sys.executable, str(HERE / "scripts" / "remotion_scenes.py"), str(reel)],
        env=env, capture_output=True, text=True,
    )
    if r.returncode != 0:
        acts.append(f"REMOTION FAIL: {(r.stderr or r.stdout)[-300:]}")
        return acts
    acts.append("remotion render: ok")

    # Recompile the reel (manim renders cached; just re-slots + ffmpeg concat)
    r = subprocess.run(
        ["bash", str(HERE / "scripts" / "run.sh"), str(reel)],
        env=env, capture_output=True, text=True,
    )
    if r.returncode != 0:
        acts.append(f"ART_RUN FAIL: {(r.stderr or r.stdout)[-300:]}")
        return acts
    review = reel / f"{reel.name}-slate.mp4"
    sz = f"{review.stat().st_size // 1024}K" if review.exists() else "missing"
    acts.append(f"recut: {review.name} ({sz})")
    return acts


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("reel", nargs="?", type=Path)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--outro", action="store_true",
                    help="Also append OutroSeries+OutroCTA beats, generate audio, render, recut")
    ap.add_argument("--books", type=Path, default=HERE.parent)
    ap.add_argument("--out", type=Path, default=HERE / "UPDATE.md")
    a = ap.parse_args()

    reels = []
    if a.reel:
        reels = [a.reel.resolve()]
    elif a.all:
        for book in sorted(p for p in a.books.resolve().iterdir() if p.is_dir()):
            yt = book / "youtube"
            if yt.is_dir():
                reels += sorted(r for r in yt.iterdir()
                                if r.is_dir() and (r / "beat_sheet.json").exists())
    else:
        sys.exit("give a <REEL> or --all")

    recs = [r for r in (analyze(x) for x in reels) if r]
    drifted = [r for r in recs if r["drift"]]
    mascots = [r for r in drifted if r["mascot"]]
    outro_pending = [r for r in recs if not r["outro_done"]] if a.outro else []

    mode = "APPLY" if a.apply else "DRY-RUN"
    outro_tag = " + OUTRO" if a.outro else ""
    print(f"[update] {mode}{outro_tag}: {len(recs)} reels scanned, "
          f"{len(drifted)} drifted ({len(mascots)} old mascot outros)"
          + (f", {len(outro_pending)} need outro append" if a.outro else ""))

    L = ["# UPDATE.md — spec drift across built reels", "",
         f"_Mode: {mode}{outro_tag}. {len(recs)} reels, {len(drifted)} drifted, "
         f"{len(mascots)} carry the old mascot outro._", ""]

    if drifted:
        L += ["| Book | Reel | Old outro (beat) | Orphan mp3s | Missing audio | ABOUT/AUTHOR |",
              "|---|---|:-:|--:|--:|:-:|"]
        for r in drifted:
            book = r["book"].name
            mo = r["mascot"]["bid"] if r["mascot"] else "—"
            aa = ("both" if r["about"] and r["author"]
                  else "ABOUT" if r["about"] else "AUTHOR" if r["author"] else "NONE")
            L.append(f"| {book} | {r['reel'].name} | {mo} | {len(r['orphans'])} | "
                     f"{len(r['missing'])} | {aa} |")
        L.append("")

    if a.apply:
        if drifted:
            print("[update] applying strip (deletes files; restores pristine audio)...")
            for r in drifted:
                acts = strip(r, None)
                print(f"  {r['reel'].name}: " + ("; ".join(acts) if acts else "nothing to strip"))

        if a.outro:
            print(f"[update] appending outro beats for {len(outro_pending)} reels...")
            results = []
            for r in outro_pending:
                acts = apply_outro(r)
                line = f"  {r['reel'].name}: " + " | ".join(acts)
                print(line)
                results.append({"reel": r["reel"].name, "book": r["book"].name, "acts": acts})

            ok = [x for x in results if not any("FAIL" in a for a in x["acts"])]
            fail = [x for x in results if any("FAIL" in a for a in x["acts"])]
            L += [f"## Outro append ({len(outro_pending)} reels)", ""]
            if ok:
                L += [f"**{len(ok)} succeeded.**", ""]
            if fail:
                L += [f"**{len(fail)} failed:**", ""]
                for f_ in fail:
                    L.append(f"- {f_['book']}/{f_['reel']}: " +
                             " | ".join(a for a in f_["acts"] if "FAIL" in a))
                L.append("")
        else:
            L.append(f"\n_Stripped {len(drifted)} reels._")
            if not a.outro:
                L.append("_Next: run with `--outro --apply` to append + audio + render the new outros._")
    else:
        L.append("\n_Dry-run — nothing changed. Re-run with `--apply` to strip, "
                 "`--outro --apply` to also append + render the new outros._")
        if a.outro and outro_pending:
            L += ["", f"## Outro pending ({len(outro_pending)} reels)",
                  "These reels need OutroSeries + OutroCTA beats appended.", ""]
            for r in outro_pending[:20]:
                L.append(f"- {r['book'].name}/{r['reel'].name}")
            if len(outro_pending) > 20:
                L.append(f"- … and {len(outro_pending) - 20} more")

    a.out.write_text("\n".join(L))
    print(f"[update] report -> {a.out}")


if __name__ == "__main__":
    main()
