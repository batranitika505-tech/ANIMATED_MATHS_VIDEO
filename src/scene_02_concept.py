"""
Scene 2: Concept Introduction & Linearity
Duration: ~53.5 seconds (Matches Voice-over: 52.0s + 1.5s buffer)
"""
from manim import *

BG_COLOR = "#0B0F19"
GRID_COLOR = "#1E293B"
AXIS_COLOR = "#64748B"
TEXT_COLOR = "#F8FAFC"
MUTED_TEXT = "#94A3B8"
ACCENT = "#38BDF8"
GOLD = "#F59E0B"
GREEN = "#10B981"
RED = "#EF4444"

class Scene02Concept(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # Header
        header = Text("Mathematical Definition: Linear Transformation", font_size=28, weight=BOLD, color=TEXT_COLOR)
        header.to_corner(UL, buff=0.5)
        self.play(FadeIn(header), run_time=1.2)

        # Mapping definition (00:01 - 00:10)
        mapping_text = Text("A mapping  T: ℝ² → ℝ²  is linear if it satisfies two conditions:", font_size=22, color=MUTED_TEXT)
        mapping_text.next_to(header, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(mapping_text), run_time=2.0)
        self.wait(3.5)

        # Axiom 1: Additivity (00:10 - 00:24)
        ax1_title = Text("1. Additivity (Preserves Vector Addition)", font_size=22, color=GOLD, weight=BOLD)
        ax1_formula = Text("T(u + v) = T(u) + T(v)", font_size=28, color=TEXT_COLOR, weight=BOLD)
        ax1_desc = Text("Transforming a sum equals the sum of the transformed vectors.", font_size=18, color=MUTED_TEXT)
        ax1_group = VGroup(ax1_title, ax1_formula, ax1_desc).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        ax1_group.shift(UP * 0.7 + LEFT * 2.5)

        box1 = SurroundingRectangle(ax1_group, color=GOLD, buff=0.25, stroke_width=1.5, corner_radius=0.1)
        self.play(FadeIn(ax1_group), Create(box1), run_time=2.5)
        self.wait(7.5)

        # Axiom 2: Homogeneity (00:24 - 00:36)
        ax2_title = Text("2. Homogeneity (Preserves Scalar Multiplication)", font_size=22, color=ACCENT, weight=BOLD)
        ax2_formula = Text("T(c · u) = c · T(u)", font_size=28, color=TEXT_COLOR, weight=BOLD)
        ax2_desc = Text("Scaling the input vector by scalar c scales the output by c.", font_size=18, color=MUTED_TEXT)
        ax2_group = VGroup(ax2_title, ax2_formula, ax2_desc).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        ax2_group.next_to(box1, DOWN, buff=0.35, aligned_edge=LEFT)

        box2 = SurroundingRectangle(ax2_group, color=ACCENT, buff=0.25, stroke_width=1.5, corner_radius=0.1)
        self.play(FadeIn(ax2_group), Create(box2), run_time=2.5)
        self.wait(7.5)

        # Fixed Origin Corollary (00:36 - 00:45)
        self.play(
            FadeOut(ax1_group), FadeOut(box1),
            FadeOut(ax2_group), FadeOut(box2),
            FadeOut(mapping_text),
            run_time=1.5
        )

        origin_title = Text("Crucial Consequence: The Origin Must Remain Fixed", font_size=24, color=GOLD, weight=BOLD)
        origin_title.next_to(header, DOWN, buff=0.4, aligned_edge=LEFT)

        proof_step1 = Text("Setting scalar c = 0 in homogeneity:", font_size=20, color=MUTED_TEXT)
        proof_step2 = Text("T(0) = T(0 · u) = 0 · T(u) = 0", font_size=26, color=GREEN, weight=BOLD)
        proof_box = VGroup(origin_title, proof_step1, proof_step2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        proof_box.shift(LEFT * 1.5 + UP * 1.0)

        self.play(FadeIn(proof_box), run_time=2.0)
        self.wait(5.0)

        # Translation comparison (00:45 - 00:53)
        trans_title = Text("Why is a translation NOT linear?", font_size=22, color=RED, weight=BOLD)
        trans_f = Text("f(v) = v + b  (where b ≠ 0)", font_size=22, color=TEXT_COLOR)
        trans_why1 = Text("• f(0) = 0 + b = b ≠ 0  (Origin is displaced!)", font_size=18, color=RED)
        trans_why2 = Text("• f(u + v) = u + v + b ≠ f(u) + f(v) = u + v + 2b", font_size=18, color=RED)
        trans_conc = Text("∴ Pure spatial translations are AFFINE, not linear.", font_size=19, color=GOLD, weight=BOLD)

        trans_group = VGroup(trans_title, trans_f, trans_why1, trans_why2, trans_conc).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        trans_group.next_to(proof_box, DOWN, buff=0.35, aligned_edge=LEFT)

        box_trans = SurroundingRectangle(trans_group, color=RED, buff=0.2, stroke_width=1.5, corner_radius=0.1)
        self.play(FadeIn(trans_group), Create(box_trans), run_time=2.5)
        self.wait(7.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)
