#!/usr/bin/env python3
"""build_deck.py — beat_sheet.json → deck.html (self-contained talking HTML deck).
Palette-aware: reads metadata.palette + metadata.typography from the beat sheet
and emits the matching CSS :root tokens + font-family.

Usage:
  python3 build_deck.py <lecture_folder>
  python3 build_deck.py <lecture_folder> beat_sheet.nbb.json   # named variant
"""
import base64, json, sys, re as _re
from pathlib import Path

if len(sys.argv) < 2:
    sys.exit("Usage: build_deck.py <lecture_folder> [beat_sheet_filename]")
HERE = Path(sys.argv[1]).resolve()
BS_NAME = sys.argv[2] if len(sys.argv) > 2 else "beat_sheet.json"

sheet = json.loads((HERE / BS_NAME).read_text())
segs = sheet["segments"]
N = len(segs)
_chm = _re.search(r'[/\\](\d+)-', sheet.get("source", ""))
_chnum = str(int(_chm.group(1))) if _chm else "?"

# ── palette → CSS :root tokens ────────────────────────────────────────────────
# Colour values are verbatim from runtime/remotion/src/tokens/*.ts.
# teardown = VOX (vox.ts); default flip 2026-07.
PALETTES = {
    "brutalist": {
        "bg": "hsl(43,23%,93%)",
        "fg": "hsl(0,0%,7%)",
        "accent": "#ea580c",
        "muted": "hsl(0,0%,40%)",
        "muted_bg": "hsl(40,10%,85%)",
        "card": "hsl(43,20%,90%)",
        "green": "#16a34a",
        "warn": "#b91c1c",
        "font": "'JetBrains Mono',ui-monospace,monospace",
        "gfonts": "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700;800&display=swap",
    },
    # teardown: VOX palette — white ground, warm ink, red is the ONE accent (TEAL===INK)
    "teardown": {
        "bg": "#FFFFFF",
        "fg": "#2A1A0E",
        "accent": "#C8102E",
        "muted": "#545454",
        "muted_bg": "#F0F0F0",
        "card": "#F8F8F8",
        "green": "#2A1A0E",   # TEAL === INK in teardown grammar
        "warn": "#C8102E",    # same as accent — only one hue
        "font": "Montserrat,'Helvetica Neue',Arial,sans-serif",
        "gfonts": "https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=EB+Garamond:ital,wght@0,400;0,600;0,700;1,400&display=swap",
    },
    # humanitarians: muted editorial (Economist/FT-adjacent)
    "humanitarians": {
        "bg": "#F3EBDD",
        "fg": "#2F2A26",
        "accent": "#E4572E",  # CRIMSON burnt orange
        "muted": "#29335C",   # SLATE navy
        "muted_bg": "#EDE4D4",
        "card": "#EDE4D4",
        "green": "#1F4E5F",   # TEAL petrol
        "warn": "#E4572E",
        "font": "'EB Garamond',Georgia,serif",
        "gfonts": "https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Montserrat:wght@400;600;700;800&display=swap",
    },
    # medhavy: Okabe-Ito colorblind-safe, warm eggshell ground
    "medhavy": {
        "bg": "#F0EAD6",
        "fg": "#000000",
        "accent": "#D55E00",  # CRIMSON vermillion
        "muted": "#4D4D4D",   # SLATE neutral gray
        "muted_bg": "#E4DEC4",
        "card": "#E4DEC4",
        "green": "#009E73",   # TEAL bluish green (Okabe-Ito)
        "warn": "#D55E00",
        "font": "'EB Garamond',Georgia,serif",
        "gfonts": "https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Montserrat:wght@400;600;700;800&display=swap",
    },
}

meta = sheet.get("metadata", {})
palette_name = meta.get("palette", "brutalist")
tok = dict(PALETTES.get(palette_name, PALETTES["brutalist"]))

