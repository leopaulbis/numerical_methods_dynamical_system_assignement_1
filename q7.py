import matplotlib.pyplot as plt
import numpy as np
import os

# Define the standard map function
def standard_map(x, y, a):
    new_x = (x + a * np.sin(y)) % (2 * np.pi)
    new_y = (y + new_x) % (2 * np.pi)
    return new_x, new_y

# Define a range of 'a' values from -0.1 to -2.1
a_values = np.arange(-0.1, -2.2, -0.2)

# Define a list of initial conditions as [x, y] pairs
initial_conditions = [[-1, 2], [1.0, 1.0], [-2.0, 3]]  # Add more initial conditions as needed

# Number of iterations for each 'a' and initial condition
num_iterations = 1000

# Create a directory to save the plots (if needed)
if not os.path.exists('standard_map_plots'):
    os.makedirs('standard_map_plots')

# Iterate through each initial condition
for ic_idx, initial_condition in enumerate(initial_conditions):
    # Create a subdirectory for each initial condition
    ic_dir = f'standard_map_plots/ic_{ic_idx}'
    if not os.path.exists(ic_dir):
        os.makedirs(ic_dir)

    # Iterate through each 'a' value and create and save plots
    for a in a_values:
        # Lists to store coordinates
        x_values = []
        y_values = []

        # Generate points for the dynamics
        for _ in range(num_iterations):
            x, y = initial_condition
            x_values.append(x)
            y_values.append(y)
            initial_condition = standard_map(x, y, a)

        # Create a plot
        plt.figure(figsize=(8, 6))
        plt.plot(x_values, y_values, linestyle='-', color='blue', linewidth=0.5)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Standard Map Dynamics (a={a}) - Initial Condition ({initial_condition[0]:.2f}, {initial_condition[1]:.2f})')
        plt.grid(True)

        # Save the plot as an image in the subdirectory
        plt.savefig(f'{ic_dir}/standard_map_a_{a:.1f}.png')

        # Close the plot to avoid overlapping in the next iteration
        plt.close()