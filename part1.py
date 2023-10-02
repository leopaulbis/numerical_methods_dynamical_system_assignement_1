import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

##Part1: Logistic Map
##Graph 1
def f_1(x,a):
    return(a*x*(1-x))

# # tracé du repère et de la grille
# fig=figure(figsize=(10, 10))
# #fig=plt.figure()
# ax = fig.add_subplot(111, aspect='equal')
# ax.grid()
# ax.spines['bottom'].set_position('zero')
# ax.spines['left'].set_position('zero')
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)


plt.subplot(1,2,1)
# 1st term
u=0.2
#value of a
a=2
#number of iteration
n=100
x = [u,u]
y = [0,f_1(u,a)]
plt.plot(x,y,linestyle='--',color='blue',linewidth=0.5)
# construction of the terms
for i in range(n):
    x = [u,u]
    y = [u,f_1(u,a)]
    plt.plot(x,y,linestyle='--',color='blue',linewidth=0.5)
    x = [u,f_1(u,a)]
    y = [f_1(u,a),f_1(u,a)]
    plt.plot(x,y,linestyle='--',color='blue',linewidth=0.5)

    u = f_1(u,a)

x=np.linspace(0,1,100)
y=f_1(x,2)
plt.title('Simulation logistic map for 100 iterations, x0=0.2 and a=2')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,label='f_1(x)')
plt.plot(x,x,label='y=x')
plt.legend()
plt.grid(True)

##Graph 2
plt.subplot(1,2,2)
u=0.4
#value of a
a=3.2
#number of iteration
n=100
x = [u,u]
y = [0,f_1(u,a)]
plt.plot(x,y,linestyle='--',color='blue',linewidth=0.5)
# construction of the terms
for i in range(n):
    x = [u,u]
    y = [u,f_1(u,a)]
    plt.plot(x,y,linestyle='--',color='blue',linewidth=0.5)
    x = [u,f_1(u,a)]
    y = [f_1(u,a),f_1(u,a)]
    plt.plot(x,y,linestyle='--',color='blue',linewidth=0.5)

    u = f_1(u,a)

plt.title('Simulation logistic map for 100 iterations, x0=0.4 and a=3.2')
x=np.linspace(0,1,100)
y=f_1(x,2)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,label='f_1(x)')
plt.plot(x,x,label='y=x')
plt.legend()
plt.grid(True)
plt.show()