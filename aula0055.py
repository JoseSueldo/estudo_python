import random
c = 0
computer = random.randint(1, 5)
j = int(input('De 1 a 5 qual número o computador escolheu : '))
if j!= computer:
    print('Você perdeu!')
    while c < 4:
        computer = random.randint(1,5)
        j = int(input('Escolha um numero de 1 a 5 :'))
        if j != computer:
            print('Você perdeu')
        elif j == computer:
            print('Você ganhou')
            break
        c += 1
elif j ==computer:
    print('Você ganhou')