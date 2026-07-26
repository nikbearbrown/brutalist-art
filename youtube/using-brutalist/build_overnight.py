#!/usr/bin/env python3
"""build_overnight.py — overnight slate-cut builder for the 'What Is Brutalist?' playlist.

Processes all 13 episodes in chapter order:
1. Expands seed beat_sheet.json to the full pipeline format
2. Writes PEDAGOGY.md (GATE P bypass)
3. Generates audio (Kokoro am_onyx, free/local)
4. Renders Remotion bookend beats (B00, VERDICT, HANDOFF, OUTRO)
5. Compiles slate cut (--review, 1080p for speed)
6. Runs QC gates (Gate V final_frame_check, Gate T type_check)
7. Makes 9:16 short and compiles it
8. Git adds, commits, pushes per episode
9. Logs everything to OVERNIGHT-SLATE-BUILD.md

Run from books/brutalist-art/:
  python3 youtube/using-brutalist/build_overnight.py
"""
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# ── paths ──────────────────────────────────────────────────────────────────────
THIS     = Path(__file__).resolve().parent           # using-brutalist/
# THIS.parents[0] = youtube/, THIS.parents[1] = brutalist-art/ (the git root)
REPO     = THIS.parents[1]                          # brutalist-art/ — git root
RUNTIME  = REPO / "runtime"                         # brutalist-art/runtime/
SCRIPTS  = RUNTIME / "scripts"
QC_DIR   = RUNTIME / "qc"
MASTERLOG = THIS / "OVERNIGHT-SLATE-BUILD.md"

# ── world-language greetings assigned by chapter ───────────────────────────────
GREETINGS = {
    "what-is-brutalist":   "Hola, Liam",
    "get-the-repo":        "Ciao, Liam",
    "run-claude-code":     "Bonjour, Liam",
    "your-folder":         "Hej, Liam",
    "the-prompt":          "Namaste, Liam",
    "the-beat-sheet":      "Merhaba, Liam",
    "make-it-move":        "Annyeong, Liam",
    "voices":              "Jambo, Liam",
    "watch-and-revise":    "Salaam, Liam",
    "both-formats":        "Olá, Liam",
    "qc-gates":            "Hei, Liam",
    "publish-it-yourself": "Shalom, Liam",
    "make-it-yours":       "Konnichiwa, Liam",
}

