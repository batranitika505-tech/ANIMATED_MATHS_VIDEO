"""
Scene 6: Summary Takeaways, Credits & Closing Frame
Duration: ~32.3 seconds (Matches Voice-over: 30.8s + 1.5s buffer)
"""
from manim import *

BG_COLOR = "#0B0F19"
GRID_COLOR = "#1E293B"
TEXT_COLOR = "#F8FAFC"
MUTED_TEXT = "#94A3B8"
ACCENT = "#38BDF8"
GOLD = "#F59E0B"
GREEN = "#10B981"

class Scene06Summary(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # Part 1: Three Things to Remember (00:00 - 00:18)
        title = Text("Three Things to Remember", font_size=32, weight=BOLD, color=GOLD)
        title.to_edge(UP, buff=0.7)

        t1 = VGroup(
            Text("1. Linearity & Fixed Origin:", font_size=20, color=ACCENT, weight=BOLD),
            Text("Preserves vector addition and scalar multiplication: T(cu + dv) = cT(u) + dT(v).  T(0) = 0.", font_size=17, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)

        t2 = VGroup(
            Text("2. Basis Vectors Determine Space:", font_size=20, color=GREEN, weight=BOLD),
            Text("The columns of matrix A are precisely where standard basis vectors e₁ and e₂ land.", font_size=17, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)

        t3 = VGroup(
            Text("3. Determinant Dictates Area & Orientation:", font_size=20, color=GOLD, weight=BOLD),
            Text("The absolute determinant |det(A)| scales areas; its sign dictates if space is preserved or flipped.", font_size=17, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)

        takeaways = VGroup(t1, t2, t3).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        takeaways.next_to(title, DOWN, buff=0.5)

        card = SurroundingRectangle(takeaways, color=GRID_COLOR, buff=0.25, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.85, corner_radius=0.1)

        self.play(FadeIn(title), FadeIn(card), FadeIn(takeaways), run_time=2.0)
        self.wait(12.0)

        # Philosophical Quote & Outro (00:18 - 00:23)
        quote = Text("“One matrix.  Infinite vectors.  A transformed space.”", font_size=24, color=ACCENT, weight=BOLD)
        quote.next_to(card, DOWN, buff=0.45)
        self.play(Write(quote), run_time=2.0)
        self.wait(4.0)

        # Transition to Final Submission Credits Card (00:23 - 00:32)
        self.play(FadeOut(title), FadeOut(card), FadeOut(takeaways), FadeOut(quote), run_time=1.2)

        cred_title = Text("M3 Mathematics Animation Video Project", font_size=26, weight=BOLD, color=TEXT_COLOR)
        cred_topic = Text("Linear Transformations: How Matrices Transform Space", font_size=19, color=ACCENT)
        cred_stud = Text("Student Name: NITIKA   |   Student ID: E25B070581", font_size=16, color=GOLD, weight=BOLD)

        ref_head = Text("References:", font_size=16, color=MUTED_TEXT, weight=BOLD)
        refs = Text("• Gilbert Strang, Introduction to Linear Algebra (5th Ed.)\n• Grant Sanderson, 3Blue1Brown: Essence of Linear Algebra\n• David C. Lay, Linear Algebra and Its Applications", font_size=14, color=MUTED_TEXT)

        soft_head = Text("Software & AI Disclosure:", font_size=16, color=MUTED_TEXT, weight=BOLD)
        soft_info = Text("• Manim Community Edition  • FFmpeg  • Python  • ReportLab\n• AI Disclosure: Antigravity AI (Gemini 3.8 Flash) for script assistance and animation structuring\n• Narration: macOS High-Fidelity Voice Synthesis  |  Music: Ambient CC0", font_size=13, color=MUTED_TEXT)

        cred_box = VGroup(
            cred_title, cred_topic, cred_stud,
            VGroup(ref_head, refs).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            VGroup(soft_head, soft_info).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        ).arrange(DOWN, buff=0.22).move_to(ORIGIN)

        cred_border = SurroundingRectangle(cred_box, color=GRID_COLOR, buff=0.3, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.9, corner_radius=0.1)

        self.play(FadeIn(cred_border), FadeIn(cred_box), run_time=1.5)
        self.wait(7.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)
