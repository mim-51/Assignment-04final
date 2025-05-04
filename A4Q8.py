import numpy as np
from scipy.optimize import linprog

payoff = np.array([
    [-1, -2, 8],
    [7, 5, -1],
    [6, 0, 12]
])

n = payoff.shape[0]  
c = np.ones(n)
A_ub = -payoff.T
b_ub = -np.ones(payoff.shape[1])
bounds = [(0, None) for _ in range(n)]

res_B = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
value = 1 / res_B.fun
strategy_B = res_B.x * value

m = payoff.shape[1]  
c_dual = -np.ones(m)
A_dual = payoff
b_dual = np.ones(n)
bounds_dual = [(0, None) for _ in range(m)]

res_A = linprog(c_dual, A_ub=A_dual, b_ub=b_dual, bounds=bounds_dual)
strategy_A = res_A.x * value

print(f"Value of the Game: {value:.2f}")
print("Player B's Optimal Strategy:")
print(np.round(strategy_B, 4))
print("Player A's Optimal Strategy:")
print(np.round(strategy_A, 4))
