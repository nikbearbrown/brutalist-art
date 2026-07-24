#!/usr/bin/env python3
"""brand_variant.py — scaffold an audience variant beat sheet from the canonical one.

Every reel starts with beat_sheet.json (the NikBearBrown / default cut). An audience
variant is written as beat_sheet.<suffix>.json. Directory-isolated brands
(use_dir: hai, medhavy, nbb) write that file inside a new <suffix>- directory;
other brands write it as a sibling of the source beat_sheet.json.

The canonical beat_sheet.json is NEVER modified.

This script does the DETERMINISTIC half — it sets audience metadata (voice_id from the
.env, palette, register, audience). The creative half — rewriting each beat's narration
into the register, the signature tangent, the audience outro — is done by Claude Code,
guided by the hai / medhavy SKILL. No API calls, no spend.

Directory convention for use_dir brands (hai/medhavy/nbb/claude; source never modified):
  <book>/youtube/<slug>/              →  <book>/youtube/<suffix>-<slug>/
  <book>/lectures/<chapter>-lecture/  →  <book>/<suffix>-lectures/<chapter>-lecture/
Inside the <suffix>- dir: beat_sheet.<suffix>.json + copies of any lecture build scripts.

Default TTS engine per brand (written into metadata.engine + metadata.voice_kokoro):
  nbb/brutalist  → ElevenLabs (ELEVENLABS_VOICE_NIKBEARBROWN) — the only paid brand default
  hai            → kokoro / af_kore  (override: engine="elevenlabs", use metadata.voice_id)
  medhavy        → kokoro / af_kore  (override: engine="elevenlabs", use metadata.voice_id)
  musinique      → kokoro / am_puck  (override: engine="elevenlabs", use metadata.voice_id)
  neu            → kokoro / bm_fable (override: engine="elevenlabs", use metadata.voice_id)

Usage:
  python3 scripts/brand_variant.py <REEL_OR_LECTURE> {neu|hai|medhavy|nbb|musinique|claude|claude-liam|claude-hai|claude-medhavy|claude-musinique}
"""
import argparse, json, os, re, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]          # runtime/

