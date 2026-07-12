#!/usr/bin/env python3
"""onda_catalog.py — generate a Brutalist Template Library catalog video from Onda's own metadata.

For a chosen list of Onda slugs, this reads each component's meta.json (title + pickWhen) and
its exported component/schema names, then writes:

  beats/templates-onda.beats.json   — intro (Brutalist philosophy) + Onda credit + one segment
                                       per template (number + name + Onda's OWN pickWhen as the
                                       "use" line) + outro (coverage + next)
  src/harness/registry.ts           — static imports + ONDA_DATA for exactly these slugs

The "use" line is Onda's pickWhen, not invented. Aim ~15 templates for a ~5-minute video.
Next: riff_audio.py -> riff_conform.py -> render (RiffTour reads templates-onda.conformed.json).

Usage:
  python3 scripts/onda_catalog.py --slugs bar-chart,count-up,line-chart,pie-reveal,progress-bar,\
timeline,title-card,lower-third,stat-card,quote-card,chapter-card,end-card,underline,highlight,callout
"""
import argparse, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]                      # brutalist/remotion/
ONDA = HERE.parents[1] / "vox" / "remotion" / "_bench" / "onda"  # the onda registry
COMPONENTS = ONDA / "registry" / "components"
REL = "../../../../vox/remotion/_bench/onda/registry/components"  # import prefix from src/harness/
ONDA_TOTAL = 70  # Onda's own published catalog size (components); we adopted a subset


def use_line(pickwhen: str) -> str:
    """Onda's pickWhen, trimmed to the 'when' clause (drop the 'Use X instead' note)."""
    s = re.split(r"\s+Use\s+`|\.\s+Use\s+|\s+Use\s+\w", pickwhen)[0].strip().rstrip(".")
    return "Reach for it when " + s[0].lower() + s[1:] + "."


# Intro variants — same Brutalist message, different words. One is chosen per video by the
# episode index (derived from --start-num) so the opener is never verbatim twice in a row.
INTROS = [
    ("Brutalist is a simple deal. The AI writes the Remotion; you make the calls. But you can't ask for a template you don't know exists.",
     "So this is the library — 367 templates, adapted from open-source Remotion sets. We go through them a few at a time. First set: Onda."),
    ("Here's the Brutalist bargain: the machine writes the motion graphics, you stay the one who decides. And you can only ask for what you know is there.",
     "This is that library — 367 Remotion templates, pulled from open source and catalogued. We walk them a handful at a time. Onda's up first."),
    ("In Brutalist, the code is the cheap part — the AI writes Remotion all day. What's scarce is knowing the shelf, so you reach for the right thing.",
     "So we're taking inventory: 367 open-source Remotion templates, a few every video. Onda leads."),
    ("The whole Brutalist idea: let the AI generate, keep the judgment human. But judgment needs a menu — you can't order off one you've never seen.",
     "This is the menu — 367 Remotion templates, adapted from open source, shown a few at a time. Starting with Onda."),
    ("Brutalist splits the work clean: the AI does the typing, you do the choosing. The catch is you have to know a thing exists to choose it.",
     "Which is what this series is — 367 open-source Remotion templates, walked a few per video. First up, Onda."),
]


def _pascal(slug: str) -> str:
    """code-block -> CodeBlock, audio-visualizer -> AudioVisualizer."""
    return "".join(p[:1].upper() + p[1:] for p in re.split(r"[-_]", slug) if p)


