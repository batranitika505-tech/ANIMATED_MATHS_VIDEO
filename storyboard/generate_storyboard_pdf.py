"""
Storyboard PDF Generator for M3 Mathematics Animation Video Project
Uses ReportLab to generate a publication-quality 6-scene Storyboard PDF.
"""
import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748B"))
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 570, "M3 Mathematics Animation Video Project — Six-Scene Storyboard")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 564, 738, 564)
        
        # Footer
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(738, 30, page_text)
        self.drawString(54, 30, "Topic: Linear Transformations: How Matrices Transform Space | Course: M3")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 42, 738, 42)
        self.restoreState()

def build_pdf(filename=None):
    if filename is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(script_dir, "storyboard.pdf")
    os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)
    doc = SimpleDocTemplate(
        filename,
        pagesize=landscape(letter),
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#2563EB"),
        spaceAfter=12
    )
    
    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#334155")
    )
    
    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=10,
        spaceAfter=6
    )
    
    scene_title_style = ParagraphStyle(
        'SceneTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#1E3A8A")
    )
    
    cell_bold = ParagraphStyle(
        'CellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#0F172A")
    )
    
    cell_text = ParagraphStyle(
        'CellText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#334155")
    )
    
    math_text = ParagraphStyle(
        'MathText',
        parent=styles['Normal'],
        fontName='Courier-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#B45309")
    )
    
    story = []
    
    # Title & Metadata Banner
    story.append(Paragraph("M3 MATHEMATICS ANIMATION VIDEO PROJECT", subtitle_style))
    story.append(Paragraph("Official Six-Scene Production Storyboard", title_style))
    story.append(Paragraph("<b>Topic:</b> Linear Transformations: How Matrices Transform Space", ParagraphStyle('SubSub', parent=styles['Normal'], fontName='Helvetica', fontSize=11, leading=15, textColor=colors.HexColor("#475569"))))
    story.append(Spacer(1, 8))
    
    meta_table_data = [
        [
            Paragraph("<b>Course:</b> M3 — Linear Algebra and Calculus", meta_style),
            Paragraph("<b>Target Total Duration:</b> 295 s (~4 min 55 s)", meta_style),
            Paragraph("<b>Resolution:</b> 1920 × 1080 (1080p, 16:9)", meta_style)
        ],
        [
            Paragraph("<b>Student Name:</b> NITIKA", meta_style),
            Paragraph("<b>Student ID:</b> E25B070581", meta_style),
            Paragraph("<b>Format:</b> MP4 (H.264 / AAC Audio)", meta_style)
        ]
    ]
    meta_table = Table(meta_table_data, colWidths=[240, 240, 204])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#E2E8F0")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))
    
    # Scenes Table
    scenes = [
        {
            "id": "SCENE 1",
            "title": "Hook / Context & Curiosity",
            "duration": "35 sec\n(00:00 - 00:35)",
            "visual": "Dark navy canvas. Title card with student details. Cartesian plane with basis vectors e1 (emerald) and e2 (coral). Grid continuously stretches and shears. Hook text: 'What if four numbers could reshape an entire infinite plane?'",
            "narration": "Welcome to M3 Linear Algebra. What if a small table of just four numbers could tilt, stretch, and reshape an entire infinite coordinate plane? Linear transformations power graphics, robotics, and neural networks. Today we ask: How does a matrix transform space?",
            "equations": "A = [[a, b], [c, d]]\ne1 = (1, 0), e2 = (0, 1)\nCentral Question: T(v) = ?",
            "techniques": "FadeIn, Write, ApplyMatrix teaser, dynamic coordinate distortion."
        },
        {
            "id": "SCENE 2",
            "title": "Concept Introduction & Linearity",
            "duration": "50 sec\n(00:35 - 01:25)",
            "visual": "Formal mapping T: R2 -> R2. Additivity highlighted: vectors u and v add tip-to-tail, and T(u+v) matches T(u)+T(v). Homogeneity: scaling u by 2 doubles output. Origin lock: T(0) = 0. Translation shown shifting origin with a red non-linear rejection.",
            "narration": "A transformation T is linear if it satisfies two strict rules: additivity, T(u+v) = T(u)+T(v), and homogeneity, T(cu) = cT(u). Crucially, T(0) must equal 0. The origin remains anchored! Pure translations move the origin, making them affine, not linear.",
            "equations": "T: R² → R²\nT(u + v) = T(u) + T(v)\nT(cu) = cT(u)\nT(0) = 0 (Fixed Origin)",
            "techniques": "TransformMatchingTex, vector addition animation, origin pulse marker, translation rejection cross."
        },
        {
            "id": "SCENE 3",
            "title": "Visual Intuition & Basis Vectors",
            "duration": "55 sec\n(01:25 - 02:20)",
            "visual": "High-contrast 2D grid. Highlight basis vectors e1=(1,0) (green) and e2=(0,1) (red). Unit square filled with translucent cyan. Introduce matrix A=[[2,1],[1,2]]. Col 1=(2,1) lands e1; Col 2=(1,2) lands e2. Grid lines shear into parallelograms continuously.",
            "narration": "The secret of linear algebra: to know where every vector goes, track the standard basis vectors! In our matrix A, row one is 2, 1; row two is 1, 2. Col 1 tells us e1 lands at (2,1). Col 2 tells us e2 lands at (1,2). The unit square deforms smoothly into a parallelogram.",
            "equations": "A = [[2, 1], [1, 2]]\nT(e1) = (2, 1)\nT(e2) = (1, 2)\nUnit Square: (0,0)-(1,0)-(1,1)-(0,1)",
            "techniques": "ApplyMatrix, continuous plane interpolation, polygon coordinate morphing, column color linking."
        },
        {
            "id": "SCENE 4",
            "title": "Worked Mathematical Examples",
            "duration": "70 sec\n(02:20 - 03:30)",
            "visual": "Split-screen layout. Left: Coordinate plane. Right: Step-by-step matrix multiplication. Vector v=(1,1) -> row 1: 2(1)+1(1)=3; row 2: 1(1)+2(1)=3 -> (3,3). Vector w=(2,-1) -> (3,0). Geometric area: det(A)=(2)(2)-(1)(1)=3. Unit square area 1 -> Parallelogram area 3.",
            "narration": "Let's calculate algebraically. For v=(1,1), multiplying row 1 gives 2(1)+1(1)=3, row 2 gives 1(1)+2(1)=3, so T(v)=(3,3). For w=(2,-1), row 1 gives 3, row 2 gives 0: lands on the x-axis at (3,0). The determinant is 4-1=3, proving the parallelogram has three times the initial area!",
            "equations": "A(1,1)ᵀ = (3, 3)ᵀ\nA(2,-1)ᵀ = (3, 0)ᵀ\ndet(A) = ad - bc = 4 - 1 = 3\nArea = |det(A)| × 1 = 3",
            "techniques": "Row-vector multiplication highlight, vector trajectory motion, determinant bracket callout, area shading."
        },
        {
            "id": "SCENE 5",
            "title": "Interpretation: det(A)=1 & Rotations",
            "duration": "65 sec\n(03:43 - 04:47)",
            "visual": "Length vs area scaling. Key statement: 'det(A)=1 preserves area and orientation, but is NOT necessarily a rotation.' Visual example: A=[[2,0],[0,0.5]] (det=1) stretches horizontally 2x, compresses vertically 0.5x; area remains 1.0 unit². Rigid rotations preserve BOTH area and vector lengths. Summary of det > 0, det < 0, det = 0.",
            "narration": "A matrix alters lengths and directions. Length scaling is direction-dependent. Crucially, det(A)=1 preserves area and orientation, but is not necessarily a rotation! Matrix [[2,0],[0,0.5]] has det=1: stretches horizontal by 2, compresses vertical by 0.5. Area is preserved, but lengths change! Rigid rotations preserve BOTH area and all vector lengths.",
            "equations": "det(A) = 1: Area & Orientation preserved\nSqueeze: [[2,0],[0,0.5]], det=1\nRotation: R(θ) preserves area & lengths\ndet>0: Preserve | det<0: Reverse | det=0: Collapse",
            "techniques": "Unit square to 2x0.5 rectangle morph, comparison cards, callout highlight box."
        },
        {
            "id": "SCENE 6",
            "title": "Summary Takeaways & Credits",
            "duration": "35 sec\n(04:20 - 04:55)",
            "visual": "Clean three-takeaway summary card with animated checkmarks. Philosophical closing quote: 'One matrix. Infinite vectors. A transformed space.' Final academic credits card displaying student credentials, course, references, software credits, and AI disclosure.",
            "narration": "Remember three core takeaways: First, linear transformations preserve addition and scaling, anchoring the origin. Second, matrix columns encode the destination of basis vectors. Third, the determinant dictates area scaling and orientation. One matrix. Infinite vectors. A transformed space.",
            "equations": "1. Linearity: T(cu + dv) = cT(u) + dT(v)\n2. Columns = Transformed Basis\n3. Area Factor = |det(A)|",
            "techniques": "Sequential checkmark reveals, elegant typography fading, professional outro fade to black."
        }
    ]
    
    # Table headers
    headers = [
        Paragraph("<b>Scene & Time</b>", cell_bold),
        Paragraph("<b>Title & Visual Description</b>", cell_bold),
        Paragraph("<b>Narration Script</b>", cell_bold),
        Paragraph("<b>Key Equations</b>", cell_bold),
        Paragraph("<b>Animation Methods</b>", cell_bold)
    ]
    
    table_rows = [headers]
    for sc in scenes:
        col0 = Paragraph(f"<b>{sc['id']}</b><br/><font color='#64748B'>{sc['duration']}</font>", cell_bold)
        col1 = Paragraph(f"<b>{sc['title']}</b><br/><br/>{sc['visual']}", cell_text)
        col2 = Paragraph(sc['narration'], cell_text)
        col3 = Paragraph(sc['equations'].replace('\n', '<br/>'), math_text)
        col4 = Paragraph(sc['techniques'], cell_text)
        table_rows.append([col0, col1, col2, col3, col4])
    
    col_widths = [75, 175, 220, 114, 100]
    t = Table(table_rows, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1E293B")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t)
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated Storyboard PDF: {filename}")

if __name__ == "__main__":
    build_pdf()
