c = 0
lista = []
while c < 8:
    valor = float(input('Informe o valor do produto: '))
    lista.append(valor)
    c = c + 1
print('X'*10)
print('O produto mais caro é :',max(lista))
print('O produto mais barato é:',min(lista))