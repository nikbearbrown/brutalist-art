#!/usr/bin/env python3
"""Non-destructively convert bears-doodles PNG references to SVG/transparent PNG pairs."""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "converted"
REFS = OUT / "references"
SVGS = OUT / "svg"
PNGS = OUT / "png"
MANIFEST = OUT / "icons.json"

ANIMALS = (
    "bed bug", "bluebottle fly", "bunny rabbit", "cheetah", "cicada",
    "crocodile", "deer", "dolphin", "echidna", "elephant", "firefly",
    "fox", "giraffe", "gorilla", "humpback whale", "kangaroo", "koala",
    "leopard", "orangutan", "platypus", "polar bear", "red panda",
    "rhinoceros", "seahorse", "shark", "tiger", "wolf", "zebra", "bear",
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def clean_prompt(filename: str) -> str:
    stem = Path(filename).stem
    stem = re.sub(r"^httpss\.mj\.run[A-Za-z0-9_-]+_", "", stem)
    stem = re.sub(
        r"_[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}_\d+$",
        "",
        stem,
        flags=re.I,
    )
    return re.sub(r"[_\s]+", " ", stem).strip()


def category_subject(prompt: str) -> tuple[str, str]:
    lower = prompt.lower()
    for animal in sorted(ANIMALS, key=len, reverse=True):
        if re.search(rf"\b{re.escape(animal)}\b", lower):
            return "animal", animal
    if any(word in lower for word in ("earth", "moon", "mars", "planet", "lander", "flying saucer")):
        return "space", next((w for w in ("earth", "moon", "mars", "lander", "flying saucer") if w in lower), "space")
    if any(word in lower for word in ("flask", "voltmeter", "ammeter")):
        return "object", next(w for w in ("flask", "voltmeter", "ammeter") if w in lower)
    if any(word in lower for word in ("dolly parton", "james bond", "atticus finch", "marge simpson", "milhouse", "groundskeeper", "dexter", "artemis fowl", "male model")):
        subject = next(w for w in ("dolly parton", "james bond", "atticus finch", "marge simpson", "milhouse", "groundskeeper", "dexter", "artemis fowl", "male model") if w in lower)
        return "person", subject
    return "doodle", "illustration"


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "illustration"


def run(*args: str) -> None:
    subprocess.run(args, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main() -> None:
    for directory in (REFS, SVGS, PNGS):
        directory.mkdir(parents=True, exist_ok=True)

    sources = sorted(ROOT.glob("*.png"), key=lambda p: p.name.lower())
    counters: Counter[str] = Counter()
    records = []

    for source in sources:
        prompt = clean_prompt(source.name)
        category, subject = category_subject(prompt)
        base = f"{category}-{slug(subject)}"
        counters[base] += 1
        icon_id = f"{base}-{counters[base]:03d}"
        ref_name = f"{icon_id}-reference.png"
        png_name = f"{icon_id}-transparent.png"
        svg_name = f"{icon_id}-rough.svg"
        reference = REFS / ref_name
        transparent = PNGS / png_name
        svg = SVGS / svg_name
        pbm = OUT / f".{icon_id}.pbm"

        if not reference.exists():
            try:
                reference.hardlink_to(source)
            except OSError:
                shutil.copy2(source, reference)

        run(
            "magick", str(source), "-alpha", "on", "-fuzz", "10%",
            "-transparent", "white", str(transparent),
        )
        run(
            "magick", str(source), "-background", "white", "-alpha", "remove",
            "-alpha", "off", "-colorspace", "Gray", "-threshold", "72%", str(pbm),
        )
        run("potrace", str(pbm), "--svg", "--tight", "--alphamax", "1.0",
            "--opttolerance", "0.25", "--output", str(svg))
        pbm.unlink(missing_ok=True)

        records.append({
            "icon_id": icon_id,
            "category": category,
            "subject": subject,
            "source": {
                "filename": source.name,
                "prompt_from_filename": prompt,
                "sha256": sha256(source),
                "bytes": source.stat().st_size,
            },
            "derivative": {
                "reference": f"references/{ref_name}",
                "svg": f"svg/{svg_name}",
                "transparent_png": f"png/{png_name}",
                "method": "white-background removal plus monochrome Potrace vectorization",
                "style": "source-preserving rough traced line art",
                "review_status": "generated-needs-human-review",
            },
        })

    manifest = {
        "collection": "bears-doodles-converted",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_directory": str(ROOT),
        "source_count": len(sources),
        "records": records,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"converted": len(records), "manifest": str(MANIFEST)}, indent=2))


if __name__ == "__main__":
    main()
