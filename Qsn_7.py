def sum_n(n,s=0):
    for i in range(1,n+1):
        s = s+i

    return s

n = int(input('A number: '))

x = sum_n(n)

print(x)