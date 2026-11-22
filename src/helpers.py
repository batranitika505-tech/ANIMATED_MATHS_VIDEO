"""
Helper functions and custom Mobjects for M3 Linear Transformations Animation
"""
from manim import *
from .config import *

def create_styled_plane(x_range=[-4, 4, 1], y_range=[-3, 3, 1], x_length=8, y_length=6):
    """Creates a high-contrast, modern coordinate plane."""
    plane = NumberPlane(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        background_line_style={
            "stroke_color": GRID_COLOR,
            "stroke_width": 1.5,
            "stroke_opacity": 0.7
        },
        axis_config={
            "stroke_color": AXIS_COLOR,
            "stroke_width": 2.5,
            "include_numbers": False,
        }
    )
    return plane

def get_styled_vector(plane, coords, color, label_text=None, label_dir=UP):
    """Constructs a beautifully styled arrow vector with optional label."""
    vec = Arrow(
        plane.c2p(0, 0),
        plane.c2p(coords[0], coords[1]),
        buff=0,
        color=color,
        stroke_width=4.5,
        max_tip_length_to_length_ratio=0.25
    )
    if label_text:
        label = Text(label_text, color=color, font_size=20)
        label.next_to(vec.get_end(), label_dir, buff=0.15)
        return VGroup(vec, label)
    return vec

def get_unit_square(plane, color=SQUARE_COLOR, fill_opacity=0.35):
    """Returns the unit square with vertices (0,0), (1,0), (1,1), (0,1)."""
    p0 = plane.c2p(0, 0)
    p1 = plane.c2p(1, 0)
    p2 = plane.c2p(1, 1)
    p3 = plane.c2p(0, 1)
    square = Polygon(
        p0, p1, p2, p3,
        stroke_color=color,
        stroke_width=3,
        fill_color=color,
        fill_opacity=fill_opacity
    )
    return square

def get_header(title_text, subtitle_text=None):
    """Returns a standardized professional scene header."""
    title = Text(title_text, font_size=32, color=TEXT_COLOR, weight=BOLD)
    group = VGroup(title)
    if subtitle_text:
        sub = Text(subtitle_text, font_size=20, color=MUTED_TEXT)
        sub.next_to(title, DOWN, buff=0.15)
        group.add(sub)
    group.to_corner(UL, buff=0.5)
    return group
