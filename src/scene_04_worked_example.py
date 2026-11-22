"""
Scene 4: Worked Mathematical Example
Duration: ~82.5 seconds (Matches Voice-over: 81.0s + 1.5s buffer)
"""
from manim import *

BG_COLOR = "#0B0F19"
GRID_COLOR = "#1E293B"
AXIS_COLOR = "#64748B"
TEXT_COLOR = "#F8FAFC"
MUTED_TEXT = "#94A3B8"
ACCENT = "#38BDF8"
GOLD = "#FBBF24"
PURPLE = "#A855F7"
CYAN = "#06B6D4"
GREEN = "#10B981"

class Scene04WorkedExample(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # Header
        header = Text("Step-by-Step Mathematical Calculations", font_size=26, weight=BOLD, color=TEXT_COLOR)
        header.to_corner(UL, buff=0.45)
        self.play(FadeIn(header), run_time=1.2)

        # Coordinate plane on left
        plane = NumberPlane(
            x_range=[-2, 5, 1],
            y_range=[-2, 5, 1],
            x_length=6.5,
            y_length=5.5,
            background_line_style={"stroke_color": GRID_COLOR, "stroke_width": 1.5, "stroke_opacity": 0.8},
            axis_config={"stroke_color": AXIS_COLOR, "stroke_width": 2.0, "include_numbers": False}
        )
        plane.shift(LEFT * 2.8 + DOWN * 0.3)
        self.play(Create(plane), run_time=1.8)

        # PART 1: Vector v = (1, 1) -> (3, 3) (00:03 - 00:28)
        v_arrow = Arrow(plane.c2p(0, 0), plane.c2p(1, 1), buff=0, color=GOLD, stroke_width=4.5)
        v_label = Text("v = (1, 1)", font_size=18, color=GOLD, weight=BOLD).next_to(plane.c2p(1, 1), UR, buff=0.1)

        self.play(GrowArrow(v_arrow), Write(v_label), run_time=1.5)

        # Algebraic panel on right
        calc_box1 = VGroup(
            Text("Example 1: v = [1, 1]ᵀ", font_size=20, color=GOLD, weight=BOLD),
            Text("T(v) = A · v = [ [2, 1], [1, 2] ] [1, 1]ᵀ", font_size=18, color=TEXT_COLOR),
            Text("Row 1:  2(1) + 1(1) = 2 + 1 = 3", font_size=18, color=ACCENT),
            Text("Row 2:  1(1) + 2(1) = 1 + 2 = 3", font_size=18, color=ACCENT),
            Text("∴  T(1, 1) = (3, 3)", font_size=22, color=GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        calc_box1.shift(RIGHT * 3.4 + UP * 0.8)

        card1 = SurroundingRectangle(calc_box1, color=GRID_COLOR, buff=0.2, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.85, corner_radius=0.1)

        self.play(FadeIn(card1), FadeIn(calc_box1), run_time=2.5)
        self.wait(7.0)

        # Animate v stretching to (3, 3)
        v_new_arrow = Arrow(plane.c2p(0, 0), plane.c2p(3, 3), buff=0, color=GOLD, stroke_width=4.5)
        v_new_label = Text("T(v) = (3, 3)", font_size=18, color=GOLD, weight=BOLD).next_to(plane.c2p(3, 3), UR, buff=0.1)

        self.play(
            Transform(v_arrow, v_new_arrow),
            Transform(v_label, v_new_label),
            run_time=3.5
        )
        self.wait(7.5)

        # PART 2: Vector w = (2, -1) -> (3, 0) (00:28 - 00:53)
        self.play(FadeOut(calc_box1), FadeOut(card1), run_time=1.0)

        w_arrow = Arrow(plane.c2p(0, 0), plane.c2p(2, -1), buff=0, color=PURPLE, stroke_width=4.5)
        w_label = Text("w = (2, -1)", font_size=18, color=PURPLE, weight=BOLD).next_to(plane.c2p(2, -1), DR, buff=0.1)

        self.play(GrowArrow(w_arrow), Write(w_label), run_time=1.5)

        calc_box2 = VGroup(
            Text("Example 2: w = [2, -1]ᵀ", font_size=20, color=PURPLE, weight=BOLD),
            Text("T(w) = A · w", font_size=18, color=TEXT_COLOR),
            Text("Row 1:  2(2) + 1(-1) = 4 - 1 = 3", font_size=18, color=ACCENT),
            Text("Row 2:  1(2) + 2(-1) = 2 - 2 = 0", font_size=18, color=ACCENT),
            Text("∴  T(2, -1) = (3, 0)", font_size=22, color=GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        calc_box2.shift(RIGHT * 3.4 + UP * 0.8)

        card2 = SurroundingRectangle(calc_box2, color=GRID_COLOR, buff=0.2, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.85, corner_radius=0.1)

        self.play(FadeIn(card2), FadeIn(calc_box2), run_time=2.5)
        self.wait(7.0)

        # Animate w moving to (3, 0)
        w_new_arrow = Arrow(plane.c2p(0, 0), plane.c2p(3, 0), buff=0, color=PURPLE, stroke_width=4.5)
        w_new_label = Text("T(w) = (3, 0)", font_size=18, color=PURPLE, weight=BOLD).next_to(plane.c2p(3, 0), UP, buff=0.1)

        self.play(
            Transform(w_arrow, w_new_arrow),
            Transform(w_label, w_new_label),
            run_time=3.5
        )
        self.wait(8.0)

        # PART 3: Determinant & Area Scaling (00:53 - 01:22)
        self.play(
            FadeOut(w_arrow), FadeOut(w_label),
            FadeOut(v_arrow), FadeOut(v_label),
            FadeOut(calc_box2), FadeOut(card2),
            run_time=1.5
        )

        p0 = plane.c2p(0, 0)
        p1 = plane.c2p(1, 0)
        p2 = plane.c2p(1, 1)
        p3 = plane.c2p(0, 1)
        orig_sq = Polygon(p0, p1, p2, p3, stroke_color=CYAN, stroke_width=2.5, fill_color=CYAN, fill_opacity=0.4)

        tp0 = plane.c2p(0, 0)
        tp1 = plane.c2p(2, 1)
        tp2 = plane.c2p(3, 3)
        tp3 = plane.c2p(1, 2)
        trans_poly = Polygon(tp0, tp1, tp2, tp3, stroke_color=CYAN, stroke_width=2.5, fill_color=CYAN, fill_opacity=0.4)

        det_box = VGroup(
            Text("Area Scaling & Determinant", font_size=20, color=GOLD, weight=BOLD),
            Text("det(A) = ad - bc", font_size=18, color=TEXT_COLOR),
            Text("det(A) = (2)(2) - (1)(1) = 4 - 1 = 3", font_size=18, color=ACCENT, weight=BOLD),
            Text("Original Area = 1.0 unit²", font_size=18, color=MUTED_TEXT),
            Text("Parallelogram Area = 3.0 units²", font_size=18, color=CYAN, weight=BOLD),
            Text("Area Scaling Factor = |det(A)| = 3", font_size=20, color=GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        det_box.shift(RIGHT * 3.3 + UP * 0.5)

        card3 = SurroundingRectangle(det_box, color=GRID_COLOR, buff=0.2, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.85, corner_radius=0.1)

        self.play(FadeIn(orig_sq), FadeIn(card3), FadeIn(det_box), run_time=2.5)
        self.wait(6.0)

        self.play(Transform(orig_sq, trans_poly), run_time=4.0)
        self.wait(14.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)
