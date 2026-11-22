# M3 Viva Voce Examination: Questions and Model Answers
## Topic: Linear Transformations — How Matrices Transform 2D Space

**Course:** M3 — Linear Algebra and Calculus  
**Candidate Name:** NITIKA  
**Candidate ID:** E25B070581  

---

### Q1: What is the formal mathematical definition of a linear transformation?
**Answer:**  
A mapping $T: V \to W$ between two vector spaces over a field $\mathbb{F}$ (such as $\mathbb{R}$) is a linear transformation if it satisfies two fundamental properties for all vectors $\mathbf{u}, \mathbf{v} \in V$ and all scalars $c \in \mathbb{F}$:
1. **Additivity:** $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$
2. **Homogeneity:** $T(c\mathbf{u}) = cT(\mathbf{u})$  
These can be combined into the single superposition principle: $T(c\mathbf{u} + d\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v})$.

---

### Q2: Why must the origin remain fixed under any linear transformation?
**Answer:**  
By homogeneity, for any vector $\mathbf{v}$, choose scalar $c = 0$. Then:
$$T(\mathbf{0}) = T(0 \cdot \mathbf{v}) = 0 \cdot T(\mathbf{v}) = \mathbf{0}$$
Thus, the zero vector in the domain always maps to the zero vector in the codomain. If $T(\mathbf{0}) \ne \mathbf{0}$, the transformation is strictly non-linear.

---

### Q3: Why is a spatial translation not a linear transformation?
**Answer:**  
A translation is defined as $f(\mathbf{v}) = \mathbf{v} + \mathbf{b}$ where $\mathbf{b} \ne \mathbf{0}$.  
First, $f(\mathbf{0}) = \mathbf{0} + \mathbf{b} = \mathbf{b} \ne \mathbf{0}$, violating the fixed-origin condition.  
Second, $f(\mathbf{u} + \mathbf{v}) = \mathbf{u} + \mathbf{v} + \mathbf{b}$, whereas $f(\mathbf{u}) + f(\mathbf{v}) = \mathbf{u} + \mathbf{v} + 2\mathbf{b}$. Since $\mathbf{b} \ne 2\mathbf{b}$, additivity fails. Translations are affine transformations, not linear ones.

---

### Q4: What are the domain and codomain of the transformation shown in the video?
**Answer:**  
Both the domain and codomain are the 2-dimensional Euclidean real vector space $\mathbb{R}^2$. The mapping is an endomorphism $T: \mathbb{R}^2 \to \mathbb{R}^2$.

---

### Q5: How is a linear transformation represented by a matrix?
**Answer:**  
Every linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ is uniquely determined by its action on the standard basis vectors. For $\mathbb{R}^2$, the standard basis vectors are $\mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ and $\mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.  
The columns of the standard matrix $A$ are precisely the transformed basis vectors:
$$A = \begin{pmatrix} | & | \\ T(\mathbf{e}_1) & T(\mathbf{e}_2) \\ | & | \end{pmatrix}$$
Then for any vector $\mathbf{v}$, $T(\mathbf{v}) = A\mathbf{v}$.

---

### Q6: In your project, what matrix was used, and what are its column vectors?
**Answer:**  
We used the matrix:
$$A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$
Column 1 is $T(\mathbf{e}_1) = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$, and Column 2 is $T(\mathbf{e}_2) = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$.

---

### Q7: Show step-by-step how $A$ transforms the general vector $\mathbf{v} = (1, 1)^T$.
**Answer:**  
Using row-column matrix multiplication:
$$T\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2(1) + 1(1) \\ 1(1) + 2(1) \end{pmatrix} = \begin{pmatrix} 2 + 1 \\ 1 + 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix}$$
Alternatively, by linearity:
$$T(1\mathbf{e}_1 + 1\mathbf{e}_2) = 1T(\mathbf{e}_1) + 1T(\mathbf{e}_2) = \begin{pmatrix} 2 \\ 1 \end{pmatrix} + \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix}$$

---

### Q8: Show step-by-step how $A$ transforms $\mathbf{w} = (2, -1)^T$.
**Answer:**  
Row 1: $2(2) + 1(-1) = 4 - 1 = 3$.  
Row 2: $1(2) + 2(-1) = 2 - 2 = 0$.  
Therefore, $T\begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \end{pmatrix}$. The vector lands squarely on the positive x-axis.

---

### Q9: What happens geometrically to the unit grid under a linear transformation?
**Answer:**  
Because a linear transformation preserves addition and scaling, two geometric invariants are strictly maintained:
1. Lines remain straight lines (they do not curve).
2. Parallel lines remain parallel and evenly spaced.
3. The origin remains anchored at $(0,0)$.  
The square grid cells deform smoothly into a congruent grid of parallelograms.

---

### Q10: What are the coordinates of the transformed unit square in your demonstration?
**Answer:**  
The unit square vertices $(0,0)$, $(1,0)$, $(1,1)$, $(0,1)$ transform to:
- $(0,0) \to (0,0)$
- $(1,0) \to (2,1)$
- $(1,1) \to (3,3)$
- $(0,1) \to (1,2)$  
These four points form the vertices of a parallelogram.

---

