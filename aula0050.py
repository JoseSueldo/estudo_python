from random import randint
c = 0
x = randint(1, 10)
lista = []
p = []
div = []
while c <= 20:
    print(x)
    if x > 5:
        p .append(x)
    if x %3 ==0:
        div.append(x)
    x = randint(1, 10)
    c = c + 1
#Numeros maior que 5 na lista
#print(p)
print('_'*10)
print(f'({len(p)}) sorteados são maior que 5')
print('_'*10)
print(f'({len(div)}) numeros são divisíveis por 3')








'''if x % 2 == 0:
    if x > 5:
        p = x
        print(f'Temos {p} maior que 5')
        p = p + 1
'''




