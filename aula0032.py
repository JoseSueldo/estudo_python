'''
Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
jogador vai tentar descobrir qual foi o valor sorteado.
'''
from random import randint
lista = (1, 2, 3, 4, 5)
computador = randint(1, 5)
print('De 0 a 5 tente adivinhar o número que o computador jogou')
print('*'*10)
jogador = int(input('Escolha o número: '))
print('computador jogou ( {} )'.format([computador]))
'''if computador == 1:
    if jogador == 1:
        print('Você ganhou')
    elif jogador == 2:
        print('Perdeu ')
    elif jogador == 3:
        print('Perdeu')
    elif jogador == 4:
        print('Perdeu')
elif computador == 2:
    if jogador == 1:
        print('Perdeu')
    elif jogador == 2:
        print('Você ganhou')
    elif jogador == 3:
        print('perdeu')
    elif jogador == 4:
        print('perdeu')
    elif jogador == 5:
        print('Perdeu')
elif computador == 3:
    if jogador == 1:
        print('Perdeu')
    elif jogador == 2:
        print('Perdeu')
    elif jogador == 3:
        print('Você ganhou')
    elif jogador == 4:
        print('Perdeu')
    elif jogador == 5:
        print('Perdeu')
elif computador == 4:
    if jogador == 1:
        print('Perdeu')
    elif jogador == 2:
        print('Perdeu')
    elif jogador == 3:
        print('Perdeu')
    elif jogador == 4:
        print('Você ganhou')
    elif jogador == 5:
        print('Perdeu')
elif computador == 5:
    if jogador == 1:
        print('Perdeu')
    elif jogador ==2:
        print('Perdeu')
    elif jogador == 3:
        print('Perdeu')
    elif jogador == 4:
        print('Perdeu')
    elif jogador == 5:
        print('Você ganhou')
'''
n = 0
while jogador != computador:
    print('Você perdeu!')
    break
if jogador == computador:
    print('Você ganhou ')