'''
numeros = []
calc = 0
for _ in range(7):
    numeros.append(int(input('Digite um número: ')))
print(numeros)
calc = sum(numeros)
print(f'A soma é de todos os valores digitados é {calc}')

'''
contador = 0
c = 0
while contador < 7:
    contador = contador + 1
    print(f'{contador}')
    c = c + contador
print('')
print(c)

