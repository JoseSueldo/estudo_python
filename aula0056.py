c = 0
lista = []
p = int(input('Quantos números deseja digitar : '))
while c != p:
    n = int(input('Digite um numero : '))
    lista.append(n)
    if n == 1111:
        print('ENCERRADO')
        break
    c +=1

soma = sum(lista)
print(f'A soma de todos os números é de {soma}')