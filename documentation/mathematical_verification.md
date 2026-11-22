# Mathematical Verification Report: Linear Transformations in 2D Space

**Course:** M3 — Linear Algebra and Calculus  
**Topic:** Linear Transformations: How Matrices Transform Space  
**Student Name:** NITIKA  
**Student ID:** E25B070581  
**Verification Date:** 2026-11-22  
**Status:** ALL CALCULATIONS RIGOROUSLY VERIFIED  

---

## 1. Formal Definition & Axioms Verification

A transformation $T: \mathbb{R}^2 \to \mathbb{R}^2$ is linear if and only if for all vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^2$ and all scalars $c \in \mathbb{R}$:
1. **Additivity:** $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$
2. **Homogeneity (Scalar Multiplication):** $T(c\mathbf{u}) = cT(\mathbf{u})$

### Preservation of the Zero Vector (Fixed Origin):
Setting $c = 0$:
$$T(\mathbf{0}) = T(0 \cdot \mathbf{u}) = 0 \cdot T(\mathbf{u}) = \mathbf{0}$$
*Proof of Non-Linearity of Translation:*
Let $f(\mathbf{v}) = \mathbf{v} + \mathbf{b}$ where $\mathbf{b} \ne \mathbf{0}$.
$$f(\mathbf{0}) = \mathbf{0} + \mathbf{b} = \mathbf{b} \ne \mathbf{0}$$
$$f(\mathbf{u} + \mathbf{v}) = \mathbf{u} + \mathbf{v} + \mathbf{b} \ne f(\mathbf{u}) + f(\mathbf{v}) = \mathbf{u} + \mathbf{v} + 2\mathbf{b}$$
Hence, pure translations are affine transformations, not linear transformations. The origin must remain invariant under any linear transformation.

---

## 2. Main Transformation Matrix

The transformation matrix selected for the core demonstration is:
$$A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$

For an arbitrary input vector $\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}$:
$$T(\mathbf{v}) = A\mathbf{v} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 2x + y \\ x + 2y \end{pmatrix}$$

---

## 3. Standard Basis Vector Transformations

The columns of matrix $A$ represent the transformed coordinates of the standard basis vectors:

### Basis Vector 1 ($\mathbf{e}_1$):
$$\mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$
$$T(\mathbf{e}_1) = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 2(1) + 1(0) \\ 1(1) + 2(0) \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$
*Verification:* Column 1 of $A$ is $\begin{pmatrix} 2 \\ 1 \end{pmatrix}$. Match confirmed.

### Basis Vector 2 ($\mathbf{e}_2$):
$$\mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$
$$T(\mathbf{e}_2) = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 2(0) + 1(1) \\ 1(0) + 2(1) \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$
*Verification:* Column 2 of $A$ is $\begin{pmatrix} 1 \\ 2 \end{pmatrix}$. Match confirmed.

---

## 4. Worked General Vector Examples

### Example 1: Vector $\mathbf{v} = (1, 1)^T$
$$\mathbf{v} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$
$$T(\mathbf{v}) = A\mathbf{v} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$
Row 1 calculation:
$$2(1) + 1(1) = 2 + 1 = 3$$
Row 2 calculation:
$$1(1) + 2(1) = 1 + 2 = 3$$
$$T\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix}$$

*Linear Combination Check:*
$$\mathbf{v} = 1\mathbf{e}_1 + 1\mathbf{e}_2$$
$$T(\mathbf{v}) = 1T(\mathbf{e}_1) + 1T(\mathbf{e}_2) = \begin{pmatrix} 2 \\ 1 \end{pmatrix} + \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 2+1 \\ 1+2 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix}$$
*Verification:* Both matrix multiplication and basis vector superposition yield $\begin{pmatrix} 3 \\ 3 \end{pmatrix}$. Match confirmed.

### Example 2: Vector $\mathbf{w} = (2, -1)^T$
$$\mathbf{w} = \begin{pmatrix} 2 \\ -1 \end{pmatrix}$$
$$T(\mathbf{w}) = A\mathbf{w} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 2 \\ -1 \end{pmatrix}$$
Row 1 calculation:
$$2(2) + 1(-1) = 4 - 1 = 3$$
Row 2 calculation:
$$1(2) + 2(-1) = 2 - 2 = 0$$
$$T\begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \end{pmatrix}$$