### Q11: What is the determinant of matrix $A$, and how is it calculated?
**Answer:**  
For a $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $\det(A) = ad - bc$.  
For our matrix:
$$\det(A) = (2)(2) - (1)(1) = 4 - 1 = 3$$

---

### Q12: What is the geometric interpretation of the determinant?
**Answer:**  
The absolute value of the determinant, $|\det(A)|$, is the **area scaling factor** of the transformation. Any 2D shape with initial area $S$ will have an area of $|\det(A)| \cdot S$ after transformation. Here, the unit square of area $1$ transforms into a parallelogram of area $3 \times 1 = 3\text{ units}^2$.

---

### Q13: What does the sign of the determinant signify?
**Answer:**  
The sign indicates **orientation preservation**:
- If $\det(A) > 0$, orientation is preserved (counter-clockwise loops stay counter-clockwise; no flipping of space).
- If $\det(A) < 0$, orientation is reversed (space is turned over / reflected).
- If $\det(A) = 0$, the transformation collapses space into a lower dimension (a line or a point).

---

### Q14: Does a linear transformation scale all vector lengths by the same factor?
**Answer:**  
No. Area scaling is uniform, but length scaling is generally anisotropic (direction-dependent).  
In our example:
- Vector $(1, 1)$ of length $\sqrt{2} \approx 1.414$ maps to $(3, 3)$ of length $3\sqrt{2} \approx 4.243$, scaled by $3$.
- Vector $(1, -1)$ of length $\sqrt{2}$ maps to $(1, -1)$ of length $\sqrt{2}$, scaled by $1$ (unchanged).  
- Vector $\mathbf{e}_1 = (1, 0)$ of length $1$ maps to $(2, 1)$ of length $\sqrt{5} \approx 2.236$.

---

### Q15: What are the eigenvalues and eigenvectors of your matrix $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$?
**Answer:**  
The characteristic equation is $\det(A - \lambda I) = (2 - \lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = 0$, yielding:
- $\lambda_1 = 3$ with eigenvector $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
- $\lambda_2 = 1$ with eigenvector $\mathbf{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.  
Vectors along these directions do not rotate; they are purely scaled by their respective eigenvalues. Notice also that $\det(A) = \lambda_1 \cdot \lambda_2 = 3 \times 1 = 3$.

---

### Q16: Does $\det(A) = 1$ always imply a rigid rotation?
**Answer:**  
No! A determinant of $1$ means that **area and orientation are preserved**, but the transformation is not necessarily a rigid rotation.  
For example, the squeeze mapping $A = \begin{pmatrix} 2 & 0 \\ 0 & 0.5 \end{pmatrix}$ has:
$$\det(A) = (2)(0.5) - (0)(0) = 1.0$$
It preserves the area of any region (the unit square becomes a $2 \times 0.5$ rectangle of area $1.0$), and preserves orientation. However, it stretches horizontal vectors by a factor of $2$ and compresses vertical vectors by a factor of $0.5$, altering vector lengths.  
In contrast, **rigid rotations** preserve **both area and all vector lengths** (they are orthogonal matrices where $R^T R = I$, making them isometries).

---

### Q17: Give examples of pure scaling, rotation, reflection, and shear matrices.
**Answer:**  
1. **Uniform Scaling:** $S = \begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$ ($\det = k^2$).
2. **Rotation by angle $\theta$:** $R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ ($\det = 1$, preserves all lengths and areas).
3. **Reflection across x-axis:** $M = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ ($\det = -1$, reverses orientation).
4. **Squeeze / Shear:** $A = \begin{pmatrix} 2 & 0 \\ 0 & 0.5 \end{pmatrix}$ or $K = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$ ($\det = 1$, area-preserving non-rotations).

---

### Q18: What does a singular matrix ($\det(A) = 0$) do to 2D space?
**Answer:**  
A singular matrix has linearly dependent columns. It squashes the entire 2D plane into a 1D line (if rank = 1) or a single 0D point at the origin (if rank = 0). Because a line has zero 2D area, the area scaling factor is $\det(A) = 0$. Such transformations are non-invertible.

---

### Q18: What is Manim Community Edition, and how does it animate mathematical transformations?
**Answer:**  
Manim (Mathematical Animation Engine) is an open-source Python framework created by Grant Sanderson (3Blue1Brown) and maintained by the Manim Community. In Manim, objects are vector-based `Mobject`s (such as `Vector`, `NumberPlane`, `Polygon`, `MathTex`). Animations such as `ApplyMatrix` or `Transform` interpolate mathematical states over time, rendering smooth vector transitions frame-by-frame via Cairo and FFmpeg.

---

### Q19: In Manim, how is the grid transformation implemented?
**Answer:**  
We can apply the matrix directly to a `NumberPlane` using `plane.animate.apply_matrix(matrix)` or `ApplyMatrix(matrix, plane)`. This maps every coordinate point $(x, y)$ in the plane to $(2x+y, x+2y)$ continuously across the animation duration.

---

### Q20: How did you ensure audio-visual synchronization throughout the 5-minute video?
**Answer:**  
The script was broken down into timed sentences with known syllable and word counts. Audio was generated for each scene segment, and scene transitions in Manim were keyed to the narration duration using exact `self.wait()` intervals matching the audio segment lengths, followed by multi-stream multiplexing with FFmpeg.