# typography override: metadata.typography can override the palette font stack
# teardown: display (Montserrat) is the primary body font; serif is for editorial moments only
typo = meta.get("typography", {})
if typo:
    serif = typo.get("serif", "")
    display = typo.get("display", "")
    if palette_name == "teardown" and display and "Montserrat" in display:
        tok["font"] = f"{display},'Helvetica Neue',Arial,sans-serif"
    elif serif and "Garamond" in serif:
        tok["font"] = f"'{serif}',Georgia,serif"

# ── helpers ───────────────────────────────────────────────────────────────────
def title_html(parts):
    return "".join(f'<span class="o">{t}</span>' if acc else t for t, acc in parts)

# inline audio
audio_map = {}
for s in segs:
    mp3 = HERE / "audio" / f"{s['id']}.mp3"
    if mp3.exists():
        audio_map[s["id"]] = "data:audio/mpeg;base64," + base64.b64encode(mp3.read_bytes()).decode()

slides_html = []
for s in segs:
    dark = " sdark" if s.get("dark") else ""
    cap = s["beats"][0].get("text") or s["beats"][0].get("narration_text", "")
    slides_html.append(f'''<section class="slide{dark}" data-id="{s['id']}">
  <div class="smeta"><span class="lbl">// SLIDE {s['num']:02d} — {s['section']}</span><div class="sdiv"></div><span class="dot8"></span></div>
  <h1 class="stitle">{title_html(s['title'])}</h1>
  <div class="cbody">{s['body_html']}</div>
  <div class="ccap"><span class="ccap-tag">NARRATION</span><p>{cap}</p></div>
</section>''')