*Linear Combination Check:*
$$\mathbf{w} = 2\mathbf{e}_1 - 1\mathbf{e}_2$$
$$T(\mathbf{w}) = 2\begin{pmatrix} 2 \\ 1 \end{pmatrix} - 1\begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix} - \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \end{pmatrix}$$
*Verification:* Both methods yield $\begin{pmatrix} 3 \\ 0 \end{pmatrix}$. Match confirmed.

---

## 5. Geometric Transformation of the Unit Square

Original Unit Square Vertices:
- $V_0 = (0, 0)$
- $V_1 = (1, 0)$
- $V_2 = (1, 1)$
- $V_3 = (0, 1)$

Transformed Vertices:
- $T(V_0) = T(0, 0) = (0, 0)$
- $T(V_1) = T(1, 0) = (2, 1)$
- $T(V_2) = T(1, 1) = (3, 3)$
- $T(V_3) = T(0, 1) = (1, 2)$

Parallelogram Side Vectors:
- Side 1: $T(V_1) - T(V_0) = (2, 1) - (0, 0) = (2, 1)$
- Side 2: $T(V_3) - T(V_0) = (1, 2) - (0, 0) = (1, 2)$
- Opposite Side 1: $T(V_2) - T(V_3) = (3, 3) - (1, 2) = (2, 1)$ (Parallel and equal to Side 1)
- Opposite Side 2: $T(V_2) - T(V_1) = (3, 3) - (2, 1) = (1, 2)$ (Parallel and equal to Side 2)

*Shape Confirmation:* Opposite sides are parallel and congruent vectors, proving the transformed shape is an exact parallelogram.

---

## 6. Determinant, Area Scaling, and Orientation

### Determinant Calculation:
$$\det(A) = ad - bc = (2)(2) - (1)(1) = 4 - 1 = 3$$

### Geometric Area Calculation:
- **Original Square Area:** $1 \times 1 = 1\text{ unit}^2$.
- **Transformed Parallelogram Area:** Given by the 2D cross product magnitude of its bounding vectors $T(\mathbf{e}_1) = (2, 1)$ and $T(\mathbf{e}_2) = (1, 2)$:
$$\text{Area} = |x_1 y_2 - x_2 y_1| = |(2)(2) - (1)(1)| = |4 - 1| = 3\text{ units}^2$$
$$\text{Area Scaling Factor} = \frac{\text{Area}_{\text{final}}}{\text{Area}_{\text{initial}}} = \frac{3}{1} = 3 = |\det(A)|$$

### Orientation Preservation:
Since $\det(A) = +3 > 0$:
- The transformation preserves orientation.
- The order of basis vectors $\mathbf{e}_1 \to \mathbf{e}_2$ forms a counter-clockwise angle of $90^\circ$.
- The transformed vectors $T(\mathbf{e}_1) = (2,1) \to T(\mathbf{e}_2) = (1,2)$ also maintain a counter-clockwise orientation (angle of $T(\mathbf{e}_1)$ is $\arctan(0.5) \approx 26.57^\circ$, angle of $T(\mathbf{e}_2)$ is $\arctan(2) \approx 63.43^\circ$, with positive cross product $(2)(2)-(1)(1) = +3$).

---

## 7. Length Scaling vs. Area Scaling Distinction

Length scaling varies with vector direction (anisotropy) and is governed by eigenvalues and eigenvectors:

### Eigenvalues of $A$:
$$\det(A - \lambda I) = \begin{vmatrix} 2 - \lambda & 1 \\ 1 & 2 - \lambda \end{vmatrix} = (2 - \lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda - 3)(\lambda - 1) = 0$$
$$\lambda_1 = 3, \quad \lambda_2 = 1$$

### Eigenvectors:
- For $\lambda_1 = 3$: $(A - 3I)\mathbf{v} = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \mathbf{0} \implies y = x$. Eigenvector $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
  - Length change: $\|\mathbf{v}_1\| = \sqrt{2} \approx 1.414$, $\|T(\mathbf{v}_1)\| = \|(3, 3)\| = \sqrt{18} = 3\sqrt{2} \approx 4.243$. Scaling factor = $\mathbf{3.0}$.
