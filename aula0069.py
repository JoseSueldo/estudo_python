p = int(input('Primeiro elemento : '))
r = int(input('Razão : '))
n = 10
u = p + (n - 1) * r
u += 1
for var in range (p, u, r):
        print(var)