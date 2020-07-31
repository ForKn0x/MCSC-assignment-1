n = int(input('a number'))

def fact_for(n):
    fact = 1
    for x in range(1,n+1):
        fact = fact*x
    
    return fact

f = fact_for(n)

print(f)

def fact_while(n,fact=1,i=1):
    while i!=(n+1):
        fact = fact*i
        i += 1

    return fact


z = fact_while(n)

print(z)