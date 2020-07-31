import numpy as np
g= 9.8
def height(h_0,v_0,t):
    h = h_0+v_0*t-(1/2)*g*t*t
    return h

def velocity(v_0,t):
    v = v_0-g*t
    return v

h = height(1.2,5.4,0.5)
v = velocity(5.4,0.5)

print("For T=0.5 -> Height: ",round(h,2)," Velocity: ",round(v,2))

h = height(1.2,5.4,2)
v = velocity(5.4,2)

print("For T=2 -> Height: ",round(h,2)," Velocity: ",round(v,2))

