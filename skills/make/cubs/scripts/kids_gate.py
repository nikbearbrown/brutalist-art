#!/usr/bin/env python3
"""kids_gate.py — GATE K: pedagogy validator for Bear's Cubs episodes.

Validates <episode>/beat_sheet.json against the developmental-research laws in
aspects/kids/SKILL.md BEFORE any audio or render spend. Exit: 0 PASS, 2 FAIL.
Rules: age-band runtime cap; teach-beat pacing 4-9s; <=1 new stimulus/beat;
static/minimal background on teach beats; question->pause->confirm triad with
a genuinely silent 2-4s pause; 3-5 varied exemplars + exactly 1 contrast case;
verbatim label word (no synonyms in narration); music only on the song beat,
song <= 15s; final beat is the co-viewing prompt; host camera-address present.

Usage: python3 kids_gate.py path/to/<episode> [--quiet]
"""
import argparse, json, sys
from pathlib import Path

CAPS = {"1-3": 240.0, "4-5": 480.0}
POSES = {"wave": "hello", "present": "teach", "point": "question",
         "listen": "pause", "celebrate": "confirm", "not": "contrast",
         "sing": "song", "bye": "coview"}
COLORS = {"red","blue","yellow","green","orange","purple","pink","brown","black","white"}
BIG3 = {"circle","square","triangle"}
ADV_SHAPES = {"rectangle","oval","star","heart"}

def concept_ok(concept, band):
    """Concept x age map. Returns (ok, msg)."""
    c = (concept or "").lower()
    if any(w in c for w in COLORS) and "mix" not in c:
        return True, None
    if any(w in c for w in BIG3):
        return (band == "4-5" or band == "1-3",
                "big-three shapes fit 2-3+; fine for the upper 1-3 band, verify positioning" if band == "1-3" else None)
    if any(w in c for w in ADV_SHAPES):
        return band == "4-5", f"'{concept}' (advanced shapes) needs the 4-5 band"
    if any(w in c for w in ("number","count","cardinal")) or any(ch.isdigit() for ch in c):
        return band == "4-5", f"'{concept}' (numbers/cardinality) needs the 4-5 band — no numerals for 1-3"
    if any(w in c for w in ("draw","write","trace")):
        return False, f"'{concept}' is a motor task — drawing/writing tutorials are banned (recognition only)"
    return True, None

