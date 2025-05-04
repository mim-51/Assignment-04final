import numpy as np
import pandas as pd

def north_west_corner(s, d, c):
    m, n = len(s), len(d)
    allocation = np.zeros((m, n))
    total_cost = 0
    steps = []  # To save steps as tables

    i, j = 0, 0
    while i < m and j < n:
        allocation_amount = min(s[i], d[j])
        allocation[i][j] = allocation_amount
        total_cost += allocation_amount * c[i][j]

        # Save table for the current step
        table = pd.DataFrame(data=allocation, columns=["P", "Q", "R", "S", "T"], 
                             index=["A", "B", "C", "D"]).astype(int)
        steps.append({"step_table": table, "supply": s.copy(), "demand": d.copy(), "cost": total_cost})

        s[i] -= allocation_amount
        d[j] -= allocation_amount

        if s[i] == 0:
            i += 1
        else:
            j += 1

    return allocation, total_cost, steps

# Problem data
c = np.array([[4, 3, 1, 2, 6],
                 [5, 2, 3, 4, 5],
                 [3, 5, 6, 3, 2],
                 [2, 4, 4, 5, 3]])
s= [80, 60, 40, 20]
d= [60, 60, 30, 40, 10]

# Solve problem
allocation, total_cost, steps = north_west_corner(s, d, c)

# Print each step as a table
for idx, step in enumerate(steps):
    print(f"Step {idx + 1}:")
    print(step["step_table"])
    print("Remaining Supply:", step["supply"])
    print("Remaining Demand:", step["demand"])
    print("Cumulative Cost:", step["cost"])
    print("---")
