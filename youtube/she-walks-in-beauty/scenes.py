"""scenes.py — Manim lyric cards for 'She Walks in Beauty' by Lord Byron (1814)
Spoken by Nate. All beats GRAPHIC; B99 REMOTION CTA.
Palette: night — BG #0D0806, PARCHMENT #F2EDE5, GOLD #B8966E, MUTED #7A6A5E.
Each scene: dark bg, two poem lines fade in, hold to beat duration.
"""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "runtime" / "manim"))
from animated_graphics import *

NIGHT    = "#0D0806"
PARCHMENT = "#F2EDE5"
GOLD     = "#B8966E"
MUTED    = "#7A6A5E"


def _dur(bid):
    bs = pathlib.Path(__file__).parent / "beat_sheet.json"
    if not bs.exists():
        return 0.0
    for b in json.loads(bs.read_text()).get("beats", []):
        if b["beat_id"] == bid:
            return float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0.0)
    return 0.0


def _lyric_card(scene, bid, line1, line2, stanza_label=None, is_final=False):
    """Dark-bg lyric card: optional stanza header + two poem lines + optional attribution."""
    scene.camera.background_color = NIGHT

    if stanza_label:
        lbl = Text(stanza_label, font=DISPLAY, color=GOLD, font_size=20, weight="MEDIUM")
        lbl.to_corner(UL, buff=0.6)
        scene.play(FadeIn(lbl), run_time=0.4)

    l1 = Text(line1, font=SERIF, color=PARCHMENT, font_size=30)
    l1.move_to(UP * 0.55)
    l2 = Text(line2, font=SERIF, color=PARCHMENT, font_size=30)
    l2.move_to(DOWN * 0.35)

    scene.play(FadeIn(l1), run_time=0.7)
    scene.play(FadeIn(l2), run_time=0.7)

    if is_final:
        attr = Text("— Lord Byron, 1814", font=SERIF, color=MUTED, font_size=20, slant=ITALIC)
        attr.to_edge(DOWN, buff=0.6)
        scene.play(FadeIn(attr), run_time=0.5)

    scene.wait(max(0.5, _dur(bid) - getattr(scene, 'time', 0.0)))


# ── STANZA I ──────────────────────────────────────────────
class B00_SheLike(Scene):
    def construct(self):
        _lyric_card(self, "B00",
            "She walks in beauty, like the night",
            "Of cloudless climes and starry skies",
            stanza_label="STANZA I")


class B01_DarkAndBright(Scene):
    def construct(self):
        _lyric_card(self, "B01",
            "And all that's best of dark and bright",
            "Meet in her aspect and her eyes")


class B02_TenderLight(Scene):
    def construct(self):
        _lyric_card(self, "B02",
            "Thus mellowed to that tender light",
            "Which heaven to gaudy day denies")


# ── STANZA II ─────────────────────────────────────────────
class B03_OneShade(Scene):
    def construct(self):
        _lyric_card(self, "B03",
            "One shade the more, one ray the less",
            "Had half impaired the nameless grace",
            stanza_label="STANZA II")


class B04_RavenTress(Scene):
    def construct(self):
        _lyric_card(self, "B04",
            "Which waves in every raven tress",
            "Or softly lightens o'er her face")


class B05_DwellingPlace(Scene):
    def construct(self):
        _lyric_card(self, "B05",
            "Where thoughts serenely sweet express",
            "How pure, how dear their dwelling-place")


# ── STANZA III ────────────────────────────────────────────
class B06_ThatCheek(Scene):
    def construct(self):
        _lyric_card(self, "B06",
            "And on that cheek, and o'er that brow",
            "So soft, so calm, yet eloquent",
            stanza_label="STANZA III")


class B07_DaysInGoodness(Scene):
    def construct(self):
        _lyric_card(self, "B07",
            "The smiles that win, the tints that glow",
            "But tell of days in goodness spent")


class B08_Innocent(Scene):
    def construct(self):
        _lyric_card(self, "B08",
            "A mind at peace with all below",
            "A heart whose love is innocent!",
            is_final=True)
