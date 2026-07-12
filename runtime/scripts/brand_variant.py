#!/usr/bin/env python3
"""brand_variant.py — scaffold an audience variant beat sheet from the canonical one.

Every reel starts with beat_sheet.json (the NikBearBrown / default cut). An audience
variant is beat_sheet.<suffix>.json — the SAME reel rewritten in another voice: new
register (narration), new narration voice, new palette, a different outro. The canonical
beat_sheet.json is NEVER modified.

This script does the DETERMINISTIC half — it creates beat_sheet.<suffix>.json as a copy
of beat_sheet.json with the audience metadata set (voice_id read from the .env, palette,
register, audience). The creative half — rewriting each beat's narration into the
register, the signature tangent, the audience outro — is done by Claude Code, guided by
the hai / medhavy SKILL. No API calls, no spend.

Usage:
  python3 scripts/brand_variant.py <REEL> {neu|hai|medhavy}
"""
import argparse, json, os, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]          # runtime/

AUD = {
    "neu": {"suffix": "neu", "audience": "NEU", "voice_env": "ELEVENLABS_VOICE_NEU",
            "voice_fallback_env": "ELEVENLABS_VOICE_NIKBEARBROWN",
            "palette": "neu", "register": "Lecture", "charter": "NEU.md",
            "author_section": "Northeastern"},
    "hai": {"suffix": "hai", "audience": "HAI", "voice_env": "ELEVENLABS_VOICE_HUMANITARIANS",
            "palette": "humanitarians", "register": "Pragmatist", "charter": "HAI.md",
            "author_section": "Humanitarians AI"},
    "medhavy": {"suffix": "medhavy", "audience": "MEDHAVY", "voice_env": "ELEVENLABS_VOICE_MEDHAVY",
                "palette": "medhavy", "register": "Wonder", "charter": "MEDHAVY.md",
                "author_section": "Medhavy.com"},
    "nbb": {"suffix": "nbb", "audience": "NikBearBrown", "voice_env": "ELEVENLABS_VOICE_NIKBEARBROWN",
            "palette": "teardown", "register": "Teardown", "charter": "NIKBEARBROWN.md",
            "author_section": "NikBearBrown"},
}


def read_env_voice(var):
    env = HERE / ".env"
    if not env.exists():
        return None
    for line in env.read_text().splitlines():
        m = re.match(rf"\s*{re.escape(var)}\s*=\s*(.+)\s*$", line)
        if m:
            return m.group(1).strip().strip("'\"")
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("reel", type=Path)
    ap.add_argument("audience", choices=list(AUD))
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    cfg = AUD[a.audience]
    reel = a.reel.resolve()

    src = reel / "beat_sheet.json"
    if not src.exists():
        sys.exit(f"[variant] no beat_sheet.json in {reel}")
    out = reel / f"beat_sheet.{cfg['suffix']}.json"
    if out.exists() and not a.force:
        sys.exit(f"[variant] {out.name} already exists (use --force to reset it from canonical)")

    sheet = json.loads(src.read_text())
    meta = sheet.setdefault("metadata", {})
    voice_id = read_env_voice(cfg["voice_env"])
    voice_note = "set"
    if not voice_id and cfg.get("voice_fallback_env"):
        # NEU: no per-prof voice set -> fall back to Bear's default voice (AUDIENCES.md).
        voice_id = read_env_voice(cfg["voice_fallback_env"])
        if voice_id:
            voice_note = f"fallback→{cfg['voice_fallback_env']}"
    if not voice_id:
        voice_note = "MISSING (.env)"

    # audience metadata
    meta["audience"] = cfg["audience"]
    meta["derived_from"] = "beat_sheet.json"
    meta["register"] = cfg["register"]
    meta["palette"] = cfg["palette"]
    meta["outro_source"] = f"AUTHOR.MD :: {cfg['author_section']}"
    if voice_id:
        meta["voice_id"] = voice_id
    # a checklist Claude Code works down (the creative half):
    meta["_variant_todo"] = [
        f"rewrite every beat narration_text in the {cfg['register']} register "
        f"(voices/{cfg['register'].lower()}/VOICE.md + {cfg['charter']}) — voice only, facts unchanged",
        "signature tangent 0-1 per video, ONLY on a clear opportunity (see SKILL)",
        f"swap the outro to the {cfg['audience']} outro from {meta['outro_source']}",
        "then build audience-namespaced (audio in the new voice, scenes in the new palette)",
    ]
    # durations will change with the rewrite; drop stale render stamps so they recompute
    for b in sheet.get("beats", []):
        b.pop("actual_duration_s", None)
        b.get("shot", {}).pop("rendered", None) if isinstance(b.get("shot"), dict) else None

    out.write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
    print(f"[variant] wrote {out.name}  audience={cfg['audience']}  register={cfg['register']}  "
          f"palette={cfg['palette']}  voice_id={voice_note}")
    print(f"[variant] {len(sheet.get('beats', []))} beats to rewrite in {cfg['register']} — "
          f"next: Claude Code follows the {a.audience} SKILL to rewrite narration + outro + tangent")


if __name__ == "__main__":
    main()
