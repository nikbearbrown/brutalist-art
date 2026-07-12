#!/usr/bin/env python3
"""td_script_gate.py — the Teardown-Script gate.

Validates a style-agnostic vox beat_sheet.json produced by the `script`
command against the fused standard: the Brown Blue pedagogical constitution
(sequencing + arc) and the Teardown voice (forbidden-phrase scan). It is the
deterministic half — it cannot judge whether the narration is *good*, only
whether the STRUCTURE obeys the constitution and the derived length is sane.

Renderer-agnostic on purpose: it reads role / narration / duration only. It
never looks at shot.source, so the same script passes whether it is later
dressed as pure Manim, nbb house style, Remotion, or doodle.

Usage:
  python3 td_script_gate.py <reel_dir | beat_sheet.json> [--quiet]

Exit 0 = Gate-1 + Gate-2 pass (warnings allowed).
Exit 1 = a hard check failed.
Free/local. Python stdlib only.
"""
import argparse, json, re, sys
from pathlib import Path

ROLES = ["HOOK", "INSTANCE", "TRANSFORM", "ABSTRACTION", "TANGENT", "PAYOFF", "BOUNDARY"]

# Teardown VOICE.md forbidden phrases (case-insensitive substring scan).
FORBIDDEN = [
    "one could argue", "it seems as though", "it can be shown",
    "obviously", "clearly", "innovative", "revolutionary",
    "premium", "sleek", "seamless", "cutting-edge", "game-chang",
]
# Vocabulary/notation tells that must NOT appear in the HOOK (§1.2, §2).
HOOK_BANS = ["is defined as", "we define", "denoted by", "by definition",
             "today we'll cover", "today we will cover", "in this video we'll"]


def load(target: Path):
    p = target if target.is_file() else target / "beat_sheet.json"
    if not p.exists():
        sys.exit(f"[td-gate] no beat_sheet.json at {target}")
    return json.loads(p.read_text()), p


def dur(b):
    try:
        return float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0)
    except (TypeError, ValueError):
        return 0.0


