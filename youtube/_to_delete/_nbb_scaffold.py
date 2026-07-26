#!/usr/bin/env python3
"""Scaffold the @NikBearBrown 'What Is Brutalist?' playlist — a self-serve,
open-source course on using github.com/nikbearbrown/brutalist.art to make
videos. Liam for Bear. No support, no email. Star appreciated.
Placed at brutalist-art/youtube/_nbb_scaffold.py; builds ./using-brutalist/."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))           # .../brutalist-art/youtube
PL = os.path.join(BASE, "using-brutalist")
os.makedirs(PL, exist_ok=True)

REPO = "https://github.com/nikbearbrown/brutalist.art"
CHANNEL = "@NikBearBrown"
PLAYLIST_TITLE = "What Is Brutalist? — Make Videos with the Open-Source Toolkit"

EPISODES = [
 dict(slug="what-is-brutalist", title="What Is Brutalist?",
   one_idea="Brutalist is a free, local, audio-first toolkit that turns a folder of your work into a finished explainer video — the beat sheet is the program that renders the film.",
   acts=["A folder of your work goes in, a video comes out","Audio-first: narration sets the clock","The beat sheet is the program that renders the film","Local and free: Kokoro voices, Manim, Remotion","Open source — download it and make your own"]),
 dict(slug="get-the-repo", title="Get the Repo",
   one_idea="Clone the repo and run ./setup --install — no account, no email, no support tickets; a star is appreciated.",
   acts=["git clone the repo","./setup --install","What you get: skills, runtime, voices","Self-serve: no support, no email","A star is appreciated"]),
 dict(slug="run-claude-code", title="Run Claude Code",
   one_idea="Open Claude Code in the folder that holds your work and the Brutalist skills with caffeinate claude --dangerously-skip-permissions.",
   acts=["Open Claude Code in your folder","caffeinate keeps your Mac awake","--dangerously-skip-permissions runs it unattended","One command, one entry point","./art drives the stages"]),
 dict(slug="your-folder", title="Your Work in One Folder",
   one_idea="Put everything — notes, code, figures, data, the draft — in one folder; that folder is the raw material Claude reads to find the stories worth animating.",
   acts=["One folder equals one conversation","Notes, code, figures, data, drafts","Claude reads it to find stories","Nothing lives only on your desktop","Reproducible from the folder"]),
 dict(slug="the-prompt", title="The Prompt: Generic to Specific",
   one_idea="Start from the generic seed, then steer with your specifics — name the project, the result, the figure, and the one idea a viewer should leave with.",
   acts=["The generic seed prompt","Name your project and your result","Name the figure worth showing","Name the one idea to leave with","Have Liam say 'Bear' for your name"]),
 dict(slug="the-beat-sheet", title="The Beat Sheet Is the Program",
   one_idea="beat_sheet.json is the film as code — narration, timing, voice, visual lane, and render instructions; regenerate the video from it any time.",
   acts=["The film is code","Narration, beats, timing, voice","A visual lane per beat","Slates mark what's not filled yet","Regenerate any time"]),
 dict(slug="make-it-move", title="Make It Move",
   one_idea="Brutalist renders every beat it can — Manim fragments, Remotion scenes, cards — and leaves the rest as labeled slates for you to fill.",
   acts=["Manim for math and motion","Remotion for scenes and cards","The machine builds what it can","Slates label what's missing","Fill the pantry, recompile"]),
 dict(slug="voices", title="Voices: Free and Local",
   one_idea="Kokoro gives you free, local voices — pick one and keep it; no cloud, no cost.",
   acts=["Kokoro: free and local","Pick a voice (am_onyx, af_heart…)","Keep it consistent","Audio is the master clock","No cloud, no cost"]),
 dict(slug="watch-and-revise", title="Watch and Revise",
   one_idea="Watch the cut, then ask for changes in plain language — a wrong number, a slow pace, a better chart; plain language in, better video out.",
   acts=["Watch the review cut","Say what's off in plain language","A number, a pace, a chart","Iterate until it's right","The human conducts"]),
 dict(slug="both-formats", title="16:9 and 9:16",
   one_idea="Every video ships in both landscape and vertical — build 16:9, then reformat to 9:16 with the 916 command and check the framing.",
   acts=["Landscape and vertical","Build 16:9 first","Reformat with the 916 command","Check subject, captions, safe areas","One film, two shapes"]),
 dict(slug="qc-gates", title="QC Gates: Catch the Overlaps",
   one_idea="Turn the layout gates on with ART_QC=1 — the toolkit checks text-on-figure overlaps, safe areas, and contrast, and blocks until they are clean.",
   acts=["ART_QC=1 turns the gates on","The text-on-figure overlap check","Safe area and contrast","It blocks until clean","Fix the label, recompile"]),
 dict(slug="publish-it-yourself", title="Publish It Yourself",
   one_idea="There is no gatekeeper — cut the clean master with art final and post it to your own channel; you own the video and the account.",
   acts=["art final cuts the clean master","No publishing script required","Post to your own channel","You own the video","Your account, your rules"]),
 dict(slug="make-it-yours", title="Make It Yours",
   one_idea="Fork it, change the skins and scenes, and send it back — it is open source; a star is appreciated.",
   acts=["Open source: fork it","Change skins, scenes, voices","Contribute back","A star is appreciated","Go make yours"]),
]

def scaffold(c, n):
    d = os.path.join(PL, c["slug"])
    os.makedirs(d, exist_ok=True)
    beats = [dict(id="B00", act="COLD OPEN", lane="REMOTION", scene="ClaudeComposerAsk",
                  narration=f"Hey Claude — {c['title']}")]
    for i, a in enumerate(c["acts"], 1):
        beats.append(dict(id=f"A{i}", act=f"ACT {i}", lane="REMOTION", scene="segment-card", narration=a))
    beats.append(dict(id="OUTRO", act="CLOSE", lane="REMOTION", scene="ClaudeTitleOutro",
                      narration=f"{c['title']} — Brutalist. {CHANNEL}."))
    bs = dict(metadata=dict(slug=c["slug"], title=c["title"], channel="claude-liam",
              persona="Liam", in_for="Liam, for Bear", folderLabel=CHANNEL,
              register="Teardown", engine="kokoro", voice="am_onyx", palette="claude",
              genre="ai-explainer", topic="BRUTALIST — OPEN SOURCE", one_idea=c["one_idea"],
              source=REPO, repo=REPO, publish_url="https://youtube.com/@NikBearBrown",
              chapter_number=n, playlist_title=PLAYLIST_TITLE, duration_estimate_s=120,
              build=dict(cut="scaffold", note="Seed for the open-source Brutalist course; build with Brutalist, audio-first, ART_QC=1.")),
              beats=beats)
    json.dump(bs, open(os.path.join(d, "beat_sheet.json"), "w"), indent=2, ensure_ascii=False)
    open(os.path.join(d, "description.txt"), "w").write(
        f"{c['title']}\n\n{c['one_idea']}\n\n"
        f"Brutalist is open source. Download it, use it, make your own videos:\n{REPO}\n"
        "Self-serve — no support, no email. If you find it useful, a star is appreciated.\n\n"
        f"Channel: https://youtube.com/@NikBearBrown\n")
    open(os.path.join(d, "BUILD-PROMPT.md"), "w").write(
        f"# {c['title']} — Brutalist (open source, {CHANNEL})\n\n"
        f"Persona: Liam, for Bear. Channel: {CHANNEL}. Repo: {REPO}\n\n"
        f"One idea: {c['one_idea']}\n\n## Acts\n" +
        "\n".join(f"{i}. {a}" for i, a in enumerate(c["acts"], 1)) +
        "\n\nFraming: self-serve open source. No support, no email. Star appreciated. "
        "Scaffold only — build with Brutalist, audio-first, ART_QC=1.\n")

for n, c in enumerate(EPISODES, 1):
    scaffold(c, n)

lines = ["# " + PLAYLIST_TITLE, "", f"Channel: https://youtube.com/@NikBearBrown  ·  Persona: Liam, for Bear",
         f"Repo (open source — star appreciated): {REPO}", "",
         "Self-serve: no support, no email. If you want to download Brutalist and use it to make videos, this is how.",
         "", "| # | Title | Folder |", "|---|---|---|"]
for n, c in enumerate(EPISODES, 1):
    lines.append(f"| {n} | {c['title']} | `{c['slug']}` |")
open(os.path.join(PL, "PLAYLIST.md"), "w").write("\n".join(lines) + "\n")
print(f"scaffolded {len(EPISODES)} episodes into {PL}")
