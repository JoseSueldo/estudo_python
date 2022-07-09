c = 0
contador = 0
lista = []
maior = []
menor = []
while c < 3:
    idade = int(input('Informe a idade :'))
    if idade >= 18:
        maior.append(idade)
    if idade <= 5:
        menor.append(idade)
    lista.append(idade)
    c = c + 1
soma_das_notas = sum(lista)

print(f'A soma das idades é :{soma_das_notas}')
print(f'Temos ({len(maior)}) idades maior que 18')
print(f'Temos ({len(menor)}) idades menor que 5')
print(f'A maior idade lida foi ({max(lista)})')