- For $\lambda_2 = 1$: $(A - 1I)\mathbf{v} = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \mathbf{0} \implies y = -x$. Eigenvector $\mathbf{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.
  - Length change: $\|\mathbf{v}_2\| = \sqrt{2} \approx 1.414$, $\|T(\mathbf{v}_2)\| = \|(1, -1)\| = \sqrt{2} \approx 1.414$. Scaling factor = $\mathbf{1.0}$ (isometric along this direction!).
- For basis vector $\mathbf{e}_1 = (1, 0)$:
  - Initial length = $1.0$.
  - Transformed vector $T(\mathbf{e}_1) = (2, 1)$, final length = $\sqrt{2^2 + 1^2} = \sqrt{5} \approx 2.236$. Scaling factor = $\sqrt{5} \approx 2.236$.

**Conclusion:** Length scaling is direction-dependent ($\min = 1.0$, $\max = 3.0$), whereas **area scaling is uniform everywhere and strictly equal to $\det(A) = 3$**.

---

## 8. Area-Preserving Transformations vs. Rigid Rotations ($\det(A) = 1$)

A crucial distinction in linear algebra is that **$\det(A) = 1$ preserves area and orientation, but is NOT necessarily a rigid rotation**:

### Counterexample: The Hyperbolic Squeeze Mapping
Consider the diagonal transformation:
$$A_{\text{squeeze}} = \begin{pmatrix} 2 & 0 \\ 0 & 0.5 \end{pmatrix}$$

1. **Determinant & Area Scaling:**
   $$\det(A_{\text{squeeze}}) = (2)(0.5) - (0)(0) = 1.0 - 0 = 1.0$$
   $$\text{Area Scaling Factor} = |\det(A_{\text{squeeze}})| = 1.0$$
   Any region of initial area $S$ has final area $1.0 \times S = S$. The area is strictly preserved.

2. **Action on the Unit Square:**
   - $(0,0) \to (0,0)$
   - $(1,0) \to (2,0)$  (Horizontal base stretched by factor of $2.0$)
   - $(1,1) \to (2,0.5)$
   - $(0,1) \to (0,0.5)$  (Vertical height compressed by factor of $0.5$)
   $$\text{Transformed Area} = 2.0 \times 0.5 = 1.0\text{ unit}^2$$

3. **Length Changes (Non-Isometry):**
   - Basis vector $\mathbf{e}_1 = (1, 0) \implies \|T(\mathbf{e}_1)\| = \|(2, 0)\| = 2.0$ (Length doubled).
   - Basis vector $\mathbf{e}_2 = (0, 1) \implies \|T(\mathbf{e}_2)\| = \|(0, 0.5)\| = 0.5$ (Length halved).
   Since vector lengths are not preserved, $A_{\text{squeeze}}$ is **not an isometry** and **not a rigid rotation**.

### Comparison: True Rigid Rotations (Isometries)
A pure 2D rotation by angle $\theta$ has standard matrix:
$$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$
- Determinant: $\det(R(\theta)) = \cos^2\theta - (-\sin^2\theta) = \cos^2\theta + \sin^2\theta = 1.0$.
- Inner Product Preservation: $(R\mathbf{u}) \cdot (R\mathbf{v}) = \mathbf{u}^T R^T R \mathbf{v} = \mathbf{u}^T I \mathbf{v} = \mathbf{u} \cdot \mathbf{v}$.
- Length Preservation: $\|R(\theta)\mathbf{v}\| = \|\mathbf{v}\|$ for every vector $\mathbf{v} \in \mathbb{R}^2$.
**Conclusion:** Rigid rotations preserve **both** area and vector lengths, whereas a general transformation with $\det(A) = 1$ (such as shear or squeeze mappings) preserves area and orientation without preserving vector lengths.

---

## 9. Computational Verification Script

Verified via Python 3.13 NumPy script:
```python
import numpy as np

A = np.array([[2, 1], [1, 2]])
e1 = np.array([1, 0])
e2 = np.array([0, 1])
v1 = np.array([1, 1])
v2 = np.array([2, -1])

assert np.array_equal(A @ e1, np.array([2, 1]))
assert np.array_equal(A @ e2, np.array([1, 2]))
assert np.array_equal(A @ v1, np.array([3, 3]))
assert np.array_equal(A @ v2, np.array([3, 0]))
assert np.isclose(np.linalg.det(A), 3.0)
print("All assertions passed successfully!")
```
Result: **PASSED (100% Verified)**

