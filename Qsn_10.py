import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-3,3,100)

y = 3*(x**2)

plt.title('y=3*x^2')

plt.xlabel('x')

plt.ylabel('y')

plt.plot(x,y)

plt.show()