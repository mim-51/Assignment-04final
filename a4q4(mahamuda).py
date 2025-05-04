import numpy as np
import pandas as pd

M = 1e5  # Big M value
c = np.array([4, 3, 0, 0, 0, M, M, M], dtype=float)
A = np.array([   # Constraint matrix (coefficients of x1, x2, s1, s2, s3, A1, A2, A3)
    [200, 100, -1,  0,  0, 1, 0, 0],
    [1,   2,   0, -1,  0, 0, 1, 0],
    [40, 40,  0,  0, -1, 0, 0, 1]
], dtype=float)
b = np.array([4000, 50, 1400], dtype=float)  # Right-hand side constants

basis = [5, 6, 7]  # Basic variables indices initially: A1, A2, A3 => indices 5, 6, 7

def simplex_table(A, b, c, basis):
    m, n = A.shape
    iteration = 0
    while True:
        B = A[:, basis]  # Basic matrix
        B_inv = np.linalg.inv(B)
        cb = c[basis]
        xb = B_inv.dot(b)
        zj_cj = c - cb.dot(B_inv.dot(A))
        z = cb.dot(xb)

        # Print simplex table
        table = pd.DataFrame(np.hstack((A, b.reshape(-1, 1))), columns=[f"x{i+1}" for i in range(n)] + ["RHS"])
        table["BV"] = [f"x{basis[i]+1}" for i in range(m)]
        table = table[["BV"] + [col for col in table.columns if col != "BV"]]
        print(f"\n--- Iteration {iteration} ---")
        print(table)
        print("Zj - Cj:", zj_cj)
        print("Z =", z)

        # Check optimality
        if all(zj_cj >= 0):
            return xb, basis, z  # Optimal

        entering = np.argmin(zj_cj)     # Entering variable (most negative zj - cj)
        d = B_inv.dot(A[:, entering])

        ratios = [xb[i]/d[i] if d[i] > 0 else np.inf for i in range(m)]# Ratio test (only positive entries in direction vector)
        if all(r == np.inf for r in ratios):
            raise Exception("Unbounded solution")

        leaving = np.argmin(ratios)
        basis[leaving] = entering
        iteration += 1

xb, final_basis, final_cost = simplex_table(A, b, c, basis) # Run the Big M simplex method

# Extract optimal solution
solution = np.zeros_like(c)
for i, bi in enumerate(final_basis):
    solution[bi] = xb[i]

solution_values = {
    'x1 (Food A)': solution[0],
    'x2 (Food B)': solution[1],
    'Min Cost': final_cost
}

print("\n✅ Optimal Solution:")
for k, v in solution_values.items():
    print(f"{k}: {v}")