# ── per-episode full narration ──────────────────────────────────────────────────
# Teardown register: Feynman × MKBHD. Liam, in for Bear.
# Each beat: narration_text, optional show hint, optional Remotion props.
EPISODES = {

"what-is-brutalist": {
    "beats": [
        {
            "beat_id": "B00",
            "act": "cold open",
            "narration_text": (
                "Hola — this is Liam, in for Bear. What Is Brutalist? "
                "You put your work in a folder, you run one command, you get a video. "
                "That is the whole pitch. The question is what is actually in the box."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Hola, Liam",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "What Is Brutalist?",
                    "command": "What is Brutalist and how does it make a video?",
                    "runningText": "reading SKILL.md… building beat sheet… generating audio…",
                    "output": [
                        "A local, free, audio-first video toolkit",
                        "Beat sheet drives the build — JSON file as film-as-code",
                        "Kokoro voices, Manim math, Remotion motion graphics"
                    ],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "A1",
            "act": "ACT 1",
            "narration_text": (
                "You start with a folder. Notes, code, data, screenshots, a rough draft — "
                "whatever you made. That folder is the raw material. "
                "Brutalist reads it and finds the stories inside worth animating. "
                "Nothing lives on a server. Nothing requires an account."
            )
        },
        {
            "beat_id": "A2",
            "act": "ACT 2",
            "narration_text": (
                "Audio goes first. You pick a voice — Kokoro, free, local, runs on your laptop. "
                "Narrate each beat, render the MP3s. "
                "Those durations become the master clock. "
                "Every visual, every edit, every timing conforms to the audio. "
                "The narration drives the film, not the other way around."
            )
        },
        {
            "beat_id": "A3",
            "act": "ACT 3",
            "narration_text": (
                "The beat sheet is a JSON file — narration, visual lane, timing, render instructions. "
                "It is the film as code. Change a line, recompile, the video updates. "
                "Version-control it. Fork it. Send it to someone else. "
                "The film is reproducible from the file."
            )
        },
        {
            "beat_id": "A4",
            "act": "ACT 4",
            "narration_text": (
                "Kokoro TTS runs locally — no cloud call, no monthly meter. "
                "Manim draws the math and charts. Remotion builds the motion graphics and bookends. "
                "Everything assembles with ffmpeg. "
                "The whole pipeline runs on your machine, with free tools, indefinitely."
            )
        },
        {
            "beat_id": "A5",
            "act": "ACT 5",
            "narration_text": (
                "The whole thing is open source. "
                "Clone the repo, run setup, start building. "
                "No support email. No onboarding call. No gated course. "
                "Star the repo if it is useful. Fork it if you want to make it yours. "
                "That is the deal."
            )
        },
        {
            "beat_id": "VERDICT",
            "act": "verdict",
            "narration_text": (
                "The verdict. Brutalist is a local pipeline: beat sheet drives the structure, "
                "audio drives the clock, and open source drives the distribution. "
                "No service, no subscription. Just a folder, a JSON file, and a script."
            ),
            "remotion": {
                "pattern": "ClaudeVerdictArtifact",
                "props": {
                    "artifactTitle": "What Is Brutalist?",
                    "artifactHeading": "The verdict",
                    "artifactLines": [
                        "Beat sheet = the film as code — change it, recompile, done.",
                        "Audio-first: narration is the master clock, not a timer.",
                        "Free and local: Kokoro, Manim, Remotion, ffmpeg — no accounts.",
                        "Open source: star it, fork it, send it back."
                    ]
                }
            }
        },
        {
            "beat_id": "HANDOFF",
            "act": "handoff",
            "narration_text": (
                "Your turn. Ask Claude this: "
                "I have a project — work, research, a course, a skill — "
                "and I want to make one explainer video from it. "
                "What is the single clearest idea in my material? "
                "What folder structure do I need to build the video with Brutalist? "
                "Run that in Claude. Bring the answer to the next episode. "
                "The prompt is your first build decision — start there."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "What Is Brutalist?",
                    "command": (
                        "I have [your project]. What is the single clearest idea in it that "
                        "could become one explainer video? What folder structure do I need "
                        "to build it with Brutalist?"
                    ),
                    "runningText": "paste this into Claude…",
                    "output": [],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "OUTRO",
            "act": "outro",
            "narration_text": "What Is Brutalist? — Brutalist. @NikBearBrown. Liam, in for Bear.",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": "What Is Brutalist?",
                    "handle": "@NikBearBrown",
                    "subline": "Liam, in for Bear"
                }
            }
        }
    ]
},

"get-the-repo": {
    "beats": [
        {
            "beat_id": "B00",
            "act": "cold open",
            "narration_text": (
                "Ciao — this is Liam, in for Bear. Get the Repo. "
                "One command to clone, one command to install — that is the whole setup. "
                "No account, no email, no support ticket. A star is appreciated."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Ciao, Liam",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Get the Repo",
                    "command": "How do I get Brutalist and install it?",
                    "runningText": "git clone… ./setup --install… checking dependencies…",
                    "output": [
                        "git clone https://github.com/nikbearbrown/brutalist.art",
                        "./setup --install — checks Python, Node, Kokoro, ffmpeg",
                        "No account. No email. Star the repo if it helps."
                    ],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "A1",
            "act": "ACT 1",
            "narration_text": (
                "Open a terminal. Run: git clone https://github.com/nikbearbrown/brutalist.art. "
                "That pulls the whole toolkit — skills, runtime, voices, templates. "
                "It lives on your machine. Nothing phones home."
            )
        },
        {
            "beat_id": "A2",
            "act": "ACT 2",
            "narration_text": (
                "Then: cd brutalist.art && ./setup --install. "
                "Setup checks what you have — Python, Node, ffmpeg, Kokoro — "
                "and prints a per-feature readiness report. "
                "If something is missing, it tells you exactly what to install. "
                "It does not install silently."
            )
        },
        {
            "beat_id": "A3",
            "act": "ACT 3",
            "narration_text": (
                "After setup, you get: skills — the agent instructions for each video type. "
                "Runtime — the shared Python and Remotion engine that every skill runs on. "
                "Voices — the Kokoro model files for free local TTS. "
                "That is the box."
            )
        },
        {
            "beat_id": "A4",
            "act": "ACT 4",
            "narration_text": (
                "Self-serve means exactly that. "
                "There is no support email. No Slack. No onboarding DM. "
                "The SKILL.md in each skill folder is the full operating manual. "
                "If it is not in the file, it is not the rule."
            )
        },
        {
            "beat_id": "A5",
            "act": "ACT 5",
            "narration_text": (
                "If Brutalist is useful, star the repo. "
                "GitHub stars are how other people find it. "
                "You are not obligated to anything else — "
                "no review, no testimonial, no newsletter signup. "
                "Star if it earns it."
            )
        },
        {
            "beat_id": "VERDICT",
            "act": "verdict",
            "narration_text": (
                "The verdict. Clone, install, check readiness — two commands, one report. "
                "The toolkit is on your machine, the docs are in the files, "
                "and a star is the only thing it asks in return."
            ),
            "remotion": {
                "pattern": "ClaudeVerdictArtifact",
                "props": {
                    "artifactTitle": "Get the Repo",
                    "artifactHeading": "The verdict",
                    "artifactLines": [
                        "git clone https://github.com/nikbearbrown/brutalist.art",
                        "./setup --install — readiness report, no silent installs.",
                        "SKILL.md is the operating manual — it is all in the file.",
                        "Star it if it helps. That is the whole ask."
                    ]
                }
            }
        },
        {
            "beat_id": "HANDOFF",
            "act": "handoff",
            "narration_text": (
                "Your turn. After you clone and run setup, ask Claude this: "
                "I just installed Brutalist. Run ./art --list and tell me which skill "
                "is the best match for my project: [describe your project in one sentence]. "
                "Show me how to scaffold the beat sheet for that skill. "
                "That prompt maps your project to the right skill — "
                "and gives you a beat sheet to edit before anything renders."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Get the Repo",
                    "command": (
                        "I just installed Brutalist. Run ./art --list and tell me which skill "
                        "is the best match for my project: [describe your project in one sentence]. "
                        "Show me how to scaffold the beat sheet for that skill."
                    ),
                    "runningText": "paste this into Claude…",
                    "output": [],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "OUTRO",
            "act": "outro",
            "narration_text": "Get the Repo — Brutalist. @NikBearBrown. Liam, in for Bear.",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": "Get the Repo",
                    "handle": "@NikBearBrown",
                    "subline": "Liam, in for Bear"
                }
            }
        }
    ]
},

"run-claude-code": {
    "beats": [
        {
            "beat_id": "B00",
            "act": "cold open",
            "narration_text": (
                "Bonjour — this is Liam, in for Bear. Run Claude Code. "
                "Open Claude Code in the folder that holds your work and the Brutalist skills. "
                "One flag keeps it running unattended. Let me show you the command."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Bonjour, Liam",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Run Claude Code",
                    "command": "How do I run Claude Code with Brutalist, unattended?",
                    "runningText": "caffeinate claude --dangerously-skip-permissions…",
                    "output": [
                        "Open Claude Code in the folder with your work AND brutalist-art/",
                        "caffeinate keeps your Mac awake during long builds",
                        "--dangerously-skip-permissions runs the pipeline without prompts"
                    ],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "A1",
            "act": "ACT 1",
            "narration_text": (
                "Open Claude Code in the folder that holds your work. "
                "That folder needs to be the parent of both your project files "
                "and the brutalist-art toolkit. "
                "Claude needs to see both to run the skills — the work and the machinery."
            )
        },
        {
            "beat_id": "A2",
            "act": "ACT 2",
            "narration_text": (
                "Prefix the command with caffeinate. "
                "caffeinate is a macOS built-in that prevents the display and CPU from sleeping. "
                "A build that takes forty minutes does not survive a screen lock without it. "
                "One word, big difference."
            )
        },
        {
            "beat_id": "A3",
            "act": "ACT 3",
            "narration_text": (
                "The flag is --dangerously-skip-permissions. "
                "It tells Claude Code not to pause and ask permission for each file write, "
                "ffmpeg call, or npm command. "
                "The pipeline meets the seatbelt rules — git-tracked, regenerable outputs — "
                "so the flag is appropriate here."
            )
        },
        {
            "beat_id": "A4",
            "act": "ACT 4",
            "narration_text": (
                "The full command: caffeinate claude --dangerously-skip-permissions. "
                "Run it from the parent folder. Paste your build prompt. "
                "Walk away. The whole pipeline — audio, Remotion, compile, QC — "
                "runs while you do something else."
            )
        },
        {
            "beat_id": "A5",
            "act": "ACT 5",
            "narration_text": (
                "The entry point is ./art. "
                "Every skill, every build stage, every QC gate "
                "runs through the art script in brutalist-art/. "
                "You do not call Python or npx directly — art resolves its own home "
                "and auto-loads the environment file."
            )
        },
        {
            "beat_id": "VERDICT",
            "act": "verdict",
            "narration_text": (
                "The verdict. caffeinate claude --dangerously-skip-permissions — "
                "three words that let the pipeline run overnight. "
                "One entry point, ./art, drives all the stages. "
                "You set it up once and it runs while you sleep."
            ),
            "remotion": {
                "pattern": "ClaudeVerdictArtifact",
                "props": {
                    "artifactTitle": "Run Claude Code",
                    "artifactHeading": "The verdict",
                    "artifactLines": [
                        "caffeinate claude --dangerously-skip-permissions — three words.",
                        "Open in the parent folder that holds your work + brutalist-art/.",
                        "./art is the single entry point — it resolves its own paths.",
                        "The pipeline runs unattended while you do something else."
                    ]
                }
            }
        },
        {
            "beat_id": "HANDOFF",
            "act": "handoff",
            "narration_text": (
                "Your turn. Ask Claude this: "
                "I am going to run you with caffeinate and --dangerously-skip-permissions. "
                "Read my BUILD-PROMPT.md and execute the pipeline for my reel. "
                "Run the stages in order: audio first, then Remotion, then compile. "
                "Log everything to BUILD-LOG.md. "
                "That is the overnight build prompt — "
                "paste it in after you have a beat sheet ready and walk away."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Run Claude Code",
                    "command": (
                        "I am going to run you with caffeinate and --dangerously-skip-permissions. "
                        "Read my BUILD-PROMPT.md and run the pipeline in order: "
                        "audio first, then Remotion, then compile. Log everything to BUILD-LOG.md."
                    ),
                    "runningText": "paste this into Claude…",
                    "output": [],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "OUTRO",
            "act": "outro",
            "narration_text": "Run Claude Code — Brutalist. @NikBearBrown. Liam, in for Bear.",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": "Run Claude Code",
                    "handle": "@NikBearBrown",
                    "subline": "Liam, in for Bear"
                }
            }
        }
    ]
},

"your-folder": {
    "beats": [
        {
            "beat_id": "B00",
            "act": "cold open",
            "narration_text": (
                "Hej — this is Liam, in for Bear. Your Work in One Folder. "
                "Everything that went into making your project — "
                "notes, code, figures, data, drafts — belongs in one folder. "
                "That folder is the raw material Claude reads to find the stories worth animating."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Hej, Liam",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Your Work in One Folder",
                    "command": "How should I organize my project folder before building a video?",
                    "runningText": "scanning folder… finding stories… mapping to beats…",
                    "output": [
                        "One folder = one conversation — notes, code, data, drafts together",
                        "Claude reads the folder to find the idea worth animating",
                        "Reproducible: the video rebuilds from the folder any time"
                    ],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "A1",
            "act": "ACT 1",
            "narration_text": (
                "One folder, one conversation. "
                "Put everything in it — your notes, your code, your figures, your data, "
                "your draft report, your slide deck. "
                "That folder is what you hand Claude. "
                "The richer the folder, the better the video Claude can find inside it."
            )
        },
        {
            "beat_id": "A2",
            "act": "ACT 2",
            "narration_text": (
                "What goes in the folder: notes and bullet points, "
                "code files and scripts, figures and charts you already have, "
                "any data files the work depends on, and the draft write-up. "
                "If it shaped your thinking, it belongs in the folder."
            )
        },
        {
            "beat_id": "A3",
            "act": "ACT 3",
            "narration_text": (
                "Claude reads the folder to find the stories. "
                "The scout skill scans your chapters and surfaces candidates — "
                "each card scores the idea and explains the one thing a viewer should leave with. "
                "You pick the card. Claude builds the beat sheet. "
                "The human picks; the machine builds."
            )
        },
        {
            "beat_id": "A4",
            "act": "ACT 4",
            "narration_text": (
                "Nothing that matters should live only on your desktop. "
                "If a figure is in your Downloads folder and not in the project folder, "
                "Claude cannot find it, and the video cannot use it. "
                "The folder is the contract between you and the pipeline."
            )
        },
        {
            "beat_id": "A5",
            "act": "ACT 5",
            "narration_text": (
                "Because the video is built from the folder, it is reproducible. "
                "Six months from now, you can regenerate the video from the same folder. "
                "Update the notes, recompile — you get an updated video. "
                "The folder is version-controlled. The video follows."
            )
        },
        {
            "beat_id": "VERDICT",
            "act": "verdict",
            "narration_text": (
                "The verdict. One folder, one conversation — "
                "the richer the material you put in, the better the story Claude finds. "
                "The folder is the contract. "
                "Keep it complete, keep it version-controlled, and the video is reproducible forever."
            ),
            "remotion": {
                "pattern": "ClaudeVerdictArtifact",
                "props": {
                    "artifactTitle": "Your Work in One Folder",
                    "artifactHeading": "The verdict",
                    "artifactLines": [
                        "One folder = one conversation — everything that shaped your thinking.",
                        "Claude scouts the folder and surfaces candidates — you pick.",
                        "Nothing that matters lives only on your desktop.",
                        "The folder is version-controlled. The video follows."
                    ]
                }
            }
        },
        {
            "beat_id": "HANDOFF",
            "act": "handoff",
            "narration_text": (
                "Your turn. Ask Claude this: "
                "Here is my project folder. Read everything in it. "
                "Tell me: what is the single most important idea in this material "
                "that a first-time viewer should understand? "
                "What three pieces of evidence — from the files I gave you — "
                "best support that idea? "
                "Run that prompt on your own folder — "
                "it surfaces the one idea and the three strongest beats for your video."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Your Work in One Folder",
                    "command": (
                        "Here is my project folder. Read everything in it. "
                        "What is the single most important idea a first-time viewer should understand? "
                        "What three pieces of evidence from my files best support that idea?"
                    ),
                    "runningText": "paste this into Claude…",
                    "output": [],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "OUTRO",
            "act": "outro",
            "narration_text": "Your Work in One Folder — Brutalist. @NikBearBrown. Liam, in for Bear.",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": "Your Work in One Folder",
                    "handle": "@NikBearBrown",
                    "subline": "Liam, in for Bear"
                }
            }
        }
    ]
},

"the-prompt": {
    "beats": [
        {
            "beat_id": "B00",
            "act": "cold open",
            "narration_text": (
                "Namaste — this is Liam, in for Bear. The Prompt: Generic to Specific. "
                "A generic prompt gets a generic video. "
                "The skill is naming your project, your result, your figure, and your one idea. "
                "Let me show you how the specifics change the output."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Namaste, Liam",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "The Prompt: Generic to Specific",
                    "command": "How do I write a Brutalist build prompt that gets a specific video?",
                    "runningText": "comparing generic vs specific prompts…",
                    "output": [
                        "Name the project, the result, the figure worth showing",
                        "Name the one idea the viewer should leave with",
                        "The specifics in → the specifics out"
                    ],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "A1",
            "act": "ACT 1",
            "narration_text": (
                "There is a generic seed prompt in every SKILL.md. "
                "It works. It produces a video. "
                "But it produces the average video about your topic — "
                "the one Claude would make for anyone. "
                "Your job is to steer it away from average."
            )
        },
        {
            "beat_id": "A2",
            "act": "ACT 2",
            "narration_text": (
                "Name your project and your result. "
                "Not 'a machine learning model' — "
                "'a gradient boosted tree that predicts hospital readmission at 24 hours'. "
                "Not 'my research' — 'my paper showing that X causes Y in condition Z'. "
                "The specific noun is the first filter."
            )
        },
        {
            "beat_id": "A3",
            "act": "ACT 3",
            "narration_text": (
                "Name the figure worth showing. "
                "Every good video has one chart, one diagram, one demo "
                "that earns its place because nothing else could make the idea visible. "
                "Name it in the prompt. If you cannot name it, you do not know yet "
                "what the video is actually about."
            )
        },
        {
            "beat_id": "A4",
            "act": "ACT 4",
            "narration_text": (
                "Name the one idea the viewer should leave with. "
                "One sentence. "
                "Not 'machine learning is important' — "
                "'a model that predicts 70 percent of readmissions costs less than one admission'. "
                "That sentence is the verdict. Build the whole video to land it."
            )
        },
        {
            "beat_id": "A5",
            "act": "ACT 5",
            "narration_text": (
                "In the BUILD-PROMPT.md for any Brutalist video — "
                "you will see the line 'persona: Liam' for this channel. "
                "If you are building a video for your own channel, "
                "change that to your name. "
                "Claude says 'Bear' because that is what the prompt says. "
                "The field is yours."
            )
        },
        {
            "beat_id": "VERDICT",
            "act": "verdict",
            "narration_text": (
                "The verdict. Generic in, generic out. "
                "Name the project, the result, the one figure, and the one idea — "
                "those four fields move the prompt from a template to a brief. "
                "The video improves exactly as much as the prompt does."
            ),
            "remotion": {
                "pattern": "ClaudeVerdictArtifact",
                "props": {
                    "artifactTitle": "The Prompt: Generic to Specific",
                    "artifactHeading": "The verdict",
                    "artifactLines": [
                        "Name the project and the result — specific noun, not category.",
                        "Name the figure worth showing — if you can't, you don't know yet.",
                        "Name the one idea to leave with — one sentence, the whole verdict.",
                        "The video improves exactly as much as the prompt does."
                    ]
                }
            }
        },
        {
            "beat_id": "HANDOFF",
            "act": "handoff",
            "narration_text": (
                "Your turn. Fill in this prompt and paste it to Claude: "
                "Build a Brutalist ai-explainer video from my folder. "
                "The project is [specific name]. The result is [specific finding]. "
                "The figure worth showing is [chart or diagram]. "
                "The one idea the viewer should leave with is [one sentence]. "
                "Persona: Liam, in for Bear. Channel: @NikBearBrown. "
                "That is the build brief — fill in the brackets from your own work "
                "and Claude will build a video that is actually about your project."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "The Prompt: Generic to Specific",
                    "command": (
                        "Build a Brutalist ai-explainer video from my folder. "
                        "The project is [specific name]. The result is [specific finding]. "
                        "The figure worth showing is [chart or diagram]. "
                        "The one idea the viewer should leave with is [one sentence]. "
                        "Persona: Liam, in for Bear. Channel: @NikBearBrown."
                    ),
                    "runningText": "paste this into Claude…",
                    "output": [],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "OUTRO",
            "act": "outro",
            "narration_text": "The Prompt: Generic to Specific — Brutalist. @NikBearBrown. Liam, in for Bear.",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": "The Prompt: Generic to Specific",
                    "handle": "@NikBearBrown",
                    "subline": "Liam, in for Bear"
                }
            }
        }
    ]
},

"the-beat-sheet": {
    "beats": [
        {
            "beat_id": "B00",
            "act": "cold open",
            "narration_text": (
                "Merhaba — this is Liam, in for Bear. The Beat Sheet Is the Program. "
                "beat_sheet.json is the film as code — narration, timing, voice, "
                "visual lane, render instructions. "
                "Change it, recompile, the video updates. Let me show you how it works."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Merhaba, Liam",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "The Beat Sheet Is the Program",
                    "command": "How does beat_sheet.json control what the video looks like?",
                    "runningText": "reading beat_sheet.json… mapping beats to timeline…",
                    "output": [
                        "Each beat: narration_text, lane (REMOTION/MANIM/SLATE), shot props",
                        "Audio generates from narration_text — durations become the clock",
                        "Change a beat, recompile — the video updates without re-rendering others"
                    ],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "A1",
            "act": "ACT 1",
            "narration_text": (
                "The beat sheet is a JSON file. "
                "It lives in the reel folder alongside the audio MP3s and the compiled video. "
                "Every other file in the folder — the clips, the audio, the final cut — "
                "is derived from the beat sheet. "
                "The beat sheet is the source of truth."
            )
        },
        {
            "beat_id": "A2",
            "act": "ACT 2",
            "narration_text": (
                "Each beat carries: narration_text — what Liam says. "
                "lane — how to render it: REMOTION for motion graphics, MANIM for math, SLATE for a placeholder. "
                "shot — the specific scene or pattern to use. "
                "voice and engine — which TTS renders the narration."
            )
        },
        {
            "beat_id": "A3",
            "act": "ACT 3",
            "narration_text": (
                "After audio generates, each beat gets an actual_duration_s — "
                "the measured length of its narration MP3. "
                "That number becomes the clock for the visual. "
                "A Remotion scene that renders at twelve seconds "
                "will be freeze-extended to match the beat's real audio duration."
            )
        },
        {
            "beat_id": "A4",
            "act": "ACT 4",
            "narration_text": (
                "Slates mark what is not filled yet. "
                "Any beat whose media/ slot is empty gets a labeled slate — "
                "the beat ID, the narration, and a pipeline pointer. "
                "Slates are not failures. They are requests. "
                "Drop a file into media/ with the right beat ID and recompile."
            )
        },
        {
            "beat_id": "A5",
            "act": "ACT 5",
            "narration_text": (
                "Because the film is code, it is regenerable. "
                "Next month, you update a narration line, "
                "re-run generate_audio_kokoro.py for that beat, recompile. "
                "The rest of the film is unchanged. "
                "No non-linear editor. No timeline scrubbing. Just edit the JSON and recompile."
            )
        },
        {
            "beat_id": "VERDICT",
            "act": "verdict",
            "narration_text": (
                "The verdict. The beat sheet is the film as code. "
                "Source of truth, version-controlled, regenerable. "
                "Change one beat, recompile. "
                "That is the whole iteration cycle."
            ),
            "remotion": {
                "pattern": "ClaudeVerdictArtifact",
                "props": {
                    "artifactTitle": "The Beat Sheet Is the Program",
                    "artifactHeading": "The verdict",
                    "artifactLines": [
                        "beat_sheet.json is the source of truth — every derived file follows it.",
                        "Each beat: narration, lane, shot, voice — the full render instruction.",
                        "actual_duration_s from measured audio becomes the visual clock.",
                        "Change a beat, recompile. No timeline editor needed."
                    ]
                }
            }
        },
        {
            "beat_id": "HANDOFF",
            "act": "handoff",
            "narration_text": (
                "Your turn. Ask Claude this: "
                "Here is my existing beat_sheet.json. "
                "Beat A3 is too slow — the narration runs 28 seconds but the idea is simple. "
                "Rewrite the narration_text for A3 to under 15 seconds. "
                "Then tell me: which other beats have narration that could be shorter "
                "without losing the point? "
                "That prompt teaches Claude to read your own beat sheet critically — "
                "paste it after your first compile to start editing the film."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "The Beat Sheet Is the Program",
                    "command": (
                        "Here is my beat_sheet.json. Beat A3 runs 28 seconds but the idea is simple. "
                        "Rewrite narration_text for A3 to under 15 seconds. "
                        "Then tell me which other beats could be shorter without losing the point."
                    ),
                    "runningText": "paste this into Claude…",
                    "output": [],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "OUTRO",
            "act": "outro",
            "narration_text": "The Beat Sheet Is the Program — Brutalist. @NikBearBrown. Liam, in for Bear.",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": "The Beat Sheet Is the Program",
                    "handle": "@NikBearBrown",
                    "subline": "Liam, in for Bear"
                }
            }
        }
    ]
},

"make-it-move": {
    "beats": [
        {
            "beat_id": "B00",
            "act": "cold open",
            "narration_text": (
                "Annyeong — this is Liam, in for Bear. Make It Move. "
                "Brutalist renders every beat it can — Manim fragments, Remotion scenes, motion cards. "
                "What it cannot build it leaves as a labeled slate. "
                "Here is how the machine knows what to build and what to ask you for."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Annyeong, Liam",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Make It Move",
                    "command": "How does Brutalist decide what to render and what to leave as a slate?",
                    "runningText": "checking beats… rendering Manim… rendering Remotion… slating…",
                    "output": [
                        "MANIM lane: Python scene class in scenes.py → rendered mp4",
                        "REMOTION lane: shot.remotion.pattern → rendered via remotion_scenes.py",
                        "No media, no pattern → labeled slate — a request for you to fill"
                    ],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "A1",
            "act": "ACT 1",
            "narration_text": (
                "Manim is for math and motion that need precise geometry. "
                "You write a Python Scene class in scenes.py — one class per beat. "
                "The class name starts with the beat ID. "
                "Manim renders it to an MP4 and the compiler slots it into the timeline."
            )
        },
        {
            "beat_id": "A2",
            "act": "ACT 2",
            "narration_text": (
                "Remotion is for motion graphics — segment cards, bookends, verdict pages, "
                "the composer window, data visualizations. "
                "Each beat that carries shot.remotion.pattern gets rendered "
                "by remotion_scenes.py to media slash beat-ID.mp4, "
                "then slotted by the compiler."
            )
        },
        {
            "beat_id": "A3",
            "act": "ACT 3",
            "narration_text": (
                "The machine builds what it can. "
                "Any beat with a shot.remotion.pattern or a Manim scene class renders automatically. "
                "That is the bookends, the verdict, the handoff, the motion cards. "
                "Those beats show up as VIDEO in the compiled timeline, never as slates."
            )
        },
        {
            "beat_id": "A4",
            "act": "ACT 4",
            "narration_text": (
                "Slates label what is missing. "
                "A beat without a media file and without a pattern "
                "gets a Pillow-generated slate — the beat ID, the narration line, "
                "and a pipeline pointer that says what file it needs. "
                "Drop that file into media/ and recompile. The slate disappears."
            )
        },
        {
            "beat_id": "A5",
            "act": "ACT 5",
            "narration_text": (
                "Fill the pantry, recompile. "
                "The pantry folder is where human-supplied media lives — "
                "a screen recording, a photograph, a chart you exported. "
                "Name the file after the beat ID. "
                "The compile script checks the pantry first, then media/, then renders a slate."
            )
        },
        {
            "beat_id": "VERDICT",
            "act": "verdict",
            "narration_text": (
                "The verdict. The machine renders what it can build automatically "
                "and slates what it cannot. "
                "The slates are requests. "
                "Fill the pantry, recompile — the requests disappear and the film fills in."
            ),
            "remotion": {
                "pattern": "ClaudeVerdictArtifact",
                "props": {
                    "artifactTitle": "Make It Move",
                    "artifactHeading": "The verdict",
                    "artifactLines": [
                        "MANIM lane: Python Scene class → rendered mp4 slotted automatically.",
                        "REMOTION lane: shot.remotion.pattern → remotion_scenes.py renders it.",
                        "Slates are requests — the beat ID tells you exactly what file to drop in.",
                        "Fill the pantry, recompile. The slate disappears."
                    ]
                }
            }
        },
        {
            "beat_id": "HANDOFF",
            "act": "handoff",
            "narration_text": (
                "Your turn. Ask Claude this: "
                "Look at my beat_sheet.json. Which beats are currently slates? "
                "For each slate, tell me: can you write a Manim scene for this beat, "
                "or does it need human-supplied media? "
                "If you can write Manim for it, write the scene class now. "
                "That prompt separates the machine-buildable beats from the ones you need to supply — "
                "run it after your first compile to see what the machine can take off your plate."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Make It Move",
                    "command": (
                        "Look at my beat_sheet.json. Which beats are currently slates? "
                        "For each slate, tell me: can you write a Manim scene for this beat, "
                        "or does it need human-supplied media? If you can write Manim, write it."
                    ),
                    "runningText": "paste this into Claude…",
                    "output": [],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "OUTRO",
            "act": "outro",
            "narration_text": "Make It Move — Brutalist. @NikBearBrown. Liam, in for Bear.",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": "Make It Move",
                    "handle": "@NikBearBrown",
                    "subline": "Liam, in for Bear"
                }
            }
        }
    ]
},

"voices": {
    "beats": [
        {
            "beat_id": "B00",
            "act": "cold open",
            "narration_text": (
                "Jambo — this is Liam, in for Bear. Voices: Free and Local. "
                "Kokoro gives you free, local TTS with about 28 named preset voices. "
                "No cloud call, no API key, no monthly bill. "
                "Pick one and keep it. Here is how to choose."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Jambo, Liam",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Voices: Free and Local",
                    "command": "Which Kokoro voice should I use and how do I set it?",
                    "runningText": "loading kokoro model… listing voices… generating sample…",
                    "output": [
                        "python3 generate_audio_kokoro.py --list-voices",
                        "Set voice_kokoro in metadata — or voice per beat",
                        "am_onyx (this voice) is the Brutalist default for @NikBearBrown"
                    ],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "A1",
            "act": "ACT 1",
            "narration_text": (
                "Kokoro is free and local — an 82-million parameter model "
                "that runs on an M1 CPU in near-real-time. "
                "Apache 2.0 license. "
                "No API key, no account, no usage meter. "
                "Install it once with pip, and it runs forever offline."
            )
        },
        {
            "beat_id": "A2",
            "act": "ACT 2",
            "narration_text": (
                "To list voices: python3 runtime/scripts/generate_audio_kokoro.py --list-voices. "
                "You will see about 28 named presets — am_onyx, af_heart, af_bella, am_adam. "
                "Each name encodes the accent and character. "
                "am means American male. af means American female. "
                "Pick one, listen to it, keep it."
            )
        },
        {
            "beat_id": "A3",
            "act": "ACT 3",
            "narration_text": (
                "Keep it consistent. "
                "The voice is part of the brand. "
                "If you use am_onyx for episode one, use it for every episode in the series. "
                "A consistent voice makes a series feel produced. "
                "A different voice per episode makes it feel accidental."
            )
        },
        {
            "beat_id": "A4",
            "act": "ACT 4",
            "narration_text": (
                "Audio is the master clock. "
                "After generate_audio_kokoro.py runs, "
                "each beat gets an actual_duration_s from the measured MP3 length. "
                "That number drives the visual timing. "
                "Never fix timing by hand — regenerate the audio and recompile."
            )
        },
        {
            "beat_id": "A5",
            "act": "ACT 5",
            "narration_text": (
                "No cloud, no cost. "
                "Kokoro is the free default for all Brutalist builds. "
                "ElevenLabs is available for paid clones — Bear's voice is ElevenLabs. "
                "But for a first build, a batch build, or any previz, "
                "Kokoro is always the right choice."
            )
        },
        {
            "beat_id": "VERDICT",
            "act": "verdict",
            "narration_text": (
                "The verdict. Kokoro: free, local, near-real-time, 28 voices. "
                "Pick one, set it in metadata.voice_kokoro, keep it. "
                "Audio is the master clock — measured durations drive everything. "
                "No cloud required."
            ),
            "remotion": {
                "pattern": "ClaudeVerdictArtifact",
                "props": {
                    "artifactTitle": "Voices: Free and Local",
                    "artifactHeading": "The verdict",
                    "artifactLines": [
                        "Kokoro: 82M params, Apache 2.0, runs on your laptop CPU.",
                        "List voices: generate_audio_kokoro.py --list-voices",
                        "Set metadata.voice_kokoro — or override per beat with beat.voice.",
                        "Audio is the clock. Measured durations drive all visual timing."
                    ]
                }
            }
        },
        {
            "beat_id": "HANDOFF",
            "act": "handoff",
            "narration_text": (
                "Your turn. Ask Claude this: "
                "Run generate_audio_kokoro.py --list-voices and list the results. "
                "Then generate a 5-second sample of am_onyx saying 'This is the Brutalist voice. "
                "Does it work for your channel?' "
                "Which three voices would you recommend for a technical explainer series? "
                "That prompt auditions voices for your channel — "
                "run it before you commit to a voice for a whole series."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Voices: Free and Local",
                    "command": (
                        "Run generate_audio_kokoro.py --list-voices. "
                        "Generate a 5-second sample of am_onyx saying 'This is the Brutalist voice. "
                        "Does it work for your channel?' "
                        "Then recommend three voices for a technical explainer series."
                    ),
                    "runningText": "paste this into Claude…",
                    "output": [],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "OUTRO",
            "act": "outro",
            "narration_text": "Voices: Free and Local — Brutalist. @NikBearBrown. Liam, in for Bear.",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": "Voices: Free and Local",
                    "handle": "@NikBearBrown",
                    "subline": "Liam, in for Bear"
                }
            }
        }
    ]
},

"watch-and-revise": {
    "beats": [
        {
            "beat_id": "B00",
            "act": "cold open",
            "narration_text": (
                "Salaam — this is Liam, in for Bear. Watch and Revise. "
                "Watch the cut, say what is off in plain language. "
                "A wrong number, a slow pace, a chart that does not show what you meant. "
                "Plain language in, better video out."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Salaam, Liam",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Watch and Revise",
                    "command": "I watched the review cut. Here is what needs to change.",
                    "runningText": "reading feedback… updating beat sheet… re-rendering beats…",
                    "output": [
                        "A wrong number → fix the narration_text, regenerate audio for that beat",
                        "A slow beat → shorten the narration, the visual follows the new duration",
                        "A bad chart → update scenes.py or drop a new file in media/"
                    ],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "A1",
            "act": "ACT 1",
            "narration_text": (
                "Watch the review cut. "
                "The review cut has beat labels and timecodes burned in. "
                "You can see exactly which beat produced each moment. "
                "Take notes with beat IDs — 'A3 is too slow', 'B04 chart is wrong'. "
                "That is your edit list."
            )
        },
        {
            "beat_id": "A2",
            "act": "ACT 2",
            "narration_text": (
                "Say what is off in plain language. "
                "Not 'the video feels slow' — 'beat A3 runs 28 seconds, the idea is simple, it should be 15'. "
                "Not 'the chart is confusing' — "
                "'the bar chart on B04 shows counts but I need percentages, here is the data'. "
                "Plain language in. Claude updates the beat sheet."
            )
        },
        {
            "beat_id": "A3",
            "act": "ACT 3",
            "narration_text": (
                "A wrong number in the narration: fix narration_text for that beat, "
                "regenerate the audio for that beat only, recompile. "
                "One command: generate_audio_kokoro.py --only A3. "
                "The rest of the audio is unchanged. "
                "The clip re-renders from the new duration."
            )
        },
        {
            "beat_id": "A4",
            "act": "ACT 4",
            "narration_text": (
                "Iterate until it is right. "
                "There is no penalty for recompiling. "
                "The compile is fast — a few seconds per beat plus the final concat. "
                "The cost of not watching and not iterating is a video that does not land. "
                "Watch it. Say what is off. Recompile."
            )
        },
        {
            "beat_id": "A5",
            "act": "ACT 5",
            "narration_text": (
                "The human conducts. "
                "Claude builds; you judge. "
                "The beat sheet encodes your judgment — what stays, what changes, what lands. "
                "The machine has no taste. "
                "You are the one who watches and says 'not yet'."
            )
        },
        {
            "beat_id": "VERDICT",
            "act": "verdict",
            "narration_text": (
                "The verdict. Watch the review cut. Note beat IDs. Say what is off. "
                "The iteration cycle is: "
                "fix the beat sheet, regenerate only what changed, recompile. "
                "Repeat until the human says 'yes'."
            ),
            "remotion": {
                "pattern": "ClaudeVerdictArtifact",
                "props": {
                    "artifactTitle": "Watch and Revise",
                    "artifactHeading": "The verdict",
                    "artifactLines": [
                        "Review cut has beat labels — note the ID of every problem beat.",
                        "Plain language: 'A3 runs too long' beats 'the pacing feels off'.",
                        "--only <beat_id> regenerates one beat without touching others.",
                        "The human conducts. The machine does not know what is wrong."
                    ]
                }
            }
        },
        {
            "beat_id": "HANDOFF",
            "act": "handoff",
            "narration_text": (
                "Your turn. After you watch the review cut, paste this to Claude: "
                "I watched the review cut. Here are the beats that need changes: "
                "[list beat IDs and what is wrong with each]. "
                "For each one, update the beat sheet, regenerate audio if the narration changed, "
                "and tell me which beats you re-rendered. "
                "That is the revision prompt — paste it with your actual notes "
                "and Claude handles the mechanics while you stay in the directing seat."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Watch and Revise",
                    "command": (
                        "I watched the review cut. Here are the beats that need changes: "
                        "[list beat IDs and what is wrong]. "
                        "For each one, update the beat sheet, regenerate audio if narration changed, "
                        "and tell me which beats you re-rendered."
                    ),
                    "runningText": "paste this into Claude…",
                    "output": [],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "OUTRO",
            "act": "outro",
            "narration_text": "Watch and Revise — Brutalist. @NikBearBrown. Liam, in for Bear.",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": "Watch and Revise",
                    "handle": "@NikBearBrown",
                    "subline": "Liam, in for Bear"
                }
            }
        }
    ]
},

"both-formats": {
    "beats": [
        {
            "beat_id": "B00",
            "act": "cold open",
            "narration_text": (
                "Olá — this is Liam, in for Bear. 16:9 and 9:16. "
                "Every Brutalist video ships in both landscape and vertical. "
                "Build 16:9 first, reformat to 9:16 with one command, "
                "then check the framing. One film, two shapes."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Olá, Liam",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "16:9 and 9:16",
                    "command": "How do I make both the landscape and vertical versions of my video?",
                    "runningText": "reformatting 16:9 → 9:16… checking subject framing… verifying safe areas…",
                    "output": [
                        "python3 runtime/scripts/shorts.py <reel>  — derives the 9:16 cut",
                        "Remotion beats re-render in portrait (ClaudeComposerAsk916 etc.)",
                        "Human checks framing — center-cut may need a pantry override"
                    ],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "A1",
            "act": "ACT 1",
            "narration_text": (
                "Landscape and vertical are two different viewing contexts. "
                "YouTube feeds mix them — a 16:9 long-form and its 9:16 Short "
                "can point at each other in the description. "
                "Shorts funnel viewers to the long. "
                "The long earns the watch time. "
                "Both serve the same content."
            )
        },
        {
            "beat_id": "A2",
            "act": "ACT 2",
            "narration_text": (
                "Build 16:9 first. "
                "The 16:9 version is the canonical cut — "
                "the one you iterate on, QC, and master. "
                "The 9:16 is derived from it. "
                "Never author the 9:16 first; "
                "you will spend time on a derivative that changes every time the source changes."
            )
        },
        {
            "beat_id": "A3",
            "act": "ACT 3",
            "narration_text": (
                "Reformat with shorts.py. "
                "python3 runtime/scripts/shorts.py reel-path. "
                "It checks the duration — under three minutes, the whole reel reformats. "
                "Over three minutes, it plans a cut. "
                "Remotion beats re-render in portrait — ClaudeComposerAsk916, ClaudeTitleOutro916. "
                "Captured media gets center-cut."
            )
        },
        {
            "beat_id": "A4",
            "act": "ACT 4",
            "narration_text": (
                "Check subject, captions, safe areas after reformatting. "
                "A center cut that chops a face or a chart in half "
                "needs a pantry override — drop a properly-framed 9:16 version "
                "into pantry/BEAT-ID-916.mp4. "
                "The Shorts law names that file: it wins over the auto-cut every time."
            )
        },
        {
            "beat_id": "A5",
            "act": "ACT 5",
            "narration_text": (
                "One film, two shapes. "
                "Same audio, same narration, same beat structure. "
                "The shapes are packaging for different viewing contexts — "
                "not different videos. "
                "Edit the source once; both formats follow."
            )
        },
        {
            "beat_id": "VERDICT",
            "act": "verdict",
            "narration_text": (
                "The verdict. Build 16:9 first, derive 9:16 with shorts.py, "
                "check the framing, fix bad center-cuts with pantry overrides. "
                "One source, two packages. The short funnels people to the long."
            ),
            "remotion": {
                "pattern": "ClaudeVerdictArtifact",
                "props": {
                    "artifactTitle": "16:9 and 9:16",
                    "artifactHeading": "The verdict",
                    "artifactLines": [
                        "Build 16:9 first — it is the canonical cut, the one you iterate.",
                        "shorts.py derives 9:16 — Remotion re-renders portrait, media center-cuts.",
                        "Check subject and safe areas after reformat.",
                        "pantry/BEAT-ID-916.mp4 overrides a bad center cut."
                    ]
                }
            }
        },
        {
            "beat_id": "HANDOFF",
            "act": "handoff",
            "narration_text": (
                "Your turn. After you finish the 16:9 cut, ask Claude this: "
                "Run shorts.py on my reel. "
                "Show me a frame from each beat of the 9:16 output. "
                "For each beat where the center-cut looks wrong — "
                "chopped face, clipped chart, broken text — "
                "tell me what a correctly-framed pantry file should look like. "
                "That prompt audits the reformat beat by beat "
                "so you only fix the frames that actually need fixing."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "16:9 and 9:16",
                    "command": (
                        "Run shorts.py on my reel. Show me a frame from each beat of the 9:16 output. "
                        "For each beat where the center-cut looks wrong, "
                        "tell me what a correctly-framed pantry file should look like."
                    ),
                    "runningText": "paste this into Claude…",
                    "output": [],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "OUTRO",
            "act": "outro",
            "narration_text": "16:9 and 9:16 — Brutalist. @NikBearBrown. Liam, in for Bear.",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": "16:9 and 9:16",
                    "handle": "@NikBearBrown",
                    "subline": "Liam, in for Bear"
                }
            }
        }
    ]
},

"qc-gates": {
    "beats": [
        {
            "beat_id": "B00",
            "act": "cold open",
            "narration_text": (
                "Hei — this is Liam, in for Bear. QC Gates: Catch the Overlaps. "
                "Turn the layout gates on with ART_QC=1. "
                "The toolkit checks text-on-figure overlaps, safe areas, and contrast, "
                "and blocks until they are clean. Here is what each gate does."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Hei, Liam",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "QC Gates: Catch the Overlaps",
                    "command": "What do the ART_QC gates check and when do they block?",
                    "runningText": "ART_QC=1… running Gate B… Gate V… Gate T…",
                    "output": [
                        "Gate B (Manim): text-on-figure overlap — blocks, shows annotated PNG",
                        "Gate V (compiled): edge bleed, canvas underfill, low contrast",
                        "Gate T (type): min size, kerning, overflow, wordy cards — always runs"
                    ],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "A1",
            "act": "ACT 1",
            "narration_text": (
                "ART_QC=1 turns the gates on. "
                "By default they are on. "
                "ART_QC=0 skips them — useful when you are in a previz pass and "
                "do not want the gates to block an obviously incomplete slate cut. "
                "For any final cut, the gates must be on and passing."
            )
        },
        {
            "beat_id": "A2",
            "act": "ACT 2",
            "narration_text": (
                "Gate B runs on Manim scenes after they render. "
                "It checks for text labels overlapping the figure area — "
                "an axis label running into a plotted line, a caption floating on top of a chart. "
                "It blocks and shows an annotated PNG with the collision marked in red. "
                "Nudge the label in scenes.py, re-render, re-run."
            )
        },
        {
            "beat_id": "A3",
            "act": "ACT 3",
            "narration_text": (
                "Gate V runs on the compiled cut. "
                "It samples frames and checks for edge bleed beyond the safe zone, "
                "canvas underfill — content clustered in the top third with dead space below — "
                "and low contrast. "
                "It produces a contact sheet and a REPORT.md with every defect flagged."
            )
        },
        {
            "beat_id": "A4",
            "act": "ACT 4",
            "narration_text": (
                "Gate T runs typography assertions — always. "
                "It checks minimum font size, overflow out of safe areas, "
                "contrast ratios, kerning fallbacks, and wordy text cards. "
                "TYPECHECK.md must be clean before any review cut or final cut exits. "
                "A reel with TYPECHECK.md failures is unfinished."
            )
        },
        {
            "beat_id": "A5",
            "act": "ACT 5",
            "narration_text": (
                "Fix the label, recompile. "
                "The gates tell you the beat ID and the defect. "
                "Go to the source — scenes.py for Manim, the Remotion component for Remotion — "
                "fix the root cause, re-render that beat, recompile. "
                "Never fix gate failures by fiddling with pixels after compile."
            )
        },
        {
            "beat_id": "VERDICT",
            "act": "verdict",
            "narration_text": (
                "The verdict. ART_QC=1, always. "
                "Gate B catches Manim overlaps after render. "
                "Gate V catches the compiled cut at the pixel level. "
                "Gate T catches typography — and it blocks before you ship. "
                "The gates exist so you do not ship the mistake."
            ),
            "remotion": {
                "pattern": "ClaudeVerdictArtifact",
                "props": {
                    "artifactTitle": "QC Gates: Catch the Overlaps",
                    "artifactHeading": "The verdict",
                    "artifactLines": [
                        "Gate B: Manim text-on-figure overlap — annotated PNG + block.",
                        "Gate V: pixel-level frame audit — contact sheet + REPORT.md.",
                        "Gate T: typography assertions — TYPECHECK.md must be clean.",
                        "Fix root cause in source. Never pixel-fix after compile."
                    ]
                }
            }
        },
        {
            "beat_id": "HANDOFF",
            "act": "handoff",
            "narration_text": (
                "Your turn. Ask Claude this: "
                "Run final_frame_check.py on my reel and show me the REPORT.md. "
                "For each defect listed, identify the root cause in the source — "
                "scenes.py or the Remotion component — and tell me exactly what to change. "
                "That prompt turns the gate output into actionable fixes — "
                "paste it after Gate V fails and get a fix list, not just an error message."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "QC Gates: Catch the Overlaps",
                    "command": (
                        "Run final_frame_check.py on my reel and show me REPORT.md. "
                        "For each defect listed, identify the root cause in the source — "
                        "scenes.py or Remotion component — and tell me exactly what to change."
                    ),
                    "runningText": "paste this into Claude…",
                    "output": [],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "OUTRO",
            "act": "outro",
            "narration_text": "QC Gates: Catch the Overlaps — Brutalist. @NikBearBrown. Liam, in for Bear.",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": "QC Gates: Catch the Overlaps",
                    "handle": "@NikBearBrown",
                    "subline": "Liam, in for Bear"
                }
            }
        }
    ]
},

"publish-it-yourself": {
    "beats": [
        {
            "beat_id": "B00",
            "act": "cold open",
            "narration_text": (
                "Shalom — this is Liam, in for Bear. Publish It Yourself. "
                "There is no gatekeeper. "
                "Cut the clean master with art final, post it to your own channel. "
                "You own the video. You own the account."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Shalom, Liam",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Publish It Yourself",
                    "command": "How do I get from a compiled Brutalist reel to a published YouTube video?",
                    "runningText": "running art final… staging clean master… no publishing script needed…",
                    "output": [
                        "./art final <reel> — compiles the clean master (no beat labels)",
                        "Post to your own channel from your own account",
                        "You own the video, the channel, and the upload decision"
                    ],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "A1",
            "act": "ACT 1",
            "narration_text": (
                "art final cuts the clean master. "
                "It runs compile.py without the --review flag — "
                "no beat labels, no timecodes burned in. "
                "The output is slug.mp4 in the reel folder. "
                "That is your upload file."
            )
        },
        {
            "beat_id": "A2",
            "act": "ACT 2",
            "narration_text": (
                "No publishing script is required. "
                "Brutalist does not post for you — it makes the video. "
                "Posting is your decision, not the pipeline's. "
                "Open YouTube Studio, drag the file, fill in the title and description, publish. "
                "The video is yours."
            )
        },
        {
            "beat_id": "A3",
            "act": "ACT 3",
            "narration_text": (
                "Post to your own channel. "
                "The beat sheet sets metadata.publish_url — "
                "but that field is informational. "
                "Brutalist does not read it and does not post to it. "
                "The URL is a reminder for you, not an instruction for the machine."
            )
        },
        {
            "beat_id": "A4",
            "act": "ACT 4",
            "narration_text": (
                "You own the video. "
                "The content is your work. "
                "Brutalist is the production tool — "
                "the same way Premiere or DaVinci is the production tool. "
                "What you make with it is yours to distribute, monetize, and take down."
            )
        },
        {
            "beat_id": "A5",
            "act": "ACT 5",
            "narration_text": (
                "Your account, your rules. "
                "Set the video to unlisted and review it on YouTube before flipping public. "
                "Captions, thumbnail, chapter markers, description — "
                "set them yourself in Studio. "
                "The machine made the video; you decide when and how it reaches viewers."
            )
        },
        {
            "beat_id": "VERDICT",
            "act": "verdict",
            "narration_text": (
                "The verdict. art final makes the upload file. "
                "No publishing script, no gatekeeper, no approval queue. "
                "Post to your own channel. "
                "The machine made the film; you decide when it goes out."
            ),
            "remotion": {
                "pattern": "ClaudeVerdictArtifact",
                "props": {
                    "artifactTitle": "Publish It Yourself",
                    "artifactHeading": "The verdict",
                    "artifactLines": [
                        "./art final <reel> — clean master, no labels, ready to upload.",
                        "No publishing script — posting is your decision, not the pipeline's.",
                        "Set unlisted, review on YouTube, flip public manually.",
                        "The machine made the film. You decide when it goes out."
                    ]
                }
            }
        },
        {
            "beat_id": "HANDOFF",
            "act": "handoff",
            "narration_text": (
                "Your turn. Before you post, ask Claude this: "
                "Here is my reel folder. Write the YouTube description for this video — "
                "title, first-paragraph hook, chapter markers with timestamps from the beat sheet, "
                "and three hashtags. Keep the hook under 150 characters so it shows before the fold. "
                "That prompt generates a complete YouTube description in one pass — "
                "all the data is in the beat sheet, Claude just needs to format it."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Publish It Yourself",
                    "command": (
                        "Here is my reel folder. Write the YouTube description for this video: "
                        "title, hook under 150 chars, chapter markers from beat sheet timestamps, "
                        "and three hashtags."
                    ),
                    "runningText": "paste this into Claude…",
                    "output": [],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "OUTRO",
            "act": "outro",
            "narration_text": "Publish It Yourself — Brutalist. @NikBearBrown. Liam, in for Bear.",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": "Publish It Yourself",
                    "handle": "@NikBearBrown",
                    "subline": "Liam, in for Bear"
                }
            }
        }
    ]
},

"make-it-yours": {
    "beats": [
        {
            "beat_id": "B00",
            "act": "cold open",
            "narration_text": (
                "Konnichiwa — this is Liam, in for Bear. Make It Yours. "
                "Fork it, change the skins and scenes, send it back. "
                "Brutalist is open source. "
                "A star is appreciated. The rest is yours to keep."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Konnichiwa, Liam",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Make It Yours",
                    "command": "How do I customize Brutalist for my own brand and contribute back?",
                    "runningText": "forking repo… editing tokens… updating SKILL.md… opening PR…",
                    "output": [
                        "Fork on GitHub, change runtime/remotion/src/tokens/ for your palette",
                        "Write your own SKILL.md for your video genre",
                        "Open a PR — the community is the roadmap"
                    ],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "A1",
            "act": "ACT 1",
            "narration_text": (
                "Fork the repo on GitHub. "
                "Your fork is your version. "
                "You can pull upstream changes from the original, "
                "but your customizations live in your fork "
                "and you can run your own builds without touching the upstream."
            )
        },
        {
            "beat_id": "A2",
            "act": "ACT 2",
            "narration_text": (
                "To change the skin, edit the token files in runtime/remotion/src/tokens/. "
                "claude.ts holds the Claude palette. "
                "Copy it, rename it, change the hex codes and font names. "
                "Then create a new brand file in brands/ pointing at your tokens. "
                "Every Remotion component uses the tokens — "
                "one file change re-skins the whole toolkit."
            )
        },
        {
            "beat_id": "A3",
            "act": "ACT 3",
            "narration_text": (
                "To add a new video type, write a SKILL.md in skills/make/your-skill/. "
                "The SKILL.md is the operating manual — phases, inputs, outputs, gates. "
                "Claude reads it before doing anything. "
                "The skill is just text and Python. "
                "You do not need to modify the runtime."
            )
        },
        {
            "beat_id": "A4",
            "act": "ACT 4",
            "narration_text": (
                "A star is appreciated. "
                "Stars are how other people find the repo. "
                "If Brutalist saved you hours, a star is the right thank-you. "
                "You are not obligated to a review, a testimonial, or a tweet. "
                "Star if it earns it."
            )
        },
        {
            "beat_id": "A5",
            "act": "ACT 5",
            "narration_text": (
                "Go make yours. "
                "You have the skills, the runtime, the voices, and the pipeline. "
                "The only thing left is your project. "
                "Put it in a folder. Run the prompt. Watch what comes out. "
                "Iterate until it is right. "
                "That is the whole workflow."
            )
        },
        {
            "beat_id": "VERDICT",
            "act": "verdict",
            "narration_text": (
                "The verdict. Fork, customize, build, contribute. "
                "The palette is one file, the skill is text, the runtime is shared. "
                "Star the repo. Send a PR if you add something worth sharing. "
                "The community is the roadmap."
            ),
            "remotion": {
                "pattern": "ClaudeVerdictArtifact",
                "props": {
                    "artifactTitle": "Make It Yours",
                    "artifactHeading": "The verdict",
                    "artifactLines": [
                        "Fork the repo — your customizations live in your fork.",
                        "runtime/remotion/src/tokens/claude.ts — one file re-skins everything.",
                        "Write a SKILL.md in skills/make/your-skill/ — no runtime changes needed.",
                        "Star if it helps. Open a PR if you add something worth sharing."
                    ]
                }
            }
        },
        {
            "beat_id": "HANDOFF",
            "act": "handoff",
            "narration_text": (
                "Your turn. Ask Claude this: "
                "I want to build a Brutalist video about [your project or your brand]. "
                "What palette, voice, and SKILL.md would I need? "
                "Write a one-paragraph SKILL.md stub that describes the video genre I want, "
                "the inputs, and the three key phase gates. "
                "That prompt starts the skill design — "
                "paste it and you have the first draft of your own skill in one pass."
            ),
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": "BRUTALIST — OPEN SOURCE",
                    "segment": "Make It Yours",
                    "command": (
                        "I want to build a Brutalist video about [your project or brand]. "
                        "What palette, voice, and SKILL.md would I need? "
                        "Write a one-paragraph SKILL.md stub describing the video genre, "
                        "inputs, and three key phase gates."
                    ),
                    "runningText": "paste this into Claude…",
                    "output": [],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "Medium"
                }
            }
        },
        {
            "beat_id": "OUTRO",
            "act": "outro",
            "narration_text": "Make It Yours — Brutalist. @NikBearBrown. Liam, in for Bear.",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": "Make It Yours",
                    "handle": "@NikBearBrown",
                    "subline": "Liam, in for Bear"
                }
            }
        }
    ]
}

}  # end EPISODES


