def sumx(n,s=0):
    sq=[]
    for i in range(1,n+1):
        sq.append(i*i)

    for x in sq:
        s = s+x
    
    return s

n = int(input('Give me a number'))

print(sumx(n))