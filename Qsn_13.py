import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-3,3,100)
y = np.linspace(-3,3,100)
X, Y = np.meshgrid(x, y)

def f(x,y):
    return (1 - (x/2) + x**5 + y**5) / (np.exp((-x**2) - (y**2)))

Z = f(X,Y)
fig = plt.figure()

ax = Axes3D(fig)

plt.contourf(X,Y,Z,10)

plt.show()
