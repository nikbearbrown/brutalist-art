---
name: feedback-scene-dur-pattern
description: Use _dur(bid) + getattr(scene,'time',0.0) to pad Manim scenes to beat duration; fixes slow-mo without breaking Gate A
metadata:
  type: feedback
---

Use this pattern at the end of every Manim `construct()` to pad the scene to the beat's `actual_duration_s`:

```python
import json

def _dur(bid):
    bs = pathlib.Path(__file__).parent / "beat_sheet.json"
    if not bs.exists():
        return 0.0
    for b in json.loads(bs.read_text()).get("beats", []):
        if b["beat_id"] == bid:
            return float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0.0)
    return 0.0

# End of construct():
self.wait(max(0.5, _dur("BXX") - getattr(self, 'time', 0.0)))
```

**Why:** `run.sh` passes no duration to Manim — scenes render at natural animation speed (~4-6s). Without padding, `compile.py` slow-stretches the clip 3-4x to fill the beat, producing unusable extreme slow-mo. The `_dur()` helper reads from the reel's own `beat_sheet.json` (cwd = reel dir during render), so it auto-scales to whichever voice take is active.

**Why `getattr`:** Gate A static pre-flight calls `construct()` without the Manim renderer, so `self.time` doesn't exist. `getattr(self, 'time', 0.0)` returns 0 safely, and Gate A doesn't actually animate, so the large wait value doesn't matter.

**How to apply:** Add `_dur()` and the final `self.wait()` to every new Manim scene. For shared scenes.py used across voice variants (e.g. primary + 11labs), the helper auto-reads each reel's own beat_sheet.json — no changes needed per variant.