AUD = {
    "neu": {"suffix": "neu", "audience": "NEU", "voice_env": "ELEVENLABS_VOICE_NEU",
            "voice_fallback_env": "ELEVENLABS_VOICE_NIKBEARBROWN",
            "palette": "neu", "register": "Lecture", "charter": "NEU.md",
            "author_section": "Northeastern",
            "engine": "kokoro", "voice_kokoro": "bm_fable"},
    "hai": {"suffix": "hai", "audience": "HAI", "voice_env": "ELEVENLABS_VOICE_HUMANITARIANS",
            "palette": "humanitarians", "register": "Pragmatist", "charter": "HAI.md",
            "author_section": "Humanitarians AI",
            "persona": "Kore, in for Humanitarians AI",
            "engine": "kokoro", "voice_kokoro": "af_kore", "use_dir": True},
    "medhavy": {"suffix": "medhavy", "audience": "MEDHAVY", "voice_env": "ELEVENLABS_VOICE_MEDHAVY",
                "palette": "medhavy", "register": "Wonder", "charter": "MEDHAVY.md",
                "author_section": "Medhavy.com",
                "engine": "kokoro", "voice_kokoro": "af_kore", "use_dir": True},
    "nbb": {"suffix": "nbb", "audience": "NikBearBrown", "voice_env": "ELEVENLABS_VOICE_NIKBEARBROWN",
            "palette": "teardown", "register": "Teardown", "charter": "NIKBEARBROWN.md",
            "author_section": "NikBearBrown", "engine": "elevenlabs", "use_dir": True},
    "claude": {"suffix": "claude", "audience": "Claude", "voice_env": "ELEVENLABS_VOICE_NIKBEARBROWN",
               "palette": "claude", "register": "Teardown", "charter": "CLAUDE-BRAND.md",
               "author_section": "NikBearBrown", "engine": "elevenlabs", "use_dir": True},
    # Liam — the nbb persona's substitute narrator (IN-FOR-BEAR LAW, CLAUDE-BRAND.md):
    # same @NikBearBrown channel and Teardown register, kokoro voice so batch/series
    # builds spend no ElevenLabs credits. B00 narration must say "…this is Liam, in
    # for Bear." and the outro signs off the same way. Wagwan stays Bear's.
    "claude-liam": {"suffix": "claude-liam", "audience": "Claude", "voice_env": "ELEVENLABS_VOICE_LIAM",
                    "palette": "claude", "register": "Teardown", "charter": "CLAUDE-BRAND.md",
                    "author_section": "NikBearBrown",
                    "engine": "kokoro", "voice_kokoro": "am_onyx", "use_dir": True},
    "claude-hai": {"suffix": "claude-hai", "audience": "HAI", "voice_env": "ELEVENLABS_VOICE_HUMANITARIANS",
                   "palette": "claude", "register": "Pragmatist", "charter": "CLAUDE-BRAND.md",
                   "author_section": "Humanitarians AI",
                   "persona": "Kore, in for Humanitarians AI",
                   "engine": "kokoro", "voice_kokoro": "af_kore", "use_dir": True},
    "claude-medhavy": {"suffix": "claude-medhavy", "audience": "MEDHAVY", "voice_env": "ELEVENLABS_VOICE_MEDHAVY",
                       "palette": "claude", "register": "Wonder", "charter": "CLAUDE-BRAND.md",
                       "author_section": "Medhavy.com",
                       "engine": "kokoro", "voice_kokoro": "af_kore", "use_dir": True},
    "claude-musinique": {"suffix": "claude-musinique", "audience": "MUSINIQUE", "voice_env": "ELEVENLABS_VOICE_MUSINIQUE",
                         "palette": "claude", "register": "Baldwin", "charter": "CLAUDE-BRAND.md",
                         "author_section": "Musinique",
                         "engine": "kokoro", "voice_kokoro": "am_puck", "use_dir": True},
    "musinique": {"suffix": "musinique", "audience": "MUSINIQUE",
                  "voice_env": "ELEVENLABS_VOICE_MUSINIQUE",
                  "palette": "musinique", "register": "Baldwin", "charter": "MUSINIQUE.md",
                  "author_section": "Musinique",
                  "engine": "kokoro", "voice_kokoro": "am_puck"},
}


def get_brand_dir(reel: Path, suffix: str) -> Path:
    """Return the <suffix>- output directory for brands that use directory isolation."""
    parts = list(reel.parts)
    if 'lectures' in parts:
        idx = parts.index('lectures')
        book_dir = Path(*parts[:idx])
        return book_dir / f'{suffix}-lectures' / reel.name
    return reel.parent / f'{suffix}-{reel.name}'


