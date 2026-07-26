#!/usr/bin/env python3
"""Faithful, non-destructive brand-palette PNG→SVG and SVG color remapping."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from PIL import Image

PALETTE = (
    ("true-black", "#000000"),
    ("canvas-black", "#0A0A0A"),
    ("canvas-soft-black", "#111111"),
    ("cream", "#F5F1E8"),
    ("brand-rust", "#C15F3C"),
    ("blue", "#0072B2"),
    ("bluish-green", "#009E73"),
    ("yellow", "#F0E442"),
    ("reddish-purple", "#CC79A7"),
    ("sky-blue", "#56B4E9"),
)
HEX_RE = re.compile(r"(?<![\w-])#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})(?![\w-])")
RGB_RE = re.compile(
    r"rgb\(\s*(\d+(?:\.\d+)?%?)\s*[, ]\s*(\d+(?:\.\d+)?%?)\s*[, ]\s*(\d+(?:\.\d+)?%?)\s*\)",
    re.I,
)
P3_RE = re.compile(
    r"color\(\s*display-p3\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)(?:\s*/\s*[\d.]+)?\s*\)",
    re.I,
)
NAMED_PAINT_RE = re.compile(
    r"(?P<prefix>(?:fill|stroke|stop-color|flood-color|lighting-color)\s*(?:=|:)\s*[\"']?)"
    r"(?P<color>white|black|red|gray|grey|blue|green|yellow|purple|orange)"
    r"(?P<suffix>(?=[\s;\"'}>]))",
    re.I,
)
NAMED_RGB = {
    "white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0),
    "gray": (128, 128, 128), "grey": (128, 128, 128), "blue": (0, 0, 255),
    "green": (0, 128, 0), "yellow": (255, 255, 0), "purple": (128, 0, 128),
    "orange": (255, 165, 0),
}


def hex_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    if len(value) == 3:
        value = "".join(c * 2 for c in value)
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def srgb_to_lab(rgb: tuple[int, int, int]) -> tuple[float, float, float]:
    values = []
    for channel in rgb:
        c = channel / 255.0
        values.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    r, g, b = values
    x = (r * 0.4124564 + g * 0.3575761 + b * 0.1804375) / 0.95047
    y = (r * 0.2126729 + g * 0.7151522 + b * 0.0721750)
    z = (r * 0.0193339 + g * 0.1191920 + b * 0.9503041) / 1.08883

    def f(t: float) -> float:
        delta = 6 / 29
        return t ** (1 / 3) if t > delta ** 3 else t / (3 * delta ** 2) + 4 / 29

    fx, fy, fz = f(x), f(y), f(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


PALETTE_RGB = tuple((name, color, hex_rgb(color), srgb_to_lab(hex_rgb(color))) for name, color in PALETTE)


def nearest(rgb: tuple[int, int, int]) -> tuple[int, int, int]:
    lab = srgb_to_lab(rgb)
    return min(
        PALETTE_RGB,
        key=lambda entry: sum((lab[i] - entry[3][i]) ** 2 for i in range(3)),
    )[2]


def remap_raster(source: Path, destination: Path) -> dict:
    with Image.open(source) as opened:
        image = opened.convert("RGBA")
    rgba = np.asarray(image, dtype=np.uint8).copy()
    flat_rgb = rgba[:, :, :3].reshape(-1, 3)
    flat_alpha = rgba[:, :, 3].reshape(-1)
    palette_rgb = np.asarray([entry[2] for entry in PALETTE_RGB], dtype=np.uint8)
    palette_lab = np.asarray([entry[3] for entry in PALETTE_RGB], dtype=np.float32)
    indices = np.empty(len(flat_rgb), dtype=np.uint8)

    # Chunked vectorization bounds memory even for poster-sized source images.
    chunk_size = 500_000
    for start in range(0, len(flat_rgb), chunk_size):
        stop = min(start + chunk_size, len(flat_rgb))
        values = flat_rgb[start:stop].astype(np.float32) / 255.0
        linear = np.where(
            values <= 0.04045,
            values / 12.92,
            ((values + 0.055) / 1.055) ** 2.4,
        )
        x = (linear[:, 0] * 0.4124564 + linear[:, 1] * 0.3575761 + linear[:, 2] * 0.1804375) / 0.95047
        y = linear[:, 0] * 0.2126729 + linear[:, 1] * 0.7151522 + linear[:, 2] * 0.0721750
        z = (linear[:, 0] * 0.0193339 + linear[:, 1] * 0.1191920 + linear[:, 2] * 0.9503041) / 1.08883
        delta = 6 / 29
        fx = np.where(x > delta ** 3, np.cbrt(x), x / (3 * delta ** 2) + 4 / 29)
        fy = np.where(y > delta ** 3, np.cbrt(y), y / (3 * delta ** 2) + 4 / 29)
        fz = np.where(z > delta ** 3, np.cbrt(z), z / (3 * delta ** 2) + 4 / 29)
        lab = np.stack((116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)), axis=1)
        distances = ((lab[:, None, :] - palette_lab[None, :, :]) ** 2).sum(axis=2)
        indices[start:stop] = distances.argmin(axis=1)

    flat_rgb[:] = palette_rgb[indices]
    flat_rgb[flat_alpha == 0] = 0
    image = Image.fromarray(rgba, "RGBA")
    counts = {}
    opaque_indices = indices[flat_alpha > 0]
    unique_indices, unique_counts = np.unique(opaque_indices, return_counts=True)
    for palette_index, count in zip(unique_indices.tolist(), unique_counts.tolist()):
        counts[PALETTE[palette_index][1]] = count
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination, optimize=True)
    return {
        "width": image.width,
        "height": image.height,
        "palette_pixels": counts,
    }


def normalize_hex(token: str) -> tuple[tuple[int, int, int], str]:
    value = token.lstrip("#")
    alpha = ""
    if len(value) == 8:
        alpha = value[6:8]
        value = value[:6]
    elif len(value) == 4:
        alpha = value[3] * 2
        value = "".join(c * 2 for c in value[:3])
    if len(value) == 3:
        value = "".join(c * 2 for c in value)
    return hex_rgb(value), alpha


def remap_svg_text(text: str) -> tuple[str, dict]:
    replacements: dict[str, str] = {}

    def replace_hex(match: re.Match) -> str:
        token = match.group(0)
        rgb, alpha = normalize_hex(token)
        target_rgb = nearest(rgb)
        target = "#{:02X}{:02X}{:02X}".format(*target_rgb) + alpha.upper()
        replacements[token] = target
        return target

    def replace_rgb(match: re.Match) -> str:
        def channel(value: str) -> int:
            return round(float(value[:-1]) * 2.55) if value.endswith("%") else min(255, round(float(value)))
        rgb = tuple(channel(match.group(i)) for i in (1, 2, 3))
        target_rgb = nearest(rgb)
        target = "#{:02X}{:02X}{:02X}".format(*target_rgb)
        replacements[match.group(0)] = target
        return target

    def replace_p3(match: re.Match) -> str:
        rgb = tuple(max(0, min(255, round(float(match.group(i)) * 255))) for i in (1, 2, 3))
        target_rgb = nearest(rgb)
        target = "#{:02X}{:02X}{:02X}".format(*target_rgb)
        replacements[match.group(0)] = target
        return target

    def replace_named(match: re.Match) -> str:
        name = match.group("color").lower()
        target_rgb = nearest(NAMED_RGB[name])
        target = "#{:02X}{:02X}{:02X}".format(*target_rgb)
        replacements[name] = target
        return match.group("prefix") + target

    text = HEX_RE.sub(replace_hex, text)
    text = RGB_RE.sub(replace_rgb, text)
    text = P3_RE.sub(replace_p3, text)
    text = NAMED_PAINT_RE.sub(replace_named, text)
    return text, replacements


def remap_svg(source: Path, destination: Path) -> dict:
    original = source.read_text(encoding="utf-8", errors="replace")
    remapped, replacements = remap_svg_text(original)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(remapped, encoding="utf-8")
    return {"color_replacements": replacements, "replacement_count": len(replacements)}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--repair-output", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    output = (args.output or root / "brand-palette").resolve()
    output.mkdir(parents=True, exist_ok=True)
    palette_png_dir = output / "palette-png"
    vector_dir = output / "vector-svg"
    svg_dir = output / "remapped-svg"

    if args.repair_output:
        repaired = 0
        changed = 0
        replacement_total = 0
        for svg in sorted(output.rglob("*.svg")):
            original = svg.read_text(encoding="utf-8", errors="replace")
            remapped, replacements = remap_svg_text(original)
            repaired += 1
            replacement_total += len(replacements)
            if remapped != original:
                svg.write_text(remapped, encoding="utf-8")
                changed += 1
        report = {"scanned": repaired, "changed": changed, "replacement_kinds": replacement_total}
        (output / "palette-repair.json").write_text(json.dumps(report, indent=2) + "\n")
        print(json.dumps(report))
        return

    pngs = sorted(p for p in root.rglob("*.png") if output not in p.parents)
    svgs = sorted(p for p in root.rglob("*.svg") if output not in p.parents)
    jobs = [("png", p) for p in pngs] + [("svg", p) for p in svgs]
    if args.limit:
        jobs = jobs[:args.limit]
    records = []
    failures = []

    for index, (kind, source) in enumerate(jobs, 1):
        relative = source.relative_to(root)
        try:
            if kind == "png":
                palette_png = palette_png_dir / relative
                vector = (vector_dir / relative).with_suffix(".svg")
                if args.force or not palette_png.exists():
                    details = remap_raster(source, palette_png)
                else:
                    details = {"status": "existing"}
                if args.force or not vector.exists():
                    vector.parent.mkdir(parents=True, exist_ok=True)
                    subprocess.run(
                        [
                            "vtracer", "--input", str(palette_png), "--output", str(vector),
                            "--colormode", "color", "--hierarchical", "stacked",
                            "--mode", "spline", "--filter_speckle", "2",
                            "--color_precision", "8", "--path_precision", "3",
                        ],
                        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                    )
                    remapped, replacements = remap_svg_text(vector.read_text(encoding="utf-8"))
                    vector.write_text(remapped, encoding="utf-8")
                    details["vector_color_replacements"] = len(replacements)
                outputs = {
                    "palette_png": str(palette_png.relative_to(output)),
                    "vector_svg": str(vector.relative_to(output)),
                }
            else:
                destination = svg_dir / relative
                details = remap_svg(source, destination) if args.force or not destination.exists() else {"status": "existing"}
                outputs = {"remapped_svg": str(destination.relative_to(output))}
            records.append({
                "kind": kind,
                "source": str(relative),
                "source_sha256": sha256(source),
                "outputs": outputs,
                "details": details,
            })
            print(f"[{index}/{len(jobs)}] {kind}: {relative}", flush=True)
        except Exception as error:
            failures.append({"kind": kind, "source": str(relative), "error": str(error)})
            print(f"[{index}/{len(jobs)}] FAILED {kind}: {relative}: {error}", flush=True)

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_root": str(root),
        "output_root": str(output),
        "palette": [{"role": name, "hex": color} for name, color in PALETTE],
        "method": {
            "distance": "nearest CIE Lab Euclidean color",
            "png": "RGBA palette mapping followed by full-color VTracer",
            "svg": "geometry-preserving fill/stroke/gradient hexadecimal and rgb() paint remap",
            "non_destructive": True,
        },
        "discovered": {"png": len(pngs), "svg": len(svgs)},
        "processed": len(records),
        "failed": len(failures),
        "records": records,
        "failures": failures,
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"processed": len(records), "failed": len(failures), "manifest": str(output / "manifest.json")}))


if __name__ == "__main__":
    main()
