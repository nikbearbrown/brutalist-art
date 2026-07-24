# Smithsonian Open Access — local CC0 archival library

This folder is the archival still library for `brutalist-art`. It feeds
**VOX beats** in `deep-explainer` and `ai-explainer` reels — real historic
hardware, objects, documents, and named people where AI-illustration falls
short. Every image here is **CC0** (Smithsonian Open Access). The provenance
sidecar beside each image IS the rights record; no tier-2/3 escalation needed.

The library is **metadata-first**: the index is a searchable JSONL of object
metadata (id, title, unit, credit, object_type, date, thumbnail_url, search
tokens). The **full-res image URL is not stored** in the index for API-built
indexes — it is resolved at fetch time by calling the SI content-detail endpoint
(`GET /content/{id}`). S3-built indexes include the image_url directly.
Images are downloaded one at a time, on explicit accept, after you have looked
at the thumbnail and judged register fit.

## When to use this library

**Yes — register fit:**
- Real historic hardware (UNIVAC, ENIAC, IBM mainframes, early electronics)
- Named named people (portraits for biography/history beats)
- Named artifacts (moon rocks, aircraft, documents, instruments)
- Period photographs of events / places cited in the narration

**No — wrong register:**
- Abstract/conceptual beats ("server corridor", "data flowing") — AI-generate or doodle
- Doodle beats (MinutePhysics-style) — photo-real archival is off-register
- Anything the SI doesn't have — these belong in tier-2/3 sourcing

## Contents

```
library/smithsonian/
  README.md           # this file
  index.jsonl         # metadata index (one JSONL row per object)
  index_meta.json     # build stats (row count, units covered, build date)
  images/             # shelved + Topaz-upscaled CC0 images
    si-<id>-<slug>.jpg        # the image
    si-<id>-<slug>.source.txt # CC0 provenance sidecar (mandatory)
```

## API key setup

The index builder uses the **Smithsonian Open Access API** (api.si.edu), which
is hosted on api.data.gov. A free key is required for API mode.

1. Register at **https://api.data.gov/signup/** (instant, email confirm)
2. Add to `brutalist-art/.env`:
   ```
   SI_API_KEY=your_key_here
   ```
3. Build the index:
   ```bash
   python3 runtime/scripts/smithsonian_index.py
   ```

**No key? Use S3 streaming mode** (slower — streams multi-hundred-MB NDJSON
files from the public SI Open Access S3 bucket, filters on-the-fly):
```bash
python3 runtime/scripts/smithsonian_index.py --s3
```

## Topaz Photo AI

Upscaling uses **Topaz Photo AI CLI** at:
```
/Applications/Topaz Photo AI.app/Contents/Resources/bin/tpai
```

The fetch script invokes:
```
tpai --cli <input.jpg> --output <dir> --format jpg
```

Topaz runs on its current Autopilot preset (Autopilot chooses denoise/sharpen/
upscale models per image). If `tpai` is not installed or the path has moved,
the original downloaded file is shelved as-is with a console warning — the
pipeline continues, just without upscaling.

## Runtime loop — how a vox beat gets filled

```
1.  pantry_search "<beat's visual terms>"
      → shows local library hits AND Smithsonian metadata candidates

2.  LOOK at the thumbnail URL for any Smithsonian hit.
    A token match is a lead, not a verdict.
    Judge: relevance AND register fit (does it survive greyscale/duotone
    cutout + Ken Burns crop?).

3.  Accept →
      python3 runtime/scripts/smithsonian_fetch.py --id <SI_ID> \
          --copy <reel> --beat <BID>
    This downloads, Topaz-upscales, shelves with CC0 sidecar, and drops
    the result into <reel>/pantry/<BID>-<slug>.png.

4.  Run pantry intake once per touched reel:
      python3 runtime/scripts/pantry.py <reel>
    Set shot.focus per still (look at it); the sidecar is pre-filled.

5.  No good candidate anywhere → leave the SHOPPING/SHOTLIST card
    unchecked; it stays a human search (or an AI-generate for tier-1 generic).
```

**The second time a reel needs the same image** — it is already shelved. The
fetch script returns it immediately from `library/smithsonian/images/`; no
re-download.

## Index command reference

```bash
# Build (API, all register units):
python3 runtime/scripts/smithsonian_index.py --api-key YOUR_KEY

# Build (API, specific units):
python3 runtime/scripts/smithsonian_index.py --units NMAH NPG

# Build (S3, no key):
python3 runtime/scripts/smithsonian_index.py --s3

# Resume after interruption (skip already-indexed ids):
python3 runtime/scripts/smithsonian_index.py --resume

# Stats:
python3 runtime/scripts/smithsonian_index.py --stats
```

## Fetch command reference

```bash
# Fetch by SI object id:
python3 runtime/scripts/smithsonian_fetch.py --id nmah_12345

# Fetch by id + drop into pantry:
python3 runtime/scripts/smithsonian_fetch.py --id nmah_12345 \
    --copy ../physics-qm/youtube/my-reel --beat B07

# Search by terms (interactive):
python3 runtime/scripts/smithsonian_fetch.py "UNIVAC computer console"

# Search + auto-accept top hit (non-interactive):
python3 runtime/scripts/smithsonian_fetch.py "UNIVAC" --yes

# List shelved images:
python3 runtime/scripts/smithsonian_fetch.py --list
```

## Register units indexed

| Unit code | Name |
|---|---|
| NMAH | National Museum of American History (incl. computing/electronics) |
| NASM | National Air and Space Museum |
| NPG  | National Portrait Gallery |
| NMAAHC | National Museum of African American History and Culture |
| SIL  | Smithsonian Institution Libraries |
| SIA  | Smithsonian Institution Archives |
| SAAM | Smithsonian American Art Museum |

The whole Smithsonian catalog is ~11M objects. This register slice (CC0 +
has-image + these units) runs to low hundreds of thousands — manageable as a
local index.

## Provenance sidecar format

Every shelved image has a `.source.txt` beside it. Example:
```
CC0
SI_ID: nmah_1246867
Title: UNIVAC I Console
Unit: NMAH
Credit: Gift of Remington Rand, Inc.
Source URL: https://ids.si.edu/ids/download?id=NMAH-1246867
License: CC0 — Smithsonian Open Access https://www.si.edu/openaccess
```

This sidecar is the full provenance record. The pantry intake creates a
`media/<BID>.source.txt` in the reel — that sidecar is what populates the
credits roll. No further rights verification is needed for CC0 stills.
