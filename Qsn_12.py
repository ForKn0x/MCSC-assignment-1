import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

thita = np.linspace(0,20*np.pi,100)

x = 2*thita*np.cos(thita)

y = 2*thita*np.sin(thita)

z = 1+(2*thita)

fig = plt.figure()
a = Axes3D(fig)

a.plot3D(x,y,z)

a.scatter3D(x,y,z)

plt.show()