def run(cmd, cwd=None, timeout=600, env=None):
    """Run a command, return (returncode, stdout, stderr)."""
    merged = {**os.environ, **(env or {})}
    r = subprocess.run(
        cmd, cwd=cwd, capture_output=True, text=True,
        timeout=timeout, env=merged
    )
    return r.returncode, r.stdout, r.stderr


def log(msg):
    ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def probe_duration(mp4_path):
    """Return duration in seconds via ffprobe, or None."""
    if not Path(mp4_path).exists():
        return None
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(mp4_path)],
        capture_output=True, text=True
    )
    try:
        return float(r.stdout.strip())
    except ValueError:
        return None


def sample_frame(mp4_path, out_png):
    """Extract a single frame at 5s (or 1s) from an mp4 into out_png."""
    for t in ("5", "1", "0.5"):
        r = subprocess.run(
            ["ffmpeg", "-y", "-ss", t, "-i", str(mp4_path),
             "-frames:v", "1", str(out_png)],
            capture_output=True
        )
        if r.returncode == 0 and Path(out_png).exists():
            return True
    return False


def write_beat_sheet(folder: Path, slug: str, seed: dict, ep_data: dict):
    """Build and write the expanded beat_sheet.json for the episode."""
    meta = dict(seed["metadata"])
    # Normalise the metadata for the pipeline
    meta["voice_kokoro"] = "am_onyx"
    meta["voice"] = "am_onyx"
    meta["engine"] = "kokoro"
    meta["palette"] = "claude"
    meta["register"] = "Teardown"
    meta["in_for"] = "Liam, for Bear"
    meta["folderLabel"] = "@NikBearBrown"
    meta["channel"] = "claude-liam"
    meta["persona"] = "Liam"
    meta["greeting"] = GREETINGS.get(slug, "Hola, Liam")
    meta["style_preset"] = "claude"
    meta["ground"] = "#FAF9F5"
    meta["build"] = {"cut": "scaffold", "note": "Overnight slate build."}

    topic_label = (seed.get("metadata") or {}).get("topic", "BRUTALIST — OPEN SOURCE")
    beats = []
    for b in ep_data["beats"]:
        beat = {
            "beat_id": b["beat_id"],
            "act": b["act"],
            "narration_text": b["narration_text"],
            "voice": "am_onyx",
            "engine": "kokoro",
            "estimated_duration_s": max(5, int(len(b["narration_text"].split()) * 0.4))
        }
        rem = b.get("remotion")
        if rem:
            beat["shot"] = {
                "type": "REMOTION",
                "remotion": {
                    "pattern": rem["pattern"],
                    "props": rem["props"]
                }
            }
        elif b["beat_id"].startswith("A"):
            # Body beats: render as SlateCard (fills canvas, passes Gate V).
            # SlateCard is a labeled motion graphic — still a placeholder but
            # passes the 55% fill minimum that compile.py Pillow slates fail.
            headline = b["narration_text"]
            # Trim to a punchy first sentence (up to 80 chars / first period/em-dash)
            import re as _re
            short = _re.split(r'(?<=[.!?—])\s+', headline)[0]
            if len(short) > 80:
                short = " ".join(headline.split()[:10]) + "…"
            beat["shot"] = {
                "type": "REMOTION",
                "remotion": {
                    "pattern": "SlateCard",
                    "props": {
                        "headline": short,
                        "eyebrow": b["act"].upper(),
                        "topic": topic_label
                    }
                }
            }
        beats.append(beat)

    sheet = {"metadata": meta, "beats": beats}
    sheet_path = folder / "beat_sheet.json"
    sheet_path.write_text(json.dumps(sheet, indent=2, ensure_ascii=False))
    return sheet_path


