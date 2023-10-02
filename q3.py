import numpy as np
from matplotlib import pyplot as plt

# Definition of the standard map
def standard_map(x, y, a):
    new_x = (x + a * np.sin(x + y)) % (2 * np.pi)
    new_y = (x + y) % (2 * np.pi)
    if new_x>np.pi:
        new_x=new_x-2*np.pi
    if new_y>np.pi:
        new_y=new_y-2*np.pi
    return new_x, new_y

# Standard map applied three times (f^3)
def F(x, y, a):
    for _ in range(3):
        x, y = standard_map(x, y, a)
    return x, y

# Jacobian of the standard map
def jacobian_standard(x, y, a):
    J = np.array([
        [1 + a * np.cos(x + y), a * np.cos(x + y)],
        [1, 1]
    ])
    return J

# Jacobian of the standard map^3 using the chain rule
def jacobian_standard3(xy, a):
    #jacobian of the standard map evaluate in (x,y)
    J_F1 = jacobian_standard(*xy, a)
    #jacobian of the standard map evaluate in F(x,y)
    J_F2 = jacobian_standard(*standard_map(*xy, a), a)
    #jacobian of the standard map evaluate in F(F(x,y))
    J_F3 = jacobian_standard(*standard_map(*standard_map(*xy, a), a), a)

    return np.dot(np.dot(J_F3, J_F2), J_F1)

# Compute the jacobian of f^3(x, y, a) - (x, y)
def jacobian_standard3_minus_identity(xy, a):
    J_standard3 = jacobian_standard3(xy, a)
    dim = J_standard3.shape[0]
    I = np.identity(dim)
    return J_standard3- I

# Solve f^3(x,y)-(x,y) by the newton's method
def find_periodic_point(a, initial_guess, max_iterations=1000, tolerance=1e-10):
    xy = np.array(initial_guess,dtype=np.float64)

    for _ in range(max_iterations):
        # Calculate f^3(x, y, a)
        standard3_xy = F(xy[0],xy[1],a)

        # Calculate the jacobian of f^3(x, y, a) - (x, y)
        J = jacobian_standard3_minus_identity(xy, a)

        # Calculate f^3(x, y, a) - (x, y)
        residual = np.array(standard3_xy) - xy

        # Check if we are close to the solution
        if np.abs(residual[0]) < tolerance and np.abs(residual[1])<tolerance:

                    return xy

        # Newton's iterations
        xy = xy-np.linalg.solve(J, residual)

    return None


a_value = -0.7

initial_guess = (1,1)

periodic_point = find_periodic_point(a_value, initial_guess)

if periodic_point is not None:
    print(f"3-Periodic point for a = {a_value}: (x, y) = {periodic_point}")
    print(f"Value of f^3(x,y)={F(periodic_point[0],periodic_point[1],a_value)}")
else:
    print("No periodic point of period 3 found. Please revise your initial estimate or increase the number of iterations.")

###Plot the Orbit
num_iterations = 1000
initial_condition = np.array(periodic_point)

def simulate_standard_map(x0, y0, a, iterations):
    x_values = []
    y_values = []
    x, y = x0, y0
    for _ in range(iterations):
        x, y = standard_map(x, y, a)
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

x,y=simulate_standard_map(periodic_point[0],periodic_point[1],a_value,num_iterations)

#plot of the orbit
plt.title("Orbit for a 3-periodic point")
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,'.')
plt.show()

###Plot the invariant curve

def generate_invariant_curve(center_point, a, perturbation,num_iterations=100):
    invariant_curve = []
    current_point = center_point + perturbation * np.random.randn(2)
    for _ in range(num_iterations):
        invariant_curve.append(current_point)
        current_point = standard_map(current_point[0], current_point[1], a)
    return np.array(invariant_curve)

# Generate an invariant curve around the 3-periodic point
invariant_curve = generate_invariant_curve(periodic_point, a_value,0.01)
invariant_curve_ = generate_invariant_curve(periodic_point, a_value,0)
# Extract x and y coordinates of the invariant curve
x_values_curve = invariant_curve[:, 0]
y_values_curve = invariant_curve[:, 1]
x_values_curve_=invariant_curve_[:,0]
y_values_curve_=invariant_curve_[:,1]

fig, axs = plt.subplots(1, 2, figsize=(25, 6))

axs[0].plot(x_values_curve, y_values_curve, linestyle='-', color='b',linewidth=0.2,label="invariant curve with 0.01 pertubation")
axs[1].plot(x_values_curve_, y_values_curve_, linestyle='-', color='black',linewidth=0.2,label="invariant curve whithout perturbation")

#Plot of the 3-periodic point
axs[0].scatter(periodic_point[0], periodic_point[1], c='red', marker='o', label='4-Periodic Point')
axs[1].scatter(periodic_point[0], periodic_point[1], c='red', marker='o', label='4-Periodic Point')
axs[0].annotate(str(0), (periodic_point[0], periodic_point[1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
axs[1].annotate(str(0), (periodic_point[0], periodic_point[1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

#Plot the other point of the orbit
for i in range(2):
    periodic_point=standard_map(periodic_point[0],periodic_point[1],a_value)
    if i==0:
        axs[0].scatter(periodic_point[0], periodic_point[1], c='green', marker='o',label="Orbit's point")  # Mark them in green
        axs[1].scatter(periodic_point[0], periodic_point[1], c='green', marker='o',label="Orbit's point")
    axs[0].scatter(periodic_point[0], periodic_point[1], c='green', marker='o')
    axs[0].annotate(str(i+1), (periodic_point[0], periodic_point[1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    axs[1].scatter(periodic_point[0], periodic_point[1], c='green', marker='o')
    axs[1].annotate(str(i+1), (periodic_point[0], periodic_point[1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)


axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].set_title('Invariant Curve (With Perturbation)')
axs[0].legend()
axs[0].grid(True)

axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].set_title('Invariant Curve (No Perturbation)')
axs[1].legend()
axs[1].grid(True)

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()