def tier_for(total_s, n_abs):
    m = total_s / 60.0
    if m <= 4:
        return "Single-insight (2–4 min)"
    if m <= 8:
        return "Standard (4–8 min)"
    return "Multi-act (8–15 min — needs explicit user approval at Gate 1)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    sheet, path = load(Path(a.target).resolve())
    meta = sheet.get("metadata", {})
    beats = sheet.get("beats", [])
    fails, warns, notes = [], [], []

    # ---- metadata / Gate-1 preconditions -----------------------------------
    if not (meta.get("key_case") or "").strip():
        fails.append("§1.1 metadata.key_case is empty — name the key exercise/case.")
    if (meta.get("register") or "").lower() != "teardown":
        warns.append(f"metadata.register is {meta.get('register')!r}, expected 'Teardown'.")
    if not beats:
        sys.exit("[td-gate] beat sheet has no beats.")

    roles = [(b.get("beat_id", f"#{i}"), (b.get("role") or "").upper())
             for i, b in enumerate(beats)]
    for bid, r in roles:
        if r not in ROLES:
            fails.append(f"{bid}: role {r!r} not in {ROLES}.")

    # ---- Gate-2 arc ---------------------------------------------------------
    if roles[0][1] != "HOOK":
        fails.append(f"§4 first beat must be HOOK (is {roles[0][1] or 'unset'}).")
    if roles[-1][1] != "BOUNDARY":
        warns.append("§7 last beat should be BOUNDARY (fused with the outro).")
    if not any(r == "BOUNDARY" for _, r in roles):
        fails.append("§7 no BOUNDARY beat — every video ends with not-taught + a viewer exercise.")
    if not any(r == "PAYOFF" for _, r in roles):
        fails.append("§4 no PAYOFF beat — the hook must be resolved on screen.")

    # ≥2 INSTANCE before each ABSTRACTION (count resets after each ABSTRACTION).
    seen_instances = 0
    for bid, r in roles:
        if r == "INSTANCE":
            seen_instances += 1
        elif r == "ABSTRACTION":
            if seen_instances < 2:
                fails.append(f"{bid}: §1.3/§4 ABSTRACTION has only {seen_instances} "
                             f"prior INSTANCE beat(s) — needs ≥2 moving instances first.")
            seen_instances = 0  # reset window for the next abstraction

    # every equation-landing ABSTRACTION must be immediately followed by TANGENT
    for i, b in enumerate(beats):
        if (b.get("role") or "").upper() == "ABSTRACTION" and b.get("lands_equation"):
            nxt = (beats[i + 1].get("role") or "").upper() if i + 1 < len(beats) else ""
            if nxt != "TANGENT":
                fails.append(f"{b.get('beat_id')}: §4 ABSTRACTION lands an equation but is not "
                             f"followed by a TANGENT bracket (equations.md).")

    # PAYOFF should reference the hook (self-declared flag; heuristic only)
    for b in beats:
        if (b.get("role") or "").upper() == "PAYOFF" and not b.get("references_hook", False):
            warns.append(f"{b.get('beat_id')}: set references_hook:true once the PAYOFF puts "
                         f"the HOOK's object back on screen (§4).")
    # BOUNDARY must carry a concrete viewer exercise
    for b in beats:
        if (b.get("role") or "").upper() == "BOUNDARY" and not (b.get("viewer_exercise") or "").strip():
            fails.append(f"{b.get('beat_id')}: §7 BOUNDARY needs a non-empty viewer_exercise.")

    # HOOK must open unsolved: no vocabulary/notation/utility framing
    hook = next((b for b in beats if (b.get("role") or "").upper() == "HOOK"), None)
    if hook:
        h = (hook.get("narration_text") or "").lower()
        for phrase in HOOK_BANS:
            if phrase in h:
                fails.append(f"{hook.get('beat_id')}: §2 HOOK contains {phrase!r} — open with the "
                             f"unsolved mystery, zero vocabulary/utility framing.")

    # ---- Teardown voice: forbidden-phrase scan (warn) ----------------------
    for b in beats:
        t = (b.get("narration_text") or "").lower()
        for phrase in FORBIDDEN:
            if phrase in t:
                warns.append(f"{b.get('beat_id')}: teardown voice forbids {phrase!r} — "
                             f"say what actually happens / what it optimized for.")

    # ---- length procedure (§5) ---------------------------------------------
    total = sum(dur(b) for b in beats)
    n_abs = sum(1 for _, r in roles if r == "ABSTRACTION")
    for b in beats:
        d = dur(b)
        if d and not (3.0 <= d <= 12.0) and (b.get("role") or "").upper() != "BOUNDARY":
            warns.append(f"{b.get('beat_id')}: beat is {d:.1f}s — one sentence ≈ 5–9s; "
                         f"split or trim (§5.2). Never pad, never rush.")
    tier = tier_for(total, n_abs)

    # ---- report -------------------------------------------------------------
    if not a.quiet:
        print(f"[td-gate] {path}")
        print(f"  key case : {meta.get('key_case','(unset)')}")
        print(f"  register : {meta.get('register','(unset)')}   pedagogy: {meta.get('pedagogy','(unset)')}")
        print(f"  arc      : {' → '.join(r for _, r in roles)}")
        print(f"  length   : {total:.0f}s ≈ {total/60:.1f} min   ({n_abs} abstraction[s]) → {tier}")
        print(f"  beats    : {len(beats)}")
        print("  ── Gate-1 audit ──")
        table = [
            ("Key exercise / key case named", bool((meta.get('key_case') or '').strip())),
            ("Opens on HOOK, no vocab/utility framing", roles[0][1] == "HOOK" and hook is not None),
            (">=2 moving INSTANCEs before each ABSTRACTION",
             not any("prior INSTANCE" in f for f in fails)),
            ("Every equation-landing ABSTRACTION -> TANGENT",
             not any("TANGENT bracket" in f for f in fails)),
            ("PAYOFF resolves the HOOK", any(r == "PAYOFF" for _, r in roles)),
            ("BOUNDARY: not-taught + viewer exercise",
             any(r == "BOUNDARY" for _, r in roles)
             and not any("viewer_exercise" in f for f in fails)),
            ("Length derived + tier reported", True),
        ]
        for label, ok in table:
            print(f"    [{'x' if ok else ' '}] {label}")
        for f in fails:
            print(f"  FAIL  {f}")
        for w in warns:
            print(f"  warn  {w}")

    if fails:
        print(f"[td-gate] GATE FAILED — {len(fails)} hard issue(s), {len(warns)} warning(s).")
        sys.exit(1)
    print(f"[td-gate] PASS — {len(warns)} warning(s). Arc obeys the Brown Blue constitution.")
    sys.exit(0)


if __name__ == "__main__":
    main()
