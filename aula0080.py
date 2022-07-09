import random

lista = []

c = 0

chave = []

while c < 30:

        x = random.randint(1,15)

        lista.append(x)

        c += 1

c == 30

print(lista)

num = int(input('Informe uma chave : '))

ver = lista.count(num)

print(ver)