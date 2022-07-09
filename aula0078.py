lista15 = []

lista10 = []

for n in range (15):

        v = int(input('Informe um valor : '))

        lista15.append(v)

        if v % 10 == 0:

                lista10.append(v)

print(lista15)

print(lista10)