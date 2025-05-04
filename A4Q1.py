import numpy as np
import matplotlib.pyplot as plt
x1 = np.linspace(0, 5, 100)

c1 = (10 - x1)/2  
c2 = 6 - x1        
c3 = x1 - 2        
c4 = (x1 - 1)/2    
plt.figure(figsize=(10, 6))
plt.plot(x1, c1, label=r'$x_1 + 2x_2 \leq 10$')
plt.plot(x1, c2, label=r'$x_1 + x_2 \leq 6$')
plt.plot(x1, c3, label=r'$x_1 - x_2 \leq 2$')
plt.plot(x1, c4, label=r'$x_1 - 2x_2 \leq 1$')

plt.fill(
    [0, 1, 3, 4, 2, 0],  
    [0, 0, 1, 2, 4, 5],  
    alpha=0.2,
    label='Feasible Region'
)

vertices = [(0,0), (1,0), (3,1), (4,2), (2,4), (0,5)]
Z_values = [2*x1 + x2 for (x1, x2) in vertices]
optimal = vertices[np.argmax(Z_values)]

plt.scatter(*optimal, c='red', zorder=5)
plt.annotate(f'Optimal (4, 2)\nZ=10', (4.1, 2.1))
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.legend()
plt.grid(True)
plt.title('Graphical Solution of LP Problem')
plt.show()
print(f"Optimal solution: x1 = {optimal[0]}, x2 = {optimal[1]}, Z = {max(Z_values)}")