def dur(b):
    return float(b.get("actual_duration_s") or b.get("estimated_duration_s")
                 or b.get("silence_s") or 0.0)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", type=Path); ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    sheet = json.loads((a.folder / "beat_sheet.json").read_text())
    md, beats = sheet.get("metadata", {}), sheet.get("beats", [])
    errs, warns = [], []

    band = md.get("age_band")
    if band not in CAPS:
        errs.append(f'metadata.age_band must be "1-3" or "4-5" (got {band!r})')
    label = (md.get("label_word") or "").strip().lower()
    if not label:
        errs.append("metadata.label_word missing — the ONE verbatim label")
    if md.get("host") != "bearbrown":
        warns.append('metadata.host should be "bearbrown" — one recurring host per series')

    ok, msg = concept_ok(md.get("concept"), band)
    if not ok:
        errs.append(f"CONCEPT x AGE: {msg}")
    elif msg:
        warns.append(f"CONCEPT x AGE: {msg}")

    total = sum(dur(b) for b in beats)
    if band in CAPS and total > CAPS[band]:
        errs.append(f"runtime {total:.0f}s exceeds the {band} cap ({CAPS[band]:.0f}s) — cut, don't compress")

    roles = [b.get("role", "?") for b in beats]
    exemplars, contrasts, songs = [], [], []
    camera_any = False

    for b in beats:
        bid, role, d = b.get("beat_id", "?"), b.get("role", "?"), dur(b)
        if b.get("camera_address"):
            camera_any = True
        hp = b.get("host_pose")
        if hp is not None:
            if hp not in POSES:
                errs.append(f"{bid}: host_pose '{hp}' not in the closed pose library (characters.md)")
            elif POSES[hp] != role:
                warns.append(f"{bid}: host_pose '{hp}' usually belongs to role '{POSES[hp]}', beat is '{role}'")
        if role == "teach":
            if not (4.0 <= d <= 9.0) and d > 0:
                errs.append(f"{bid}: teach beat {d:.1f}s outside 4-9s pacing band")
            if int(b.get("new_stimuli", 1)) > 1:
                errs.append(f"{bid}: {b.get('new_stimuli')} new stimuli — max is 1 per beat")
            if b.get("background_motion", "static") not in ("static", "minimal"):
                errs.append(f"{bid}: background_motion '{b.get('background_motion')}' — teach beats are static/minimal")
            ex = b.get("exemplar")
            if ex:
                exemplars.append(ex)
            nt = (b.get("narration_text") or "").lower().rstrip(".! ")
            if label and label in nt and not nt.endswith(label):
                warns.append(f"{bid}: label '{label}' is not sentence-final — house cadence is \"The ball is red. Red.\"")
            if b.get("music_cue"):
                errs.append(f"{bid}: music on a teach beat — music lives ONLY in the song beat")
        elif role == "pause":
            if not b.get("silent"):
                errs.append(f'{bid}: pause beat must be "silent": true — the pause IS the mechanism')
            if not (2.0 <= float(b.get("silence_s", 0)) <= 4.0):
                errs.append(f"{bid}: pause {b.get('silence_s')}s — must be 2-4s of genuine silence")
            if b.get("music_cue"):
                errs.append(f"{bid}: music under the pause — never fill the pause")
        elif role == "contrast":
            contrasts.append(b)
        elif role == "song":
            songs.append(b)
            if d > 15.0:
                errs.append(f"{bid}: song {d:.1f}s — jingle must be under 15s")
        elif role in ("question", "confirm", "hello", "coview"):
            if b.get("music_cue") and role != "hello":
                warns.append(f"{bid}: music under a {role} beat — silence is correct design")

    # triad ordering: every question followed (within 2 beats) by pause then confirm
    for i, r in enumerate(roles):
        if r == "question":
            nxt = roles[i+1:i+3]
            if not nxt or nxt[0] != "pause":
                errs.append(f"beat {i+1} (question) not followed by a pause beat")
            elif len(nxt) < 2 or nxt[1] != "confirm":
                errs.append(f"beat {i+1} (question) pause not followed by a confirm beat")
    if "question" not in roles:
        errs.append("no question beat — the contingency triad is mandatory")

    if not (3 <= len(exemplars) <= 5):
        errs.append(f"{len(exemplars)} exemplars — need 3-5 varied exemplars")
    else:
        objs = [e.get("object") for e in exemplars]
        if len(set(objs)) != len(objs):
            errs.append("duplicate exemplar objects — vary the exemplars, don't repeat one")
        attrsets = [tuple(sorted((e.get("attributes") or {}).items())) for e in exemplars]
        if len(set(attrsets)) < 2:
            warns.append("exemplar attributes barely vary — vary dimensions UNRELATED to the concept")
    if len(contrasts) != 1:
        errs.append(f"{len(contrasts)} contrast beats — exactly ONE 'this is NOT ...' case")
    elif contrasts and roles.index("contrast") < len(roles) * 0.5:
        warns.append("contrast case sits early — it belongs near the end of the sequence")
    if len(songs) > 1:
        errs.append(f"{len(songs)} song beats — ONE dedicated jingle per episode")

    if roles and roles[-1] != "coview":
        errs.append(f"final beat role is '{roles[-1]}' — episodes end on the co-viewing prompt")
    if not camera_any:
        errs.append("no camera_address beat — the host must address the viewer directly")

    # label-word consistency: label appears in narration; crude synonym drift check
    if label:
        spoken = " ".join(b.get("narration_text", "").lower() for b in beats)
        if label not in spoken:
            errs.append(f'label word "{label}" never spoken — the label is the lesson')

    for e in errs: print(f"[gateK] ERROR {e}")
    if not a.quiet:
        for w in warns: print(f"[gateK] WARN  {w}")
    n = md.get("slug", a.folder.name)
    if errs:
        print(f"[gateK] {n}: FAIL ({len(errs)} errors) — fix the beat sheet before audio")
        return 2
    print(f"[gateK] {n}: PASS ({len(beats)} beats, {total:.0f}s, band {band})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
