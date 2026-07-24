#!/usr/bin/env python3
"""
build_hai_fellows.py — batch-build claude-liam explainer reels for HAI Fellows.

Phase 2 of the hai-fellows batch:
  - Reads manifest.json (flat list, 152 candidates)
  - Fixes author attributions (Seth Brown for zip1, Dhruv Patel, Yatra Rawat,
    Nina Harris Co-Founder, UNKNOWN → Nik Bear Brown)
  - For each entry: creates folder, extracts content from HTML, writes
    beat_sheet.json, generates Kokoro audio, renders Remotion beats,
    compiles to .mp4, runs visual QC frame sampling
  - Logs to BUILD-LOG.md; writes SERIES-INDEX.md at end

Flags:
  --dry-run       Parse and plan without generating any files
  --no-audio      Skip Kokoro audio generation
  --no-remotion   Skip remotion_scenes.py render
  --no-compile    Skip compile.py step
  --no-qc         Skip visual QC frame sampling
  --force         Delete and rebuild already-built folders
  --only SLUG     Build only this slug
  --start-at N    Start at 1-based index N

Spec:
  - Liam voice (@NikBearBrown), Kokoro am_onyx, claude palette
  - Teardown register narration
  - "Your turn" B05 READS the prompt aloud + discusses it
  - Remotion scenes rendered: B00 (ClaudeComposerAsk), B05 (Your turn),
    B06 (ClaudeTitleOutro)
  - SLATE beats B01–B04 for content (filled by human or later pipeline)
  - Visual QC: 4 frames sampled after compile → _qc/frames/

Free pipeline: Kokoro am_onyx, no ElevenLabs, no higgsfield, no publishing.
HONESTY: never invent statistics, quotes, or data not present in the article.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import textwrap
import time
import urllib.request
from datetime import datetime
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("pip install beautifulsoup4")

# --- Paths -------------------------------------------------------------------
THIS_FILE   = Path(__file__).resolve()
HAI_DIR     = THIS_FILE.parent                    # brutalist-art/youtube/hai-fellows/
ART_HOME    = THIS_FILE.parents[2]                # brutalist-art/
SCRIPTS     = ART_HOME / "runtime" / "scripts"
SOURCE_ZIP1 = HAI_DIR / "_source" / "zip1" / "posts"
SOURCE_ZIP2 = HAI_DIR / "_source" / "zip2" / "posts"
MANIFEST    = HAI_DIR / "manifest.json"
BUILD_LOG   = HAI_DIR / "BUILD-LOG.md"
SERIES_INDEX = HAI_DIR / "SERIES-INDEX.md"

# --- Greeting lexicon (SKILL.md — one-word only for Liam) -------------------
GREETINGS = [
    "Hola", "Olá", "Bonjour", "Ciao", "Hallo", "Hej", "Hei", "Ahoj",
    "Cześć", "Privet", "Yassou", "Merhaba", "Shalom", "Salaam", "Jambo",
    "Habari", "Sawubona", "Selam", "Namaste", "Vanakkam", "Annyeong",
    "Sawadee", "Halo", "Kumusta", "Aloha", "Talofa", "Bula", "Konnichiwa",
]

# --- Author corrections (source: user instructions + article text) -----------
AUTHOR_CORRECTIONS = {
    # All zip1/Zebonastic articles → Seth Brown, Fellow
    "_zip1_all": ("Seth Brown", "Fellow"),
    # Named corrections from user
    "Dhruv":        ("Dhruv Patel",        "Fellow"),
    "Yatra":        ("Yatra Rawat",        "Fellow"),
    "Nina Harris":  ("Nina Harris",        "Co-Founder"),
    # Full names recovered from article text
    "Anshika":      ("Anshika Khandelwal", "Fellow"),
    "Rithanya":     ("Rithanya Chandran",  "Fellow"),
    # UNKNOWN rows → Nik Bear Brown (Founder) as safe default
    "UNKNOWN":      ("Nik Bear Brown",     "Founder"),
}


def credit_line(author: str, credit_type: str) -> str:
    if credit_type == "Founder":
        return f"{author} — Founder, Humanitarians AI"
    if credit_type == "Co-Founder":
        return f"{author} — Co-Founder, Humanitarians AI"
    return f"{author} — Humanitarians AI Fellow"


def corrected_author(row: dict) -> tuple[str, str]:
    if row.get("source") == "Zebonastic":
        return AUTHOR_CORRECTIONS["_zip1_all"]
    raw = row.get("author", "UNKNOWN")
    if raw in AUTHOR_CORRECTIONS:
        return AUTHOR_CORRECTIONS[raw]
    return raw, row.get("credit_type", "Fellow")


# --- HTML content extraction -------------------------------------------------
def get_source_path(row: dict) -> Path | None:
    src = row.get("source_file", "")
    for d in (SOURCE_ZIP1, SOURCE_ZIP2):
        p = d / src
        if p.exists():
            return p
    return None


def clean(t: str) -> str:
    t = re.sub(r'[​‌‍﻿]', '', t)
    return re.sub(r'\s+', ' ', t).strip()


def split_sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]


def best_sentences(paras: list[str], n: int = 2, max_words: int = 22) -> str:
    """
    Teardown register: pick the n most direct, declarative sentences.
    Prefer: short, specific, active voice, no subordinate clauses.
    """
    scored = []
    for p in paras:
        for sent in split_sentences(p):
            words = sent.split()
            wc = len(words)
            if wc < 5 or wc > 40:
                continue
            score = 0
            # Short = punchy
            score += max(0, 20 - wc) * 2
            # Specific: has a number, proper noun, or named thing
            if re.search(r'\d|\b[A-Z][a-z]+\b', sent):
                score += 10
            # Declarative: doesn't start with If/When/While/Although
            if not re.match(r'^(?:If|When|While|Although|Because|Since|As |Despite)', sent):
                score += 8
            # Avoid boilerplate phrases
            if any(ph in sent.lower() for ph in [
                "subscribe", "thanks for", "click here", "in conclusion",
                "in this article", "in this post", "we will", "we are going"
            ]):
                score -= 50
            scored.append((score, sent))

    scored.sort(key=lambda x: -x[0])
    picked = [s for _, s in scored[:n]]
    return " ".join(picked)


def extract_paragraphs(html_path: Path) -> list[str]:
    html = html_path.read_text(errors="replace")
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(["nav", "footer", "aside"]):
        tag.decompose()
    paras = []
    for p in soup.find_all("p"):
        t = clean(p.get_text())
        if len(t) < 45:
            continue
        if any(kw in t.lower() for kw in [
            "subscribe for free", "thanks for reading",
            "subscribe to receive", "share this post",
            "unsubscribe", "manage your subscription",
        ]):
            continue
        paras.append(t)
    return paras


def extract_numbers(paras: list[str]) -> list[str]:
    stats = []
    for p in paras:
        for sent in split_sentences(p):
            if re.search(r'\$\d|\d+%|\b\d{2,}\s+(?:million|billion|thousand|percent|hours|days|weeks|years|people|users|applications)', sent, re.I):
                stats.append(sent.strip())
    return stats[:8]


def teardown_beats(paras: list[str]) -> dict:
    """
    Extract content for each beat in Teardown register.
    Teardown: mechanism first, then verdict. Short sentences. Specific nouns.
    """
    if not paras:
        empty = ""
        return dict(hook=empty, context=empty, claim=empty, evidence=empty)

    # Hook: first para's best punchy sentence
    hook_sents = split_sentences(paras[0])
    hook = hook_sents[0][:200] if hook_sents else paras[0][:200]
    # Truncate hook to one complete sentence
    for ch in '.!?':
        i = hook.find(ch)
        if 15 < i < 180:
            hook = hook[:i + 1]
            break

    # Context (B01): 2nd-3rd para best sentences
    context = best_sentences(paras[1:4], n=2)

    # Claim (B02): strongest declarative sentence from mid-article
    mid = len(paras) // 2
    claim_pool = paras[max(0, mid - 2):mid + 3]
    claim = best_sentences(claim_pool, n=2)

    # Evidence (B03): para with most specifics (numbers, names, tools)
    evidence = ""
    best_ev_score = -1
    for p in paras[2:]:
        score = sum([
            bool(re.search(r'\$\d|\d+%|\b\d{2,}\b', p)) * 10,
            bool(re.search(r'\bbuilt\b|\bcreated\b|\bdeveloped\b|\bimplemented\b', p, re.I)) * 6,
            bool(re.search(r'\bfor example\b|\bspecifically\b|\bin practice\b', p, re.I)) * 4,
        ])
        if score > best_ev_score:
            best_ev_score = score
            evidence = best_sentences([p], n=2)

    return dict(hook=hook, context=context, claim=claim, evidence=evidence)


# --- Beat authoring ----------------------------------------------------------
def greeting_for(index: int) -> str:
    return GREETINGS[index % len(GREETINGS)]


def make_b00_output(row: dict, paras: list[str]) -> list[str]:
    concept = row.get("concept", "")
    lines = []
    for m in re.finditer(
        r'(?:SECTION|CHAPTER|PART|CLAIM|IDEA)\s*\d*[:\.]?\s*([^\n|]{15,65})',
        concept, re.I
    ):
        candidate = m.group(1).strip().rstrip('.')
        if len(candidate) > 15:
            lines.append(candidate)
        if len(lines) >= 3:
            break

    if len(lines) < 3:
        for p in paras[:8]:
            for sent in split_sentences(p):
                words = sent.split()
                if 4 < len(words) < 14 and not any(
                    kw in sent.lower() for kw in ["subscribe", "thanks"]
                ):
                    candidate = sent.rstrip('.!?')
                    lines.append(candidate[:65])
                    break
            if len(lines) >= 3:
                break

    while len(lines) < 3:
        lines.append("…")

    return [l[:70] for l in lines[:3]]


def make_handoff_prompt(row: dict, paras: list[str]) -> str:
    """Concise, specific prompt the viewer can paste into Claude."""
    title = row["title"]
    kind  = row.get("kind", "")
    author, _ = corrected_author(row)

    prompts = {
        "book-review": (
            f"I'm building a [game / tool / system]. "
            f"Extract the three most surprising design decisions from {title} "
            f"and tell me one thing I should do differently because of each."
        ),
        "tutorial": (
            f"Walk me through the simplest version of the technique from "
            f"'{title}'. Give me the code or steps, then tell me where it fails."
        ),
        "how-to": (
            f"I want to build what the article '{title}' describes. "
            f"Give me a ten-line starting point, then name the first thing I'll break."
        ),
        "research": (
            f"What's the strongest objection to the central claim in '{title}'? "
            f"State it, then tell me what evidence would change your mind."
        ),
        "project": (
            f"I'm replicating the project from '{title}'. "
            f"What's the hardest part I'll hit and how do I get past it?"
        ),
    }

    base = prompts.get(kind, (
        f"Take the central idea from '{title}' and give me the three most "
        f"actionable takeaways — one sentence each. Then name the failure mode "
        f"I'm most likely to hit."
    ))
    return base


def make_b05_narration(handoff_prompt: str) -> str:
    """B05 reads the prompt aloud and discusses it — HANDOFF LAW."""
    # Make prompt speech-friendly (no markdown, reasonable length)
    prompt_clean = re.sub(r'\s+', ' ', handoff_prompt).strip()
    # Trim to ~120 chars so it reads cleanly in narration
    if len(prompt_clean) > 130:
        cut = prompt_clean[:130].rfind(' ')
        prompt_clean = prompt_clean[:cut] + "…"
    return (
        f"Your turn. Paste this into Claude — "
        f"{prompt_clean} "
        f"That's the prompt that actually tests whether you got it. "
        f"Run it and see where it surprises you."
    )


PROGRAM_BEAT_TEXT = (
    "Humanitarians AI is an educational bridge program where Fellows learn "
    "experiential AI by doing AI — building real projects and shipping real research."
)


def make_beat_sheet(row: dict, index: int, paras: list[str]) -> dict:
    slug   = row["slug"]
    title  = row["title"]
    author, credit_type = corrected_author(row)
    credit = credit_line(author, credit_type)
    greeting = greeting_for(index)
    beats_content = teardown_beats(paras)
    handoff_prompt = make_handoff_prompt(row, paras)

    # B00 — cold open, "This is Liam, in for Bear."
    hook = beats_content["hook"]
    b00_narration = (
        f"This is Liam — in for Bear. "
        f"{hook} "
        f"One idea. Let's see if it holds."
    )

    # B01 — context
    b01_narration = beats_content["context"] or hook

    # B02 — claim
    b02_narration = beats_content["claim"] or beats_content["context"]

    # B03 — evidence
    b03_narration = beats_content["evidence"] or beats_content["claim"]

    # B04 — program beat + credit (Teardown: concise, punchy)
    b04_narration = (
        f"Written by {credit}. "
        f"{PROGRAM_BEAT_TEXT}"
    )

    # B05 — handoff: reads the prompt, discusses it
    b05_narration = make_b05_narration(handoff_prompt)

    # B06 — outro
    title_period = title.rstrip()
    if not title_period.endswith(('.', '?', '!')):
        title_period += "."
    b06_narration = (
        f"{title}. Subscribe if this saved you a read. Liam, in for Bear."
    )

    # ClaudeComposerAsk props
    kind_map = {
        "book-review": "GAME DESIGN",
        "tutorial": "HAI · TUTORIAL",
        "how-to": "HAI · HOW-TO",
        "research": "HAI · RESEARCH",
        "analysis": "HAI · ANALYSIS",
        "opinion": "HAI · PERSPECTIVE",
        "project": "HAI · PROJECT",
        "introduction": "HAI · INTRO",
        "explainer": "HAI · EXPLAINER",
        "essay": "HAI · ESSAY",
    }
    topic   = kind_map.get(row.get("kind", ""), "HUMANITARIANS AI")
    b00_out = make_b00_output(row, paras)
    b00_cmd = f"distill the one idea from: {title[:58]}"

    return {
        "metadata": {
            "title": title,
            "slug": slug,
            "topic": topic,
            "register": "Teardown",
            "audience": "HAI Fellows",
            "brand": "claude",
            "channel": "claude-liam",
            "engine": "kokoro",
            "voice_kokoro": "am_onyx",
            "palette": "claude",
            "style_preset": "claude",
            "ground": "#FAF9F5",
            "color_semantics": "claude fidelity: INK #3D3929; SPARK #D97757 one accent.",
            "folderLabel": "@NikBearBrown",
            "author": author,
            "credit_type": credit_type,
            "credit_line": credit,
            "source": row.get("source", ""),
            "source_file": row.get("source_file", ""),
            "kind": row.get("kind", ""),
            "greeting": f"{greeting}, Liam",
            "tags": ["Humanitarians AI", "HAI Fellows", author, title[:40]],
            "note": (
                f"HAI Fellows batch v2 — Teardown register, @NikBearBrown, "
                f"Remotion animated bookends. Credit: {credit}. "
                f"HONESTY: all numbers trace to source article."
            ),
        },
        "beats": [
            {
                "beat_id": "B00",
                "act": "ASK",
                "narration_text": b00_narration,
                "shot": {
                    "type": "GRAPHIC",
                    "source": "remotion",
                    "motion": "type-on",
                    "remotion": {
                        "pattern": "ClaudeComposerAsk",
                        "props": {
                            "greeting": f"{greeting}, Liam",
                            "topic": topic,
                            "segment": title[:52],
                            "command": b00_cmd,
                            "runningText": "reading the article…",
                            "folderLabel": "@NikBearBrown",
                            "output": b00_out,
                        },
                    },
                },
                "estimated_duration_s": 20.0,
            },
            {
                "beat_id": "B01",
                "act": "CONTEXT",
                "narration_text": b01_narration,
                "shot": {
                    "type": "SLATE",
                    "source": "pipeline",
                    "sparkLine": "Context.",
                    "needs": "PIPELINE → fill media/B01.mp4",
                },
                "estimated_duration_s": 30.0,
            },
            {
                "beat_id": "B02",
                "act": "CLAIM",
                "narration_text": b02_narration,
                "shot": {
                    "type": "SLATE",
                    "source": "pipeline",
                    "sparkLine": "The claim.",
                    "needs": "PIPELINE → fill media/B02.mp4",
                },
                "estimated_duration_s": 30.0,
            },
            {
                "beat_id": "B03",
                "act": "EVIDENCE",
                "narration_text": b03_narration,
                "shot": {
                    "type": "SLATE",
                    "source": "pipeline",
                    "sparkLine": "Evidence.",
                    "needs": "PIPELINE → fill media/B03.mp4",
                },
                "estimated_duration_s": 30.0,
            },
            {
                "beat_id": "B04",
                "act": "PROGRAM",
                "narration_text": b04_narration,
                "shot": {
                    "type": "SLATE",
                    "source": "pipeline",
                    "sparkLine": "Humanitarians AI.",
                    "needs": "PIPELINE → fill media/B04.mp4",
                },
                "estimated_duration_s": 22.0,
            },
            {
                "beat_id": "B05",
                "act": "HANDOFF",
                "narration_text": b05_narration,
                "shot": {
                    "type": "GRAPHIC",
                    "source": "remotion",
                    "motion": "type-on",
                    "remotion": {
                        "pattern": "ClaudeComposerAsk",
                        "props": {
                            "greeting": "Your turn.",
                            "topic": topic,
                            "segment": title[:52],
                            "command": handoff_prompt[:200],
                            "runningText": "paste this into Claude…",
                            "folderLabel": "@NikBearBrown",
                        },
                    },
                },
                "estimated_duration_s": 20.0,
            },
            {
                "beat_id": "B06",
                "act": "OUTRO",
                "narration_text": b06_narration,
                "shot": {
                    "type": "GRAPHIC",
                    "source": "remotion",
                    "motion": "fade",
                    "remotion": {
                        "pattern": "ClaudeTitleOutro",
                        "props": {
                            "title": title_period,
                            "handle": "@NikBearBrown",
                            "subline": "Liam, in for Bear.",
                        },
                    },
                },
                "estimated_duration_s": 5.0,
            },
        ],
    }


# --- SOURCES.md --------------------------------------------------------------
def write_sources(reel_dir: Path, row: dict, paras: list[str], html_path: Path):
    author, credit_type = corrected_author(row)
    stats = extract_numbers(paras)
    lines = [
        f"# SOURCES — {row['title']}",
        "",
        f"**Source file:** `{row.get('source_file', '?')}`  ",
        f"**Publication:** {row.get('source', '')}  ",
        f"**Author:** {credit_line(author, credit_type)}  ",
        "",
        "## Statistics cited on-screen (all trace to this article, none invented)",
        "",
    ]
    lines += [f"- {s}" for s in stats] or ["- (no statistics detected in article)"]
    lines += [
        "",
        "## Source file",
        "",
        f"`{html_path.name}`",
        "",
        f"_Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}_",
    ]
    (reel_dir / "SOURCES.md").write_text("\n".join(lines) + "\n")


# --- BUILD-PROMPT.md ---------------------------------------------------------
def write_build_prompt(reel_dir: Path, slug: str):
    (reel_dir / "BUILD-PROMPT.md").write_text(textwrap.dedent(f"""\
    # BUILD PROMPT — {slug}

    Paste this into Claude Code (from `books/`) to build the final cut:

    ```bash
    python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \\
        brutalist-art/youtube/hai-fellows/{slug} --no-gate
    python3 brutalist-art/runtime/scripts/remotion_scenes.py \\
        brutalist-art/youtube/hai-fellows/{slug}
    python3 brutalist-art/runtime/scripts/compile.py \\
        brutalist-art/youtube/hai-fellows/{slug} --review
    python3 brutalist-art/runtime/scripts/compile.py \\
        brutalist-art/youtube/hai-fellows/{slug}
    ```

    Free pipeline only. Do not publish.
    Review cut: `brutalist-art/youtube/hai-fellows/{slug}/{slug}-slate.mp4`
    """))


# --- Image download (non-blocking) ------------------------------------------
def download_images(row: dict, reel_dir: Path):
    urls = row.get("image_urls", [])
    if not urls:
        return
    pantry = reel_dir / "pantry"
    pantry.mkdir(exist_ok=True)
    for i, url in enumerate(urls[:5]):
        try:
            ext = url.split("?")[0].split(".")[-1][:5] or "jpg"
            dest = pantry / f"image_{i:02d}.{ext}"
            if dest.exists():
                continue
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=12) as resp:
                dest.write_bytes(resp.read())
        except Exception:
            pass


# --- Visual QC frame sampling ------------------------------------------------
FFMPEG = shutil.which("ffmpeg") or "ffmpeg"

def run_qc(reel_dir: Path, slug: str):
    """
    Sample 4 frames spread across the review cut → _qc/frames/.
    Light automated check: resolution, file-size proxy for blank frames.
    Human reviews the frames for layout defects (edge bleed, overflow, overlap).
    Full pixel-level audit prompt: skills/make/ai-explainer/SKILL.md §QC.
    """
    review_mp4 = reel_dir / f"{slug}-slate.mp4"
    if not review_mp4.exists():
        return
    qc_dir = reel_dir / "_qc" / "frames"
    qc_dir.mkdir(parents=True, exist_ok=True)

    # Probe duration
    r = subprocess.run(
        [FFMPEG, "-i", str(review_mp4)],
        capture_output=True, text=True
    )
    dur_match = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", r.stderr)
    dur_s = 30.0
    if dur_match:
        h, m, s = dur_match.groups()
        dur_s = int(h) * 3600 + int(m) * 60 + float(s)

    # Sample 4 evenly-spaced frames
    offsets = [dur_s * f for f in (0.1, 0.35, 0.65, 0.9)]
    issues = []
    for i, t in enumerate(offsets):
        out_png = qc_dir / f"frame_{i:02d}_{t:.1f}s.png"
        subprocess.run(
            [FFMPEG, "-ss", str(t), "-i", str(review_mp4),
             "-vframes", "1", "-q:v", "2", str(out_png), "-y"],
            capture_output=True
        )
        if out_png.exists():
            sz = out_png.stat().st_size
            # A frame under 5KB is probably blank/black — flag it
            if sz < 5000:
                issues.append(f"frame_{i:02d}: suspiciously small ({sz}B) at t={t:.1f}s")

    # Write minimal QC report
    report_lines = [
        f"# QC — {slug}",
        f"",
        f"Review cut: `{review_mp4.name}`  Duration: {dur_s:.1f}s",
        f"Frames sampled: {len(offsets)} (at {', '.join(f'{t:.1f}s' for t in offsets)})",
        f"",
        "## Automated checks",
        "",
    ]
    if issues:
        report_lines += [f"- WARN: {i}" for i in issues]
    else:
        report_lines.append("- All sampled frames non-blank ✓")

    report_lines += [
        "",
        "## Human review checklist",
        "",
        "Open each frame in `_qc/frames/` and check:",
        "1. No text touching or crossing frame borders (x<0, x>1920, y<0, y>1080)",
        "2. All essential text inside 5% safe area (x 96–1824, y 54–1026)",
        "3. No text overflowing its box or clipped behind a shape",
        "4. No overlapping/colliding elements",
        "5. @NikBearBrown chip inside safe area, not covering content",
        "6. Contrast legible at normal viewing distance",
        "",
        f"_Auto-generated {datetime.now().strftime('%Y-%m-%d %H:%M')}_",
    ]
    (reel_dir / "_qc" / "REPORT.md").write_text("\n".join(report_lines) + "\n")


# --- Subprocess runner -------------------------------------------------------
def run(cmd, timeout=600, env=None):
    r = subprocess.run(
        cmd, capture_output=True, text=True,
        timeout=timeout, env=env or os.environ.copy()
    )
    return r.returncode, (r.stdout + "\n" + r.stderr).strip()


# --- Log helpers -------------------------------------------------------------
def init_log():
    if not BUILD_LOG.exists():
        BUILD_LOG.write_text(
            "# HAI Fellows Build Log\n\n"
            "| # | Slug | Author | Status | MP4 | Note |\n"
            "|---|------|--------|--------|-----|------|\n"
        )


def append_log(n: int, slug: str, author: str, status: str, mp4: str, note: str):
    with open(BUILD_LOG, "a") as f:
        f.write(f"| {n} | `{slug}` | {author} | {status} | `{mp4}` | {note} |\n")


# --- Build one video ---------------------------------------------------------
def build_one(
    n: int, row: dict,
    dry_run: bool, no_audio: bool, no_remotion: bool,
    no_compile: bool, no_qc: bool, force: bool
) -> str:
    slug  = row["slug"]
    title = row["title"]
    author, credit_type = corrected_author(row)

    reel_dir   = HAI_DIR / slug
    review_mp4 = reel_dir / f"{slug}-slate.mp4"
    final_mp4  = reel_dir / f"{slug}.mp4"

    # Skip or force
    if not force:
        if (review_mp4.exists() and review_mp4.stat().st_size > 50_000) or \
           (final_mp4.exists()  and final_mp4.stat().st_size  > 50_000):
            sz = (review_mp4 if review_mp4.exists() else final_mp4).stat().st_size
            note = f"already built ({sz // 1024}KB)"
            print(f"[{n:03d}] SKIP  {slug}  ({note})", flush=True)
            append_log(n, slug, author, "SKIP", str(review_mp4.relative_to(HAI_DIR)), note)
            return "SKIP"
    elif reel_dir.exists():
        shutil.rmtree(reel_dir)
        print(f"[{n:03d}] FORCE  cleared {slug}", flush=True)

    print(f"\n{'='*65}", flush=True)
    print(f"[{n:03d}] START  {slug}", flush=True)
    print(f"       {credit_line(author, credit_type)}", flush=True)

    env = os.environ.copy()
    env["ART_HOME"] = str(ART_HOME)

    try:
        html_path = get_source_path(row)
        if html_path is None:
            raise RuntimeError(f"Source HTML not found: {row.get('source_file', '?')}")

        paras = extract_paragraphs(html_path)
        if not paras:
            raise RuntimeError("No paragraphs extracted from HTML")

        if dry_run:
            print(f"[{n:03d}] DRY-RUN  {slug}  ({len(paras)} paras)", flush=True)
            return "DRY-RUN"

        # Scaffold
        reel_dir.mkdir(parents=True, exist_ok=True)
        (reel_dir / "media").mkdir(exist_ok=True)
        (reel_dir / "mp3").mkdir(exist_ok=True)

        bs = make_beat_sheet(row, n, paras)
        (reel_dir / "beat_sheet.json").write_text(
            json.dumps(bs, indent=2, ensure_ascii=False)
        )
        print(f"[{n:03d}] beat_sheet written ({len(bs['beats'])} beats, Teardown, @NikBearBrown)", flush=True)

        write_sources(reel_dir, row, paras, html_path)
        write_build_prompt(reel_dir, slug)
        download_images(row, reel_dir)

        # Audio (Kokoro am_onyx)
        if not no_audio:
            print(f"[{n:03d}] Kokoro am_onyx audio…", flush=True)
            rc, out = run(
                ["python3", str(SCRIPTS / "generate_audio_kokoro.py"),
                 str(reel_dir), "--no-gate"],
                timeout=600, env=env,
            )
            if rc != 0:
                raise RuntimeError(f"audio failed:\n{out[-600:]}")
            print(f"[{n:03d}] audio done", flush=True)

        # Remotion — render B00/B05/B06 (ClaudeComposerAsk + ClaudeTitleOutro)
        if not no_remotion:
            print(f"[{n:03d}] rendering Remotion beats (B00/B05/B06)…", flush=True)
            rc, out = run(
                ["python3", str(SCRIPTS / "remotion_scenes.py"), str(reel_dir)],
                timeout=900, env=env,
            )
            if rc != 0:
                print(f"[{n:03d}] WARN remotion soft-fail — bookends stay slates: "
                      f"{out[-200:]}", flush=True, file=sys.stderr)
            else:
                print(f"[{n:03d}] Remotion done", flush=True)

        # Compile review cut
        if not no_compile:
            print(f"[{n:03d}] compiling review cut…", flush=True)
            rc, out = run(
                ["python3", str(SCRIPTS / "compile.py"),
                 str(reel_dir), "--review"],
                timeout=600, env=env,
            )
            if rc != 0:
                raise RuntimeError(f"compile (review) failed:\n{out[-600:]}")

            # Final cut (soft-fail if slates remain)
            run(["python3", str(SCRIPTS / "compile.py"), str(reel_dir)],
                timeout=600, env=env)

        # Visual QC frame sampling
        if not no_qc and not no_compile:
            try:
                run_qc(reel_dir, slug)
                print(f"[{n:03d}] QC frames written → _qc/frames/", flush=True)
            except Exception as qc_err:
                print(f"[{n:03d}] QC warn: {qc_err}", flush=True, file=sys.stderr)

        # Verify
        mp4 = review_mp4 if review_mp4.exists() else final_mp4
        if not no_compile and not mp4.exists():
            raise RuntimeError(f"MP4 not found after compile: {review_mp4}")

        sz = mp4.stat().st_size // 1024 if mp4.exists() else 0
        note = f"{sz}KB"
        print(f"[{n:03d}] DONE  {slug}  ({note})", flush=True)
        append_log(n, slug, author, "BUILT",
                   str(mp4.relative_to(HAI_DIR)) if mp4.exists() else "-", note)
        return "BUILT"

    except Exception as e:
        msg = str(e)[:200]
        print(f"[{n:03d}] FAIL  {slug}  {msg}", flush=True, file=sys.stderr)
        append_log(n, slug, author, "FAIL", "-", msg)
        return "FAIL"


# --- SERIES-INDEX.md ---------------------------------------------------------
def write_series_index(rows: list[dict], results: list[tuple]):
    built  = sum(1 for _, s in results if s in ("BUILT", "SKIP"))
    failed = sum(1 for _, s in results if s == "FAIL")
    lines = [
        "# HAI Fellows Explainer Series — Index",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}  "
        f"Built: {built} | Failed: {failed} | Total: {len(rows)}",
        "",
        "| # | Title | Credit | Kind | Slug | Status |",
        "|---|-------|--------|------|------|--------|",
    ]
    for (n, row), (_, status) in zip(enumerate(rows, 1), results):
        author, ct = corrected_author(row)
        credit = credit_line(author, ct)
        lines.append(
            f"| {n} | {row['title'][:55]} | {credit[:48]} "
            f"| {row.get('kind', '')} | `{row['slug'][:42]}` | {status} |"
        )
    SERIES_INDEX.write_text("\n".join(lines) + "\n")
    print(f"\nSERIES-INDEX.md → {SERIES_INDEX}", flush=True)


# --- Fix manifest (bakes author corrections) ---------------------------------
def fix_manifest(data: list[dict]) -> list[dict]:
    for row in data:
        row["author"], row["credit_type"] = corrected_author(row)
    return data


# --- Main --------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run",    action="store_true")
    ap.add_argument("--no-audio",   action="store_true")
    ap.add_argument("--no-remotion",action="store_true")
    ap.add_argument("--no-compile", action="store_true")
    ap.add_argument("--no-qc",      action="store_true")
    ap.add_argument("--force",      action="store_true",
                    help="Delete and rebuild already-built folders")
    ap.add_argument("--only",       metavar="SLUG")
    ap.add_argument("--start-at",   type=int, default=1)
    args = ap.parse_args()

    with open(MANIFEST) as f:
        data = json.load(f)
    data = fix_manifest(data)

    if not args.dry_run:
        MANIFEST.write_text(json.dumps(data, indent=2, ensure_ascii=False))
        print(f"[fix] manifest.json updated ({len(data)} rows, author corrections baked)",
              flush=True)

    if args.only:
        rows = [r for r in data if r["slug"] == args.only]
        if not rows:
            sys.exit(f"Slug not found: {args.only}")
    else:
        rows = data[args.start_at - 1:]

    init_log()
    print(f"\n{'='*65}", flush=True)
    print(f"HAI Fellows batch — {len(rows)} videos", flush=True)
    print(f"  brand: claude-liam | voice: am_onyx | logo: @NikBearBrown", flush=True)
    print(f"  register: Teardown | Your-turn reads prompt", flush=True)
    if args.dry_run:
        print("  DRY-RUN — no files written", flush=True)
    if args.force:
        print("  --force — rebuilding all", flush=True)
    print(f"{'='*65}\n", flush=True)

    results = []
    t0 = time.time()
    for i, row in enumerate(rows):
        n = i + args.start_at
        status = build_one(
            n, row,
            dry_run=args.dry_run,
            no_audio=args.no_audio,
            no_remotion=args.no_remotion,
            no_compile=args.no_compile,
            no_qc=args.no_qc,
            force=args.force,
        )
        results.append((n, status))

    elapsed = time.time() - t0
    built   = sum(1 for _, s in results if s == "BUILT")
    skipped = sum(1 for _, s in results if s == "SKIP")
    failed  = sum(1 for _, s in results if s == "FAIL")

    print(f"\n{'='*65}", flush=True)
    print(f"DONE — {built} built, {skipped} skipped, {failed} failed  "
          f"({elapsed / 60:.1f} min)", flush=True)
    print(f"{'='*65}", flush=True)

    if not args.dry_run and not args.only:
        write_series_index(data, results)

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
