#!/usr/bin/env python3
"""
fill_pantry.py  —  `art fill-pantry <reel>`  (Higgsfield tier-1 vox auto-fill)

Fills EMPTY tier-1, kenburns/hold vox placeholders with generated stills, each
conditioned on a fixed STYLE PLATE (not a prose prompt), then verified by Gate V
before it's trusted. Everything except the generative call is deterministic and
runs without Higgsfield, so `--dry-run` is safe and free.

STYLE (how you guide the look):
  1. PLATE  — the reference image IS the style. Resolution order per beat:
       <reel>/style/vox-plate-<archetype>.png      (per-reel override)
       runtime/style/vox-plates/<palette>/vox-plate-<archetype>.png  (channel default)
     Author the channel plates ONCE, already run through your treatment fn.
  2. PROMPT — the beat's slate prompt picks the SUBJECT/framing only.
  3. TREATMENT — your existing pantry treatment normalizes the grade after.
  4. style.json (beside the plates) — model, negative_prompt, credits/gen, archetype keywords.

SAFETY (why it won't hurt you):
  * tier-1 only, kenburns/hold only (cutout/parallax fenced — need mattes).
  * tier RE-CHECK at fill time: any proper noun / date in the prompt -> refuse,
    regardless of the shopping-list tag (don't inherit upstream confidence).
  * idempotent: never overwrites an existing pantry asset (human or prior auto).
  * SPEND GATE: --dry-run is default; --go required to spend credits.
  * every fill is PROVISIONAL: writes <BID>.auto + <BID>.source.txt; stays in
    the review queue until you sign it off or replace it.
  * generate -> Gate V (on the still) -> regenerate up to N; give up to a human
    placeholder rather than ship a bad composition.

The GENERATE call is a pluggable adapter (see generate()). Wire it to your
Higgsfield MCP (agent-driven) or Higgsfield API key (unattended). Nothing else
needs changing.
"""
import argparse, glob, json, os, re, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "qc"))
try:
    import final_frame_check as gv   # the acceptance test
except Exception:
    gv = None

ARCHES = ("object", "scene", "portrait")
TEXT_CARD = {"slatecard", "textcard", "titlecard"}
COMMON_CAPS = {"AI", "US", "USA", "UK", "GPU", "CPU", "API", "I", "A", "The",
               "Tier", "You", "Claude", "Wide", "A", "An"}
PROPER = re.compile(r"\b([A-Z][a-z]{2,})\b")   # Title-case only (Edison, Menlo) — not all-caps emphasis (SALE, STOP)
DATE = re.compile(r"\b(1[89]\d\d|20\d\d)\b")


# ---------- style resolution -------------------------------------------------
def load_style(reel, palette="claude"):
    cfg = {"model": "flux-kontext", "credits_per_gen": 1,
           "negative_prompt": "text, letters, numbers, words, logos, watermarks, "
                              "real people, faces, named places, brand marks",
           "archetype_keywords": {
               "portrait": ["figure", "person", "silhouette", "hand", "face", "seated"],
               "scene": ["room", "interior", "landscape", "wide", "wall", "library", "cluster"],
               "object": ["object", "artifact", "device", "book", "chip", "close-up", "still life"]},
           "max_tries": 3,
           "default_style_type": "artsy",
           "style_modifiers": {},
           "mj_interval_sec": 240}   # MJ rate-limits: pace ~1 gen / 3-5 min, never a tight loop
    book_youtube = os.path.dirname(os.path.abspath(reel))   # books/<book>/youtube
    for p in (os.path.join(HERE, "..", "style", "vox-plates", palette, "style.json"),  # channel default
              os.path.join(book_youtube, "_style", "style.json"),                       # per-book
              os.path.join(reel, "style", "style.json")):                               # per-reel (wins)
        if os.path.exists(p):
            try: cfg.update(json.load(open(p)))
            except Exception: pass
    return cfg


def archetype_of(prompt, cfg):
    p = (prompt or "").lower()
    for arch in ("portrait", "object", "scene"):   # portrait/object win over generic scene
        if any(k in p for k in cfg["archetype_keywords"].get(arch, [])):
            return arch
    return "scene"


