"""
scenes.py — claude-liam-context-dreaming
Claude, Dreaming.
Lamis Mukta — AI Native DevCon London, June 2026

Palette: Claude brand
  PAGE   #FAF9F5  cream ground
  INK    #3D3929  warm near-black
  SPARK  #D97757  terracotta — ONE accent per beat
  SOFT   #73705F  secondary text
  GHOST  #A9A491  caption / ghost text
  BORDER #E5E2D9  subtle divider

One Manim scene per GRAPHIC beat.
Render one scene:
  manim -qh --fps 30 -r 1920,1080 scenes.py B05_RAGAsLibrary
  mv media/videos/scenes/*/B05_RAGAsLibrary.mp4 manim/B05.mp4
"""

from manim import *
import numpy as np

try:            # geometry-stub environments (static_scene_check) lack these
    BOLD
except NameError:
    BOLD = "BOLD"
try:
    ITALIC
except NameError:
    ITALIC = "ITALIC"
try:
    NORMAL
except NameError:
    NORMAL = "NORMAL"

PAGE   = "#FAF9F5"
INK    = "#3D3929"
SPARK  = "#D97757"
SOFT   = "#73705F"
GHOST  = "#A9A491"
BORDER = "#E5E2D9"

config.background_color = PAGE


def source_caption(scene):
    cap = Text(
        "After Mukta 2026 — Learning while you sleep (AI Native DevCon London)",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


# ─── ACT I ────────────────────────────────────────────────────────────────────

class B05_RAGAsLibrary(Scene):
    def construct(self):
        dur = 12.78

        title = Text("RAG: A Very Fast Library", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Document slabs
        slab_data = [
            ("doc_A", "[0.21, 0.83, 0.07…]"),
            ("doc_B", "[0.54, 0.31, 0.92…]"),
            ("doc_C", "[0.08, 0.67, 0.45…]"),
        ]
        slabs = VGroup()
        for i, (doc, vec) in enumerate(slab_data):
            bg = Rectangle(width=5.8, height=0.72, color=BORDER,
                           fill_color=PAGE, fill_opacity=1, stroke_width=1.5)
            bg.shift(RIGHT * 1.6 + UP * (0.8 - i * 0.9))
            doc_txt = Text(doc, font_size=19, color=INK, weight=BOLD)
            doc_txt.move_to(bg).shift(LEFT * 2.1)
            vec_txt = Text(vec, font_size=16, color=SOFT)
            vec_txt.move_to(bg).shift(RIGHT * 0.8)
            slabs.add(VGroup(bg, doc_txt, vec_txt))

        # Query box
        qbox = Rectangle(width=2.4, height=0.72, color=INK,
                         fill_color=PAGE, fill_opacity=1, stroke_width=2)
        qbox.shift(LEFT * 4.3 + UP * 0.8)
        qlbl = Text("query", font_size=21, color=INK, weight=BOLD)
        qlbl.move_to(qbox)

        # Search arrow to nearest slab
        search_arr = Arrow(
            qbox.get_right(),
            slabs[0][0].get_left(),
            color=GHOST, stroke_width=2.5, buff=0.08,
        )
        nearest_lbl = Text("nearest", font_size=17, color=SOFT)
        nearest_lbl.next_to(search_arr, UP, buff=0.1)

        # Terracotta question mark — 'findable?'
        q_mark = Text("?", font_size=58, color=SPARK, weight=BOLD)
        q_mark.shift(RIGHT * 1.6 + DOWN * 1.9)
        findable = Text("findable", font_size=21, color=SPARK)
        findable.next_to(q_mark, DOWN, buff=0.08)

        self.play(FadeIn(slabs), run_time=1.0)
        self.play(FadeIn(VGroup(qbox, qlbl)), run_time=0.5)
        self.play(GrowArrow(search_arr), FadeIn(nearest_lbl), run_time=0.9)
        self.wait(0.6)
        self.play(FadeIn(q_mark), FadeIn(findable), run_time=0.7)
        self.wait(dur - 4.7)


class B06_SleepSynthesis(Scene):
    def construct(self):
        dur = 15.47

        title = Text("Sleep: Synthesis, Not Retrieval", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Three experience nodes arranged in a triangle
        positions = [LEFT * 3.5 + UP * 0.6, RIGHT * 3.5 + UP * 0.6, DOWN * 2.2]
        labels    = ["experience A", "experience B", "experience C"]
        nodes = VGroup()
        node_circles = []
        for pos, lbl in zip(positions, labels):
            c = Circle(radius=0.55, color=INK, fill_color=PAGE,
                       fill_opacity=1, stroke_width=2)
            c.move_to(pos)
            t = Text(lbl, font_size=17, color=SOFT)
            t.next_to(c, DOWN, buff=0.12)
            nodes.add(VGroup(c, t))
            node_circles.append(c)

        # Terracotta arcs between nodes — use position arrays directly (avoid get_center())
        arc_ab = CurvedArrow(positions[0], positions[1], angle=-PI / 4,
                             color=SPARK, stroke_width=2.5)
        arc_ac = CurvedArrow(positions[0], positions[2], angle=PI / 4,
                             color=SPARK, stroke_width=2.5)
        arc_bc = CurvedArrow(positions[1], positions[2], angle=-PI / 4,
                             color=SPARK, stroke_width=2.5)
        arcs = VGroup(arc_ab, arc_ac, arc_bc)

        # Emergent pattern node at center
        center_pos = np.array([0.0, 0.0, 0.0])
        pattern_c = Circle(radius=0.62, color=SPARK, fill_color=SPARK,
                           fill_opacity=0.15, stroke_width=2.5)
        pattern_c.move_to(center_pos)
        pattern_lbl = Text("pattern", font_size=21, color=SPARK, weight=BOLD)
        pattern_lbl.move_to(center_pos)
        pattern_grp = VGroup(pattern_c, pattern_lbl)

        # Radial arrows from center to each position
        radial_arrows = VGroup(*[
            Arrow(center_pos, pos, color=SPARK, stroke_width=1.8, buff=0.6)
            for pos in positions
        ])

        self.play(FadeIn(nodes), run_time=1.0)
        self.wait(0.5)
        self.play(Create(arcs), run_time=1.5)
        self.wait(0.4)
        self.play(FadeIn(pattern_grp), Create(radial_arrows), run_time=1.0)
        self.wait(dur - 5.4)


# ─── ACT II ───────────────────────────────────────────────────────────────────

class B13_KnowledgeTaxonomy(Scene):
    def construct(self):
        dur = 14.19

        title = Text("RAG by Knowledge Type", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        rows = [
            ("Episodic",    1.00, INK),   # full
            ("Semantic",    0.46, SOFT),  # half
            ("Procedural",  0.08, SPARK), # near-zero — terracotta
        ]

        bar_max_w = 6.5
        bar_h     = 0.72
        bar_x0    = -0.9   # left edge of bars
        y_positions = [1.2, 0.0, -1.2]

        row_groups = []
        for (label, frac, color), y in zip(rows, y_positions):
            row_lbl = Text(label, font_size=24, color=INK, weight=BOLD)
            row_lbl.move_to([bar_x0 - 1.7, y, 0])

            # Empty track
            track = Rectangle(width=bar_max_w, height=bar_h,
                               color=BORDER, fill_color=PAGE,
                               fill_opacity=1, stroke_width=1.2)
            track.move_to([bar_x0 + bar_max_w / 2, y, 0])

            # Filled bar
            fill_w = max(bar_max_w * frac, 0.12)
            bar = Rectangle(width=fill_w, height=bar_h,
                            color=color, fill_color=color,
                            fill_opacity=0.82, stroke_width=0)
            bar.move_to([bar_x0 + fill_w / 2, y, 0])

            row_groups.append((row_lbl, track, bar))

        # RAG label above bar area
        rag_lbl = Text("RAG strength →", font_size=19, color=SOFT)
        rag_lbl.move_to([bar_x0 + bar_max_w / 2, 2.3, 0])
        self.add(rag_lbl)

        for row_lbl, track, bar in row_groups:
            self.add(row_lbl, track)

        # Animate bars in sequence
        self.wait(0.4)
        for (_, _, bar), (row_lbl, track, _) in zip(rows, row_groups):
            pass

        # Episodic
        self.play(Create(row_groups[0][2]), run_time=0.9)
        self.wait(0.4)
        # Semantic
        self.play(Create(row_groups[1][2]), run_time=0.9)
        self.wait(0.4)
        # Procedural — terracotta, near-zero
        self.play(Create(row_groups[2][2]), run_time=0.7)
        proc_marker = Text("← falls apart", font_size=20, color=SPARK)
        proc_marker.next_to(row_groups[2][2], RIGHT, buff=0.3)
        self.play(FadeIn(proc_marker), run_time=0.5)
        self.wait(dur - 5.2)


class B15_ConsolidationCross(Scene):
    def construct(self):
        dur = 12.97

        title = Text("Consolidation: Fragments → Regularities", font_size=35, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Left: fragmented blobs
        blob_positions = [LEFT * 4.5 + UP * 0.8, LEFT * 3.2 + UP * 0.1,
                          LEFT * 4.8 + DOWN * 0.6, LEFT * 3.8 + DOWN * 1.0]
        blob_sizes     = [0.38, 0.44, 0.32, 0.40]
        blobs = VGroup(*[
            Ellipse(width=s * 2, height=s * 1.4, color=INK,
                    fill_color=PAGE, fill_opacity=1, stroke_width=1.5).move_to(p)
            for p, s in zip(blob_positions, blob_sizes)
        ])
        frags_lbl = Text("fragments", font_size=20, color=SOFT)
        frags_lbl.shift(LEFT * 4.1 + DOWN * 1.7)

        # Consolidation arrow
        arrow = Arrow(LEFT * 2.0, RIGHT * 1.0, color=INK,
                      stroke_width=2.5, buff=0)
        arrow_lbl = Text("consolidation", font_size=19, color=INK)
        arrow_lbl.next_to(arrow, UP, buff=0.15)

        # Right: clean pattern output
        pattern_box = Rectangle(width=2.8, height=2.2, color=BORDER,
                                fill_color=PAGE, fill_opacity=1, stroke_width=1.5)
        pattern_box.shift(RIGHT * 3.5)
        for i in range(3):
            ln = Line(RIGHT * 2.3 + UP * (0.55 - i * 0.55),
                      RIGHT * 4.7 + UP * (0.55 - i * 0.55),
                      color=GHOST, stroke_width=1.0)
            self.add(ln)

        # Terracotta label: regularities
        reg_lbl = Text("regularities", font_size=22, color=SPARK, weight=BOLD)
        reg_lbl.shift(RIGHT * 3.5 + DOWN * 1.5)

        self.play(FadeIn(blobs), FadeIn(frags_lbl), run_time=0.9)
        self.wait(0.3)
        self.play(GrowArrow(arrow), Write(arrow_lbl), run_time=1.0)
        self.play(FadeIn(pattern_box), run_time=0.7)
        self.play(FadeIn(reg_lbl), run_time=0.6)
        self.wait(dur - 4.5)


# ─── ACT III ──────────────────────────────────────────────────────────────────

class B21_PessimisticVsOptimistic(Scene):
    def construct(self):
        dur = 17.11

        title = Text("Locking Strategies Compared", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        row_y  = [0.8, -1.4]
        labels = ["Pessimistic", "Optimistic"]
        colors = [INK, SPARK]

        # Row labels
        for lbl, y, col in zip(labels, row_y, colors):
            t = Text(lbl, font_size=26, color=col, weight=BOLD)
            t.move_to([- 4.5, y, 0])
            self.add(t)

        # ── Pessimistic row ──
        # Lock icon
        lock_box = Rectangle(width=0.9, height=0.9, color=INK,
                             fill_color=PAGE, fill_opacity=1, stroke_width=2)
        lock_box.move_to([-2.8, row_y[0], 0])
        lock_lbl = Text("🔒", font_size=28)
        lock_lbl.move_to(lock_box)

        # Blocked readers
        blocked_arr = Arrow([-1.8, row_y[0], 0], [-0.3, row_y[0], 0],
                            color=GHOST, stroke_width=2, buff=0)
        blocked_lbl = Text("readers blocked", font_size=18, color=SOFT)
        blocked_lbl.next_to(blocked_arr, UP, buff=0.1)

        # Exclusive write box
        write_box = Rectangle(width=2.2, height=0.72, color=INK,
                              fill_color=PAGE, fill_opacity=1, stroke_width=2)
        write_box.move_to([1.5, row_y[0], 0])
        write_lbl = Text("exclusive write", font_size=18, color=INK)
        write_lbl.move_to(write_box)

        # ── Optimistic row ──
        # Free read arrows
        read_arrs = VGroup(*[
            Arrow([-2.8, row_y[1] + 0.32 - i * 0.32, 0],
                  [-1.0, row_y[1] + 0.32 - i * 0.32, 0],
                  color=GHOST, stroke_width=2.0, buff=0)
            for i in range(3)
        ])
        free_lbl = Text("readers free", font_size=18, color=SOFT)
        free_lbl.move_to([-1.9, row_y[1] - 0.62, 0])

        # Write arrow
        write_arr2 = Arrow([-1.0, row_y[1], 0], [0.8, row_y[1], 0],
                           color=SPARK, stroke_width=2.5, buff=0)
        write_lbl2 = Text("write (tentative)", font_size=18, color=SPARK)
        write_lbl2.next_to(write_arr2, DOWN, buff=0.1)

        # Conflict check at end
        check_box = RoundedRectangle(width=1.6, height=0.72, corner_radius=0.15,
                                     color=SPARK, fill_color=PAGE,
                                     fill_opacity=1, stroke_width=2)
        check_box.move_to([2.2, row_y[1], 0])
        check_lbl = Text("check\nconflict", font_size=16, color=SPARK)
        check_lbl.move_to(check_box)

        # Terracotta annotation
        borrow_lbl = Text("← borrowed from databases", font_size=19, color=SPARK)
        borrow_lbl.move_to([1.0, row_y[1] + 0.85, 0])

        # Divider
        div = Line(LEFT * 5.5, RIGHT * 5.5, color=BORDER, stroke_width=1.2)
        div.shift(DOWN * 0.25)
        self.add(div)

        # Animate pessimistic row first
        self.play(FadeIn(lock_box), FadeIn(lock_lbl), run_time=0.7)
        self.play(GrowArrow(blocked_arr), Write(blocked_lbl), run_time=0.9)
        self.play(FadeIn(write_box), FadeIn(write_lbl), run_time=0.6)
        self.wait(0.5)

        # Then optimistic row
        self.play(Create(read_arrs), FadeIn(free_lbl), run_time=0.9)
        self.play(GrowArrow(write_arr2), FadeIn(write_lbl2), run_time=0.8)
        self.play(FadeIn(check_box), FadeIn(check_lbl), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(borrow_lbl), run_time=0.6)
        self.wait(dur - 6.5)


class B22_KnowledgeDelta(Scene):
    def construct(self):
        dur = 12.65

        title = Text("The Knowledge Delta", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Before circle
        before_c = Circle(radius=0.8, color=INK, fill_color=PAGE,
                          fill_opacity=1, stroke_width=2)
        before_c.shift(LEFT * 3.8 + UP * 0.5)
        before_lbl = Text("before\nsession", font_size=18, color=SOFT)
        before_lbl.move_to(before_c)

        # After circle
        after_c = Circle(radius=0.88, color=INK, fill_color=PAGE,
                         fill_opacity=1, stroke_width=2)
        after_c.shift(RIGHT * 3.8 + UP * 0.5)
        after_lbl = Text("after\nsession", font_size=18, color=SOFT)
        after_lbl.move_to(after_c)

        # Delta arrow between
        delta_arr = Arrow(before_c.get_right(), after_c.get_left(),
                          color=GHOST, stroke_width=2.5, buff=0.1)

        # Terracotta Δ on the arrow
        delta_sym = Text("Δ", font_size=52, color=SPARK, weight=BOLD)
        delta_sym.move_to(delta_arr.get_center() + UP * 0.55)
        delta_txt = Text("knowledge delta", font_size=20, color=SPARK)
        delta_txt.next_to(delta_sym, DOWN, buff=0.05)

        # Stack of Δ symbols below: store accumulates
        stack_lbl = Text("store accumulates deltas:", font_size=18, color=SOFT)
        stack_lbl.shift(DOWN * 2.0 + LEFT * 1.2)
        stack_deltas = VGroup(*[
            Text("Δ", font_size=28, color=SPARK).shift(DOWN * 2.0 + RIGHT * (i * 0.55))
            for i in range(5)
        ])

        self.play(FadeIn(before_c), FadeIn(before_lbl), run_time=0.7)
        self.play(FadeIn(after_c), FadeIn(after_lbl), run_time=0.7)
        self.play(GrowArrow(delta_arr), run_time=0.7)
        self.play(FadeIn(delta_sym), FadeIn(delta_txt), run_time=0.7)
        self.wait(0.4)
        self.play(FadeIn(stack_lbl), run_time=0.5)
        self.play(FadeIn(stack_deltas), run_time=0.7)
        self.wait(dur - 5.4)


class B23_DebugPattern(Scene):
    def construct(self):
        dur = 15.51

        title = Text("Cross-Session Pattern Extraction", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Session timeline
        session_x = [-4.5, 0.0, 4.5]
        session_labels = ["session 1", "session 2", "session 3"]
        session_circles = []
        session_grps = VGroup()
        for x, lbl in zip(session_x, session_labels):
            bg = Rectangle(width=2.6, height=1.4, color=BORDER,
                           fill_color=PAGE, fill_opacity=1, stroke_width=1.5)
            bg.shift([x, 1.0, 0])
            t = Text(lbl, font_size=19, color=SOFT)
            t.move_to(bg)
            session_circles.append(bg)
            session_grps.add(VGroup(bg, t))

        # Connecting timeline line
        tl = Line([-5.8, 1.0, 0], [5.8, 1.0, 0], color=GHOST, stroke_width=1.2)
        self.add(tl)

        # Bug markers (dots below each session)
        bug_positions = [[x, -0.2, 0] for x in session_x]
        bugs = VGroup(*[
            Dot(point=p, radius=0.14, color=INK)
            for p in bug_positions
        ])
        bug_lbl = VGroup(*[
            Text(f"bug {i+1}", font_size=16, color=SOFT).next_to(
                Dot(point=p), DOWN, buff=0.1)
            for i, p in enumerate(bug_positions)
        ])

        # Arrows from sessions down to bugs
        sess_arrows = VGroup(*[
            Arrow([x, 0.3, 0], [x, -0.05, 0],
                  color=GHOST, stroke_width=1.8, buff=0.05)
            for x in session_x
        ])

        # Terracotta arc connecting all three bugs
        arc = CurvedArrow(
            bug_positions[0], bug_positions[2],
            angle=-PI / 5, color=SPARK, stroke_width=2.5,
        )
        pattern_tag = Text("pattern", font_size=22, color=SPARK, weight=BOLD)
        pattern_tag.shift([0.0, -1.2, 0])

        # Dream store card
        store_box = Rectangle(width=3.2, height=1.1, color=SPARK,
                              fill_color=PAGE, fill_opacity=1, stroke_width=2)
        store_box.shift([0.0, -2.6, 0])
        store_txt = Text("component failure pattern", font_size=18, color=INK)
        store_txt.move_to(store_box)
        store_hdr = Text("dream store", font_size=16, color=SPARK)
        store_hdr.next_to(store_box, UP, buff=0.1)

        extract_arr = Arrow([0.0, -1.55, 0], [0.0, -2.0, 0],
                            color=SPARK, stroke_width=2, buff=0.05)

        self.play(FadeIn(session_grps), run_time=0.8)
        self.play(Create(sess_arrows), FadeIn(bugs), FadeIn(bug_lbl), run_time=0.9)
        self.wait(0.4)
        self.play(Create(arc), FadeIn(pattern_tag), run_time=1.0)
        self.wait(0.3)
        self.play(GrowArrow(extract_arr), FadeIn(VGroup(store_box, store_txt, store_hdr)), run_time=0.9)
        self.wait(dur - 5.3)


# ─── ACT IV ───────────────────────────────────────────────────────────────────

class B29_DualFilter(Scene):
    def construct(self):
        dur = 15.94

        title = Text("Persistence × Coherence: Dual Filter", font_size=35, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Left failure: noise (single spike)
        noise_x = -4.5
        spike = Line([noise_x, -1.2, 0], [noise_x, 0.9, 0], color=SOFT, stroke_width=3)
        spike_tip = Dot(point=[noise_x, 0.9, 0], radius=0.12, color=SOFT)
        noise_lbl = Text("noise", font_size=20, color=SOFT)
        noise_lbl.shift([noise_x, -1.7, 0])
        sub_noise = Text("one-off anomaly", font_size=16, color=GHOST)
        sub_noise.shift([noise_x, -2.1, 0])

        # Right failure: incoherent fragments
        frag_x = 4.5
        frag_blobs = VGroup(*[
            Ellipse(width=0.5, height=0.35, color=SOFT,
                    fill_color=PAGE, fill_opacity=1, stroke_width=1.2
                    ).shift([frag_x + (i % 3) * 0.6 - 0.6, 0.4 - (i // 3) * 0.6, 0])
            for i in range(6)
        ])
        frag_lbl = Text("incoherent", font_size=20, color=SOFT)
        frag_lbl.shift([frag_x, -1.7, 0])
        sub_frag = Text("fragments", font_size=16, color=GHOST)
        sub_frag.shift([frag_x, -2.1, 0])

        # Center: dual gate
        gate_box = Rectangle(width=2.8, height=2.4, color=SPARK,
                             fill_color=PAGE, fill_opacity=1, stroke_width=2.5)
        gate_box.shift([0.0, -0.2, 0])
        p_line = Text("P: persistence", font_size=19, color=INK, weight=BOLD)
        p_line.move_to(gate_box).shift(UP * 0.42)
        x_sym = Text("×", font_size=28, color=SPARK, weight=BOLD)
        x_sym.move_to(gate_box)
        c_line = Text("C: coherence", font_size=19, color=INK, weight=BOLD)
        c_line.move_to(gate_box).shift(DOWN * 0.42)
        gate_grp = VGroup(gate_box, p_line, x_sym, c_line)

        # Blocking arrows from failures into gate
        block_left = Arrow([-2.5, -0.2, 0], [-1.45, -0.2, 0],
                           color=GHOST, stroke_width=2, buff=0)
        block_right = Arrow([2.5, -0.2, 0], [1.45, -0.2, 0],
                            color=GHOST, stroke_width=2, buff=0)
        blocked_x_l = Text("✗", font_size=26, color=INK).next_to(block_left, UP, buff=0.05)
        blocked_x_r = Text("✗", font_size=26, color=INK).next_to(block_right, UP, buff=0.05)

        # Pass-through arrow from gate
        pass_arr = Arrow([0.0, -1.45, 0], [0.0, -2.65, 0],
                         color=SPARK, stroke_width=2.5, buff=0)
        pass_lbl = Text("earns its place", font_size=18, color=SPARK)
        pass_lbl.next_to(pass_arr, RIGHT, buff=0.18)

        self.play(FadeIn(VGroup(spike, spike_tip, noise_lbl, sub_noise)), run_time=0.7)
        self.play(FadeIn(VGroup(frag_blobs, frag_lbl, sub_frag)), run_time=0.7)
        self.wait(0.4)
        self.play(FadeIn(gate_grp), run_time=0.9)
        self.play(
            GrowArrow(block_left), FadeIn(blocked_x_l),
            GrowArrow(block_right), FadeIn(blocked_x_r),
            run_time=0.8,
        )
        self.wait(0.4)
        self.play(GrowArrow(pass_arr), FadeIn(pass_lbl), run_time=0.7)
        self.wait(dur - 5.6)


class B32_SoftAlignment(Scene):
    def construct(self):
        dur = 16.23

        title = Text("Soft Alignment: Promote vs Reconcile", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Hot insight node (top)
        hot_box = Rectangle(width=2.6, height=0.85, color=SPARK,
                            fill_color=PAGE, fill_opacity=1, stroke_width=2)
        hot_box.shift([0.0, 2.0, 0])
        hot_lbl = Text("HOT insight", font_size=20, color=SPARK, weight=BOLD)
        hot_lbl.move_to(hot_box)

        # Test arrow down
        test_arr = Arrow([0.0, 1.57, 0], [0.0, 0.72, 0],
                         color=INK, stroke_width=2.5, buff=0)
        test_lbl = Text("test vs cold store", font_size=17, color=SOFT)
        test_lbl.next_to(test_arr, RIGHT, buff=0.15)

        # Cold store base
        cold_box = Rectangle(width=2.8, height=0.85, color=GHOST,
                             fill_color=PAGE, fill_opacity=1, stroke_width=1.5)
        cold_box.shift([0.0, 0.28, 0])
        cold_lbl = Text("COLD store", font_size=18, color=SOFT)
        cold_lbl.move_to(cold_box)

        # Branch point
        branch_dot = Dot(point=[0.0, -0.3, 0], radius=0.1, color=INK)

        # Left branch — consistent → promote
        consist_arr = Arrow([0.0, -0.35, 0], [-3.5, -1.6, 0],
                            color=SPARK, stroke_width=2.5, buff=0)
        promote_box = Rectangle(width=2.6, height=0.8, color=SPARK,
                                fill_color=PAGE, fill_opacity=1, stroke_width=2)
        promote_box.shift([-3.5, -2.1, 0])
        promote_lbl = Text("PROMOTE", font_size=20, color=SPARK, weight=BOLD)
        promote_lbl.move_to(promote_box)
        consist_tag = Text("consistent", font_size=17, color=SPARK)
        consist_tag.next_to(consist_arr, LEFT, buff=0.1).shift(DOWN * 0.2)

        # Right branch — contradictory → queue
        contra_arr = Arrow([0.0, -0.35, 0], [3.5, -1.6, 0],
                           color=SPARK, stroke_width=2.5, buff=0)
        queue_box = Rectangle(width=2.6, height=0.8, color=SPARK,
                              fill_color=PAGE, fill_opacity=1, stroke_width=2)
        queue_box.shift([3.5, -2.1, 0])
        q_mark = Text("? reconcile", font_size=19, color=SPARK, weight=BOLD)
        q_mark.move_to(queue_box)
        contra_tag = Text("contradictory", font_size=17, color=SPARK)
        contra_tag.next_to(contra_arr, RIGHT, buff=0.1).shift(DOWN * 0.2)

        self.play(FadeIn(hot_box), FadeIn(hot_lbl), run_time=0.7)
        self.play(GrowArrow(test_arr), Write(test_lbl), run_time=0.8)
        self.play(FadeIn(cold_box), FadeIn(cold_lbl), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(branch_dot), run_time=0.3)
        self.play(
            GrowArrow(consist_arr), FadeIn(consist_tag),
            run_time=0.7,
        )
        self.play(FadeIn(promote_box), FadeIn(promote_lbl), run_time=0.6)
        self.wait(0.3)
        self.play(
            GrowArrow(contra_arr), FadeIn(contra_tag),
            run_time=0.7,
        )
        self.play(FadeIn(queue_box), FadeIn(q_mark), run_time=0.6)
        self.wait(dur - 6.6)


# ─── ACT V ────────────────────────────────────────────────────────────────────

class B36_EvalGrid(Scene):
    def construct(self):
        dur = 15.36

        title = Text("Evaluation Conditions × Task Types", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        conditions = ["VANILLA", "RAG ONLY", "DREAMING+RAG"]
        tasks      = ["multi-session\ndebugging", "long-doc\nQ&A", "procedural\nlearning"]

        col_x = [-3.5, 0.0, 3.5]
        row_y = [0.5, -0.8, -2.1]
        cell_w = 3.0
        cell_h = 1.1

        # Column headers
        for cond, x in zip(conditions, col_x):
            color = SPARK if cond == "DREAMING+RAG" else SOFT
            weight = BOLD if cond == "DREAMING+RAG" else NORMAL
            t = Text(cond, font_size=19, color=color, weight=weight)
            t.move_to([x, 1.7, 0])
            self.add(t)

        # Row labels
        for task, y in zip(tasks, row_y):
            t = Text(task, font_size=16, color=SOFT)
            t.move_to([-6.0, y, 0])
            self.add(t)

        # Grid cells — appear one row at a time
        all_cells = []
        for j, y in enumerate(row_y):
            row_cells = VGroup()
            for i, x in enumerate(col_x):
                cell = Rectangle(width=cell_w, height=cell_h,
                                 color=BORDER, fill_color=PAGE,
                                 fill_opacity=1, stroke_width=1.2)
                cell.move_to([x, y, 0])
                row_cells.add(cell)
            all_cells.append(row_cells)

        # Terracotta column highlight line for DREAMING+RAG
        highlight = DashedLine(
            [3.5, 2.3, 0], [3.5, -2.7, 0],
            dash_length=0.25, dashed_ratio=0.55,
            color=SPARK, stroke_width=2,
        )

        self.wait(0.5)
        for i, row in enumerate(all_cells):
            self.play(Create(row), run_time=0.7)
            self.wait(0.25)
        self.wait(0.3)
        self.play(Create(highlight), run_time=0.6)
        self.wait(dur - 5.0)


class B38_DebugTimeline(Scene):
    def construct(self):
        dur = 13.97

        title = Text("Multi-Session Debugging: Already Primed", font_size=34, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Bug target
        bug_pos  = [4.2, -1.0, 0]
        bug_dot  = Dot(point=bug_pos, radius=0.22, color=INK)
        bug_ring = Circle(radius=0.38, color=INK, stroke_width=2)
        bug_ring.move_to(bug_pos)
        bug_lbl  = Text("bug", font_size=18, color=INK)
        bug_lbl.next_to(bug_ring, DOWN, buff=0.1)
        self.add(bug_dot, bug_ring, bug_lbl)

        session_starts = [
            ([-5.0, 1.8, 0], "session 1"),
            ([-5.0, 0.3, 0], "session 2"),
            ([-5.0, -1.0, 0], "session 3"),
        ]
        waypoints = [
            # session 1: winding path
            [[-5.0, 1.8, 0], [-2.0, 2.2, 0], [0.5, 1.4, 0], [2.5, 0.2, 0], [3.5, -0.5, 0], bug_pos],
            # session 2: shorter
            [[-5.0, 0.3, 0], [-1.8, 0.5, 0], [1.2, -0.2, 0], [3.0, -0.7, 0], bug_pos],
            # session 3: direct (terracotta)
            [[-5.0, -1.0, 0], bug_pos],
        ]
        colors_path = [GHOST, SOFT, SPARK]
        widths_path = [1.8, 2.0, 3.0]

        for (start, lbl_txt), wps, col, wid in zip(session_starts, waypoints, colors_path, widths_path):
            sess_lbl = Text(lbl_txt, font_size=18, color=SOFT)
            sess_lbl.move_to([start[0] - 0.5, start[1], 0]).shift(LEFT * 0.6)
            self.add(sess_lbl)

            for k in range(len(wps) - 1):
                seg = Arrow(wps[k], wps[k + 1], color=col,
                            stroke_width=wid, buff=0.08)
                self.play(GrowArrow(seg), run_time=0.35)

        # Terracotta label on session 3
        primed_lbl = Text("already primed", font_size=22, color=SPARK, weight=BOLD)
        primed_lbl.shift([-1.0, -1.7, 0])
        self.play(FadeIn(primed_lbl), run_time=0.6)
        self.wait(dur - (3 * 5 * 0.35 + 0.6 + 0.8))


class B39_SpeakerReportedGain(Scene):
    def construct(self):
        dur = 16.00

        title = Text("Speaker-Reported: +34–41% (Multi-Session Tasks)", font_size=31, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Baseline bar
        ground_y = -2.4
        bar_x    = 0.0
        bar_w    = 1.8
        base_h   = 1.5
        gain_lo  = 0.34
        gain_hi  = 0.41
        bar_h    = base_h * (1 + (gain_lo + gain_hi) / 2)  # ~2.625

        ground = Line([-5.5, ground_y, 0], [5.5, ground_y, 0],
                      color=BORDER, stroke_width=1.5)
        self.add(ground)

        # Baseline
        base_bar = Rectangle(width=bar_w, height=base_h, color=GHOST,
                             fill_color=GHOST, fill_opacity=0.5, stroke_width=0)
        base_bar.move_to([bar_x - 2.2, ground_y + base_h / 2, 0])
        base_lbl = Text("RAG\nonly", font_size=17, color=SOFT)
        base_lbl.move_to([bar_x - 2.2, ground_y - 0.55, 0])
        self.add(base_bar, base_lbl)

        # Dreaming bar (terracotta)
        dream_bar = Rectangle(width=bar_w, height=bar_h, color=SPARK,
                              fill_color=SPARK, fill_opacity=0.78, stroke_width=0)
        dream_bar.move_to([bar_x + 2.2, ground_y + bar_h / 2, 0])
        dream_bar_lbl = Text("DREAMING\n+RAG", font_size=17, color=SPARK, weight=BOLD)
        dream_bar_lbl.move_to([bar_x + 2.2, ground_y - 0.55, 0])

        # Gain bracket
        gain_bracket_top = ground_y + base_h
        gain_bracket_bot = ground_y + base_h
        gain_h     = bar_h - base_h
        bracket_x  = bar_x + 2.2 + bar_w / 2 + 0.3

        gain_line  = Line([bracket_x, ground_y + base_h, 0],
                          [bracket_x, ground_y + bar_h,  0],
                          color=INK, stroke_width=2)
        tick_bot   = Line([bracket_x - 0.15, ground_y + base_h, 0],
                          [bracket_x + 0.15, ground_y + base_h, 0],
                          color=INK, stroke_width=2)
        tick_top   = Line([bracket_x - 0.15, ground_y + bar_h, 0],
                          [bracket_x + 0.15, ground_y + bar_h, 0],
                          color=INK, stroke_width=2)
        gain_pct   = Text("+34–41%", font_size=22, color=INK, weight=BOLD)
        gain_pct.next_to(gain_line, RIGHT, buff=0.18)

        # Wide error bars (explicit — critical)
        err_half = 0.28
        err_top_y = ground_y + bar_h
        err_bar   = Line([bar_x + 2.2, err_top_y - err_half, 0],
                         [bar_x + 2.2, err_top_y + err_half, 0],
                         color=INK, stroke_width=3)
        err_tick_t = Line([bar_x + 2.2 - 0.22, err_top_y + err_half, 0],
                          [bar_x + 2.2 + 0.22, err_top_y + err_half, 0],
                          color=INK, stroke_width=3)
        err_tick_b = Line([bar_x + 2.2 - 0.22, err_top_y - err_half, 0],
                          [bar_x + 2.2 + 0.22, err_top_y - err_half, 0],
                          color=INK, stroke_width=3)

        # Chip 1 — Speaker-reported
        chip1_bg = RoundedRectangle(width=3.2, height=0.55, corner_radius=0.12,
                                    color=SPARK, fill_color=PAGE,
                                    fill_opacity=1, stroke_width=1.5)
        chip1_bg.shift([-0.5, ground_y - 1.4, 0])
        chip1_txt = Text("Speaker-reported", font_size=17, color=SPARK)
        chip1_txt.move_to(chip1_bg)

        # Chip 2 — Synthetic / preliminary
        chip2_bg = RoundedRectangle(width=4.0, height=0.55, corner_radius=0.12,
                                    color=SOFT, fill_color=PAGE,
                                    fill_opacity=1, stroke_width=1.2)
        chip2_bg.shift([2.7, ground_y - 1.4, 0])
        chip2_txt = Text("Synthetic benchmarks · preliminary", font_size=14, color=SOFT)
        chip2_txt.move_to(chip2_bg)

        self.play(Create(dream_bar), FadeIn(dream_bar_lbl), run_time=0.9)
        self.play(
            Create(gain_line), Create(tick_bot), Create(tick_top),
            FadeIn(gain_pct),
            Create(VGroup(err_bar, err_tick_t, err_tick_b)),
            run_time=0.9,
        )
        self.wait(0.3)
        self.play(FadeIn(chip1_bg), FadeIn(chip1_txt), run_time=0.6)
        self.wait(0.25)
        self.play(FadeIn(chip2_bg), FadeIn(chip2_txt), run_time=0.6)
        self.wait(dur - 4.55)


class B40_StaleWorkaround(Scene):
    def construct(self):
        dur = 14.14

        title = Text("Dreaming Failure: Stale Workaround", font_size=37, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Session 1 and 2 — workaround pattern
        sess_boxes = []
        for i, x in enumerate([-4.0, 0.2]):
            bg = Rectangle(width=3.2, height=1.1, color=BORDER,
                           fill_color=PAGE, fill_opacity=1, stroke_width=1.5)
            bg.shift([x, 1.5, 0])
            lbl = Text(f"session {i+1}: workaround", font_size=17, color=SOFT)
            lbl.move_to(bg)
            sess_boxes.append(VGroup(bg, lbl))

        # Terracotta extraction arrow
        extract_arr = Arrow([-1.9, 1.0, 0], [-1.9, -0.2, 0],
                            color=SPARK, stroke_width=2.5, buff=0)
        extract_lbl = Text("dream extracts pattern", font_size=17, color=SPARK)
        extract_lbl.next_to(extract_arr, RIGHT, buff=0.18)

        # Dream store — workaround stored
        stored_box = Rectangle(width=3.6, height=0.95, color=SPARK,
                               fill_color=PAGE, fill_opacity=1, stroke_width=2)
        stored_box.shift([-1.9, -0.82, 0])
        stored_lbl = Text("workaround pattern", font_size=18, color=INK)
        stored_lbl.move_to(stored_box)
        store_hdr = Text("dream store", font_size=15, color=SPARK)
        store_hdr.next_to(stored_box, UP, buff=0.08)

        # Bug-fixed indicator
        fixed_box = Rectangle(width=2.8, height=0.85, color=GHOST,
                              fill_color=PAGE, fill_opacity=1, stroke_width=1.5)
        fixed_box.shift([3.8, 1.5, 0])
        fixed_lbl = Text("bug FIXED ✓", font_size=18, color=SOFT)
        fixed_lbl.move_to(fixed_box)

        # X mark over stored workaround
        x_mark = Text("✗", font_size=62, color=INK, weight=BOLD)
        x_mark.move_to(stored_box)
        wrong_lbl = Text("wrong but persistent", font_size=19, color=INK, weight=BOLD)
        wrong_lbl.shift([-1.9, -1.95, 0])

        self.play(FadeIn(sess_boxes[0]), run_time=0.6)
        self.play(FadeIn(sess_boxes[1]), run_time=0.6)
        self.wait(0.3)
        self.play(GrowArrow(extract_arr), FadeIn(extract_lbl), run_time=0.8)
        self.play(FadeIn(stored_box), FadeIn(stored_lbl), FadeIn(store_hdr), run_time=0.7)
        self.wait(0.4)
        self.play(FadeIn(fixed_box), FadeIn(fixed_lbl), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(x_mark), FadeIn(wrong_lbl), run_time=0.7)
        self.wait(dur - 5.6)
