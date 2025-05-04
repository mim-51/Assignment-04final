from scipy.optimize import linprog
c = [45, 40, 85, 65]  
A = [
    [-3, -4, -8, -6],  
    [-2, -2, -7, -5],  
    [-6, -4, -7, -4]]
b = [-800, -200, -700]
bounds = [(0, None), (0, None), (0, None), (0, None)]  
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
if result.success:
    print("Optimal Diet Mix:")
    print(f"Food 1: {result.x[0]:.2f} units")
    print(f"Food 2: {result.x[1]:.2f} units")
    print(f"Food 3: {result.x[2]:.2f} units")
    print(f"Food 4: {result.x[3]:.2f} units")
    print(f"Minimum Cost: BDT {result.fun:.2f}")
else:
    print("No feasible solution found.")