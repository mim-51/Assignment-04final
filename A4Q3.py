from pulp import LpMaximize, LpProblem, LpVariable
problem = LpProblem("Simplex_Method", LpMaximize)
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)
problem += 12 * x1 + 15 * x2 + 14 * x3, "Objective"
problem += x1 + x2 + x3 <= 100, "Constraint 1"
problem += 3 * x1 + 2 * x2 + 5 * x3 <= 3, "Constraint 2"
problem += 0.02 * x1 + 0.04 * x2 + 0.03 * x3 <= 0.03, "Constraint 3"
status = problem.solve()
print(f"Optimal value of Z: {problem.objective.value()}")
print(f"x1 = {x1.value()}")
print(f"x2 = {x2.value()}")
print(f"x3 = {x3.value()}")