CSS = f'''
:root{{--bg:{tok['bg']};--fg:{tok['fg']};--accent:{tok['accent']};--muted:{tok['muted']};
 --muted-bg:{tok['muted_bg']};--card:{tok['card']};--green:{tok['green']};--warn:{tok['warn']};
 --font:{tok['font']};}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html,body{{height:100%;background:var(--bg);color:var(--fg);font-family:var(--font);overflow:hidden}}
body::before{{content:'';position:fixed;inset:0;pointer-events:none;z-index:0;
 background-image:radial-gradient(circle,var(--fg) 1px,transparent 1px);background-size:26px 26px;opacity:.05}}
#progress{{position:fixed;top:0;left:0;height:3px;background:var(--accent);z-index:200;transition:width .3s}}
.deck{{position:relative;width:100vw;height:100vh;overflow:hidden}}
.slide{{position:absolute;inset:0;display:none;flex-direction:column;padding:40px 60px 44px;background:var(--bg);z-index:1}}
.slide.active{{display:flex}}
.slide.sdark{{background:hsl(0,0%,6%);color:hsl(43,23%,93%)}}
.smeta{{display:flex;align-items:center;gap:14px;margin-bottom:20px;flex-shrink:0}}
.sdiv{{flex:1;height:1px;background:var(--fg);opacity:.16}}
.slide.sdark .sdiv{{background:hsl(43,23%,90%);opacity:.15}}
.dot8{{width:9px;height:9px;background:var(--accent);flex-shrink:0}}
.lbl{{font-size:13px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--muted)}}
.stitle{{font-size:clamp(26px,3.4vw,46px);font-weight:800;line-height:1.12;letter-spacing:-.5px;max-width:1050px;margin-bottom:26px;flex-shrink:0}}
.stitle .o{{color:var(--accent)}}
.cbody{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:22px;min-height:0}}
.lead{{font-size:clamp(15px,1.5vw,21px);color:var(--muted);line-height:1.55;max-width:900px}}
.slide.sdark .lead{{color:hsl(43,20%,72%)}}
/* flow / chips */
.flow{{display:flex;align-items:center;gap:14px;flex-wrap:wrap}}
.big-flow{{gap:10px}}
.chip{{border:2px solid var(--fg);padding:12px 18px;font-size:16px;font-weight:700;background:var(--card)}}
.chip.on{{background:var(--accent);color:#fff;border-color:var(--accent)}}
.chip.dim{{opacity:.5}}
.chip.warn{{border-color:var(--warn);color:var(--warn)}}
.chip b{{color:var(--accent)}}
.chip.on b,.chip.warn b{{color:inherit}}
.arw{{font-size:24px;color:var(--accent);font-weight:800}}
.phase{{display:flex;flex-direction:column;align-items:center;gap:4px;border:2px solid var(--fg);padding:14px 22px;font-size:26px;font-weight:800;background:var(--card)}}
.phase small{{font-size:11px;font-weight:600;color:var(--muted);letter-spacing:.1em;text-transform:uppercase}}
.phase.on{{background:var(--accent);color:#fff;border-color:var(--accent)}}
.phase.on small{{color:rgba(255,255,255,.85)}}
/* stats */
.stat-row{{display:flex;align-items:center;gap:26px;flex-wrap:wrap}}
.stat{{display:flex;flex-direction:column;gap:4px}}
.big{{font-size:clamp(38px,5vw,68px);font-weight:800;line-height:1}}
.big.on{{color:var(--accent)}}
.cap{{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}}
.eq{{font-size:40px;font-weight:800;color:var(--muted)}}
/* grids */
.grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}
.grid2{{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.cell-part{{border:2px solid var(--fg);padding:18px 20px;display:flex;flex-direction:column;gap:6px;background:var(--card)}}
.cell-part b{{font-size:18px;color:var(--accent);letter-spacing:.02em}}
.cell-part span{{font-size:14px;color:var(--muted);line-height:1.45}}
.cell-part i{{color:var(--warn);font-style:normal;font-weight:700}}
.cell-part.hot{{border-color:var(--accent);border-width:3px}}
.callout{{border:2px solid var(--accent);color:var(--accent);padding:14px 20px;font-size:17px;font-weight:600;align-self:flex-start}}
.callout b{{font-weight:800}}
/* wires */
.stack{{display:flex;flex-direction:column;gap:14px}}
.wire{{border-left:5px solid var(--accent);padding:6px 0 6px 18px;display:flex;flex-direction:column;gap:3px}}
.wire b{{font-size:19px;letter-spacing:.02em}}
.wire span{{font-size:14px;color:var(--muted)}}
/* balance */
.balance{{display:flex;align-items:center;gap:20px}}
.pan{{border:2px solid var(--fg);padding:18px 26px;display:flex;flex-direction:column;gap:4px;background:var(--card);flex:1}}
.pan b{{font-size:19px}}.pan span{{font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}}
.pan.surv{{border-color:var(--green)}}.pan.surv b{{color:var(--green)}}
.pan.die{{border-color:var(--warn)}}.pan.die b{{color:var(--warn)}}
.fulcrum{{font-size:38px;color:var(--accent);font-weight:800}}
/* thesis / close */
.thesis{{font-size:clamp(20px,2.4vw,32px);font-weight:700;line-height:1.35;max-width:960px;border-left:6px solid var(--accent);padding-left:24px}}
.thesis b{{color:var(--accent)}}
.close{{display:flex;flex-direction:column;gap:30px;align-items:center;text-align:center;justify-content:center;flex:1}}
.close-tags{{display:flex;gap:16px;flex-wrap:wrap;justify-content:center;font-size:14px;font-weight:800;letter-spacing:.12em;color:var(--green)}}
.close-tags span:nth-child(even){{color:hsl(0,0%,35%)}}
.sig{{font-size:14px;color:hsl(0,0%,45%);letter-spacing:.06em}}
/* caption band */
.ccap{{display:none}}
.slide.sdark .ccap{{border-top-color:hsl(43,23%,25%)}}
.ccap-tag{{font-size:11px;font-weight:800;letter-spacing:.18em;color:var(--accent);padding-top:4px;flex-shrink:0}}
.ccap p{{font-family:Georgia,'Times New Roman',serif;font-size:clamp(15px,1.6vw,22px);line-height:1.5;color:var(--fg);max-width:1080px}}
.slide.sdark .ccap p{{color:hsl(43,23%,90%)}}
/* chrome */
#controls{{position:fixed;top:16px;right:20px;display:flex;gap:8px;z-index:300}}
.ctrl{{width:38px;height:38px;border:2px solid var(--fg);background:var(--bg);color:var(--fg);font-size:15px;cursor:pointer;display:flex;align-items:center;justify-content:center}}
#dots{{position:fixed;bottom:14px;left:50%;transform:translateX(-50%);display:flex;gap:7px;z-index:100;flex-wrap:wrap;max-width:80vw;justify-content:center}}
.ndot{{width:7px;height:7px;background:var(--muted);opacity:.4;cursor:pointer}}
.ndot.active{{background:var(--accent);opacity:1;width:20px}}
#scount{{position:fixed;bottom:16px;right:22px;font-size:12px;color:var(--muted);z-index:100;letter-spacing:.1em}}
.sfoot{{position:fixed;bottom:16px;left:24px;font-size:11px;color:var(--muted);letter-spacing:.1em;z-index:100;text-transform:uppercase}}
'''