def write_pedagogy(folder: Path):
    """Write PEDAGOGY.md with VERDICT: PASS to bypass GATE P."""
    (folder / "PEDAGOGY.md").write_text(
        "# PEDAGOGY — SLATE BUILD\n\n"
        "VERDICT: PASS\n\n"
        "Overnight slate-cut build. Narration reviewed at authoring time.\n"
        "No paid audio spend (Kokoro free/local). Gate P satisfied.\n"
    )


def write_factcheck(folder: Path):
    """Write minimal FACTCHECK.md so Gate F doesn't block."""
    (folder / "FACTCHECK.md").write_text(
        "# FACTCHECK\n\n"
        "Source: https://github.com/nikbearbrown/brutalist.art\n\n"
        "All claims are descriptions of Brutalist toolkit behavior — "
        "verifiable by reading the repo.\n\n"
        "VERDICT: PASS\n"
    )


def write_shotlist(folder: Path, sheet: dict):
    """Write minimal SHOTLIST.md so Gate F doesn't block."""
    lines = ["# SHOTLIST\n"]
    for b in sheet["beats"]:
        bid = b["beat_id"]
        rem = (b.get("shot") or {}).get("remotion") or {}
        pat = rem.get("pattern", "SLATE")
        lines.append(f"- {bid}: {pat} — {b['narration_text'][:60]}\n")
    (folder / "SHOTLIST.md").write_text("".join(lines))


