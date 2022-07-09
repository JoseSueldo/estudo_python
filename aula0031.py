from random import randint
lista = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''
[0] - Pedra
[1] - Papel
[2] - Tesoura''')
esc = int(input('Escolha :'))
print('*'*10)
print('Computador jogou ({})'.format(lista[computador]))
print('Jogador jogou ({})'.format(lista[esc]))
'''
if computador == 0:
    if esc == 0:
        print('Empate')
    elif esc == 1:
        print('Jogador Venceu')
    elif esc == 2:
        print('Computador venceu')
elif computador == 1:
    if esc == 0:
        print('Jogador venceu')
    elif esc == 1:
        print('Empate')
    elif esc == 2:
        print('Computador venceu')
elif computador == 2:
    if esc == 0:
        print('Computador Venceu')
    elif esc == 1:
        print('Jogador venceu')
    elif esc == 2:
        print('Empate')
'''
while esc != computador:
    print('Você perdeu')
    break
if esc == computador:
    print('Você ganhou')
