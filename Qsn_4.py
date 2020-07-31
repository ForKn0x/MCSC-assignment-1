import numpy as np

y = np.arange(10,-0.5,-0.5)

def time(y,h=10,g=9.8):
    t = np.sqrt(2*(h-y)/g)
    return t

t = time(y)

print(t)

def velocity(T,Y):
    avg=[]
    for t,y in zip(T[:-1], Y[:-1]):
        avg.append((y - Y[np.where(Y==y)[0][0] + 1]) / (T[np.where(T==t)[0][0]+1] - t))
    return avg

print(velocity(t,y))