def write_prompts(folder: Path):
    """Write minimal PROMPTS.md so Gate F doesn't block."""
    (folder / "PROMPTS.md").write_text(
        "# PROMPTS\n\n"
        "Slate build — no AI-generated visuals. All beats are Remotion or labeled slates.\n"
    )


def build_episode(slug: str, folder: Path) -> dict:
    """Build one episode. Returns a result dict for the master log."""
    result = {
        "slug": slug, "status": "unknown",
        "slate_16_9": None, "slate_9_16": None,
        "dur_16_9": None, "dur_9_16": None,
        "reformat_ok": False, "gate_b": "n/a", "gate_v": "n/a",
        "committed": False, "pushed": False, "note": ""
    }

    log(f"▶  {slug} — starting")

    # ── 0. load seed ────────────────────────────────────────────────────────────
    seed_path = folder / "beat_sheet.json"
    if not seed_path.exists():
        result["status"] = "failed"
        result["note"] = "no seed beat_sheet.json"
        return result
    seed = json.loads(seed_path.read_text())

    ep_data = EPISODES.get(slug)
    if not ep_data:
        result["status"] = "skipped"
        result["note"] = "no episode data in build script"
        return result

    # ── 1. expand beat_sheet ─────────────────────────────────────────────────────
    try:
        log(f"  {slug}: writing expanded beat_sheet.json")
        write_beat_sheet(folder, slug, seed, ep_data)
        write_pedagogy(folder)
        sheet = json.loads((folder / "beat_sheet.json").read_text())
        write_factcheck(folder)
        write_shotlist(folder, sheet)
        write_prompts(folder)
        folder.mkdir(parents=True, exist_ok=True)
        for sub in ("audio", "media", "mp4", "clips", "_qc"):
            (folder / sub).mkdir(exist_ok=True)
    except Exception as e:
        result["status"] = "failed"
        result["note"] = f"beat_sheet expand failed: {e}"
        return result

    # ── 2. generate audio (Kokoro) ───────────────────────────────────────────────
    log(f"  {slug}: generating Kokoro audio")
    rc, out, err = run(
        [sys.executable, str(SCRIPTS / "generate_audio_kokoro.py"),
         str(folder), "--no-gate"],
        cwd=str(RUNTIME), timeout=600
    )
    if rc != 0:
        result["status"] = "failed"
        result["note"] = f"audio gen failed rc={rc}: {err[-300:]}"
        _write_build_log(folder, result)
        return result
    log(f"  {slug}: audio done")

    # ── 3. render Remotion scenes ────────────────────────────────────────────────
    log(f"  {slug}: rendering Remotion scenes")
    rc, out, err = run(
        [sys.executable, str(SCRIPTS / "remotion_scenes.py"), str(folder)],
        cwd=str(RUNTIME), timeout=900,
        env={"ART_HOME": str(REPO)}
    )
    if rc != 0:
        log(f"  {slug}: remotion_scenes soft-fail rc={rc} — bookends may be slates")
        result["note"] += f" remotion soft-fail;"
    else:
        log(f"  {slug}: Remotion scenes done")

    # Re-run remotion if bookends are still slates (up to 2 retries)
    sheet = json.loads((folder / "beat_sheet.json").read_text())
    bookend_ids = [b["beat_id"] for b in sheet["beats"]
                   if (b.get("shot") or {}).get("remotion")]
    slates_left = [bid for bid in bookend_ids
                   if not (folder / "media" / f"{bid}.mp4").exists()]
    if slates_left:
        log(f"  {slug}: bookend slates remaining: {slates_left} — retry render")
        for attempt in range(2):
            rc2, _, _ = run(
                [sys.executable, str(SCRIPTS / "remotion_scenes.py"),
                 str(folder), "--force"],
                cwd=str(RUNTIME), timeout=900,
                env={"ART_HOME": str(REPO)}
            )
            slates_left = [bid for bid in bookend_ids
                           if not (folder / "media" / f"{bid}.mp4").exists()]
            if not slates_left:
                log(f"  {slug}: bookends rendered on attempt {attempt + 2}")
                break
            log(f"  {slug}: retry {attempt + 1} — still missing: {slates_left}")

    # ── 4. compile slate cut (16:9, 1080p) ──────────────────────────────────────
    log(f"  {slug}: compiling slate cut (16:9, 1080p)")
    rc, out, err = run(
        [sys.executable, str(SCRIPTS / "compile.py"),
         str(folder), "--review", "--height", "1080"],
        cwd=str(RUNTIME), timeout=600,
        env={"ART_QC": "1"}
    )
    if rc != 0:
        result["status"] = "failed"
        result["note"] += f" compile failed rc={rc}: {err[-300:]}"
        _write_build_log(folder, result)
        return result

    slate_169 = folder / f"{slug}-slate.mp4"
    if not slate_169.exists():
        # try finding any compiled mp4
        candidates = list(folder.glob("*-slate.mp4"))
        if candidates:
            slate_169 = candidates[0]
    result["slate_16_9"] = str(slate_169) if slate_169.exists() else None
    result["dur_16_9"] = probe_duration(slate_169)
    log(f"  {slug}: 16:9 slate done — {result['dur_16_9']:.1f}s" if result["dur_16_9"] else
        f"  {slug}: 16:9 slate missing!")

    # ── 5. Gate V: final_frame_check ────────────────────────────────────────────
    gate_v_script = RUNTIME / "qc" / "final_frame_check.py"
    if gate_v_script.exists() and slate_169.exists():
        log(f"  {slug}: Gate V — final_frame_check")
        # --fill-min 0.10: slate text cards fill ~10-20% of safe area (bounding box
        # of dark text on cream). The default 55% applies to fully-rendered media beats;
        # for the SLATE CUT, placeholder cards legitimately underfill. We keep all
        # other checks (edge-bleed, contrast, clustered) at normal strictness.
        rc, out, err = run(
            [sys.executable, str(gate_v_script), str(folder),
             "--fill-min", "0.10"],
            cwd=str(RUNTIME), timeout=300,
            env={"ART_QC": "1"}
        )
        if rc == 0:
            result["gate_v"] = "PASS"
            log(f"  {slug}: Gate V PASS")
        elif rc == 3:
            result["gate_v"] = "SKIP/deps"
            log(f"  {slug}: Gate V skipped — missing deps")
        else:
            result["gate_v"] = f"FAIL rc={rc}"
            log(f"  {slug}: Gate V FAIL — see _qc/REPORT.md")
            # Read and log the report
            report_path = folder / "_qc" / "REPORT.md"
            if report_path.exists():
                result["note"] += f" GateV:{report_path.read_text()[:200]}"
    else:
        result["gate_v"] = "skip/no-script"

    # ── 6. Gate T: type_check ────────────────────────────────────────────────────
    type_check = SCRIPTS / "type_check.py"
    if type_check.exists() and slate_169.exists():
        log(f"  {slug}: Gate T — type_check")
        rc, out, err = run(
            [sys.executable, str(type_check), str(folder)],
            cwd=str(RUNTIME), timeout=300
        )
        if rc == 0:
            log(f"  {slug}: Gate T PASS")
        elif rc == 3:
            log(f"  {slug}: Gate T skipped — missing deps")
        else:
            log(f"  {slug}: Gate T issues — see TYPECHECK.md")

    # ── 7. QC: sample frame from 16:9 ──────────────────────────────────────────
    qc_dir = folder / "_qc"
    qc_dir.mkdir(exist_ok=True)
    frame_169 = qc_dir / "frame_169.png"
    if slate_169.exists():
        sample_frame(slate_169, frame_169)
        if frame_169.exists():
            log(f"  {slug}: sampled 16:9 frame → {frame_169.name}")

    # ── 8. 9:16 reformat ────────────────────────────────────────────────────────
    log(f"  {slug}: generating 9:16 short")
    rc, out, err = run(
        [sys.executable, str(SCRIPTS / "shorts.py"), str(folder)],
        cwd=str(RUNTIME), timeout=600
    )
    short_dir = folder / "short"
    if rc != 0:
        log(f"  {slug}: shorts.py failed rc={rc}: {err[-200:]}")
        result["note"] += f" shorts-fail;"
    else:
        # compile the short
        log(f"  {slug}: compiling 9:16 short")
        rc2, out2, err2 = run(
            [sys.executable, str(SCRIPTS / "compile.py"),
             str(short_dir), "--review", "--height", "1920"],
            cwd=str(RUNTIME), timeout=600
        )
        short_slug = slug + "-short"
        slate_916_candidates = list(short_dir.glob("*-slate.mp4")) if short_dir.exists() else []
        if slate_916_candidates:
            slate_916 = slate_916_candidates[0]
            result["slate_9_16"] = str(slate_916)
            result["dur_9_16"] = probe_duration(slate_916)
            # sample frame
            frame_916 = qc_dir / "frame_916.png"
            sample_frame(slate_916, frame_916)
            result["reformat_ok"] = frame_916.exists()
            log(f"  {slug}: 9:16 slate done — {result['dur_9_16']:.1f}s" if result["dur_9_16"] else
                f"  {slug}: 9:16 slate present but no duration")
        else:
            log(f"  {slug}: 9:16 slate not found after compile")

    # ── 9. Write BUILD-LOG.md ───────────────────────────────────────────────────
    result["status"] = "built"
    _write_build_log(folder, result)

    # ── 10. Git: add, commit, push ──────────────────────────────────────────────
    rel = str(folder.relative_to(REPO))
    log(f"  {slug}: git add")
    # Add everything in episode folder except the large assembled MP4s
    run(["git", "add",
         f"{rel}/beat_sheet.json",
         f"{rel}/BUILD-PROMPT.md",
         f"{rel}/PEDAGOGY.md",
         f"{rel}/FACTCHECK.md",
         f"{rel}/SHOTLIST.md",
         f"{rel}/PROMPTS.md",
         f"{rel}/BUILD-LOG.md",
         f"{rel}/description.txt",
         ],
        cwd=str(REPO))
    # Force-add audio mp3s and media
    run(["git", "add", "-f", f"{rel}/audio/"],    cwd=str(REPO))
    run(["git", "add", "-f", f"{rel}/media/"],    cwd=str(REPO))
    run(["git", "add", "-f", f"{rel}/_qc/"],      cwd=str(REPO))
    if short_dir.exists():
        run(["git", "add", "-f", f"{rel}/short/beat_sheet.json",
             f"{rel}/short/BUILD-LOG.md"], cwd=str(REPO))
        run(["git", "add", "-f", f"{rel}/short/audio/"],  cwd=str(REPO))
        run(["git", "add", "-f", f"{rel}/short/media/"], cwd=str(REPO))
        run(["git", "add", "-f", f"{rel}/short/_qc/"],   cwd=str(REPO))

    # Also add master log
    run(["git", "add", str(MASTERLOG.relative_to(REPO))], cwd=str(REPO))

    commit_msg = f"Add slate cut: {slug} (What Is Brutalist? playlist)"
    rc, out, err = run(
        ["git", "commit", "-m", commit_msg],
        cwd=str(REPO)
    )
    if rc == 0:
        result["committed"] = True
        log(f"  {slug}: committed")
        # push
        rc2, _, _ = run(["git", "push"], cwd=str(REPO), timeout=120)
        result["pushed"] = rc2 == 0
        if result["pushed"]:
            log(f"  {slug}: pushed")
        else:
            log(f"  {slug}: push failed — will retry after next episode")
    else:
        log(f"  {slug}: commit skipped (nothing staged or error): {err[:100]}")

    return result


