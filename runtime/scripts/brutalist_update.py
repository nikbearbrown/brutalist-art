#!/usr/bin/env python3
"""brutalist_update.py — flip a beat sheet to the Brutalist standard.

Steps:
  1. Back up beat_sheet.json → beat_sheet.pre-brutalist.json
  2. Flip metadata: style_preset = nikbearbrown, palette = teardown
  3. Prepend B00 (BrutalistTerminalOpen — terminal open with checklist)
  4. Insert B00B at index 1 (BrutalistAdaptCLI — "the labels are how you adapt it")
  5. Append B99 (BrutalistCommentCTA — brutalist.art CTA)
  6. Set metadata["keep_review_labels"] = true
  7. Join metadata from YouTube.json if provided

Usage (from books/):
  python3 runtime/scripts/brutalist_update.py \\
    --sheet cancer-biology/youtube/apoptosis-resistance/beat_sheet.json \\
    --folder cancer-biology \\
    --youtube-json YouTube.json \\
    --apply [--force]
"""
import argparse, hashlib, json, shutil, sys
from pathlib import Path

TEARDOWN_META = {
    "style_preset": "nikbearbrown",
    "ground": "#FFFFFF",
    "accents": {
        "data": ["#C8102E"],
        "annotation": "#C8102E",
        "highlighter": "#F6D8DC",
    },
    "color_semantics": (
        "TEARDOWN: flat white #FFFFFF / ink #2A1A0E / one red #C8102E. "
        "Good/kept = plain ink (label + position carry it). Red = the ONE accent."
    ),
}

CHECKLIST = [
    "✓ palette   teardown  #FFFFFF/#2A1A0E/#C8102E",
    "✓ B00       BrutalistTerminalOpen",
    "✓ B00B      BrutalistAdaptCLI",
    "✓ B99       BrutalistCommentCTA → brutalist.art",
    "✓ voice     NikBearBrown",
    "✓ masters   16:9 + 9:16",
    "✓ labels    keep_review_labels",
    "✓ gate      PASS",
]

# B00 narration — "you're watching a template". [title] = full title, [topic] = topic.title()
B00_NARRATIONS = {
    "A": (
        "This is an educational A-I template for you to create explainer videos"
        " — this one, {title}, for {topic}."
    ),
    "B": (
        "This is an educational A-I template for making {topic} explainers."
        " This one is {title}."
    ),
    "C": (
        "You're watching an educational A-I template — an explainer on {title},"
        " built so you can remake it for anything in {topic}."
    ),
    "D": (
        "This is a Brutalist template for creating your own explainer videos"
        " on {topic}. This one is {title}."
    ),
}

# B00B narration — "the labels are how you adapt it". No title/topic substitution.
B00B_NARRATIONS = {
    "A": (
        "See the little label in the corner of each beat — B00, B04, and so on?"
        " That tag is how you adapt it: point a command-line tool like Claude Code"
        " at a label to swap, add, or delete that beat."
    ),
    "B": (
        "Those labels on each beat aren't clutter — they're handles."
        " Tell a command-line tool like Claude Code to change beat B04"
        " — swap it, rewrite it, cut it — and it does. Audience and language too."
    ),
    "C": (
        "Every beat is tagged in the corner. Those tags let you name a beat"
        " to a command-line tool like Claude Code, and it'll swap, add, or delete it"
        " — or re-cut the whole thing for a new audience."
    ),
    "D": (
        "Keep an eye on the label on each beat. It names the block, so a"
        " command-line tool like Claude Code can change exactly that one"
        " — swap it, add one, or delete it."
    ),
}

# B00B screen lines — fixed across all variants
B00B_LINES = [
    "# every beat is tagged →  B00  B04  B12 …",
    '$ claude "swap B04 for a 9:16 diagram"',
    '$ claude "rewrite B07 for high-schoolers"',
]

# B99 code — fixed screen across all variants
B99_CODE = (
    "// want to make your own?\n"
    "// every template + the brutalist CLI\n"
    "// → brutalist.art\n"
)

# B99 narration — "make your own → brutalist.art". [topic] = topic.title()
B99_NARRATIONS = {
    "A": (
        "Want to make your own? Every template and the Brutalist tool live"
        " at brutalist dot art. Make your take on {topic}."
    ),
    "B": (
        "If you want to try it, every template and the Brutalist C-L-I are"
        " at brutalist dot art. Make your own {topic} explainer."
    ),
    "C": (
        "Find every template and the Brutalist tool at brutalist dot art"
        " — then make your own take on {topic}."
    ),
    "D": (
        "Everything's at brutalist dot art — the templates and the Brutalist C-L-I."
        " Go make your own {topic} explainer."
    ),
}


