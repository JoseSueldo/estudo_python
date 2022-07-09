l = []


def rec_fib(n):
    if n > 1:
        return rec_fib(n - 1) + rec_fib(n - 2)

    return n


for i in range(17):
    l.append(rec_fib(i))

print(l)

ll = []

for n in range(16):
    ll.append(n)

print(ll)

# 76

import random

l = []

for x in range(7):
    x = random.randint(0, 999)

    l.append(x)

print(l)