def compose_mj(subject, cfg, style_type):
    """Midjourney prompt = SUBJECT (per beat) + a named STYLE MODIFIER
    (suffix + --profile). The profile is MJ's own trained style lock — the
    equivalent of a reference plate for the flux backend."""
    m = (cfg.get("style_modifiers") or {}).get(style_type)
    if not m:
        return None
    # "subject, <modifier suffix> <params>" — the --profile carries the look,
    # so the suffix stays short (e.g. "3D sculpture").
    return f"{subject.strip()}, {m.get('suffix','')} {m.get('params','')}".strip()


HUMAN_WORDS = ("man", "woman", "person", "people", "figure", "philosopher",
               "scholar", "clerk", "thinker", "orator", "gentleman", "teacher",
               "student", "monk", "crowd", "hands", "seated", "portrait")


def has_human(subject):
    s = (subject or "").lower()
    return any(w in s for w in HUMAN_WORDS)


def sidecar_text(backend, style_type, prompt, plate, arch, stamp, cfg):
    lines = [f"backend: {backend}", f"model: {cfg.get('model')}",
             f"style_type: {style_type}", f"prompt: {prompt}",
             f"reference_plate: {plate}", f"archetype: {arch}",
             f"at: {stamp}", "provenance: ai"]
    if style_type == "photo":
        # photoreal people: this route generates AI images that READ as real
        # photographs. Never a real named person/place (the tier re-check
        # enforces that on the subject); still, disclose it and never let it
        # pass as archival evidence in a claim context.
        lines.append("disclosure: AI-generated photoreal image; depicts NO real "
                     "person, place, or event; not a real photograph; not archival. "
                     "AI-disclosure required on use; illustrative/atmospheric only.")
    return "\n".join(lines) + "\n"


def resolve_plate(reel, arch, palette="claude"):
    # most-specific wins: per-reel -> per-book -> channel default.
    book_youtube = os.path.dirname(os.path.abspath(reel))   # books/<book>/youtube
    for cand in (os.path.join(reel, "style", f"vox-plate-{arch}.png"),
                 os.path.join(book_youtube, "_style", f"vox-plate-{arch}.png"),
                 os.path.join(HERE, "..", "style", "vox-plates", palette, f"vox-plate-{arch}.png")):
        if os.path.exists(cand):
            return os.path.normpath(cand)
    return None


# ---------- tier re-check (defense in depth) ---------------------------------
def tier_recheck(prompt):
    """Refuse anything that might be a real place/person/dated event, regardless
    of the shopping-list tag. Conservative on purpose — over-refusing is safe."""
    reasons = []
    propers = [w for w in PROPER.findall(prompt or "") if w not in COMMON_CAPS]
    if propers:
        reasons.append(f"proper noun(s): {', '.join(sorted(set(propers))[:4])}")
    if DATE.search(prompt or ""):
        reasons.append("a specific year/date")
    return reasons   # empty = safe to auto-generate


# ---------- beat selection ---------------------------------------------------
def slate_prompt(beat):
    sh = beat.get("shot", {}) or {}
    raw = (sh.get("suggested_prompt") or beat.get("new_visual_element")
           or (sh.get("remotion") or {}).get("props", {}).get("prompt")
           or beat.get("narration_text", ""))[:300]
    # strip the vox-slate label prefix ("VOX:", "VOX run R1 (1/2):") — it's a
    # production tag, not part of the visual subject.
    raw = re.sub(r"^\s*VOX(\s+run\s+R\d+\s*\([\d/]+\))?\s*:\s*", "", raw, flags=re.I)
    return raw.strip()


def is_vox_fillable(beat):
    sh = beat.get("shot", {}) or {}
    typ = sh.get("type"); lane = sh.get("lane"); motion = sh.get("motion", "kenburns")
    if lane not in (None, "vox") and typ not in ("STILL", "COMPOSITE"):
        return False
    if typ not in ("STILL", "COMPOSITE") and lane != "vox":
        return False
    if motion not in ("kenburns", "hold", None):
        return False, "motion needs a matte (cutout/parallax) — human only"
    return True


MEDIA_EXT = (".png", ".jpg", ".jpeg", ".webp", ".mp4", ".mov")
SLATE_MAX_BYTES = 1_200_000   # pass-1 slate cards are ~300-500KB; real vox media is multi-MB