def slug_variant(slug: str) -> str:
    h = int(hashlib.sha1(slug.encode()).hexdigest(), 16)
    return "ABCD"[h % 4]


def shorten_title(title: str, max_chars: int = 62) -> str:
    """Trim to fit BrutalistTerminalOpen command line (16:9 baseline ≈ 90 col total).
    prefix 'brutalist explainer-video "' = 27 chars + closing '"' = 1 → leaves 62 for title."""
    if len(title) <= max_chars:
        return title
    return title[: max_chars - 1] + "…"


def build_b00(title: str, topic: str, variant: str) -> dict:
    short_title = shorten_title(title)
    cmd = f'brutalist explainer-video "{short_title}"'
    narration = B00_NARRATIONS[variant].format(
        title=title,
        topic=topic.title(),
    )
    return {
        "beat_id": "B00",
        "act": "INTRO",
        "narration_text": narration,
        "shot": {
            "type": "GRAPHIC",
            "source": "remotion",
            "motion": "fade",
            "remotion": {
                "pattern": "BrutalistTerminalOpen",
                "provenance": "proven-core/BrutalistTerminalOpen",
                "version": "1",
                "props": {
                    "command": cmd,
                    "checklist": CHECKLIST,
                    "topic": topic,
                },
                "rendered": {"out": "media/B00.mp4", "at": ""},
            },
        },
        "estimated_duration_s": 12.0,
        "audio_file": "mp3/beat-B00.mp3",
    }


def build_b00b(topic: str, variant: str) -> dict:
    narration = B00B_NARRATIONS[variant]
    return {
        "beat_id": "B00B",
        "act": "INTRO",
        "narration_text": narration,
        "shot": {
            "type": "GRAPHIC",
            "source": "remotion",
            "motion": "fade",
            "remotion": {
                "pattern": "BrutalistAdaptCLI",
                "provenance": "proven-core/BrutalistAdaptCLI",
                "version": "1",
                "props": {
                    "lines": B00B_LINES,
                    "topic": topic,
                },
                "rendered": {"out": "media/B00B.mp4", "at": ""},
            },
        },
        "estimated_duration_s": 12.0,
        "audio_file": "mp3/beat-B00B.mp3",
    }


def build_b99(slug: str, topic: str, variant: str) -> dict:
    narration = B99_NARRATIONS[variant].format(topic=topic.title())
    return {
        "beat_id": "B99",
        "act": "CTA",
        "narration_text": narration,
        "shot": {
            "type": "GRAPHIC",
            "source": "remotion",
            "motion": "fade",
            "remotion": {
                "pattern": "BrutalistCommentCTA",
                "provenance": "proven-core/BrutalistCommentCTA",
                "version": "1",
                "props": {
                    "filename": "onda.ts",
                    "code": B99_CODE,
                    "variant": variant,
                    "topic": topic,
                },
                "rendered": {"out": "media/B99.mp4", "at": ""},
            },
        },
        "estimated_duration_s": 5.0,
        "audio_file": "mp3/beat-B99.mp3",
    }