def copy_build_scripts(src: Path, dst: Path) -> list:
    """Copy lecture build scripts (build_deck.py, make_audio*.py, render.py) if present."""
    copied = []
    for p in (list(src.glob('build_deck.py')) + list(src.glob('render.py'))
              + list(src.glob('make_audio*.py'))):
        shutil.copy2(p, dst / p.name)
        copied.append(p.name)
    return copied


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

    # hai + medhavy + nbb (use_dir) write into a new brand- directory; other brands use a sibling file
    if cfg.get("use_dir"):
        out_dir = get_brand_dir(reel, cfg["suffix"])
        out = out_dir / f"beat_sheet.{cfg['suffix']}.json"
        if out.exists() and not a.force:
            sys.exit(f"[variant] {out} already exists (use --force to reset it from canonical)")
        out_dir.mkdir(parents=True, exist_ok=True)
    else:
        out_dir = reel
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
    if cfg.get("persona"):
        meta["persona"] = cfg["persona"]
    meta["outro_source"] = f"AUTHOR.MD :: {cfg['author_section']}"
    if voice_id:
        meta["voice_id"] = voice_id  # ElevenLabs override; change engine to "elevenlabs" to use it
    # Kokoro defaults — brand-specific; override by setting engine="elevenlabs" in the sheet
    if cfg.get("engine"):
        meta["engine"] = cfg["engine"]
    if cfg.get("voice_kokoro"):
        meta["voice_kokoro"] = cfg["voice_kokoro"]
    # Record house typography for brands that use directory isolation
    if a.audience == "hai":
        meta["typography"] = {"serif": "EB Garamond", "sans": "Montserrat"}
    elif a.audience == "nbb":
        meta["typography"] = {"display": "Montserrat", "serif": "EB Garamond", "mono": "PT Mono"}

    # variant_todo — hai and nbb have brand-specific required beats
    if a.audience == "hai":
        meta["_variant_todo"] = [
            "rewrite every beat narration_text/text in the Pragmatist register "
            "(voices/pragmatist/VOICE.md + brands/hai.md) — method, when to use, "
            "when NOT to/where it fails; voice only, facts unchanged",
            "optional: add ONE Irreducibly-Human tangent beat (0-1 per video, ONLY on a clear opportunity)",
            "add CLI worked exercise as the SECOND-TO-LAST beat "
            "(cli-scout lane → paste-ready ASK→OUTPUT→CHANGE→OUTPUT, NEXT STEP; "
            "see skills/make/hai/SKILL.md §Step 4)",
            f"add/replace outro with Humanitarians AI outro from {meta['outro_source']} (LAST beat)",
            "verify ending order: body → [tangent] → [CLI exercise] → [outro]",
            "then build: generate_audio_kokoro.py → palette=humanitarians → compile",
        ]
    elif a.audience == "nbb":
        meta["_variant_todo"] = [
            "rewrite every beat narration_text/text in the Teardown register "
            "(voices/teardown/VOICE.md + brands/nbb.md) — take it apart, explain how each piece "
            "works, judge the design choices; voice only, facts unchanged",
            "add LLM exercise as the SECOND-TO-LAST beat "
            "(paste-ready prompt for Claude/ChatGPT/Gemini + dig-deeper follow-up; "
            "see skills/make/nbb/SKILL.md §Step 3)",
            f"add/replace outro with NikBearBrown outro from {meta['outro_source']} (LAST beat)",
            "verify ending order: body → [LLM exercise] → [outro]",
            "GATE P before audio spend — then build: generate_audio.py (ElevenLabs only, no Kokoro) "
            "→ palette=teardown → compile",
        ]
    else:
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
    # lecture format: segments with nested beats
    for seg in sheet.get("segments", []):
        for b in seg.get("beats", []):
            b.pop("actual_duration_s", None)

    out.write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
    if cfg.get("voice_kokoro"):
        kokoro_note = f"  engine={cfg['engine']}  voice_kokoro={cfg['voice_kokoro']}"
    elif cfg.get("engine"):
        kokoro_note = f"  engine={cfg['engine']}"
    else:
        kokoro_note = ""

    if cfg.get("use_dir"):
        copied = copy_build_scripts(reel, out_dir)
        if copied:
            print(f"[variant] copied build scripts: {', '.join(sorted(copied))}")
        beat_count = len(sheet.get("beats", []))
        seg_count = len(sheet.get("segments", []))
        content_note = (f"{beat_count} beats" if beat_count else f"{seg_count} segments")
        skill_ref = (f"skills/make/{a.audience}/SKILL.md"
                     if a.audience in ("hai", "nbb")
                     else f"audience-preset brands/{a.audience}.md")
        print(f"[variant] wrote {out}  audience={cfg['audience']}  register={cfg['register']}  "
              f"palette={cfg['palette']}  11labs_voice={voice_note}{kokoro_note}")
        print(f"[variant] {content_note} to rewrite in {cfg['register']} — "
              f"next: Claude Code follows {skill_ref}")
    else:
        beat_count = len(sheet.get("beats", []))
        print(f"[variant] wrote {out.name}  audience={cfg['audience']}  register={cfg['register']}  "
              f"palette={cfg['palette']}  11labs_voice={voice_note}{kokoro_note}")
        print(f"[variant] {beat_count} beats to rewrite in {cfg['register']} — "
              f"next: Claude Code follows the {a.audience} SKILL to rewrite narration + outro + tangent")


if __name__ == "__main__":
    main()
