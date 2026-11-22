"""
Scene 5: Geometric Interpretation & Real Meaning
Duration: ~76.5 seconds (Matches Voice-over: 75.05s + 1.5s buffer)
Correctly distinguishes det(A)=1 (area-preserving) from rigid rotations (isometries).
Features visual demonstration of A = [[2, 0], [0, 0.5]] (det = 1, horizontal stretch & vertical compression).
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
PURPLE = "#A855F7"
CYAN = "#06B6D4"

class Scene05Interpretation(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # Header
        header = Text("Geometric Interpretation: Length, Area & Orientation", font_size=26, weight=BOLD, color=TEXT_COLOR)
        header.to_corner(UL, buff=0.45)
        self.play(FadeIn(header), run_time=1.2)

        # ---------------------------------------------------------
        # PART 1: Length Scaling vs Area Scaling (00:00 - 00:20)
        # ---------------------------------------------------------
        dist_title = Text("1. Length Scaling is Direction-Dependent (Anisotropic)", font_size=20, color=GOLD, weight=BOLD)
        dist_p1 = Text("• Along v = (1, 1):   Initial length = √2 ≈ 1.41  →  Final length = 3√2 ≈ 4.24  (Scaled by 3.0×)", font_size=17, color=TEXT_COLOR)
        dist_p2 = Text("• Along u = (1, -1):  Initial length = √2 ≈ 1.41  →  Final length = √2 ≈ 1.41   (Scaled by 1.0× — Unchanged!)", font_size=17, color=TEXT_COLOR)
        dist_p3 = Text("• Basis vector e₁:    Initial length = 1.00       →  Final length = √5 ≈ 2.24   (Scaled by ~2.24×)", font_size=17, color=MUTED_TEXT)
        dist_conc = Text("∴ Different vectors stretch by different amounts. There is no single 'length scaling factor'!", font_size=18, color=ACCENT, weight=BOLD)

        part1_group = VGroup(dist_title, dist_p1, dist_p2, dist_p3, dist_conc).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        part1_group.shift(UP * 0.8 + LEFT * 0.5)
        box1 = SurroundingRectangle(part1_group, color=GRID_COLOR, buff=0.25, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.85, corner_radius=0.1)

        self.play(FadeIn(box1), FadeIn(part1_group), run_time=2.0)
        self.wait(15.0)
        self.play(FadeOut(box1), FadeOut(part1_group), run_time=1.0)

        # ---------------------------------------------------------
        # PART 2: det(A) = 1 & Squeeze Mapping vs Rigid Rotation (00:20 - 00:54)
        # ---------------------------------------------------------
        part2_title = Text("2. Area-Preserving Transformations: det(A) = 1", font_size=20, color=GOLD, weight=BOLD)
        part2_title.next_to(header, DOWN, buff=0.3, aligned_edge=LEFT)

        key_statement = Text(
            "det(A) = 1 means area and orientation are preserved, but the transformation is not necessarily a rigid rotation.",
            font_size=16, color=TEXT_COLOR, weight=BOLD
        )
        key_statement.next_to(part2_title, DOWN, buff=0.18, aligned_edge=LEFT)

        # Coordinate plane on left showing squeeze mapping A = [[2, 0], [0, 0.5]]
        plane2 = NumberPlane(
            x_range=[-1, 4, 1],
            y_range=[-1, 3, 1],
            x_length=5.0,
            y_length=3.5,
            background_line_style={"stroke_color": GRID_COLOR, "stroke_width": 1.2, "stroke_opacity": 0.8},
            axis_config={"stroke_color": AXIS_COLOR, "stroke_width": 1.8, "include_numbers": False}
        )
        plane2.shift(LEFT * 3.6 + DOWN * 1.0)

        # Original Unit Square: (0,0)-(1,0)-(1,1)-(0,1), area = 1
        sq_p0 = plane2.c2p(0, 0)
        sq_p1 = plane2.c2p(1, 0)
        sq_p2 = plane2.c2p(1, 1)
        sq_p3 = plane2.c2p(0, 1)
        unit_sq2 = Polygon(sq_p0, sq_p1, sq_p2, sq_p3, stroke_color=CYAN, stroke_width=2.5, fill_color=CYAN, fill_opacity=0.45)
        sq_label = Text("Area = 1.0", font_size=14, color=CYAN, weight=BOLD).next_to(sq_p2, UR, buff=0.08)

        # Squeezed Rectangle: (0,0)-(2,0)-(2,0.5)-(0,0.5), area = 2 * 0.5 = 1.0
        sqz_p0 = plane2.c2p(0, 0)
        sqz_p1 = plane2.c2p(2, 0)
        sqz_p2 = plane2.c2p(2, 0.5)
        sqz_p3 = plane2.c2p(0, 0.5)
        squeezed_rect = Polygon(sqz_p0, sqz_p1, sqz_p2, sqz_p3, stroke_color=GOLD, stroke_width=2.5, fill_color=GOLD, fill_opacity=0.45)
        sqz_label = Text("Area = 2 × 0.5 = 1.0", font_size=14, color=GOLD, weight=BOLD).next_to(sqz_p1, UR, buff=0.1)

        # Right explanatory panel for Squeeze mapping & Rigid Rotation
        calc_squeeze = VGroup(
            Text("Example: Squeeze Mapping (Not a Rotation)", font_size=18, color=ACCENT, weight=BOLD),
            Text("A = [ [2, 0], [0, 0.5] ]", font_size=18, color=TEXT_COLOR, weight=BOLD),
            Text("• det(A) = (2)(0.5) - (0)(0) = 1.00  (Area Preserved!)", font_size=16, color=GREEN, weight=BOLD),
            Text("• Horizontal stretch:  (1, 0) → (2, 0)  [2.0× longer]", font_size=15, color=GOLD),
            Text("• Vertical compression: (0, 1) → (0, 0.5) [0.5× shorter]", font_size=15, color=GOLD),
            Text("• Vector lengths change ∴ NOT an isometry / rotation!", font_size=15, color=RED, weight=BOLD),
            Text("Rigid Rotations: Preserve BOTH area AND all vector lengths.", font_size=16, color=CYAN, weight=BOLD)
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        calc_squeeze.shift(RIGHT * 2.5 + DOWN * 1.0)

        box_sqz = SurroundingRectangle(calc_squeeze, color=GRID_COLOR, buff=0.2, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.9, corner_radius=0.1)

        self.play(FadeIn(part2_title), FadeIn(key_statement), run_time=1.5)
        self.play(Create(plane2), FadeIn(unit_sq2), FadeIn(sq_label), FadeIn(box_sqz), FadeIn(calc_squeeze), run_time=2.5)
        self.wait(6.0)

        # Transform unit square into stretched/compressed rectangle
        self.play(
            Transform(unit_sq2, squeezed_rect),
            Transform(sq_label, sqz_label),
            run_time=3.5
        )
        self.wait(18.0)

        self.play(
            FadeOut(plane2), FadeOut(unit_sq2), FadeOut(sq_label),
            FadeOut(part2_title), FadeOut(key_statement),
            FadeOut(box_sqz), FadeOut(calc_squeeze),
            run_time=1.2
        )

        # ---------------------------------------------------------
        # PART 3: Summary of Determinant Sign Cases (00:54 - 01:16)
        # ---------------------------------------------------------
        det_summary_title = Text("3. Summary of Determinant Cases", font_size=20, color=ACCENT, weight=BOLD)
        det_summary_title.next_to(header, DOWN, buff=0.35, aligned_edge=LEFT)

        case_pos = VGroup(
            Text("det(A) > 0  (Orientation Preserved)", font_size=16, color=GREEN, weight=BOLD),
            Text("Area scales by |det|. Loops remain counter-clockwise.", font_size=14, color=MUTED_TEXT),
            Text("Our Main Matrix: det(A) = +3  (Triples area, preserves orientation)", font_size=14, color=GOLD, weight=BOLD)
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        b_pos = SurroundingRectangle(case_pos, color=GREEN, buff=0.15, stroke_width=1.2, fill_color="#0F172A", fill_opacity=0.8, corner_radius=0.08)
        c_pos = VGroup(b_pos, case_pos)

        case_neg = VGroup(
            Text("det(A) < 0  (Orientation Reversed)", font_size=16, color=RED, weight=BOLD),
            Text("Area scales by |det|. Space is flipped like a mirror reflection.", font_size=14, color=MUTED_TEXT),
            Text("Example: Reflection matrix [ [1, 0], [0, -1] ]  (det = -1)", font_size=14, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        b_neg = SurroundingRectangle(case_neg, color=RED, buff=0.15, stroke_width=1.2, fill_color="#0F172A", fill_opacity=0.8, corner_radius=0.08)
        c_neg = VGroup(b_neg, case_neg)

        case_zero = VGroup(
            Text("det(A) = 0  (Singular Matrix / Dimensional Collapse)", font_size=16, color=PURPLE, weight=BOLD),
            Text("Columns are linearly dependent. 2D space squashes into a 1D line or point.", font_size=14, color=MUTED_TEXT),
            Text("Area collapses to 0. Non-invertible transformation.", font_size=14, color=RED, weight=BOLD)
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        b_zero = SurroundingRectangle(case_zero, color=PURPLE, buff=0.15, stroke_width=1.2, fill_color="#0F172A", fill_opacity=0.8, corner_radius=0.08)
        c_zero = VGroup(b_zero, case_zero)

        summary_cards = VGroup(c_pos, c_neg, c_zero).arrange(DOWN, buff=0.25)
        summary_cards.shift(DOWN * 0.2)

        self.play(FadeIn(det_summary_title), FadeIn(summary_cards), run_time=2.0)
        self.wait(17.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)
