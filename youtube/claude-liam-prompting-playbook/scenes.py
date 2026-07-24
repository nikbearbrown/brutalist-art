"""
scenes.py — claude-liam-prompting-playbook
The Prompting Playbook. Source: Anthropic Code with Claude (Margot Vanlar).
"""

from manim import *

PAGE   = "#FAF9F5"
INK    = "#3D3929"
SPARK  = "#D97757"
SOFT   = "#73705F"
GHOST  = "#A9A491"
BORDER = "#E5E2D9"
RED    = "#A44A32"

config.background_color = PAGE


class B01_TwoScenarios(Scene):
    def construct(self):
        dur = 22.74

        title = Text("Two Scenarios. One Discipline.", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        # --- Left lane: Prompt in Production ---
        left_x = -3.3
        left_hdr = Text("Prompt in Production", font_size=17, color=INK, weight=BOLD)
        left_hdr.move_to([left_x, 2.0, 0])
        self.play(FadeIn(left_hdr), run_time=0.3)

        # Stack of patches building up
        patch_labels = ["v0: core role", "+ guideline patch", "+ model-v1 fix", "+ tone override"]
        patch_colors = [GHOST, SOFT, SOFT, SOFT]
        patches = VGroup()
        for i, (lbl, col) in enumerate(zip(patch_labels, patch_colors)):
            box = RoundedRectangle(
                width=3.8, height=0.5, corner_radius=0.08,
                color=col, fill_color=PAGE, fill_opacity=1, stroke_width=1.4
            ).move_to([left_x, 1.1 - i * 0.52, 0])
            txt = Text(lbl, font_size=12, color=col)
            txt.move_to(box)
            patches.add(VGroup(box, txt))
        self.play(LaggedStart(*[FadeIn(p) for p in patches], lag_ratio=0.2), run_time=0.8)

        # Migration arrow breaks test cases
        mig_arrow = Arrow(
            start=[left_x - 0.3, -0.95, 0], end=[left_x + 0.3, -1.5, 0],
            color=RED, stroke_width=2.0, max_tip_length_to_length_ratio=0.18
        )
        mig_lbl = Text("model migration", font_size=11, color=RED)
        mig_lbl.next_to(mig_arrow, LEFT, buff=0.1)
        fail_txt = Text("test cases failing", font_size=13, color=RED, weight=BOLD)
        fail_txt.move_to([left_x, -1.9, 0])
        self.play(GrowArrow(mig_arrow), FadeIn(mig_lbl), run_time=0.4)
        self.play(FadeIn(fail_txt), run_time=0.3)

        # Divider
        div = Line([0, 2.5, 0], [0, -2.0, 0], color=BORDER, stroke_width=1.2)
        self.play(FadeIn(div), run_time=0.2)

        # --- Right lane: New Agent from Zero ---
        right_x = 3.3
        right_hdr = Text("New Agent from Zero", font_size=17, color=INK, weight=BOLD)
        right_hdr.move_to([right_x, 2.0, 0])
        self.play(FadeIn(right_hdr), run_time=0.3)

        blank_box = RoundedRectangle(
            width=3.8, height=1.0, corner_radius=0.12,
            color=GHOST, fill_color=PAGE, fill_opacity=1, stroke_width=1.4,
            stroke_opacity=0.5
        ).move_to([right_x, 0.8, 0])
        blank_lbl = Text("(blank prompt)", font_size=14, color=GHOST)
        blank_lbl.move_to(blank_box)
        self.play(FadeIn(blank_box), FadeIn(blank_lbl), run_time=0.4)

        questions = ["Which model?", "Which harness?", "What baseline?"]
        for i, q in enumerate(questions):
            qt = Text(q, font_size=13, color=SOFT)
            qt.move_to([right_x, -0.2 - i * 0.55, 0])
            self.play(FadeIn(qt), run_time=0.2)

        # --- Convergence node ---
        conv_box = RoundedRectangle(
            width=5.5, height=0.8, corner_radius=0.12,
            color=SPARK, fill_color=PAGE, fill_opacity=1, stroke_width=2.2
        ).move_to([0, -2.6, 0])
        conv_txt = Text("One Discipline: Eval Suite Before Anything Else",
                        font_size=15, color=SPARK, weight=BOLD)
        conv_txt.move_to(conv_box)

        arr_left = Arrow(
            start=[left_x, -2.15, 0], end=[-1.0, -2.6, 0],
            color=SPARK, stroke_width=1.8, max_tip_length_to_length_ratio=0.15
        )
        arr_right = Arrow(
            start=[right_x, -2.15, 0], end=[1.0, -2.6, 0],
            color=SPARK, stroke_width=1.8, max_tip_length_to_length_ratio=0.15
        )
        self.play(
            GrowArrow(arr_left), GrowArrow(arr_right),
            FadeIn(conv_box), FadeIn(conv_txt),
            run_time=0.6
        )

        self.wait(dur - 4.5)


class B02_EvalSuite(Scene):
    def construct(self):
        dur = 27.35

        title = Text("Eval Suite: Three Categories, Every Time.", font_size=34, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        col_data = [
            ("Control", GHOST, [
                "Basic plan data limit",
                "Unambiguous query",
                "Should always pass",
            ]),
            ("Edge Cases", SOFT, [
                "Proration calculation",
                "Grandfathered plan lookup",
                "Failures you've seen before",
            ]),
            ("Boundary", SPARK, [
                "Billing error → escalate",
                "Out-of-scope request → refuse",
                "Where the model's role ends",
            ]),
        ]

        col_xs = [-3.8, 0.0, 3.8]

        # Headers
        for (name, col, _), x in zip(col_data, col_xs):
            hdr = Text(name, font_size=19, color=col, weight=BOLD)
            hdr.move_to([x, 1.9, 0])
            self.play(FadeIn(hdr), run_time=0.25)

        # Column lines
        for x in [-1.9, 1.9]:
            ln = Line([x, 2.3, 0], [x, -1.2, 0], color=BORDER, stroke_width=1.1)
            self.add(ln)

        # Items
        for (name, col, items), x in zip(col_data, col_xs):
            for i, item in enumerate(items):
                box = RoundedRectangle(
                    width=3.3, height=0.6, corner_radius=0.09,
                    color=col, fill_color=PAGE, fill_opacity=1, stroke_width=1.3
                ).move_to([x, 1.0 - i * 0.75, 0])
                txt = Text(item, font_size=11, color=INK)
                txt.move_to(box)
                self.play(FadeIn(VGroup(box, txt)), run_time=0.2)

        # Arrow: run against prompt
        run_arrow = Arrow(
            start=[-1.5, -1.5, 0], end=[1.5, -1.5, 0],
            color=INK, stroke_width=1.8, max_tip_length_to_length_ratio=0.12
        )
        run_lbl = Text("run against v0 prompt", font_size=13, color=SOFT)
        run_lbl.next_to(run_arrow, UP, buff=0.1)
        self.play(GrowArrow(run_arrow), FadeIn(run_lbl), run_time=0.4)

        # Result circles pass/fail
        result_row = VGroup()
        results = [
            (GHOST, "pass"),
            (RED, "fail"),
            (RED, "fail"),
        ]
        for i, ((col, label), x) in enumerate(zip(results, col_xs)):
            circle = Circle(radius=0.28, color=col, fill_color=col, fill_opacity=0.15, stroke_width=2.0)
            circle.move_to([x, -2.1, 0])
            txt = Text(label, font_size=12, color=col, weight=BOLD)
            txt.move_to(circle)
            result_row.add(VGroup(circle, txt))
        self.play(FadeIn(result_row), run_time=0.4)

        note = Text("Without a suite, you cannot tell improvement from a different kind of wrong.",
                    font_size=14, color=SOFT)
        note.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note), run_time=0.35)

        self.wait(dur - 6.0)