def main():
    ap = argparse.ArgumentParser(
        description="Flip a beat sheet to the Brutalist standard."
    )
    ap.add_argument("--sheet", required=True, type=Path,
                    help="Path to beat_sheet.json")
    ap.add_argument("--folder", default="",
                    help="Book folder name (for YouTube.json lookup)")
    ap.add_argument("--youtube-json", type=Path,
                    help="Path to YouTube.json for metadata join")
    ap.add_argument("--apply", action="store_true",
                    help="Write changes (default: dry-run)")
    ap.add_argument("--force", action="store_true",
                    help="Re-apply even if already brutalist-updated")
    a = ap.parse_args()

    sheet_path = a.sheet.resolve()
    if not sheet_path.exists():
        sys.exit(f"[err] no beat_sheet.json at {sheet_path}")

    sheet = json.loads(sheet_path.read_text())
    meta = sheet["metadata"]
    slug = meta.get("slug", sheet_path.parent.name)
    title = meta.get("title", slug)
    topic = meta.get("topic", "TOPIC")
    variant = slug_variant(slug)

    # Remove superseded B97/B98 if present
    beats = sheet["beats"]
    removed = [b["beat_id"] for b in beats if b["beat_id"] in ("B97", "B98")]
    if removed:
        beats[:] = [b for b in beats if b["beat_id"] not in ("B97", "B98")]
        print(f"[brutalist] removed superseded beats: {', '.join(removed)}")

    # Idempotency guard
    already_done = (
        meta.get("style_preset") in ("nikbearbrown", "brutalist-teardown")
        and any(b["beat_id"] == "B00" for b in beats)
        and any(b["beat_id"] == "B00B" for b in beats)
    )
    if already_done and not a.force:
        print("[brutalist] already updated — skipping (--force to re-apply)")
        return

    print(f"[brutalist] slug:    {slug}")
    print(f"[brutalist] title:   {title[:70]}")
    print(f"[brutalist] topic:   {topic}")
    print(f"[brutalist] variant: {variant}  (CTA A/B/C/D by sha1(slug) % 4)")

    b00 = build_b00(title, topic, variant)
    b00b = build_b00b(topic, variant)
    b99 = build_b99(slug, topic, variant)

    if not a.apply:
        print("[brutalist] DRY RUN — pass --apply to write")
        print(f"  B00 command:   {b00['shot']['remotion']['props']['command'][:80]}")
        print(f"  B00 narration: {b00['narration_text'][:80]}")
        print(f"  B00B narration: {b00b['narration_text'][:80]}")
        print(f"  B99 narration: {b99['narration_text']}")
        print(f"  B99 code:\n" + "\n".join(
            "    " + l for l in B99_CODE.splitlines()
        ))
        return

    # Backup
    backup = sheet_path.with_name("beat_sheet.pre-brutalist.json")
    shutil.copy2(sheet_path, backup)
    print(f"[brutalist] backed up → {backup.name}")

    # Flip metadata
    meta["style_preset"] = TEARDOWN_META["style_preset"]
    meta["ground"] = TEARDOWN_META["ground"]
    meta["accents"] = TEARDOWN_META["accents"]
    meta["color_semantics"] = TEARDOWN_META["color_semantics"]
    meta["keep_review_labels"] = True

    # Join YouTube.json
    if a.youtube_json:
        yt_path = Path(a.youtube_json).resolve()
        if yt_path.exists():
            yt = json.loads(yt_path.read_text())
            if isinstance(yt, list):
                yt_entry = next(
                    (r for r in yt if r.get("slug") == slug
                     or r.get("folder") == a.folder),
                    {},
                )
            else:
                yt_entry = yt.get(slug) or yt.get(f"{a.folder}/{slug}") or {}
            if yt_entry:
                meta["youtube"] = yt_entry
                print(f"[brutalist] joined YouTube.json entry for {slug}")
            else:
                print(f"[brutalist] no matching YouTube.json entry for {slug} — skipping join")
        else:
            print(f"[brutalist] YouTube.json not found at {yt_path} — skipping join")

    # Prepend B00 (replace existing if --force)
    if any(b["beat_id"] == "B00" for b in beats):
        idx = next(i for i, b in enumerate(beats) if b["beat_id"] == "B00")
        beats[idx] = b00
        print("[brutalist] replaced B00 → BrutalistTerminalOpen (--force)")
    else:
        beats.insert(0, b00)
        print("[brutalist] prepended B00 → BrutalistTerminalOpen")

    # Insert B00B at index 1 (replace existing if --force)
    if any(b["beat_id"] == "B00B" for b in beats):
        idx = next(i for i, b in enumerate(beats) if b["beat_id"] == "B00B")
        beats[idx] = b00b
        print("[brutalist] replaced B00B → BrutalistAdaptCLI (--force)")
    else:
        beats.insert(1, b00b)
        print("[brutalist] inserted B00B at index 1 → BrutalistAdaptCLI")

    # Append B99 (replace existing if --force)
    if any(b["beat_id"] == "B99" for b in beats):
        idx = next(i for i, b in enumerate(beats) if b["beat_id"] == "B99")
        beats[idx] = b99
        print(f"[brutalist] replaced B99 → BrutalistCommentCTA variant {variant} (--force)")
    else:
        beats.append(b99)
        print(f"[brutalist] appended B99 → BrutalistCommentCTA variant {variant}")

    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
    print(f"[brutalist] ✓ wrote {sheet_path.name}")
    print(f"[brutalist] next:")
    print(f"  python3 runtime/scripts/generate_audio.py "
          f"cancer-biology/youtube/apoptosis-resistance --only B00 B00B B99")
    print(f"  python3 runtime/scripts/remotion_scenes.py "
          f"cancer-biology/youtube/apoptosis-resistance --force --only B00")
    print(f"  python3 runtime/scripts/remotion_scenes.py "
          f"cancer-biology/youtube/apoptosis-resistance --force --only B00B")
    print(f"  python3 runtime/scripts/remotion_scenes.py "
          f"cancer-biology/youtube/apoptosis-resistance --force --only B99")


if __name__ == "__main__":
    main()
