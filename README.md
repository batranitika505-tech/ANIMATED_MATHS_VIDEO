# M3 Mathematics Animation Video Project
## Linear Transformations: How Matrices Transform 2D Space

![Resolution](https://img.shields.io/badge/Resolution-1920x1080%20(1080p)-blue)
![Aspect Ratio](https://img.shields.io/badge/Aspect%20Ratio-16:9-green)
![Duration](https://img.shields.io/badge/Duration-~5.1%20Minutes-orange)
![Framework](https://img.shields.io/badge/Framework-Manim%20Community%20v0.22+-purple)
![Subject](https://img.shields.io/badge/Subject-M3%20Linear%20Algebra%20%26%20Calculus-red)

---

## 1. Project Overview

This repository contains the complete source code, video production pipeline, professional storyboard, numerical verification, and academic documentation for the **M3 Mathematics Animation Video Project**:

**"Linear Transformations: How Matrices Transform Space"**

The project provides an intuitive, mathematically rigorous 5-minute educational documentary designed to teach second-year engineering students how $2 \times 2$ matrices deform two-dimensional Cartesian space, the fundamental geometric role of standard basis vectors, the row-by-row mechanics of matrix multiplication, and the physical meaning of the determinant as an area scaling factor and orientation detector.

### Student Credentials:
- **Course:** M3 — Linear Algebra and Calculus
- **Student Name:** `NITIKA`
- **Student ID:** `E25B070581`
- **Video Deliverable:** `output/Linear_Transformations_Final.mp4`
- **Storyboard Document:** `storyboard/storyboard.pdf`

---

## 2. Learning Objectives

By the conclusion of this animation, a student will be able to:
1. State the axiomatic definition of a linear transformation ($T(\mathbf{u}+\mathbf{v})=T(\mathbf{u})+T(\mathbf{v})$ and $T(c\mathbf{u})=cT(\mathbf{u})$).
2. Explain why the zero vector remains fixed ($T(\mathbf{0})=\mathbf{0}$) and why spatial translations are affine, not linear.
3. Track the standard basis vectors $\mathbf{e}_1 = (1, 0)^T$ and $\mathbf{e}_2 = (0, 1)^T$ and identify them directly as the columns of the transformation matrix.
4. Perform manual matrix-vector multiplication step-by-step for general vectors in $\mathbb{R}^2$.
5. Relate the determinant $\det(A) = ad - bc$ directly to the signed area scaling of any 2D region.
6. Distinguish between uniform area scaling and direction-dependent (anisotropic) length scaling.

---

## 3. Mathematical Foundations

### 3.1 Axiomatic Definition
A transformation $T: \mathbb{R}^2 \to \mathbb{R}^2$ is linear if and only if for all $\mathbf{u}, \mathbf{v} \in \mathbb{R}^2$ and all scalars $c \in \mathbb{R}$:
$$\text{Additivity: } T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$$
$$\text{Homogeneity: } T(c\mathbf{u}) = cT(\mathbf{u})$$

Setting $c = 0$ yields the fixed-origin theorem:
$$T(\mathbf{0}) = T(0 \cdot \mathbf{u}) = 0 \cdot T(\mathbf{u}) = \mathbf{0}$$

### 3.2 The Transformation Matrix
Every linear transformation $T: \mathbb{R}^2 \to \mathbb{R}^2$ is uniquely determined by its action on the basis vectors $\mathbf{e}_1$ and $\mathbf{e}_2$:
$$A = \begin{pmatrix} | & | \\ T(\mathbf{e}_1) & T(\mathbf{e}_2) \\ | & | \end{pmatrix}$$

For any general vector $\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}$:
$$T(\mathbf{v}) = A\mathbf{v} = x T(\mathbf{e}_1) + y T(\mathbf{e}_2)$$

---

## 4. Main Worked Demonstration

Throughout the animation, the following matrix is analyzed:
$$A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$

### 4.1 Standard Basis Transformation:
- **Basis Vector 1:** $\mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \implies T(\mathbf{e}_1) = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$
- **Basis Vector 2:** $\mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \implies T(\mathbf{e}_2) = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$

### 4.2 General Vector Transformations:
1. **Vector $\mathbf{v} = (1, 1)^T$:**
   $$A\mathbf{v} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2(1) + 1(1) \\ 1(1) + 2(1) \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix}$$
2. **Vector $\mathbf{w} = (2, -1)^T$:**
   $$A\mathbf{w} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 2(2) + 1(-1) \\ 1(2) + 2(-1) \end{pmatrix} = \begin{pmatrix} 4 - 1 \\ 2 - 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \end{pmatrix}$$

### 4.3 Geometric Transformation of the Unit Square:
- Original vertices: $(0,0), (1,0), (1,1), (0,1)$
- Transformed vertices: $(0,0), (2,1), (3,3), (1,2)$ (Parallelogram)
- Determinant:
  $$\det(A) = ad - bc = (2)(2) - (1)(1) = 4 - 1 = 3$$
- **Area Scaling:** $\text{Area}_{\text{final}} = |\det(A)| \times \text{Area}_{\text{initial}} = 3 \times 1 = 3\text{ units}^2$.
### 4.4 Area-Preserving Transformations vs. Rigid Rotations ($\det(A) = 1$):
- **Key Principle:** A determinant of $1$ means area and orientation are preserved, but the transformation is **not necessarily a rigid rotation**.
- **Counterexample (Squeeze Mapping):**
  $$A_{\text{squeeze}} = \begin{pmatrix} 2 & 0 \\ 0 & 0.5 \end{pmatrix}, \quad \det(A_{\text{squeeze}}) = (2)(0.5) - 0 = 1.0$$
  - Unit square of area $1.0$ morphs into a $2.0 \times 0.5$ rectangle of area $1.0\text{ unit}^2$ (Area strictly preserved!).
  - Vector lengths change ($2\times$ horizontal stretch, $0.5\times$ vertical compression), proving it is non-isometric.
- **Rigid Rotations:** In contrast, true rotations $R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ preserve **both** area and all vector lengths ($\|R\mathbf{v}\| = \|\mathbf{v}\|$).

---

## 5. Repository Structure

```
Linear_Transformations_M3/
│
├── README.md                           # Main repository documentation & guide
├── requirements.txt                    # Python dependencies
├── .gitignore                          # Clean repository ignore rules
│
├── storyboard/
│   ├── storyboard.pdf                  # Official publication-ready 6-scene Storyboard PDF
│   ├── storyboard.md                   # Detailed storyboard markdown specification
│   └── generate_storyboard_pdf.py      # Automated ReportLab PDF generator script
│
├── src/
│   ├── main.py                         # Master render & muxing pipeline orchestrator
│   ├── scene_01_hook.py                # Scene 1: Hook, curiosity, title card, teaser
│   ├── scene_02_concept.py             # Scene 2: Formal linearity axioms & fixed origin
│   ├── scene_03_visual_intuition.py    # Scene 3: Basis vectors & continuous grid shear
│   ├── scene_04_worked_example.py      # Scene 4: Step-by-step arithmetic & area scaling
│   ├── scene_05_interpretation.py      # Scene 5: Length vs area scaling & determinant cases
│   ├── scene_06_summary.py             # Scene 6: Three takeaways, quote & academic credits
│   ├── helpers.py                      # Reusable vector graphic utilities
│   ├── config.py                       # Global colors, resolution, and metadata constants
│   └── verify_math.py                  # Independent NumPy mathematical verification script
│
├── audio/
│   ├── narration_script.md             # Complete timestamped narration script
│   ├── generate_audio.py               # Voice synthesis & ambient audio generator
│   ├── scene_timings.json              # Exact sub-second scene timings
│   └── generated_audio/                # Synthesized audio files (.wav)
│
├── assets/
│   └── credits.md                      # Comprehensive academic citations & asset licenses
│
├── output/
│   └── Linear_Transformations_Final.mp4# Final 1080p master video deliverable
│
└── documentation/
    ├── mathematical_verification.md    # Rigorous mathematical verification report
    ├── viva_questions_and_answers.md   # 20 model viva voce questions and answers
    └── AI_disclosure.md                # Academic integrity & transparent AI disclosure
```

---

## 6. Installation & Environment Setup

### System Prerequisites:
- **macOS / Linux / Windows**
- **Python 3.12+**
- **FFmpeg 6.0+**
- **Homebrew packages (macOS):** `brew install ffmpeg cairo pango pkg-config`

### Step-by-Step Installation:
```bash
# 1. Clone repository
git clone https://github.com/[YOUR-USERNAME]/M3_AnimationVideo_LinearTransformations_StudentID.git
cd Linear_Transformations_M3

# 2. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install Python dependencies
pip install -r requirements.txt
```

---

## 7. How to Render the Animation

### 1. Verify Mathematics:
```bash
python3 src/verify_math.py
```

### 2. Generate Narration & Audio Tracks:
```bash
python3 audio/generate_audio.py
```

### 3. Generate the Storyboard PDF:
```bash
python3 storyboard/generate_storyboard_pdf.py
```

### 4. Render Master 1080p Video Deliverable:
```bash
# Render high quality 1080p60 (Default)
python3 src/main.py h

# Fast preview quality (480p15)
python3 src/main.py l
```
The final multiplexed MP4 with synchronized narration and ambient score is exported to:
`output/Linear_Transformations_Final.mp4`.

---

## 8. Video Specifications & Quality Verification

| Parameter | Project Specification | Final Deliverable Value | Status |
|---|---|---|---|
| **Resolution** | 1920 × 1080 (1080p) | 1920 × 1080 | **PASSED** |
| **Aspect Ratio** | 16:9 Landscape | 16:9 Landscape | **PASSED** |
| **Frame Rate** | 60 fps | 60 fps | **PASSED** |
| **Video Codec** | H.264 / AVC | H.264 (High Profile) | **PASSED** |
| **Audio Format** | Stereo AAC (192+ kbps) | AAC Stereo (256 kbps, 44.1 kHz) | **PASSED** |
| **Duration** | ~5 Minutes (Max 7 Min) | ~5.1 Minutes (307.6 seconds) | **PASSED** |
| **Voice-over** | Clear voice-over compulsory | Synced narration across all 6 scenes | **PASSED** |

---

## 9. Academic Integrity, References & AI Disclosure

### Academic References:
1. **Gilbert Strang**, *Introduction to Linear Algebra*, 5th Edition, Wellesley-Cambridge Press, 2016.
2. **Grant Sanderson (3Blue1Brown)**, *Essence of Linear Algebra*, 2016.
3. **David C. Lay, Steven R. Lay, Judi J. McDonald**, *Linear Algebra and Its Applications*, 5th Edition, Pearson, 2015.

### Software Credits:
- **Manim Community Edition** (v0.22.1)
- **FFmpeg Multimedia Framework** (v9.0)
- **NumPy & SciPy**
- **ReportLab PDF Engine**

### AI Tool Disclosure:
In accordance with academic policies, **Antigravity AI (Gemini 3.8 Flash)** was utilized to assist in animation structuring, scene transition timing, and draft documentation. All mathematical proofs and calculations were independently coded and computationally verified via Python/NumPy. See [`documentation/AI_disclosure.md`](documentation/AI_disclosure.md) for full details.

---

## 10. GitHub Public Upload Instructions

To publish this project to GitHub:
```bash
# Initialize git repository
git init
git add .
git commit -m "feat: complete M3 Mathematics Animation Video Project on Linear Transformations"

# Link to your public GitHub repository
git remote add origin https://github.com/[YOUR-USERNAME]/M3_AnimationVideo_LinearTransformations_E25B070581.git
git branch -M main
git push -u origin main
```

