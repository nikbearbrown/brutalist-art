"""scenes.py — Manim scenes for 'What is Brutalist?' (what-is-brutalist)

One Scene subclass per GRAPHIC beat with shot.source == 'own'.
Beats: B01, B02, B03, B05, B06, B07, B08, B09, B11, B14.
Palette: teardown — flat white GROUND, ink INK, red CRIMSON, teal TEAL.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "runtime" / "manim"))
from animated_graphics import *
import numpy as np

# ── teardown palette (imported from animated_graphics, duplicated here for clarity)
# GROUND = "#FFFFFF" · INK = "#2A1A0E" · CRIMSON = "#C8102E" · TEAL = "#1F6F5C" (in teardown TEAL==INK)
# Per the palette registry: TEAL = "#2A1A0E" in teardown. We use the beat-sheet teal #1F6F5C as ACCENT_TEAL.
ACCENT_TEAL = "#1F6F5C"   # "good/kept" — only for beats that call for it


# ──────────────────────────────────────────────────────────
# B01 — ONE-CLICK SLOP (8s)
# ──────────────────────────────────────────────────────────
class B01_OneClickSlop(Scene):
    def construct(self):
        # Button
        btn_box = Rectangle(width=3.2, height=1.1, fill_color=GROUND, fill_opacity=1,
                            stroke_color=INK, stroke_width=3)
        btn_lbl = Text("MAKE VIDEO", font=DISPLAY, color=INK, font_size=32, weight=BOLD)
        btn_lbl.move_to(btn_box)
        button = VGroup(btn_box, btn_lbl).move_to(UP * 1.2)

        # Filmstrip (3 frames side by side)
        frames = []
        for i in range(3):
            f = Rectangle(width=1.1, height=1.5, fill_color="#EEEEEE", fill_opacity=1,
                          stroke_color=INK, stroke_width=1.5)
            # sprocket holes top + bottom
            for dy in [0.6, -0.6]:
                hole = Rectangle(width=0.18, height=0.22, fill_color=INK, fill_opacity=1,
                                 stroke_width=0)
                hole.move_to(f.get_center() + np.array([0, dy, 0]))
                f = VGroup(f, hole)
            frames.append(f)
        filmstrip = VGroup(*frames).arrange(RIGHT, buff=0.08).move_to(DOWN * 0.5)

        # Red SLOP stamp
        slop_lbl = Text("SLOP", font=DISPLAY, color=CRIMSON, font_size=72, weight=BOLD,
                         slant=ITALIC)
        slop_line = Line(slop_lbl.get_corner(DL) + DOWN * 0.08,
                         slop_lbl.get_corner(DR) + DOWN * 0.08,
                         stroke_width=4, color=CRIMSON)
        slop = VGroup(slop_lbl, slop_line).move_to(DOWN * 0.5).rotate(-0.2)

        # Animate
        self.play(FadeIn(button, shift=DOWN * 0.2), run_time=0.7)
        self.wait(0.5)
        # Button click — brief scale-down
        self.play(button.animate.scale(0.92), run_time=0.2)
        self.play(button.animate.scale(1.0 / 0.92), run_time=0.15)
        # Filmstrip drops out
        self.play(FadeIn(filmstrip, shift=UP * 0.3), run_time=0.8)
        self.wait(0.8)
        # Stamp lands
        slop.scale(0.01)
        self.play(slop.animate.scale(100), run_time=0.5)
        self.wait(3.3)


# ──────────────────────────────────────────────────────────
# B02 — CANNOT WATCH (8s)
# ──────────────────────────────────────────────────────────
class B02_CannotWatch(Scene):
    def construct(self):
        # Screen (right side)
        screen = Rectangle(width=3.0, height=2.0, fill_color="#1A1A1A", fill_opacity=1,
                            stroke_color=INK, stroke_width=2).shift(RIGHT * 2.8)
        # inner content bars (suggesting a playing video)
        for i, col in enumerate(["#C8102E", "#EEEEEE", "#555555"]):
            bar = Rectangle(width=2.4, height=0.3, fill_color=col, fill_opacity=0.7,
                             stroke_width=0)
            bar.move_to(screen.get_center() + UP * (0.4 - i * 0.4))
            screen.add(bar)
        screen_lbl = Text("video", font=SERIF, color="#AAAAAA", font_size=22, slant=ITALIC)
        screen_lbl.move_to(screen.get_center() + DOWN * 0.75)
        screen = VGroup(screen, screen_lbl)

        # AI node (left side) — circle with "AI" label
        ai_circle = Circle(radius=0.7, fill_color=GROUND, fill_opacity=1,
                           stroke_color=INK, stroke_width=2.5).shift(LEFT * 2.8)
        ai_lbl = Text("AI", font=DISPLAY, color=INK, font_size=34, weight=BOLD)
        ai_lbl.move_to(ai_circle)

        # Eye crossed out (small, on the AI node)
        eye_outer = Ellipse(width=0.5, height=0.3, stroke_color=SLATE, stroke_width=2)
        eye_dot = Dot(radius=0.08, color=SLATE)
        eye = VGroup(eye_outer, eye_dot).next_to(ai_circle, UP, buff=0.05)
        cross1 = Line(eye.get_corner(UL), eye.get_corner(DR), stroke_color=CRIMSON, stroke_width=3)
        cross2 = Line(eye.get_corner(UR), eye.get_corner(DL), stroke_color=CRIMSON, stroke_width=3)
        eye_crossed = VGroup(eye, cross1, cross2)

        ai_node = VGroup(ai_circle, ai_lbl, eye_crossed)

        # Dashed line that "never connects" — stops short of screen
        dash_start = ai_circle.get_right() + RIGHT * 0.1
        dash_end   = screen[0].get_left() + LEFT * 0.6
        dashed = DashedLine(dash_start, dash_end, dash_length=0.22,
                            dashed_ratio=0.5, stroke_color=SLATE, stroke_width=2)

        # Animate
        self.play(FadeIn(ai_node, shift=RIGHT * 0.2), run_time=0.8)
        self.play(FadeIn(screen, shift=LEFT * 0.2), run_time=0.8)
        self.wait(0.6)
        self.play(Create(dashed), run_time=1.0)
        self.wait(4.8)


# ──────────────────────────────────────────────────────────
# B03 — TASTE GAPS (11s)
# ──────────────────────────────────────────────────────────
class B03_TasteGaps(Scene):
    def construct(self):
        questions = ["funny?", "interesting?", "did it land?"]
        cards = VGroup()
        for q in questions:
            box = Rectangle(width=3.4, height=1.0, fill_color=GROUND, fill_opacity=1,
                            stroke_color=INK, stroke_width=2)
            checkbox = Square(side_length=0.32, stroke_color=INK, stroke_width=2,
                              fill_opacity=0)
            checkbox.next_to(box.get_left(), RIGHT, buff=0.25)
            label = Text(q, font=SERIF, color=INK, font_size=32, slant=ITALIC)
            label.next_to(checkbox, RIGHT, buff=0.25)
            card = VGroup(box, checkbox, label)
            cards.add(card)

        cards.arrange(DOWN, buff=0.35).move_to(LEFT * 0.8)

        # Human checkmark group (to be revealed on each card)
        checks = VGroup()
        for card in cards:
            checkbox = card[1]
            chk = Text("✓", font=DISPLAY, color=ACCENT_TEAL, font_size=28, weight=BOLD)
            chk.move_to(checkbox.get_center())
            checks.add(chk)

        # Human silhouette label (simple text stand-in)
        human_lbl = Text("human", font=SERIF, color=SLATE, font_size=22, slant=ITALIC)
        human_lbl.to_edge(RIGHT, buff=1.2)

        self.play(FadeIn(human_lbl), run_time=0.5)
        for i, (card, chk) in enumerate(zip(cards, checks)):
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.7)
            self.wait(0.6)
            self.play(FadeIn(chk, scale=1.3), run_time=0.5)
            self.wait(0.5)
        self.wait(3.2)


# ──────────────────────────────────────────────────────────
# B05 — TWENTY-HOUR BUG (11s)
# ──────────────────────────────────────────────────────────
class B05_TwentyHourBug(Scene):
    def construct(self):
        # Left: human + clock + red error
        clock_lbl = Text("20:00:00", font="PT Mono", color=INK, font_size=52, weight=BOLD)
        clock_lbl.shift(LEFT * 3.2 + UP * 1.2)
        clock_sub = Text("human, debugging", font=SERIF, color=SLATE, font_size=22)
        clock_sub.next_to(clock_lbl, DOWN, buff=0.2)

        error_line = Rectangle(width=2.8, height=0.38, fill_color=CRIMSON, fill_opacity=0.12,
                                stroke_color=CRIMSON, stroke_width=2)
        error_line.next_to(clock_sub, DOWN, buff=0.4)
        error_text = Text("ERROR: render failed", font="PT Mono", color=CRIMSON, font_size=18)
        error_text.move_to(error_line)
        human_side = VGroup(clock_lbl, clock_sub, error_line, error_text)

        # Divider
        divider = Line(UP * 3, DOWN * 3, stroke_color=HAIRLINE, stroke_width=2)

        # Right: machine — resolves fast
        machine_lbl = Text("0:00:03", font="PT Mono", color=INK, font_size=52, weight=BOLD)
        machine_lbl.shift(RIGHT * 3.2 + UP * 1.2)
        machine_sub = Text("machine, fixed", font=SERIF, color=ACCENT_TEAL, font_size=22)
        machine_sub.next_to(machine_lbl, DOWN, buff=0.2)
        ok_chip = LabelChip("OK", accent=ACCENT_TEAL, size=22)
        ok_chip.next_to(machine_sub, DOWN, buff=0.4)
        machine_side = VGroup(machine_lbl, machine_sub, ok_chip)

        # Waste bar under human side (red, draining)
        waste_bar_bg = Rectangle(width=2.8, height=0.22, fill_color=HAIRLINE, fill_opacity=1,
                                  stroke_width=0)
        waste_bar_bg.next_to(human_side, DOWN, buff=0.5)
        waste_bar = Rectangle(width=2.8, height=0.22, fill_color=CRIMSON, fill_opacity=0.7,
                               stroke_width=0)
        waste_bar.align_to(waste_bar_bg, LEFT).align_to(waste_bar_bg, UP)
        waste_lbl = Text("wasted time", font=SERIF, color=CRIMSON, font_size=18, slant=ITALIC)
        waste_lbl.next_to(waste_bar_bg, DOWN, buff=0.1)

        self.play(FadeIn(human_side), Create(divider), FadeIn(machine_side), run_time=1.0)
        self.wait(1.0)
        self.play(FadeIn(waste_bar_bg), FadeIn(waste_bar), FadeIn(waste_lbl), run_time=0.6)
        self.wait(1.0)
        # Drain the waste bar (transform to near-zero width, pinned left)
        empty = Rectangle(width=0.01, height=0.22, fill_color=CRIMSON, fill_opacity=0.7,
                          stroke_width=0)
        empty.align_to(waste_bar_bg, LEFT).align_to(waste_bar_bg, UP)
        self.play(Transform(waste_bar, empty), run_time=2.5)
        self.wait(4.9)


# ──────────────────────────────────────────────────────────
# B06 — TWO FAILURE MODES (14s)
# ──────────────────────────────────────────────────────────
class B06_TwoFailureModes(Scene):
    def construct(self):
        # Balance beam: horizontal bar pivoting on a fulcrum
        pivot = Triangle(fill_color=INK, fill_opacity=1, stroke_width=0).scale(0.35)
        pivot.move_to(DOWN * 1.8)
        beam = Line(LEFT * 4.5, RIGHT * 4.5, stroke_color=INK, stroke_width=4)
        beam.move_to(DOWN * 1.1)

        # Left pan label: "all human" sinking
        left_pan_lbl = Text("all human\n(time-sink)", font=SERIF, color=INK, font_size=26,
                            line_spacing=0.8)
        left_pan_lbl.move_to(LEFT * 3.5 + UP * 0.4)

        # Clock icons on left — three tiny rectangles
        clocks = VGroup()
        for i in range(3):
            c = Rectangle(width=0.4, height=0.4, stroke_color=INK, stroke_width=1.5,
                          fill_opacity=0)
            c.move_to(LEFT * (3.5 + i * 0.5 - 0.5) + DOWN * 0.4)
            clocks.add(c)

        # Right pan label: "all machine" SLOP
        right_pan_lbl = Text("all machine\n(AI slop)", font=SERIF, color=INK, font_size=26,
                              line_spacing=0.8)
        right_pan_lbl.move_to(RIGHT * 3.5 + UP * 0.4)

        slop_chip = LabelChip("SLOP", accent=CRIMSON, size=24)
        slop_chip.move_to(RIGHT * 3.5 + DOWN * 0.45)

        # Left side sinks: beam tilts left
        left_group = VGroup(left_pan_lbl, clocks)
        right_group = VGroup(right_pan_lbl, slop_chip)

        # Middle marker: "here" in teal
        middle_arrow = Arrow(UP * 0.5, DOWN * 0.1, stroke_color=ACCENT_TEAL, stroke_width=4,
                              tip_length=0.25).move_to(UP * 0.4)
        middle_lbl = LabelChip("BRUTALIST", accent=ACCENT_TEAL, size=22)
        middle_lbl.next_to(middle_arrow, UP, buff=0.15)

        self.play(Create(beam), FadeIn(pivot), run_time=0.7)
        self.play(FadeIn(left_group, shift=DOWN * 0.2), run_time=0.8)
        self.wait(0.6)
        self.play(FadeIn(right_group, shift=DOWN * 0.2), run_time=0.8)
        self.wait(0.8)
        # Tilt left (left side heavy)
        self.play(
            beam.animate.rotate(-0.18, about_point=beam.get_center()),
            left_group.animate.shift(DOWN * 0.4),
            right_group.animate.shift(UP * 0.3),
            run_time=1.2
        )
        self.wait(1.5)
        # Show the middle balance point
        self.play(FadeIn(middle_arrow, shift=DOWN * 0.1), FadeIn(middle_lbl), run_time=0.8)
        self.wait(5.8)


# ──────────────────────────────────────────────────────────
# B07 — YOU ARE THE CONDUCTOR (7s)  ← HERO BEAT
# ──────────────────────────────────────────────────────────
class B07_YouAreTheConductor(Scene):
    def construct(self):
        # Dark canvas for this hero beat
        self.camera.background_color = "#2A1A0E"

        # Baton stroke — a confident horizontal line drawn across the canvas
        baton = Line(LEFT * 5.5, RIGHT * 5.5, stroke_color=WHITE, stroke_width=6)
        baton.shift(UP * 0.8)

        # Title in EB Garamond
        title = Text("YOU ARE THE CONDUCTOR", font=SERIF, color=WHITE,
                     font_size=54, weight=BOLD)
        title.move_to(ORIGIN)

        # Red underline accent
        underline = Line(title.get_corner(DL) + DOWN * 0.1,
                         title.get_corner(DR) + DOWN * 0.1,
                         stroke_color=CRIMSON, stroke_width=5)

        # Faint tool labels below (the orchestra)
        tools = ["Manim", "Remotion", "ffmpeg"]
        tool_row = VGroup(*[
            Text(t, font=DISPLAY, color=WHITE, font_size=20, weight="MEDIUM")
            for t in tools
        ]).arrange(RIGHT, buff=1.4)
        tool_row.shift(DOWN * 1.8).set_opacity(0.35)

        # Animate: baton stroke first, then title resolves
        self.play(Create(baton), run_time=0.9)
        self.wait(0.2)
        self.play(Write(title), run_time=1.1)
        self.play(Create(underline), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(tool_row, shift=UP * 0.1), run_time=0.7)
        self.wait(3.3)


# ──────────────────────────────────────────────────────────
# B08 — THE SCORE AND THE PLAYING (13s)
# ──────────────────────────────────────────────────────────
class B08_ScoreAndPlaying(Scene):
    def construct(self):
        # Vertical divider
        divider = Line(UP * 3.2, DOWN * 3.2, stroke_color=HAIRLINE, stroke_width=2)

        # LEFT: score (annotated staff lines)
        score_lbl = SerifLabel("the score is yours", accent=CRIMSON, size=28)
        score_lbl.move_to(LEFT * 3.2 + UP * 2.2)

        staff_lines = VGroup(*[
            Line(LEFT * 5.2, ORIGIN + LEFT * 0.3,
                 stroke_color=INK, stroke_width=1.2).shift(UP * (0.8 - i * 0.4))
            for i in range(5)
        ])

        # Red circle on one line (the wrong note)
        wrong_note = Circle(radius=0.22, stroke_color=CRIMSON, stroke_width=3, fill_opacity=0)
        wrong_note.move_to(LEFT * 2.8 + UP * 0.4)

        # Hand annotation mark (a short red mark)
        annotation = Text("✗", font=DISPLAY, color=CRIMSON, font_size=36)
        annotation.next_to(wrong_note, UP, buff=0.1)

        left_group = VGroup(score_lbl, staff_lines, wrong_note, annotation)

        # RIGHT: tool-orchestra playing
        play_lbl = SerifLabel("the playing is its", accent=ACCENT_TEAL, size=28)
        play_lbl.move_to(RIGHT * 3.2 + UP * 2.2)

        tools = [("Manim", "animations"), ("Remotion", "graphics"), ("ffmpeg", "cuts")]
        tool_cards = VGroup()
        for i, (tool, role) in enumerate(tools):
            card = Rectangle(width=2.4, height=0.6, fill_color="#F5F5F5", fill_opacity=1,
                             stroke_color=INK, stroke_width=1)
            t = Text(tool, font=DISPLAY, color=INK, font_size=22, weight=BOLD)
            r = Text(role, font=SERIF, color=SLATE, font_size=18)
            VGroup(t, r).arrange(RIGHT, buff=0.25).move_to(card)
            tc = VGroup(card, t, r).shift(RIGHT * 3.2 + UP * (0.6 - i * 0.85))
            tool_cards.add(tc)

        # Baton arrow from left to right
        baton_arrow = Arrow(LEFT * 0.3, RIGHT * 0.3, stroke_color=ACCENT_TEAL,
                            stroke_width=4, tip_length=0.3).move_to(UP * 0.1)

        self.play(Create(divider), run_time=0.4)
        self.play(FadeIn(left_group, shift=RIGHT * 0.2), FadeIn(play_lbl), run_time=1.0)
        self.wait(0.6)
        self.play(LaggedStart(*[FadeIn(tc, shift=LEFT * 0.2) for tc in tool_cards],
                               lag_ratio=0.3, run_time=1.4))
        self.wait(0.8)
        self.play(GrowArrow(baton_arrow), run_time=0.8)
        self.wait(7.0)


# ──────────────────────────────────────────────────────────
# B09 — BEAT SHEET HEART (9s)
# ──────────────────────────────────────────────────────────
class B09_BeatSheetHeart(Scene):
    def construct(self):
        # Central JSON "heart"
        heart_box = Rectangle(width=3.6, height=1.8, fill_color=GROUND, fill_opacity=1,
                              stroke_color=CRIMSON, stroke_width=3)
        heart_lbl = Text("beat_sheet.json", font="PT Mono", color=INK, font_size=28, weight=BOLD)
        heart_lbl.move_to(heart_box.get_center() + UP * 0.3)
        beat_rows = Text("B01 · B02 · … · B14", font="PT Mono", color=CRIMSON, font_size=18)
        beat_rows.move_to(heart_box.get_center() + DOWN * 0.3)
        heart = VGroup(heart_box, heart_lbl, beat_rows)

        # Three derived views with arrows
        targets = [
            (UP * 2.6, "todo.json", SLATE),
            (RIGHT * 4.8, "STATUS.md", SLATE),
            (DOWN * 2.4, "the cut", ACCENT_TEAL),
        ]
        arrows_and_lbls = VGroup()
        for pos, label, col in targets:
            direction = pos / np.linalg.norm(pos)
            start = heart_box.get_center() + direction * 1.9
            end = heart_box.get_center() + pos * 0.82
            arr = Arrow(start, end, stroke_color=col, stroke_width=2.5,
                        tip_length=0.22)
            lbl = Text(label, font="PT Mono", color=col, font_size=22)
            lbl.move_to(heart_box.get_center() + pos * 1.0)
            arrows_and_lbls.add(arr, lbl)

        # Pulse animation: heart glows red briefly
        glow = heart_box.copy().set_stroke(CRIMSON, 6).set_fill(opacity=0)

        self.play(FadeIn(heart, scale=0.9), run_time=0.9)
        self.play(Create(glow), glow.animate.set_opacity(0), run_time=0.8)
        self.wait(0.4)
        for i in range(0, len(arrows_and_lbls), 2):
            arr = arrows_and_lbls[i]
            lbl = arrows_and_lbls[i + 1]
            direction = np.array(arr.get_end()) - np.array(arr.get_start())
            norm = np.linalg.norm(direction)
            shift_vec = direction / norm * 0.1 if norm > 0 else np.array([0, 0, 0])
            self.play(GrowArrow(arr), FadeIn(lbl, shift=shift_vec), run_time=0.7)
        self.wait(4.2)


# ──────────────────────────────────────────────────────────
# B11 — REQUEST CARD → PANTRY → CONFORMED CUT (15s)
# ──────────────────────────────────────────────────────────
class B11_RequestCardPantry(Scene):
    def construct(self):
        # Step 1: Request card (unfilled beat placeholder)
        card_box = Rectangle(width=3.8, height=2.0, fill_color="#FFF8F8", fill_opacity=1,
                             stroke_color=CRIMSON, stroke_width=2.5, stroke_opacity=0.9)
        card_icon = Text("[ ? ]", font="PT Mono", color=CRIMSON, font_size=40)
        card_lbl = Text("REQUEST CARD", font=DISPLAY, color=CRIMSON, font_size=20, weight=BOLD)
        card_prompt = Text("suggested prompt:", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        card_prompt_text = Text('"archival aerial footage, city"', font="PT Mono",
                                 color=INK, font_size=16)
        card_contents = VGroup(card_icon, card_lbl, card_prompt, card_prompt_text)
        card_contents.arrange(DOWN, buff=0.18)
        card_contents.move_to(card_box)
        request_card = VGroup(card_box, card_contents)
        request_card.shift(LEFT * 3.6 + UP * 0.3)

        # Arrow 1: request card → pantry
        arrow1 = Arrow(request_card.get_right() + RIGHT * 0.1,
                       request_card.get_right() + RIGHT * 1.4,
                       stroke_color=INK, stroke_width=2.5, tip_length=0.22)
        arrow1.shift(RIGHT * 0.0)

        # Step 2: Pantry bin
        pantry_box = Rectangle(width=1.8, height=2.2, fill_color="#F0F0F0", fill_opacity=1,
                                stroke_color=INK, stroke_width=2)
        pantry_lbl = Text("pantry/", font="PT Mono", color=SLATE, font_size=20)
        pantry_lbl.next_to(pantry_box, UP, buff=0.18)
        clip = Rectangle(width=1.2, height=0.6, fill_color=ACCENT_TEAL, fill_opacity=0.8,
                          stroke_width=0)
        clip_lbl = Text("clip.mp4", font="PT Mono", color=WHITE, font_size=14)
        clip_lbl.move_to(clip)
        pantry_clip = VGroup(clip, clip_lbl)
        pantry = VGroup(pantry_box, pantry_lbl)
        pantry.move_to(ORIGIN + UP * 0.3)
        arrow1.put_start_and_end_on(request_card.get_right() + RIGHT * 0.15,
                                     pantry.get_left() + LEFT * 0.15)

        # Arrow 2: pantry → timeline
        arrow2 = Arrow(ORIGIN, ORIGIN + RIGHT * 1.5, stroke_color=INK,
                        stroke_width=2.5, tip_length=0.22)

        # Step 3: Timeline slot
        timeline_box = Rectangle(width=3.2, height=0.7, fill_color=GROUND, fill_opacity=1,
                                  stroke_color=INK, stroke_width=2)
        beat_slot = Rectangle(width=1.2, height=0.5, fill_color=ACCENT_TEAL, fill_opacity=1,
                               stroke_width=0)
        beat_slot_lbl = Text("B11 ✓", font="PT Mono", color=WHITE, font_size=18, weight=BOLD)
        beat_slot_lbl.move_to(beat_slot)
        timeline = VGroup(timeline_box, beat_slot, beat_slot_lbl)
        timeline.shift(RIGHT * 3.8 + UP * 0.3)
        arrow2.put_start_and_end_on(pantry.get_right() + RIGHT * 0.15,
                                     timeline.get_left() + LEFT * 0.15)

        # Step labels
        lbl1 = Text("request card", font=SERIF, color=CRIMSON, font_size=20, slant=ITALIC)
        lbl1.next_to(request_card, DOWN, buff=0.35)
        lbl2 = Text("you drop it in", font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        lbl2.next_to(pantry, DOWN, buff=0.35)
        lbl3 = Text("auto-conformed", font=SERIF, color=ACCENT_TEAL, font_size=20, slant=ITALIC)
        lbl3.next_to(timeline, DOWN, buff=0.35)

        # Animate
        self.play(FadeIn(request_card, shift=RIGHT * 0.3), FadeIn(lbl1), run_time=0.9)
        self.wait(1.0)
        self.play(GrowArrow(arrow1), run_time=0.6)
        self.play(FadeIn(pantry, shift=LEFT * 0.2), FadeIn(lbl2), run_time=0.7)
        # Clip drops into pantry
        pantry_clip.move_to(pantry_box.get_center() + UP * 1.5)
        self.play(FadeIn(pantry_clip), pantry_clip.animate.move_to(pantry_box.get_center()),
                  run_time=0.8)
        self.wait(0.8)
        self.play(GrowArrow(arrow2), run_time=0.6)
        self.play(FadeIn(timeline, shift=LEFT * 0.2), FadeIn(lbl3), run_time=0.7)
        self.wait(7.2)


# ──────────────────────────────────────────────────────────
# B14 — THE PLAYLIST (14s)
# ──────────────────────────────────────────────────────────
class B14_ThePlaylist(Scene):
    def construct(self):
        playlist_title = SerifLabel("Brutalist — Claude for Video Production", accent=CRIMSON, size=26)
        playlist_title.to_edge(UP, buff=0.7)

        # Playlist entries: title + command
        entries = [
            ("What is Brutalist?",  "./art explainer-video"),
            ("sketch-explainer",    "./art sketch-explainer"),
            ("explainer",           "./art explainer"),
            ("deck-lecture",        "./art deck-lecture"),
            ("music-video",         "./art music-video"),
        ]
        cards = VGroup()
        for title, cmd in entries:
            thumb = Rectangle(width=1.9, height=1.1, fill_color="#EEEEEE", fill_opacity=1,
                              stroke_color=INK, stroke_width=1.5)
            # red play-button triangle inside thumbnail
            tri = Triangle(fill_color=CRIMSON, fill_opacity=0.8, stroke_width=0).scale(0.22)
            tri.move_to(thumb)
            title_txt = Text(title, font=DISPLAY, color=INK, font_size=14, weight=BOLD)
            title_txt.next_to(thumb, DOWN, buff=0.08)
            title_txt.scale_to_fit_width(min(title_txt.width, thumb.width * 0.98))
            cmd_txt = Text(cmd, font="PT Mono", color=CRIMSON, font_size=12)
            cmd_txt.next_to(title_txt, DOWN, buff=0.06)
            card = VGroup(thumb, tri, title_txt, cmd_txt)
            cards.add(card)

        cards.arrange(RIGHT, buff=0.35).move_to(DOWN * 0.6)
        # Center and scale to fit frame
        if cards.width > 13.0:
            cards.scale_to_fit_width(13.0)

        self.play(FadeIn(playlist_title, shift=DOWN * 0.2), run_time=0.7)
        self.wait(0.3)
        self.play(
            LaggedStart(*[FadeIn(card, shift=UP * 0.3) for card in cards],
                         lag_ratio=0.25, run_time=3.5)
        )
        self.wait(9.5)