class B04_PatchDebt(Scene):
    def construct(self):
        dur = 35.20

        title = Text("The Patch That Became the Bug.", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        # Timeline: three nodes left to right
        node_xs = [-4.5, 0.0, 4.5]
        node_y = 0.5

        # Node 1: Model v1 hallucination
        n1_box = RoundedRectangle(
            width=3.4, height=1.4, corner_radius=0.15,
            color=GHOST, fill_color=PAGE, fill_opacity=1, stroke_width=1.6
        ).move_to([node_xs[0], node_y, 0])
        n1_hdr = Text("Model v1", font_size=15, color=SOFT, weight=BOLD)
        n1_hdr.move_to([node_xs[0], node_y + 0.35, 0])
        n1_body = Text("Hallucinating\nplan details", font_size=13, color=SOFT)
        n1_body.move_to([node_xs[0], node_y - 0.2, 0])
        self.play(FadeIn(n1_box), FadeIn(n1_hdr), FadeIn(n1_body), run_time=0.4)

        # Arrow 1 → patch
        arr1 = Arrow(
            start=[node_xs[0] + 1.8, node_y, 0],
            end=[node_xs[1] - 1.8, node_y, 0],
            color=SPARK, stroke_width=2.0, max_tip_length_to_length_ratio=0.15
        )
        self.play(GrowArrow(arr1), run_time=0.35)

        # Node 2: Defensive instruction (patch)
        n2_box = RoundedRectangle(
            width=3.4, height=1.4, corner_radius=0.15,
            color=SPARK, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
        ).move_to([node_xs[1], node_y, 0])
        n2_hdr = Text("Defensive Patch", font_size=15, color=SPARK, weight=BOLD)
        n2_hdr.move_to([node_xs[1], node_y + 0.35, 0])
        n2_body = Text('"Never give wrong\nplan details."', font_size=12, color=INK)
        n2_body.move_to([node_xs[1], node_y - 0.2, 0])
        self.play(FadeIn(n2_box), FadeIn(n2_hdr), FadeIn(n2_body), run_time=0.4)

        patch_note = Text("Written to stop hallucination on v1.", font_size=12, color=SPARK)
        patch_note.move_to([node_xs[1], node_y - 1.1, 0])
        self.play(FadeIn(patch_note), run_time=0.3)

        # Arrow 2 → model v2
        arr2 = Arrow(
            start=[node_xs[1] + 1.8, node_y, 0],
            end=[node_xs[2] - 1.8, node_y, 0],
            color=INK, stroke_width=2.0, max_tip_length_to_length_ratio=0.15
        )
        mig_lbl = Text("model migration", font_size=12, color=SOFT)
        mig_lbl.next_to(arr2, UP, buff=0.1)
        self.play(GrowArrow(arr2), FadeIn(mig_lbl), run_time=0.35)

        # Node 3: Model v2 — instruction followed literally
        n3_box = RoundedRectangle(
            width=3.4, height=1.4, corner_radius=0.15,
            color=RED, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
        ).move_to([node_xs[2], node_y, 0])
        n3_hdr = Text("Model v2", font_size=15, color=RED, weight=BOLD)
        n3_hdr.move_to([node_xs[2], node_y + 0.35, 0])
        n3_body = Text("Follows instruction\nliterally", font_size=13, color=RED)
        n3_body.move_to([node_xs[2], node_y - 0.2, 0])
        self.play(FadeIn(n3_box), FadeIn(n3_hdr), FadeIn(n3_body), run_time=0.4)

        # What actually happens
        consequence = Text(
            "Customer has 5 GB in context.\nModel sends them to the URL instead.",
            font_size=14, color=RED
        )
        consequence.move_to([node_xs[2], node_y - 1.35, 0])
        self.play(FadeIn(consequence), run_time=0.35)

        # Horizontal line separating bottom lesson
        sep = Line([-6.5, -1.9, 0], [6.5, -1.9, 0], color=BORDER, stroke_width=1.0)
        self.play(FadeIn(sep), run_time=0.2)

        # Lesson
        lesson_hdr = Text("Best practice:", font_size=15, color=INK, weight=BOLD)
        lesson_hdr.move_to([-3.0, -2.4, 0])
        lesson_body = Text(
            "Version-control defensive instructions. Track why they exist.",
            font_size=14, color=SOFT
        )
        lesson_body.move_to([1.5, -2.4, 0])
        self.play(FadeIn(lesson_hdr), FadeIn(lesson_body), run_time=0.4)

        self.wait(dur - 7.0)


class B08_GenEvalRepair(Scene):
    def construct(self):
        dur = 33.60

        title = Text("Generate. Evaluate. Repair.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        # Three prompt nodes in a row
        node_data = [
            ("Generator", INK, "Draft schedule\nfrom constraints"),
            ("Evaluator", SPARK, "Check every rule.\nReport violations."),
            ("Repair", INK, "Fix targeted\nviolations only."),
        ]
        node_xs = [-4.0, 0.0, 4.0]
        node_y = 0.6

        nodes = []
        for (name, col, desc), x in zip(node_data, node_xs):
            box = RoundedRectangle(
                width=3.5, height=1.6, corner_radius=0.18,
                color=col, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
            ).move_to([x, node_y, 0])
            hdr = Text(name, font_size=18, color=col, weight=BOLD)
            hdr.move_to([x, node_y + 0.4, 0])
            body = Text(desc, font_size=13, color=SOFT)
            body.move_to([x, node_y - 0.25, 0])
            nodes.append(VGroup(box, hdr, body))
        self.play(LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.25), run_time=0.9)

        # Arrow Generator → Evaluator
        arr1 = Arrow(
            start=[node_xs[0] + 1.85, node_y, 0],
            end=[node_xs[1] - 1.85, node_y, 0],
            color=INK, stroke_width=1.8, max_tip_length_to_length_ratio=0.14
        )
        lbl1 = Text("draft schedule", font_size=12, color=SOFT)
        lbl1.next_to(arr1, UP, buff=0.1)
        self.play(GrowArrow(arr1), FadeIn(lbl1), run_time=0.35)

        # Arrow Evaluator → Repair
        arr2 = Arrow(
            start=[node_xs[1] + 1.85, node_y, 0],
            end=[node_xs[2] - 1.85, node_y, 0],
            color=SPARK, stroke_width=1.8, max_tip_length_to_length_ratio=0.14
        )
        lbl2 = Text("violations + evidence", font_size=12, color=SPARK)
        lbl2.next_to(arr2, UP, buff=0.1)
        self.play(GrowArrow(arr2), FadeIn(lbl2), run_time=0.35)

        # Loop-back arrow Repair → Evaluator (below)
        loop_y = node_y - 1.5
        loop_path = ArcBetweenPoints(
            start=[node_xs[2] - 0.2, node_y - 0.85, 0],
            end=[node_xs[1] + 0.2, node_y - 0.85, 0],
            angle=TAU / 6
        )
        loop_arrow = Arrow(
            start=[node_xs[2] - 0.2, node_y - 0.85, 0],
            end=[node_xs[1] + 0.2, node_y - 0.85, 0],
            color=SPARK, stroke_width=1.8, max_tip_length_to_length_ratio=0.14
        )
        loop_lbl = Text("targeted fix", font_size=12, color=SPARK)
        loop_lbl.move_to([2.0, node_y - 1.2, 0])
        self.play(GrowArrow(loop_arrow), FadeIn(loop_lbl), run_time=0.35)

        # Output arrow from Evaluator (down, when clean)
        out_arrow = Arrow(
            start=[node_xs[1], node_y - 0.85, 0],
            end=[node_xs[1], node_y - 1.75, 0],
            color=GHOST, stroke_width=1.6, max_tip_length_to_length_ratio=0.18
        )
        out_lbl = Text("clean schedule", font_size=12, color=GHOST)
        out_lbl.next_to(out_arrow, RIGHT, buff=0.1)
        self.play(GrowArrow(out_arrow), FadeIn(out_lbl), run_time=0.3)

        # Separator
        sep = Line([-6.5, -2.05, 0], [6.5, -2.05, 0], color=BORDER, stroke_width=1.0)
        self.play(FadeIn(sep), run_time=0.2)

        # Benefits row
        benefits = [
            ("Fewer tokens", SOFT),
            ("Lower latency", SOFT),
            ("Soft constraints at runtime", SPARK),
        ]
        bx = [-4.0, 0.0, 4.0]
        for (txt, col), x in zip(benefits, bx):
            bt = Text(txt, font_size=13, color=col, weight=BOLD)
            bt.move_to([x, -2.5, 0])
            self.play(FadeIn(bt), run_time=0.2)

        lesson = Text(
            "Each prompt has one job. When steps are separable, separate them.",
            font_size=14, color=INK
        )
        lesson.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(lesson), run_time=0.4)

        self.wait(dur - 7.5)