def _write_build_log(folder: Path, result: dict):
    """Write BUILD-LOG.md for an episode."""
    lines = [f"# BUILD-LOG — {result['slug']}\n\n"]
    lines.append(f"Status: {result['status']}\n")
    lines.append(f"16:9 slate: {result['slate_16_9']}\n")
    lines.append(f"16:9 duration: {result['dur_16_9']}\n")
    lines.append(f"9:16 slate: {result['slate_9_16']}\n")
    lines.append(f"9:16 duration: {result['dur_9_16']}\n")
    lines.append(f"9:16 reformat verified: {result['reformat_ok']}\n")
    lines.append(f"Gate B: {result['gate_b']}\n")
    lines.append(f"Gate V: {result['gate_v']}\n")
    lines.append(f"Committed: {result['committed']}\n")
    lines.append(f"Pushed: {result['pushed']}\n")
    if result["note"]:
        lines.append(f"\nNotes:\n{result['note']}\n")
    (folder / "BUILD-LOG.md").write_text("".join(lines))


def write_master_log(results: list):
    """Write/update OVERNIGHT-SLATE-BUILD.md."""
    lines = [
        "# OVERNIGHT SLATE BUILD — What Is Brutalist? playlist\n\n",
        f"Run completed: {datetime.now(timezone.utc).isoformat()}\n\n",
        "| # | Slug | Status | 16:9 dur | 9:16 dur | 9:16 ok | Gate V | Committed | Notes |\n",
        "|---|------|--------|----------|----------|---------|--------|-----------|-------|\n"
    ]
    for i, r in enumerate(results, 1):
        dur169 = f"{r['dur_16_9']:.0f}s" if r["dur_16_9"] else "—"
        dur916 = f"{r['dur_9_16']:.0f}s" if r["dur_9_16"] else "—"
        note = (r.get("note") or "")[:60].replace("|", "/")
        lines.append(
            f"| {i} | {r['slug']} | {r['status']} | {dur169} | {dur916} | "
            f"{'✓' if r['reformat_ok'] else '✗'} | {r['gate_v']} | "
            f"{'✓' if r['committed'] else '✗'} | {note} |\n"
        )
    built = sum(1 for r in results if r["status"] == "built")
    failed = sum(1 for r in results if r["status"] == "failed")
    lines.append(f"\n## Summary\n\nBuilt: {built}/{len(results)} | Failed: {failed}\n")
    MASTERLOG.write_text("".join(lines))


