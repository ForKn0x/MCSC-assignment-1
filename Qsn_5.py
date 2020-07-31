import math

def check(a,b,c):
    if a==0:
        return
    
    r = b**2-(4*a*c)

    if r==0:
        print(f'{-b/(2*a)} is real and equal')
    elif r>0:
        print(f'{(-b+math.sqrt(r))/2*a,(-b-math.sqrt(r))/2*a} are real and unequal')
    else:
        print("Roots are imaginary")


check(2,4,2)

check(1,3,-10)

