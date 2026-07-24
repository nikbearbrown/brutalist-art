# PEDAGOGY — claude-liam-youtube-publisher
# "Claude, Published." | youtube-publisher skill teardown

## Learning goal
Viewer leaves knowing: (1) youtube-publisher bookends a NotebookLM .mp4 with a Medhavy intro and outro — the body is never re-encoded or re-narrated; (2) the chapter match sets playlist position and is a human gate because a wrong match silently reorders the playlist; (3) three human gates stand between build and live: chapter match, description rewrite, upload confirm.

## Prediction beat
B03 poses: you have 30 NotebookLM videos and you want them in a chapter-ordered playlist. What's the single most dangerous error the automation could make silently? Viewer predicts before B04/B05 reveal: a wrong chapter match silently reorders the playlist — that's why the chapter match is a human gate.

## Concrete before abstract
B04 shows the actual --dry-run output from PUBLISH-LOG.md (3 videos, correct chapter order, no quota spent) before B05/B06/B07 state the abstract body-untouched / chapter-match / human-gate laws.

## Self-demo check
B04 is genuinely free: references the actual dry-run output from youtube/PUBLISH-LOG.md — no upload, no quota, no OAuth interactive step required. Output is the real preview that was produced before the first 5 real uploads.

## ILLUSTRATE LAW
- UI beats (5): B00, B03, BVDT, BHTF, BOUT
- Illustration beats (6): B01, B02, B04, B05, B06, B07

## VERDICT: PASS