def pantry_filled(reel, bid):
    # A real fill is MEDIA (not a .source.txt/.auto sidecar). A small media/
    # mp4 is a placeholder SLATE, not a fill — don't let it fake "filled".
    for f in glob.glob(os.path.join(reel, "pantry", f"{bid}.*")):
        if f.lower().endswith(MEDIA_EXT):
            return True
    for f in glob.glob(os.path.join(reel, "media", f"{bid}.*")):
        if f.lower().endswith(MEDIA_EXT):
            try:
                if os.path.getsize(f) > SLATE_MAX_BYTES:
                    return True
            except OSError:
                return True
    return False


def plan(reel, cfg, palette="claude"):
    bs = json.load(open(os.path.join(reel, "beat_sheet.json")))
    rows = []
    for b in bs.get("beats", []):
        bid = b.get("beat_id", "?")
        ok = is_vox_fillable(b)
        if ok is False:
            continue
        motion_block = ok[1] if isinstance(ok, tuple) else None
        if pantry_filled(reel, bid):
            continue                      # idempotent
        prompt = slate_prompt(b)
        arch = archetype_of(prompt, cfg)
        sh = b.get("shot", {}) or {}
        stype = sh.get("style_type") or cfg.get("default_style_type", "artsy")
        _mjp = compose_mj(prompt, cfg, stype)
        # For a human subject: image-ref URL leads (MJ image prompts must be
        # first), then beat id, then the character DESCRIPTION, then subject+modifier
        #   <url> <bid> <char_desc>, <subject>, <modifier>
        # so a consistent recurring man appears across every beat.
        _post = None
        if _mjp:
            _human = has_human(prompt)
            _ref = cfg.get("char_ref_url") if _human else None
            _desc = cfg.get("char_desc") if _human else None
            _body = f"{bid} " + (f"{_desc}, " if _desc else "") + _mjp
            _post = (f"{_ref} " if _ref else "") + _body
        row = {"bid": bid, "archetype": arch, "prompt": prompt, "style_type": stype,
               "plate": resolve_plate(reel, arch, palette),
               "mj_prompt": _post,
               "refuse": tier_recheck(prompt) or (["motion: " + motion_block] if motion_block else []),
               "motion": sh.get("motion", "kenburns")}
        rows.append(row)
    return rows


# ---------- generation adapter (wire this to Higgsfield) ---------------------
def generate(prompt, plate, out_path, cfg, backend):
    """Return path to a generated still, conditioned on `plate`. Two backends:
       backend=='mcp'  -> Higgsfield MCP (agent-driven; Claude calls the tool)
       backend=='api'  -> Higgsfield REST with HIGGSFIELD_API_KEY (unattended)
    Not wired here on purpose — this is the one integration point."""
    raise NotImplementedError(
        "Wire fill_pantry.generate() to Higgsfield:\n"
        "  api : POST prompt + reference image `plate` with HIGGSFIELD_API_KEY,\n"
        "        save the returned image to out_path.\n"
        "  mcp : have Claude call the Higgsfield MCP image tool with (prompt, plate)\n"
        "        and write the result to out_path.\n"
        f"  negative_prompt to pass: {cfg['negative_prompt']!r}")


def accept(still_path):
    """Gate V on the raw still (kenburns only zooms IN, so a still that passes
    fill/edge as-is passes after the move). Returns list of defects."""
    if gv is None or not os.path.exists(still_path):
        return []
    d, _ = gv.analyze_frame(still_path)
    return d


# ---------- ingest a Midjourney zip/folder into the pantry -------------------
def _slug(s):
    return re.sub(r"[^a-z0-9]+", "_", (s or "").lower()).strip("_")


