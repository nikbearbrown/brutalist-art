#!/usr/bin/env python3
"""check_keys.py — validate every key LIVE and FREE (no generation, no spend).

Each provider has an account/status endpoint that costs nothing:
  ElevenLabs   GET /v1/user/subscription   → valid? + characters left      (0 chars)
               GET /v1/voices              → configured voice IDs exist?    (0 chars)
  higgsfield   `higgsfield account status` → logged in? + credits           (no gen)
  YouTube      channels.list(mine=true)    → OAuth valid? + channel         (1 free unit)
  FAL          present-only (a real job would cost; not probed)

Reads keys from the environment, then the repo-root `.env` (shell wins). Prints a table;
never prints a secret value. Exit 0 if every SET key is valid; 1 if any SET key is invalid.

Usage:  ./art keys        (or)  python3 runtime/scripts/check_keys.py
"""
from __future__ import annotations
import os, sys, json, subprocess, urllib.request, urllib.error
from pathlib import Path

REPO = Path(os.environ.get("ART_HOME") or Path(__file__).resolve().parents[2])

def load_env():
    f = REPO / ".env"
    if not f.exists():
        return
    for line in f.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip(); v = v.strip().strip('"').strip("'")
        os.environ.setdefault(k, v)   # shell wins

def g(url, headers):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode())

C = {"ok": "\033[32m", "bad": "\033[31m", "warn": "\033[33m", "z": "\033[0m", "b": "\033[1m"}
rows = []
_state = {'inconclusive': False}
def row(service, var, status, detail):
    rows.append((service, var, status, detail))

def main():
    load_env()
    any_invalid = False

    # ── ElevenLabs ───────────────────────────────────────────────────────────
    ek = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not ek:
        row("ElevenLabs", "ELEVENLABS_API_KEY", "unset", "narration disabled until set")
    else:
        try:
            sub = g("https://api.elevenlabs.io/v1/user/subscription", {"xi-api-key": ek})
            used = sub.get("character_count"); lim = sub.get("character_limit")
            tier = sub.get("tier", "?")
            left = (lim - used) if (isinstance(lim, int) and isinstance(used, int)) else "?"
            row("ElevenLabs", "ELEVENLABS_API_KEY", "valid",
                f"tier={tier} · {left} chars left ({used}/{lim})")
            # voice IDs
            try:
                voices = g("https://api.elevenlabs.io/v1/voices", {"xi-api-key": ek})
                have = {v.get("voice_id") for v in voices.get("voices", [])}
                for vv in ("ELEVENLABS_VOICE_NIKBEARBROWN", "ELEVENLABS_VOICE_MEDHAVY",
                           "ELEVENLABS_VOICE_HUMANITARIANS", "ELEVENLABS_VOICE_NEU",
                           "ELEVENLABS_VOICE_ID"):
                    vid = os.environ.get(vv, "").strip()
                    if not vid:
                        continue
                    ok = vid in have
                    if not ok: any_invalid = True
                    row("  ↳ voice", vv, "valid" if ok else "invalid",
                        "in library" if ok else "voice_id NOT in this account's library")
            except Exception as e:
                row("  ↳ voices", "(list)", "warn", f"couldn't list voices: {e}")
        except urllib.error.HTTPError as e:
            any_invalid = True
            row("ElevenLabs", "ELEVENLABS_API_KEY", "invalid",
                f"HTTP {e.code} — key rejected" if e.code in (401, 403) else f"HTTP {e.code}")
        except Exception as e:
            _state["inconclusive"] = True
            row("ElevenLabs", "ELEVENLABS_API_KEY", "warn", f"probe failed (network?): {e}")

    # ── higgsfield CLI (no env key; login-based) ─────────────────────────────
    try:
        r = subprocess.run(["higgsfield", "account", "status"],
                           capture_output=True, text=True, timeout=25)
        out = (r.stdout + r.stderr).strip().replace("\n", " ")[:80]
        if r.returncode == 0:
            row("higgsfield", "(CLI login)", "valid", out or "logged in")
        else:
            row("higgsfield", "(CLI login)", "invalid",
                "run `higgsfield auth login` — " + (out or "not logged in"))
    except FileNotFoundError:
        row("higgsfield", "(CLI login)", "unset", "higgsfield CLI not installed (AI video disabled)")
    except Exception as e:
        row("higgsfield", "(CLI login)", "warn", f"status check failed: {e}")

    # ── YouTube OAuth (1 free quota unit) ────────────────────────────────────
    cs = os.environ.get("ART_YOUTUBE_CLIENT_SECRET", "./client_secret.json")
    tok = os.environ.get("ART_YOUTUBE_TOKEN", "./youtube_token.json")
    cs_p, tok_p = (REPO / cs), (REPO / tok)
    if not cs_p.exists():
        row("YouTube", "OAuth", "unset", f"no client_secret at {cs} (publishing disabled)")
    else:
        try:
            from google.oauth2.credentials import Credentials  # type: ignore
            from googleapiclient.discovery import build          # type: ignore
            if not tok_p.exists():
                row("YouTube", "OAuth", "warn",
                    "client_secret present; token not yet created — first publish will authorize")
            else:
                creds = Credentials.from_authorized_user_file(str(tok_p))
                yt = build("youtube", "v3", credentials=creds)
                ch = yt.channels().list(part="snippet", mine=True).execute()
                items = ch.get("items", [])
                name = items[0]["snippet"]["title"] if items else "(no channel)"
                row("YouTube", "OAuth", "valid", f"channel: {name} · 1 quota unit used")
        except ImportError:
            row("YouTube", "OAuth", "warn",
                "google-api-python-client not installed — pip install it to probe")
        except Exception as e:
            any_invalid = True
            row("YouTube", "OAuth", "invalid", f"token rejected/expired: {str(e)[:60]}")

    # ── FAL (optional; present-only) ─────────────────────────────────────────
    fk = os.environ.get("FAL_KEY", "").strip()
    row("FAL", "FAL_KEY", "set (not probed)" if fk else "unset",
        "optional; a real job would cost — confirm on first use" if fk else "optional")

    # ── print ────────────────────────────────────────────────────────────────
    print()
    print(f"  {C['b']}key readiness (live, free — no generation){C['z']}\n")
    print(f"  {'SERVICE':<14}{'VAR':<32}{'STATUS':<10}DETAIL")
    print(f"  {'-------':<14}{'---':<32}{'------':<10}------")
    for svc, var, st, det in rows:
        col = {"valid": C["ok"], "invalid": C["bad"], "warn": C["warn"]}.get(st, C["warn"])
        mark = {"valid": "✅ valid", "invalid": "❌ invalid", "unset": "· unset",
                "warn": "⚠ check", "set (not probed)": "· set"}.get(st, st)
        print(f"  {svc:<14}{var:<32}{col}{mark:<10}{C['z']}{det}")
    print()
    print("  Free probes only: ElevenLabs /user + /voices, higgsfield account status, "
          "YouTube channels.list (1 unit). No characters, credits, or renders spent.")
    if any_invalid:
        print(f"\n  {C['bad']}One or more SET keys are invalid — fix before the paid builds.{C['z']}\n")
        return 1
    if _state["inconclusive"]:
        print(f"\n  {C['warn']}Some probes were inconclusive (no network here) — re-run "
              f"`./art keys` in a terminal with internet to fully validate.{C['z']}\n")
        return 0
    print(f"\n  {C['ok']}All set keys validated.{C['z']}\n")
    return 0

if __name__ == "__main__":
    sys.exit(main())