def export_names(slug: str):
    """Find the component export (from <Name>.tsx) and schema export (from schema.ts).

    Prefer the export whose name is the PascalCase of the slug. This guards against three
    traps that produced React error #130 (a component resolving to `undefined`):
      - a helper `export const x` matched inside a JSDoc example (code-block),
      - a presets/config object exported before the real component (audio-visualizer),
      - simply grabbing the first `export const` regardless of what it is.
    The regex is anchored to line-start so `export const` inside a comment never matches.
    """
    d = COMPONENTS / slug
    want = _pascal(slug)
    tsx = sorted(d.glob("*.tsx"), key=lambda f: (f.stem != want, f.stem))  # <Pascal>.tsx first
    comp = None
    for f in tsx:
        names = re.findall(r"^export const (\w+)\s*[:=]", f.read_text(), re.M)
        if not names:
            continue
        if want in names:                                 # exact component match
            comp = (want, f.stem); break
        caps = [n for n in names if n[:1].isupper()]      # else first Capitalized export
        if caps and comp is None:
            comp = (caps[0], f.stem)
    sch = None
    sfile = d / "schema.ts"
    if sfile.exists():
        text = sfile.read_text()
        schemas = re.findall(r"^export const (\w+Schema)\b", text, re.M)
        if schemas:
            # Prefer the schema whose name is camelCase(slug)+"Schema" (e.g. nodeGraphSchema
            # for node-graph), avoiding auxiliary schemas like satelliteSchema.
            want_sch = want[0].lower() + want[1:] + "Schema"  # e.g. NodeGraph -> nodeGraphSchema
            sch = want_sch if want_sch in schemas else schemas[0]
    return comp, sch


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slugs", required=True, help="comma-separated onda slugs, in video order")
    ap.add_argument("--start-num", type=int, default=1, help="global catalog number of the first template (e.g. 21 for video 2)")
    ap.add_argument("--registry-only", action="store_true",
                    help="regenerate ONLY src/harness/registry.ts (imports depend on slugs, not narration). "
                         "Leaves the voiced beat sheet + audio untouched — use to pick up a component-resolution "
                         "fix without paying for a re-voice.")
    a = ap.parse_args()
    slugs = [s.strip() for s in a.slugs.split(",") if s.strip()]

    templates, imports, entries = [], [], []
    for i, slug in enumerate(slugs, 1):
        meta_f = COMPONENTS / slug / f"{slug}.meta.json"
        if not meta_f.exists():
            print(f"[skip] {slug}: no meta.json", file=sys.stderr); continue
        meta = json.loads(meta_f.read_text())
        comp, sch = export_names(slug)
        if not comp or not sch:
            print(f"[skip] {slug}: could not resolve exports", file=sys.stderr); continue
        (comp_name, file_stem) = comp
        title = meta.get("title", comp_name)
        gi = a.start_num + i - 1  # global catalog number
        num = f"{gi:02d}"
        templates.append({
            "id": slug, "template": f"onda:{slug}", "label": f"{num} / 59 · Onda {title}",
            "props": {"duration": 75},
            "beats": [
                {"type": "reactive", "deixis": True, "text": f"Number {gi}. The Onda {title}."},
                {"type": "analytic", "summon": True, "text": use_line(meta.get("pickWhen", ""))},
            ],
        })
        imports.append(f"import {{ {comp_name} }} from '{REL}/{slug}/{file_stem}';")
        imports.append(f"import {{ {sch} }} from '{REL}/{slug}/schema';")
        entries.append(f"  {{ slug: '{slug}', title: '{title}', Component: {comp_name}, schema: {sch} }},")

    n = len(templates)
    start, end = a.start_num, a.start_num + n - 1
    ep = max(0, (a.start_num - 1) // 20)          # episode index → rotates the intro
    intro = INTROS[ep % len(INTROS)]
    last_onda = end >= 59                          # final Onda video → hand off to a new library, not "more Onda"
    outro_sub = f"Onda {start}–{end} of 59 · next: {'a new library' if last_onda else 'more Onda'}"
    outro_lead = (f"That completes Onda — templates {start} to {end}, all 59 of the set."
                  if last_onda else f"That was Onda, templates {start} to {end} of 59.")
    outro_next = ("That's every Onda template. Next video opens a new library — same deal, a few at a time. 367 in all."
                  if last_onda else f"Next video, template {end + 1} onward — then the next set. 367 in all.")
    sheet = {
        "_comment": "Generated by onda_catalog.py from Onda meta.json. Use-lines are Onda's own pickWhen. Frames are placeholders — riff_audio writes durations, riff_conform reflows.",
        "title": f"The Brutalist Template Library — Onda {start} to {end} of 59",
        "series": "The Brutalist Template Library",
        "catalog_total": 367, "library": {"name": "Onda", "count": 59, "license": "MIT", "link": "github.com/degueba/onda"},
        "covers": [start, end], "fps": 30,
        "segments": [
            {"id": "intro", "template": None,
             "card": {"title": "THE BRUTALIST TEMPLATE LIBRARY", "sub": f"Video {ep + 1} · Onda {start}–{end} of 59"},
             "beats": [
                 {"type": "reactive", "text": f"Video {ep + 1}. {intro[0]}"},
                 {"type": "analytic", "text": f"{intro[1]} This video: Onda {start} to {end}."},
             ]},
            {"id": "onda-credit", "template": None,
             "card": {"title": "ONDA", "sub": "MIT · installed as source you own", "link": "github.com/degueba/onda"},
             "beats": [
                 {"type": "analytic", "text": "These are Onda — a premium Remotion component set. MIT licensed, installed as source you own, not a black-box dependency, with one signature motion language across the whole catalog."},
                 {"type": "analytic",
                  "text": "Thank you, Onda. We felt 59 of their 70 were useful for us — the rest, and full credit, at github.com/degueba/onda.",
                  "tts": "Thank you, Onda. We felt fifty-nine of their seventy were useful for us. You can find the rest, and full credit, at github dot com slash degueba slash onda."},
             ]},
            *templates,
            {"id": "outro", "template": None,
             "card": {"title": "THE BRUTALIST TEMPLATE LIBRARY", "sub": outro_sub},
             "beats": [
                 {"type": "analytic", "text": outro_lead},
                 {"type": "outro-topic", "render": "remotion", "source": "ABOUT.MD", "text": outro_next},
                 {"type": "outro-channel", "render": "remotion", "source": "AUTHOR.MD", "text": "Nik Bear Brown — the Brutalist template library, a few at a time."},
             ]},
        ],
    }
    if not a.registry_only:
        (HERE / "beats" / "templates-onda.beats.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False))

    registry = (
        "// GENERATED by scripts/onda_catalog.py — the catalog's Onda components.\n"
        "import type { ComponentType } from 'react';\nimport type { ZodTypeAny } from 'zod';\n\n"
        + "\n".join(imports)
        + "\n\nexport type OndaEntry = { slug: string; title: string; Component: ComponentType<any>; schema: ZodTypeAny };\n\n"
        + "export const ONDA_DATA: OndaEntry[] = [\n" + "\n".join(entries) + "\n];\n\n"
        + "export const ONDA_DATA_MAP: Record<string, OndaEntry> = Object.fromEntries(ONDA_DATA.map((e) => [e.slug, e]));\n"
    )
    (HERE / "src" / "harness" / "registry.ts").write_text(registry)

    if a.registry_only:
        print(f"[ok] {n} templates → src/harness/registry.ts ONLY (beat sheet + audio left intact)")
        print("[next] re-render — no re-voice needed")
        return 0
    print(f"[ok] {n} templates → beats/templates-onda.beats.json + src/harness/registry.ts")
    print("[next] python3 scripts/riff_audio.py beats/templates-onda.beats.json  →  riff_conform.py  →  render")
    return 0


if __name__ == "__main__":
    sys.exit(main())
