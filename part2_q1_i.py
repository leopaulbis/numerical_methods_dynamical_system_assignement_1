import numpy as np
import matplotlib.pyplot as plt

# Define the standard map function
def standard_map(x, y, a):
    new_x = (x + a * np.sin(x + y))%(2*np.pi)
    new_y = (x + y)%(2*np.pi)
    if new_x>np.pi:
        new_x=new_x-2*np.pi
    if new_y>np.pi:
        new_y=new_y-2*np.pi
    return new_x, new_y

# Simulate the dynamics for a given number of iterations
def simulate_standard_map(x0, y0, a, iterations):
    x_values = []
    y_values = []
    x, y = x0, y0
    for _ in range(iterations):
        x, y = standard_map(x, y, a)
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

# Set the fixed parameter 'a'
a = -0.7

# Number of iterations
iterations = 500

# Generate different initial conditions and simulate the dynamics
initial_conditions = [
    (0.1, 0.2),
    (-0.5, 0.8),
    (1.0, -1.5),
    (3.0, 2.0),
    (-3.0,2.0),
    (-2,2)
]

plt.figure(figsize=(12, 8))
for i, (x0, y0) in enumerate(initial_conditions):
    x_values, y_values = simulate_standard_map(x0, y0, a, iterations)
    plt.subplot(2, 3, i + 1)
    plt.plot(x_values, y_values, 'b.', markersize=1)
    plt.title(f'Initial Condition ({x0}, {y0})')
    plt.xlabel('x')
    plt.ylabel('y')

plt.tight_layout()
plt.show()