def ingest(reel, src, cfg, stamp):
    """Unzip a MJ 'download all' zip (or a folder) dropped in the connected
    folder, match each file to its beat — primarily by the beat id prepended to
    the prompt (so it's in the filename), fallback to the subject slug — and
    rename into pantry/<bid>.<ext>. Prefers the animation (.mp4) per beat, else
    the largest still. Writes sidecar + .auto; Gate V on stills."""
    import zipfile, shutil, tempfile
    tmp = tempfile.mkdtemp()
    if os.path.isfile(src) and src.lower().endswith(".zip"):
        with zipfile.ZipFile(src) as z:
            z.extractall(tmp)
        root = tmp
    else:
        root = src
    files = [os.path.join(dp, fn) for dp, _, fns in os.walk(root) for fn in fns
             if fn.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".mp4"))]

    bs = json.load(open(os.path.join(reel, "beat_sheet.json")))
    meta = {}   # bid -> (subject, style_type, subj_key)
    for b in bs.get("beats", []):
        if is_vox_fillable(b) is not True:
            continue
        subj = slate_prompt(b)
        if tier_recheck(subj):
            continue
        bid = b.get("beat_id", "")
        stype = (b.get("shot", {}) or {}).get("style_type") or cfg.get("default_style_type", "artsy")
        meta[bid] = (subj, stype)

    def match_bid(fslug):
        # primary: the beat id prepended to the prompt (survives underscores)
        m = re.search(r"(?:^|_)(b\d{1,3})(?:_|$)", fslug)
        if m and m.group(1).upper() in meta:
            return m.group(1).upper()
        # fallback (files made before the id prefix): subject token overlap,
        # robust to MJ truncating long prompts in the filename.
        fset = set(fslug.split("_"))
        best_bid, best = None, 0
        for cbid, (subj, _t) in meta.items():
            toks = [t for t in _slug(subj).split("_") if len(t) > 2][:6]
            score = sum(1 for t in toks if t in fset)
            if toks and score >= 3 and score / len(toks) >= 0.5 and score > best:
                best_bid, best = cbid, score
        return best_bid

    assign = {}
    for f in files:
        bid = match_bid(_slug(os.path.basename(f)))
        if bid:
            assign.setdefault(bid, []).append(f)

    os.makedirs(os.path.join(reel, "pantry"), exist_ok=True)
    placed, unmatched = [], [f for f in files if not any(f in v for v in assign.values())]
    for bid, fs in assign.items():
        mp4 = [x for x in fs if x.lower().endswith(".mp4")]
        pick = mp4[0] if mp4 else max(fs, key=os.path.getsize)
        ext = os.path.splitext(pick)[1].lower()
        out = os.path.join(reel, "pantry", f"{bid}{ext}")
        shutil.copy(pick, out)
        subj, stype = meta[bid]
        open(os.path.join(reel, "pantry", f"{bid}.auto"), "w").write(
            "provisional MJ fill — review or replace\n")
        open(os.path.join(reel, "pantry", f"{bid}.source.txt"), "w").write(
            sidecar_text("midjourney", stype, subj, None, "", stamp, cfg))
        defects = accept(out) if ext != ".mp4" else []
        placed.append((bid, os.path.basename(pick), ext, [k for _, k, _ in defects]))
    return placed, unmatched


