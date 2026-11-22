"""
Scene 3: Visual Intuition & Basis Vectors
Duration: ~55.7 seconds (Matches Voice-over: 54.2s + 1.5s buffer)
"""
from manim import *

BG_COLOR = "#0B0F19"
GRID_COLOR = "#1E293B"
AXIS_COLOR = "#64748B"
TEXT_COLOR = "#F8FAFC"
MUTED_TEXT = "#94A3B8"
E1_COLOR = "#10B981"
E2_COLOR = "#F43F5E"
SQUARE_COLOR = "#06B6D4"
GOLD = "#F59E0B"
ACCENT = "#38BDF8"

class Scene03VisualIntuition(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # Header
        header = Text("Basis Vectors: The Key to Space Transformation", font_size=26, weight=BOLD, color=TEXT_COLOR)
        header.to_corner(UL, buff=0.45)
        self.play(FadeIn(header), run_time=1.2)

        # Coordinate Plane (Left side)
        plane = NumberPlane(
            x_range=[-3, 5, 1],
            y_range=[-2, 5, 1],
            x_length=7.5,
            y_length=5.5,
            background_line_style={"stroke_color": GRID_COLOR, "stroke_width": 1.5, "stroke_opacity": 0.8},
            axis_config={"stroke_color": AXIS_COLOR, "stroke_width": 2.0, "include_numbers": False}
        )
        plane.shift(LEFT * 2.2 + DOWN * 0.3)

        # Unit Square
        p0 = plane.c2p(0, 0)
        p1 = plane.c2p(1, 0)
        p2 = plane.c2p(1, 1)
        p3 = plane.c2p(0, 1)
        unit_square = Polygon(p0, p1, p2, p3, stroke_color=SQUARE_COLOR, stroke_width=2.5, fill_color=SQUARE_COLOR, fill_opacity=0.35)

        # Basis vectors
        e1_arrow = Arrow(plane.c2p(0, 0), plane.c2p(1, 0), buff=0, color=E1_COLOR, stroke_width=4.5)
        e1_label = Text("e₁ = (1, 0)", font_size=18, color=E1_COLOR, weight=BOLD).next_to(e1_arrow.get_end(), DOWN, buff=0.12)

        e2_arrow = Arrow(plane.c2p(0, 0), plane.c2p(0, 1), buff=0, color=E2_COLOR, stroke_width=4.5)
        e2_label = Text("e₂ = (0, 1)", font_size=18, color=E2_COLOR, weight=BOLD).next_to(e2_arrow.get_end(), LEFT, buff=0.12)

        self.play(Create(plane), run_time=2.0)
        self.play(FadeIn(unit_square), GrowArrow(e1_arrow), Write(e1_label), GrowArrow(e2_arrow), Write(e2_label), run_time=2.0)
        self.wait(6.0)

        # Right Panel: Matrix & Column Meaning
        panel_title = Text("Transformation Matrix A", font_size=20, color=ACCENT, weight=BOLD)
        
        matrix_disp = VGroup(
            Text("[", font_size=48, color=TEXT_COLOR),
            VGroup(
                Text("2    1", font_size=26, color=TEXT_COLOR),
                Text("1    2", font_size=26, color=TEXT_COLOR)
            ).arrange(DOWN, buff=0.25),
            Text("]", font_size=48, color=TEXT_COLOR)
        ).arrange(RIGHT, buff=0.1)

        col1_desc = Text("Col 1:  T(e₁) = (2, 1)", font_size=18, color=E1_COLOR, weight=BOLD)
        col2_desc = Text("Col 2:  T(e₂) = (1, 2)", font_size=18, color=E2_COLOR, weight=BOLD)
        
        panel = VGroup(panel_title, matrix_disp, col1_desc, col2_desc).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        panel.shift(RIGHT * 3.8 + UP * 0.5)

        box_panel = SurroundingRectangle(panel, color=GRID_COLOR, buff=0.25, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.8, corner_radius=0.1)

        self.play(FadeIn(box_panel), FadeIn(panel), run_time=2.0)
        self.wait(5.0)

        # Highlight Column 1 then Column 2
        box_col1 = SurroundingRectangle(col1_desc, color=E1_COLOR, buff=0.1)
        self.play(Create(box_col1), run_time=1.0)
        self.wait(4.0)
        self.play(FadeOut(box_col1), run_time=0.5)

        box_col2 = SurroundingRectangle(col2_desc, color=E2_COLOR, buff=0.1)
        self.play(Create(box_col2), run_time=1.0)
        self.wait(4.0)
        self.play(FadeOut(box_col2), run_time=0.5)

        # Continuous Grid Transformation Animation
        transform_note = Text("Continuous Grid Deformation...", font_size=18, color=GOLD, weight=BOLD)
        transform_note.next_to(panel, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(FadeIn(transform_note), run_time=1.0)

        target_A = [[2, 1], [1, 2]]
        tp0 = plane.c2p(0, 0)
        tp1 = plane.c2p(2, 1)
        tp2 = plane.c2p(3, 3)
        tp3 = plane.c2p(1, 2)
        trans_parallelogram = Polygon(tp0, tp1, tp2, tp3, stroke_color=SQUARE_COLOR, stroke_width=2.5, fill_color=SQUARE_COLOR, fill_opacity=0.35)

        e1_new_label = Text("T(e₁) = (2, 1)", font_size=18, color=E1_COLOR, weight=BOLD).next_to(tp1, DR, buff=0.12)
        e2_new_label = Text("T(e₂) = (1, 2)", font_size=18, color=E2_COLOR, weight=BOLD).next_to(tp3, UL, buff=0.12)

        self.play(
            plane.animate.apply_matrix(target_A),
            Transform(unit_square, trans_parallelogram),
            e1_arrow.animate.put_start_and_end_on(tp0, tp1),
            Transform(e1_label, e1_new_label),
            e2_arrow.animate.put_start_and_end_on(tp0, tp3),
            Transform(e2_label, e2_new_label),
            run_time=6.0
        )
        self.wait(4.0)

        result_tag = Text("Unit Square  →  Parallelogram", font_size=18, color=SQUARE_COLOR, weight=BOLD)
        result_tag.next_to(transform_note, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(FadeIn(result_tag), run_time=1.0)
        self.wait(8.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)
