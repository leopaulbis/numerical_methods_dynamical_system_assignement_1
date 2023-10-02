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

a_value=np.arange(-0.1, -2.2, -0.2)
print(a_value)
# Number of iteration
iteration= 500
#Number of initial condition
NP=100

# Discretisation of[-pi, pi] for the initial condition
initial_conditions = np.linspace(-np.pi, np.pi, NP)

# Créer la figure
#plt.figure(figsize=(20, 30))
# plt.figure(figsize=(20, 30))
# print(len(a_value))
# # Simuler et tracer les trajectoires pour chaque condition initiale
# for a in range(len(a_value)-5):
#
#     for x0 in initial_conditions:
#         x_values, y_values = simulate_standard_map(x0, 0.0, a_value[a], iteration)
#         # plt.subplot(5,2,a+1)
#         # plt.plot(x_values, y_values, '.', markersize=1)
#         # if(a>7):
#         #     plt.xlabel('x (Modulo $2\pi$)')
#         #     plt.ylabel('y (Modulo $2\pi$)')
#         # plt.title(f'Standard map for a={a_value[a]:.2f} on [-π, π]')
#         plt.subplot(2, 3, a+1)
#         plt.plot(x_values, y_values, '.', markersize=1)
#         plt.title(f'Standard map for a={a_value[a]:.2f} on [-π, π]')
#         plt.grid(True)
#             # if (a>2):
#             #     plt.xlabel('x (Modulo $2\pi$)')
#             #     plt.ylabel('y (Modulo $2\pi$)')
#
#
#         # if(a>=6):
#         #     plt.subplot(2,3,a+1-6)
#         #     plt.plot(x_values, y_values, '.', markersize=1)
#         # if (a>=10):
#         #     plt.xlabel('x (Modulo $2\pi$)')
#         #     plt.ylabel('y (Modulo $2\pi$)')
#         # if(a==10):
#         #     plt.show()
# plt.show()
#
# plt.figure(figsize=(20,30))
# for a in range(6,len(a_value)):
#
#     for x0 in initial_conditions:
#         x_values, y_values = simulate_standard_map(x0, 0.0, a_value[a], iteration)
#         # plt.subplot(5,2,a+1)
#         # plt.plot(x_values, y_values, '.', markersize=1)
#         # if(a>7):
#         #     plt.xlabel('x (Modulo $2\pi$)')
#         #     plt.ylabel('y (Modulo $2\pi$)')
#         # plt.title(f'Standard map for a={a_value[a]:.2f} on [-π, π]')
#         plt.subplot(2, 3, a+1-6)
#         plt.plot(x_values, y_values, '.', markersize=1)
#         plt.title(f'Standard map for a={a_value[a]:.2f} on [-π, π]')
#         plt.grid(True)
#         if(a>=8):
#             plt.xlabel('x (Modulo $2\pi$)')
#             plt.ylabel('y (Modulo $2\pi$)')
#         # if(a>=6):
#         #     plt.subplot(2,3,a+1-6)
#         #     plt.plot(x_values, y_values, '.', markersize=1)
#         # if (a>=10):
#         #     plt.xlabel('x (Modulo $2\pi$)')
#         #     plt.ylabel('y (Modulo $2\pi$)')
#         # if(a==10):
#         #     plt.show()
#         #
# plt.show()
plt.figure(figsize=(20,20))
for a in range(len(a_value)):

    for x0 in initial_conditions:
        x_values, y_values = simulate_standard_map(x0, 0.0, a_value[a], iteration)
        # plt.subplot(5,2,a+1)
        # plt.plot(x_values, y_values, '.', markersize=1)
        # if(a>7):
        #     plt.xlabel('x (Modulo $2\pi$)')
        #     plt.ylabel('y (Modulo $2\pi$)')
        # plt.title(f'Standard map for a={a_value[a]:.2f} on [-π, π]')
        plt.subplot(3, 4, a+1)
        plt.plot(x_values, y_values, '.', markersize=1)
        if(a>6):
            plt.xlabel('x (Modulo $2\pi$)')
            plt.ylabel('y (Modulo $2\pi$)')
        plt.title(f'Standard map for a={a_value[a]:.2f} on [-π, π]')
        plt.grid(True)
plt.show()