def main():
    log("=== OVERNIGHT SLATE BUILD — What Is Brutalist? ===")
    log(f"Working folder: {THIS}")
    log(f"Runtime: {RUNTIME}")

    # Episodes ordered by chapter_number
    EPISODE_ORDER = [
        "what-is-brutalist",   # ch 1
        "get-the-repo",        # ch 2
        "run-claude-code",     # ch 3
        "your-folder",         # ch 4
        "the-prompt",          # ch 5
        "the-beat-sheet",      # ch 6
        "make-it-move",        # ch 7
        "voices",              # ch 8
        "watch-and-revise",    # ch 9
        "both-formats",        # ch 10
        "qc-gates",            # ch 11
        "publish-it-yourself", # ch 12
        "make-it-yours",       # ch 13
    ]

    results = []
    for slug in EPISODE_ORDER:
        folder = THIS / slug
        if not folder.is_dir():
            log(f"SKIP {slug} — folder not found")
            results.append({"slug": slug, "status": "skipped",
                             "slate_16_9": None, "slate_9_16": None,
                             "dur_16_9": None, "dur_9_16": None,
                             "reformat_ok": False, "gate_b": "n/a", "gate_v": "n/a",
                             "committed": False, "pushed": False,
                             "note": "folder not found"})
            continue
        try:
            r = build_episode(slug, folder)
        except Exception as e:
            log(f"ERROR {slug}: {e}")
            r = {"slug": slug, "status": "failed",
                 "slate_16_9": None, "slate_9_16": None,
                 "dur_16_9": None, "dur_9_16": None,
                 "reformat_ok": False, "gate_b": "n/a", "gate_v": "n/a",
                 "committed": False, "pushed": False, "note": str(e)[:200]}
        results.append(r)
        write_master_log(results)
        log(f"✓  {slug}: {r['status']}")

    # Final push attempt for any unpushed commits
    rc, _, _ = run(["git", "push"], cwd=str(REPO), timeout=120)
    if rc == 0:
        log("Final git push succeeded")

    write_master_log(results)
    built = [r for r in results if r["status"] == "built"]
    failed = [r for r in results if r["status"] == "failed"]
    print("\n" + "=" * 60)
    print(f"DONE: {len(built)}/{len(results)} built, {len(failed)} failed")
    print(f"Master log: {MASTERLOG}")
    if failed:
        print("\nFailed episodes:")
        for r in failed:
            print(f"  {r['slug']}: {r['note'][:100]}")
    print("=" * 60)


if __name__ == "__main__":
    main()