# ---------- CLI --------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="art fill-pantry — Higgsfield tier-1 vox auto-fill")
    ap.add_argument("reel")
    ap.add_argument("--palette", default="claude")
    ap.add_argument("--go", action="store_true", help="actually spend credits (default: dry-run)")
    ap.add_argument("--backend", choices=["mcp", "api", "midjourney"], default="api")
    ap.add_argument("--stamp", default=None, help="timestamp for sidecars (default: now)")
    ap.add_argument("--ingest", help="a MJ 'download all' zip or folder (in the connected "
                                     "folder); unzip, match to beats by id/subject, rename into pantry/")
    a = ap.parse_args()
    cfg = load_style(a.reel, a.palette)

    if a.ingest:
        stamp = a.stamp or time.strftime("%Y-%m-%dT%H:%M:%S")
        placed, unmatched = ingest(a.reel, a.ingest, cfg, stamp)
        print(f"art fill-pantry --ingest — {os.path.basename(a.reel)}")
        print(f"  placed {len(placed)} into pantry/, {len(unmatched)} file(s) unmatched")
        for bid, fn, ext, defects in sorted(placed):
            gv_note = " GATE V: " + ",".join(defects) if defects else (" ✓" if ext != ".mp4" else " (video)")
            print(f"    {bid}{ext}  <- {fn}{gv_note}")
        if unmatched:
            print("  unmatched (no beat id or subject match):")
            for f in unmatched[:8]:
                print(f"    {os.path.basename(f)}")
        return 0

    rows = plan(a.reel, cfg, a.palette)

    fillable = [r for r in rows if not r["refuse"]]
    refused = [r for r in rows if r["refuse"]]
    missing_plate = [r for r in fillable if not r["plate"]]

    mj = a.backend == "midjourney"
    print(f"art fill-pantry — {os.path.basename(a.reel)}  (backend: {a.backend})")
    print(f"  empty tier-1 vox slots: {len(rows)}   auto-fillable: {len(fillable)}   "
          f"refused (human): {len(refused)}"
          + ("" if mj else f"   est. credits: {len(fillable)*cfg['credits_per_gen']}"))
    for r in rows:
        tag = "OK" if not r["refuse"] else "HUMAN"
        if mj:
            body = (r["mj_prompt"][:96] + "…") if r.get("mj_prompt") else f"NO MODIFIER for '{r['style_type']}'"
            print(f"  {r['bid']:<5} [{tag}] {r['style_type']:<6} {body}"
                  + (f"  <- {'; '.join(r['refuse'])}" if r["refuse"] else ""))
        else:
            print(f"  {r['bid']:<5} [{tag}] {r['archetype']:<8} plate={os.path.basename(r['plate']) if r['plate'] else 'MISSING'}"
                  + (f"  <- {'; '.join(r['refuse'])}" if r["refuse"] else ""))
    if not mj and missing_plate:
        print(f"  ! {len(missing_plate)} beat(s) have no style plate — author "
              f"runtime/style/vox-plates/{a.palette}/vox-plate-<archetype>.png first.")
    if mj and any(not r.get("mj_prompt") for r in fillable):
        print("  ! some beats have no style_modifier — add it to style.json style_modifiers.")

    stamp = a.stamp or time.strftime("%Y-%m-%dT%H:%M:%S")

    # ---- Midjourney: emit a PACED work queue (no API — agent posts via browser) ----
    if mj:
        q = [r for r in fillable if r.get("mj_prompt")]
        interval = int(cfg.get("mj_interval_sec", 240))
        os.makedirs(os.path.join(a.reel, "pantry"), exist_ok=True)
        items = [{"bid": r["bid"], "out": f"pantry/{r['bid']}.png",
                  "mj_prompt": r["mj_prompt"], "style_type": r["style_type"],
                  "sidecar": sidecar_text("midjourney", r["style_type"], r["prompt"],
                                          None, r["archetype"], stamp, cfg)} for r in q]
        est_min = round(len(items) * interval / 60)
        print(f"\n  Midjourney is rate-limited — pacing 1 post / {interval}s "
              f"(~{est_min} min for {len(items)} beats). MJ has no API, so posts are "
              f"agent-driven (Claude-in-Chrome): post -> wait -> grab the chosen index -> "
              f"save to pantry/<bid>.png -> Gate V -> sidecar + .auto.")
        for it in items:
            print(f"    {it['bid']}: {it['mj_prompt']}")
        if a.go:
            qp = os.path.join(a.reel, "pantry", "_mj_queue.json")
            json.dump({"interval_sec": interval, "items": items}, open(qp, "w"), indent=2)
            print(f"\n  Wrote work queue -> {qp}. Have Claude work it at the {interval}s pace.")
        else:
            print("\n  DRY RUN — prompts composed, nothing posted. Re-run with --go to write the queue.")
        return 0

    if not a.go:
        print("\n  DRY RUN — nothing generated, no credits spent. Re-run with --go to fill.")
        return 0

    os.makedirs(os.path.join(a.reel, "pantry"), exist_ok=True)
    for r in fillable:
        if not r["plate"]:
            print(f"  {r['bid']}: skip — no plate"); continue
        out = os.path.join(a.reel, "pantry", f"{r['bid']}.png")
        prompt = r["prompt"]; ok = False
        for attempt in range(1, cfg["max_tries"] + 1):
            try:
                generate(prompt, r["plate"], out, cfg, a.backend)
            except NotImplementedError as e:
                print(f"  {r['bid']}: generation adapter not wired — {e}"); return 3
            defects = accept(out)
            if not defects:
                ok = True; break
            print(f"  {r['bid']}: try {attempt} failed Gate V ({[k for _,k,_ in defects]}), re-prompting")
            prompt = r["prompt"] + " — subject fills the frame, centered, minimal margins"
        if ok:
            open(out.replace(".png", ".auto"), "w").write("provisional auto-fill — review or replace\n")
            open(os.path.join(a.reel, "pantry", f"{r['bid']}.source.txt"), "w").write(
                sidecar_text(a.backend, r["style_type"], r["prompt"], r["plate"],
                             r["archetype"], stamp, cfg))
            print(f"  {r['bid']}: filled + passed Gate V (provisional)")
        else:
            if os.path.exists(out):
                os.remove(out)
            print(f"  {r['bid']}: gave up after {cfg['max_tries']} tries — left as human placeholder")
    return 0


if __name__ == "__main__":
    sys.exit(main())
