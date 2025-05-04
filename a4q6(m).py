import numpy as np

# Given data
costs = np.array([
    [16, 20, 12],
    [14, 8, 18],
    [26, 24, 16]
])
supply = np.array([200, 160, 90])
demand = np.array([180, 120, 150])

# Step 1: Initial feasible solution using Northwest Corner Rule
def north_west_corner(supply, demand):
    alloc = np.zeros((3, 3), dtype=int)
    s, d = supply.copy(), demand.copy()
    i, j = 0, 0
    while i < 3 and j < 3:
        q = min(s[i], d[j])
        alloc[i, j] = q
        s[i] -= q
        d[j] -= q
        if s[i] == 0: i += 1
        else: j += 1
    return alloc

# Step 2: Compute the u and v potentials
def compute_u_v(alloc, costs):
    u, v = np.full(3, np.nan), np.full(3, np.nan)
    u[0] = 0  # Arbitrarily set u[0] = 0
    basic = [(i, j) for i in range(3) for j in range(3) if alloc[i, j] > 0]
    
    while np.isnan(u).any() or np.isnan(v).any():
        for i, j in basic:
            if not np.isnan(u[i]) and np.isnan(v[j]):
                v[j] = costs[i, j] - u[i]
            elif not np.isnan(v[j]) and np.isnan(u[i]):
                u[i] = costs[i, j] - v[j]
    return u, v

# Step 3: Find the minimum opportunity cost and adjust the allocation
def modi_method(alloc, costs, u, v):
    min_opp = 0
    enter_cell = None
    for i in range(3):
        for j in range(3):
            if alloc[i, j] == 0:
                opp = costs[i, j] - (u[i] + v[j])
                if opp < min_opp:
                    min_opp = opp
                    enter_cell = (i, j)
    
    # If there's no negative opportunity cost, the solution is optimal
    if min_opp >= 0:
        return alloc, True
    
    # Step 4: Dynamically detect the loop
    loop = find_cycle(alloc, enter_cell)
    if not loop:
        return alloc, False
    
    # Step 5: Reallocate the flow along the cycle
    theta = min(alloc[i, j] for (i, j) in loop[1::2])  # Find the smallest allocation in the loop
    for idx, (i, j) in enumerate(loop):
        alloc[i, j] += theta if idx % 2 == 0 else -theta

    return alloc, False

# Function to dynamically detect the cycle
def find_cycle(alloc, enter_cell):
    loop = [enter_cell]
    visited = set(loop)
    direction = True  # True for supply, False for demand
    
    while len(loop) < 4:  # A valid cycle will involve 4 points (alternating supply-demand-supply-deman)
        last_i, last_j = loop[-1]
        if direction:
            # Move to the next supply node in the cycle (fill demand)
            next_cell = next((i, last_j) for i in range(3) if alloc[i, last_j] > 0 and (i, last_j) not in visited)
        else:
            # Move to the next demand node in the cycle (fill supply)
            next_cell = next((last_i, j) for j in range(3) if alloc[last_i, j] > 0 and (last_i, j) not in visited)
        
        loop.append(next_cell)
        visited.add(next_cell)
        direction = not direction

    return loop

# Run the MODI method until no negative opportunity costs are found
alloc = north_west_corner(supply, demand)
iteration = 0

while True:
    u, v = compute_u_v(alloc, costs)
    alloc, is_optimal = modi_method(alloc, costs, u, v)
    
    if is_optimal:
        break
    iteration += 1

# Calculate the total cost
total_cost = np.sum(alloc * costs)

# Output the result
print(f"Optimal Allocation:\n{alloc}\nTotal Cost: {total_cost} BDT")
