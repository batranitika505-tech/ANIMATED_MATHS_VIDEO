"""
Scene 1: Hook / Context
Duration: ~31 seconds (Matches Voice-over: 29.8s + 1.2s buffer)
"""
from manim import *

BG_COLOR = "#0B0F19"
GRID_COLOR = "#1E293B"
AXIS_COLOR = "#64748B"
TEXT_COLOR = "#F8FAFC"
MUTED_TEXT = "#94A3B8"
E1_COLOR = "#10B981"
E2_COLOR = "#F43F5E"
HIGHLIGHT_COLOR = "#38BDF8"

class Scene01Hook(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # 1. Opening Title Card with Student Info (00:00 - 00:08)
        title = Text("Linear Transformations", font_size=42, weight=BOLD, color=TEXT_COLOR)
        subtitle = Text("How Matrices Transform 2D Space", font_size=26, color=HIGHLIGHT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.25)
        
        course_tag = Text("Course: M3 — Linear Algebra and Calculus", font_size=20, color=MUTED_TEXT)
        student_info = Text("Student: NITIKA  |  ID: E25B070581", font_size=18, color=MUTED_TEXT)
        info_group = VGroup(course_tag, student_info).arrange(DOWN, buff=0.15)
        info_group.next_to(subtitle, DOWN, buff=0.6)

        title_box = VGroup(title, subtitle, info_group).move_to(ORIGIN)

        self.play(FadeIn(title_box, shift=UP * 0.3), run_time=2.0)
        self.wait(4.5)
        self.play(FadeOut(title_box, shift=UP * 0.5), run_time=1.5)

        # 2. Coordinate Grid & Basis Vectors (00:08 - 00:19)
        header = Text("Linear Transformations in 2D Space", font_size=26, color=TEXT_COLOR, weight=BOLD)
        header.to_corner(UL, buff=0.5)

        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            x_length=10,
            y_length=6,
            background_line_style={"stroke_color": GRID_COLOR, "stroke_width": 1.5, "stroke_opacity": 0.8},
            axis_config={"stroke_color": AXIS_COLOR, "stroke_width": 2.5, "include_numbers": False}
        )
        plane.shift(DOWN * 0.2)

        e1_arrow = Arrow(plane.c2p(0, 0), plane.c2p(1, 0), buff=0, color=E1_COLOR, stroke_width=4.5)
        e1_label = Text("e₁ = (1, 0)", font_size=20, color=E1_COLOR).next_to(e1_arrow.get_end(), DOWN, buff=0.15)

        e2_arrow = Arrow(plane.c2p(0, 0), plane.c2p(0, 1), buff=0, color=E2_COLOR, stroke_width=4.5)
        e2_label = Text("e₂ = (0, 1)", font_size=20, color=E2_COLOR).next_to(e2_arrow.get_end(), LEFT, buff=0.15)

        self.play(FadeIn(header), Create(plane), run_time=2.0)
        self.play(GrowArrow(e1_arrow), Write(e1_label), GrowArrow(e2_arrow), Write(e2_label), run_time=2.0)
        self.wait(3.0)

        # 3. Dynamic Grid Deformation Teaser (00:19 - 00:26)
        hook_text = Text("What if four numbers could reshape an entire infinite plane?", font_size=22, color=HIGHLIGHT_COLOR)
        hook_text.to_edge(UP, buff=0.55)

        matrix_teaser = [[1.5, 0.8], [0.5, 1.2]]
        
        self.play(
            FadeOut(header),
            FadeIn(hook_text),
            plane.animate.apply_matrix(matrix_teaser),
            e1_arrow.animate.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(1.5, 0.5)),
            e1_label.animate.next_to(plane.c2p(1.5, 0.5), DR, buff=0.15),
            e2_arrow.animate.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(0.8, 1.2)),
            e2_label.animate.next_to(plane.c2p(0.8, 1.2), UL, buff=0.15),
            run_time=4.5
        )
        self.wait(2.5)

        # 4. Central Question (00:26 - 00:31)
        question = Text("How does a matrix transform every vector in space?", font_size=24, color=TEXT_COLOR, weight=BOLD)
        question.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=1.5)
        self.wait(4.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)
