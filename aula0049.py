n = 1
p = 0
i = 0

while n <= 10:
    a = int(input('Digite um numero : '))
    n = n + 1
    if a % 2 == 0:
        p = p +1
    else:
        i = i +1
print(f'A quantidade de numeros PARES é {p}')
print(f'A quantidade de numeros IMPARES é {i}')