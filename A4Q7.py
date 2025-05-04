from scipy.optimize import linear_sum_assignment
import numpy as np
profit_matrix = np.array([
    [16, 10, 14, 11],
    [14, 11, 15, 15],
    [15, 15, 13, 12],
    [13, 12, 14, 15]
])
cost_matrix = np.max(profit_matrix) - profit_matrix
row_ind, col_ind = linear_sum_assignment(cost_matrix)
print("Optimal Assignment:")
for i, j in zip(row_ind, col_ind):
    print(f"Salesman {chr(65+i)} → City {j+1} (Profit: {profit_matrix[i][j]})")
print(f"Total Profit: {profit_matrix[row_ind, col_ind].sum()}")