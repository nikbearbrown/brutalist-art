#!/usr/bin/env python3
"""linework-to-svg.py — turn black-and-white line art into clean, gate-passing SVGs.

Tries each image, and when a trace comes out TOO COMPLEX it *simplifies and retries*
(blur + downscale + threshold harder) until it fits — keeping the first level that
works. If even the most aggressive pass can't make a clean icon, it tosses with a
reason. A bad vector is worse than none.

Usage:
  python linework-to-svg.py <png-dir-or-file> [-o OUT] [--max-bytes N] [--min-bytes N]
                            [--simplify auto|0|1|2|3]

Deps:  pip install vtracer pillow

Handles both black-on-transparent (Etsy/PNG exports) and opaque black-on-white (Midjourney).
"""
import os, re, sys, glob, argparse, hashlib
from PIL import Image, ImageFilter
import vtracer

DPAT = re.compile(r'\bd="[^"]*"')

# escalating simplification: bigger blur + smaller canvas + heavier speckle/length filtering
LEVELS = {
    0: dict(maxpx=1200, blur=0.0, speckle=10, length=8.0),
    1: dict(maxpx=900,  blur=1.2, speckle=20, length=12.0),
    2: dict(maxpx=700,  blur=2.2, speckle=40, length=18.0),
    3: dict(maxpx=520,  blur=3.6, speckle=70, length=28.0),
}

def to_grayscale_on_white(src):
    im = Image.open(src)
    has_alpha = im.mode in ("RGBA", "LA") and im.getchannel("A").getextrema()[0] < 255
    if has_alpha:
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        bg.alpha_composite(im.convert("RGBA"))
        return bg.convert("L")
    return im.convert("L")

def preprocess(src, lvl, tmp):
    cfg = LEVELS[lvl]
    g = to_grayscale_on_white(src)
    w, h = g.size
    if max(w, h) > cfg["maxpx"]:
        s = cfg["maxpx"] / max(w, h)
        g = g.resize((round(w * s), round(h * s)), Image.LANCZOS)
    if cfg["blur"] > 0:
        g = g.filter(ImageFilter.GaussianBlur(cfg["blur"]))   # merge sketchy strokes
    bw = g.point(lambda p: 0 if p < 128 else 255)             # pure black/white, drop grays
    bw.convert("RGB").save(tmp)

def add_viewbox(path):
    s = open(path).read()
    if "viewBox" not in s:
        m = re.search(r'width="(\d+)"[^>]*height="(\d+)"', s)
        if m:
            s = s.replace("<svg", f'<svg viewBox="0 0 {m.group(1)} {m.group(2)}"', 1)
            open(path, "w").write(s)
    return s

def trace(src, dst, lvl):
    cfg = LEVELS[lvl]
    tmp = dst + ".flat.png"
    preprocess(src, lvl, tmp)
    vtracer.convert_image_to_svg_py(
        tmp, dst, colormode="binary", mode="spline",
        filter_speckle=cfg["speckle"], corner_threshold=60,
        length_threshold=cfg["length"], path_precision=2,
    )
    os.remove(tmp)
    return add_viewbox(dst)

def metrics(svg):
    return dict(
        bytes=len(svg),
        paths=svg.count("<path"),
        dchars=sum(len(x) for x in DPAT.findall(svg)),
        degenerate=bool(svg.count("<path") == 1 and re.search(r'd="M0 ?0', svg) and "C" not in svg),
    )

def convert(src, dst, max_bytes, min_bytes, simplify):
    if simplify == "auto":
        levels = [0, 1, 2, 3]
    elif simplify == "0":
        levels = [0]
    else:
        levels = [int(simplify)]
    last = None
    for lvl in levels:
        svg = trace(src, dst, lvl)
        m = metrics(svg); last = (lvl, m)
        ok = (min_bytes <= m["bytes"] <= max_bytes) and (not m["degenerate"]) and (m["dchars"] > 50)
        if ok:
            return ("KEEP", lvl, m)
        # if it's too SMALL/degenerate, more simplification won't help — stop early
        if m["degenerate"] or m["bytes"] < min_bytes:
            break
    return ("toss", last[0], last[1])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("-o", "--out", default="svg-out")
    ap.add_argument("--max-bytes", type=int, default=40000)
    ap.add_argument("--min-bytes", type=int, default=800)
    ap.add_argument("--simplify", default="auto", choices=["auto", "0", "1", "2", "3"],
                    help="auto = escalate simplification until it fits; 0 = off; 1-3 = fixed level")
    a = ap.parse_args()

    srcs = sorted(glob.glob(os.path.join(a.input, "*.png"))) if os.path.isdir(a.input) else [a.input]
    if not srcs:
        print("no .png input found"); sys.exit(1)
    os.makedirs(a.out, exist_ok=True)

    kept = tossed = 0
    for src in srcs:
        raw = os.path.splitext(os.path.basename(src))[0]
        slug = re.sub(r"[^a-z0-9]+", "-", raw.lower()).strip("-")[:48].rstrip("-")
        base = f"{slug}-{hashlib.md5(raw.encode()).hexdigest()[:6]}"  # short hash keeps variants distinct
        dst = os.path.join(a.out, base + ".svg")
        try:
            verdict, lvl, m = convert(src, dst, a.max_bytes, a.min_bytes, a.simplify)
        except Exception as e:
            print(f"ERR  {os.path.basename(src)}: {e}"); continue
        tag = "" if lvl == 0 else f" [simplify L{lvl}]"
        if verdict == "KEEP":
            kept += 1
            print(f"KEEP {base}.svg  ({m['bytes']}B, {m['paths']} paths){tag}")
        else:
            os.remove(dst); tossed += 1
            why = ("degenerate/empty" if (m["degenerate"] or m["dchars"] <= 50)
                   else f"<{a.min_bytes}B under-traced (thin lines lost)" if m["bytes"] < a.min_bytes
                   else f">{a.max_bytes}B too complex even after simplify L{lvl}")
            print(f"toss {os.path.basename(src)}  ({m['bytes']}B — {why})")
    print(f"\n{kept + tossed} tried · {kept} kept -> {a.out}/ · {tossed} tossed")

if __name__ == "__main__":
    main()