JS = '''
const AUDIO = __AUDIO__;
const N = __N__;
const slides=[...document.querySelectorAll('.slide')];
const dotsEl=document.getElementById('dots');
const progress=document.getElementById('progress');
const scount=document.getElementById('scount');
const soundBtn=document.getElementById('soundBtn');
let cur=0, soundOn=false, audioEl=null;
slides.forEach((_,i)=>{const d=document.createElement('div');d.className='ndot'+(i===0?' active':'');d.onclick=()=>go(i);dotsEl.appendChild(d);});
function stop(){if(audioEl){audioEl.pause();audioEl=null;}}
function play(i){stop();if(!soundOn)return;const src=AUDIO[slides[i].dataset.id];if(!src)return;const a=new Audio(src);audioEl=a;a.play().catch(()=>{});}
function go(i){if(i<0||i>=N)return;slides[cur].classList.remove('active');dotsEl.children[cur].classList.remove('active');cur=i;slides[cur].classList.add('active');dotsEl.children[cur].classList.add('active');progress.style.width=((i+1)/N*100)+'%';scount.textContent=String(i+1).padStart(2,'0')+' / '+String(N).padStart(2,'0');location.hash=String(i+1);play(i);}
soundBtn.onclick=()=>{soundOn=!soundOn;soundBtn.textContent=soundOn?'🔊':'🔇';if(soundOn)play(cur);else stop();};
document.addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key===' '){e.preventDefault();go(cur+1);}if(e.key==='ArrowLeft')go(cur-1);if(e.key==='m')soundBtn.click();});
function initHash(){const h=parseInt(location.hash.replace('#',''));if(h>=1&&h<=N){go(h-1);}else{go(0);}}
window.addEventListener('hashchange',()=>{const h=parseInt(location.hash.replace('#',''));if(h>=1&&h<=N&&h-1!==cur)go(h-1);});
initHash();
'''

html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=1280,initial-scale=1">
<title>{sheet["title"]}</title>
<link href="{tok['gfonts']}" rel="stylesheet">
<style>{CSS}</style></head><body>
<div id="progress"></div>
<div class="deck">{"".join(slides_html)}</div>
<div id="controls"><button class="ctrl" id="soundBtn" title="sound (m)">🔇</button></div>
<div id="dots"></div>
<div id="scount">01 / {N:02d}</div>
<div class="sfoot">{sheet["series"]} · Ch.{_chnum} · {sheet.get("metadata", {}).get("audience", "Nik Bear Brown")}</div>
<script>{JS.replace("__AUDIO__", json.dumps(audio_map)).replace("__N__", str(N))}</script>
</body></html>'''

out = HERE / "deck.html"
out.write_text(html)
print(f"[ok] deck.html — {N} slides · palette={palette_name} · audio inlined for {len(audio_map)}/{N}")
