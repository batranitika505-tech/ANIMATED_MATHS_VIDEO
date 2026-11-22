"""
Mathematical Verification Script for M3 Linear Transformations Project
Verifies all matrix operations, basis vector mappings, vector transformations,
unit square vertices, determinant, area scaling, and eigenvalues.
"""
import numpy as np

def verify_all():
    print("=" * 60)
    print("M3 LINEAR TRANSFORMATIONS — INDEPENDENT NUMERICAL VERIFICATION")
    print("=" * 60)
    
    # 1. Main Matrix Definition
    A = np.array([[2, 1],
                  [1, 2]], dtype=float)
    print(f"Matrix A:\n{A}\n")
    
    # 2. Standard Basis Vectors
    e1 = np.array([1, 0], dtype=float)
    e2 = np.array([0, 1], dtype=float)
    
    Te1 = A @ e1
    Te2 = A @ e2
    print(f"Standard basis e1 = {e1} -> T(e1) = A @ e1 = {Te1}")
    print(f"Standard basis e2 = {e2} -> T(e2) = A @ e2 = {Te2}")
    assert np.allclose(Te1, [2, 1]), "T(e1) must be [2, 1]"
    assert np.allclose(Te2, [1, 2]), "T(e2) must be [1, 2]"
    print(">> Basis vector transformations: VERIFIED\n")
    
    # 3. Worked General Vectors
    v = np.array([1, 1], dtype=float)
    Tv = A @ v
    print(f"General vector v = {v} -> T(v) = A @ v = {Tv}")
    # Manual row checks:
    assert 2*1 + 1*1 == 3, "Row 1 must be 3"
    assert 1*1 + 2*1 == 3, "Row 2 must be 3"
    assert np.allclose(Tv, [3, 3]), "T(v) must be [3, 3]"
    print(">> Vector v=(1,1) transformation: VERIFIED\n")
    
    w = np.array([2, -1], dtype=float)
    Tw = A @ w
    print(f"General vector w = {w} -> T(w) = A @ w = {Tw}")
    assert 2*2 + 1*(-1) == 3, "Row 1 must be 3"
    assert 1*2 + 2*(-1) == 0, "Row 2 must be 0"
    assert np.allclose(Tw, [3, 0]), "T(w) must be [3, 0]"
    print(">> Vector w=(2,-1) transformation: VERIFIED\n")
    
    # 4. Unit Square Vertices
    V0 = np.array([0, 0], dtype=float)
    V1 = np.array([1, 0], dtype=float)
    V2 = np.array([1, 1], dtype=float)
    V3 = np.array([0, 1], dtype=float)
    
    TV0 = A @ V0
    TV1 = A @ V1
    TV2 = A @ V2
    TV3 = A @ V3
    
    print("Unit Square Vertices:")
    print(f"  V0 {V0} -> {TV0}")
    print(f"  V1 {V1} -> {TV1}")
    print(f"  V2 {V2} -> {TV2}")
    print(f"  V3 {V3} -> {TV3}")
    
    assert np.allclose(TV0, [0, 0])
    assert np.allclose(TV1, [2, 1])
    assert np.allclose(TV2, [3, 3])
    assert np.allclose(TV3, [1, 2])
    print(">> Parallelogram vertices: VERIFIED\n")
    
    # 5. Determinant & Area Scaling
    det_A = np.linalg.det(A)
    det_manual = (2 * 2) - (1 * 1)
    print(f"Determinant: manual = {det_manual}, numpy = {det_A:.4f}")
    assert det_manual == 3
    assert np.isclose(det_A, 3.0)
    
    # Area of parallelogram via cross product
    u_side = TV1 - TV0  # [2, 1]
    v_side = TV3 - TV0  # [1, 2]
    area_parallelogram = np.abs(u_side[0] * v_side[1] - u_side[1] * v_side[0])
    print(f"Original unit square area: 1.000")
    print(f"Transformed parallelogram area: {area_parallelogram:.4f}")
    assert np.isclose(area_parallelogram, 3.0)
    assert np.isclose(area_parallelogram / 1.0, det_A)
    print(">> Area scaling factor = |det(A)| = 3: VERIFIED\n")
    
    # 6. Orientation Preservation Check
    print(f"Determinant sign: {np.sign(det_A)} (Positive -> Preserves Orientation)")
    assert det_A > 0, "det(A) must be positive"
    print(">> Orientation preservation: VERIFIED\n")
    
    # 7. Linearity Axiom Checks
    c = 2.5
    u_test = np.array([3.0, -1.5])
    v_test = np.array([-1.0, 4.0])
    
    # Additivity
    assert np.allclose(A @ (u_test + v_test), (A @ u_test) + (A @ v_test))
    # Homogeneity
    assert np.allclose(A @ (c * u_test), c * (A @ u_test))
    # Zero vector
    assert np.allclose(A @ np.zeros(2), np.zeros(2))
    print(">> Linearity axioms (additivity, homogeneity, origin invariance): VERIFIED\n")
    
    # 8. Eigenvalues and Directional Length Scaling
    eigenvals, eigenvecs = np.linalg.eig(A)
    print(f"Eigenvalues: {eigenvals}")
    print(f"Eigenvectors:\n{eigenvecs}")
    assert np.allclose(np.sort(eigenvals), [1.0, 3.0])
    
    # Length of (1, 1) scaled by 3:
    len_v = np.linalg.norm(v)
    len_Tv = np.linalg.norm(Tv)
    print(f"Length of (1,1): {len_v:.4f} -> Length of T(1,1): {len_Tv:.4f} (Factor: {len_Tv/len_v:.1f})")
    assert np.isclose(len_Tv / len_v, 3.0)
    
    # Vector along second eigenvector (1, -1)
    v_iso = np.array([1, -1], dtype=float)
    Tv_iso = A @ v_iso
    len_viso = np.linalg.norm(v_iso)
    len_Tviso = np.linalg.norm(Tv_iso)
    print(f"Length of (1,-1): {len_viso:.4f} -> Length of T(1,-1): {len_Tviso:.4f} (Factor: {len_Tviso/len_viso:.1f})")
    assert np.isclose(len_Tviso / len_viso, 1.0)
    print(">> Length scaling is anisotropic (direction-dependent): VERIFIED\n")

    # 9. Area-Preserving Squeeze Transformation vs Rigid Rotation Check
    print("--- 9. Squeeze Transformation Verification (det = 1, Not a Rotation) ---")
    A_squeeze = np.array([[2.0, 0.0],
                          [0.0, 0.5]], dtype=float)
    det_squeeze = np.linalg.det(A_squeeze)
    print(f"Matrix A_squeeze:\n{A_squeeze}")
    print(f"det(A_squeeze) = {det_squeeze:.4f}")
    assert np.isclose(det_squeeze, 1.0), "det(A_squeeze) must equal 1.0"
    
    # Check transformed unit square vertices
    sqz_V0 = A_squeeze @ np.array([0, 0])
    sqz_V1 = A_squeeze @ np.array([1, 0])
    sqz_V2 = A_squeeze @ np.array([1, 1])
    sqz_V3 = A_squeeze @ np.array([0, 1])
    print(f"Transformed vertices: {sqz_V0}, {sqz_V1}, {sqz_V2}, {sqz_V3}")
    assert np.allclose(sqz_V1, [2.0, 0.0])
    assert np.allclose(sqz_V3, [0.0, 0.5])
    
    # Area calculation
    area_sqz = (sqz_V1[0] - sqz_V0[0]) * (sqz_V3[1] - sqz_V0[1])
    print(f"Transformed rectangle area = {area_sqz:.4f} (Strictly preserved: 1.0 unit²)")
    assert np.isclose(area_sqz, 1.0)
    
    # Length changes
    len_h_init = np.linalg.norm([1, 0])
    len_h_final = np.linalg.norm(sqz_V1)
    len_v_init = np.linalg.norm([0, 1])
    len_v_final = np.linalg.norm(sqz_V3)
    print(f"Horizontal vector length: {len_h_init:.2f} -> {len_h_final:.2f} (Factor: {len_h_final/len_h_init:.1f}x)")
    print(f"Vertical vector length:   {len_v_init:.2f} -> {len_v_final:.2f} (Factor: {len_v_final/len_v_init:.1f}x)")
    assert not np.isclose(len_h_final, len_h_init), "Lengths must change, proving it is not a rigid rotation"
    print(">> det(A) = 1 preserves area and orientation, but is NOT a rigid rotation: VERIFIED\n")
    
    # Rigid rotation check (theta = 45 deg)
    theta = np.pi / 4
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    det_R = np.linalg.det(R)
    assert np.isclose(det_R, 1.0)
    test_vec = np.array([3.0, 4.0])
    assert np.isclose(np.linalg.norm(R @ test_vec), np.linalg.norm(test_vec))
    print(">> Rigid rotation preserves BOTH area (det=1) AND vector lengths (isometry): VERIFIED\n")
    
    print("=" * 60)
    print("ALL MATHEMATICAL CHECKS PASSED WITH 100% PRECISION!")
    print("=" * 60)

if __name__ == "__main__":
    verify_all()

