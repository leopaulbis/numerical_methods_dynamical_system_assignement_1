import numpy as np
import matplotlib.pyplot as plt

def standard_map(x, y, a):
    new_x = (x + a * np.sin(x + y))%(2*np.pi)
    new_y = (x + y)%(2*np.pi)
    if new_x>np.pi:
        new_x=new_x-2*np.pi
    if new_y>np.pi:
        new_y=new_y-2*np.pi
    return new_x, new_y


def simulate_standard_map(x0, y0, a, iterations):
    x_values = []
    y_values = []
    x, y = x0, y0
    for _ in range(iterations):
        x, y = standard_map(x, y, a)
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

a = -0.7

# Number of iteration
iteration= 500
#Number of initial condition
NP=100

# Discretisation of[-pi, pi] for the initial condition
initial_conditions = np.linspace(-np.pi, np.pi, NP)

plt.figure(figsize=(10, 6))

# Simulate and plot the trajectories for each initial condition
for x0 in initial_conditions:
    x_values, y_values = simulate_standard_map(x0, 0.0, a, iteration)
    plt.plot(x_values, y_values, '.', markersize=1)

plt.title('Standard map for a=-0.7 on [-$\pi$, $\pi$]')
plt.xlabel('x (Modulo $2\pi$)')
plt.ylabel('y (Modulo $2\pi$)')

plt.show()
