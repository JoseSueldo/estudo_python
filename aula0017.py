vel = int(input('Informe a velocidade que você estava : '))
if vel > 60:
    multa = (vel - 60) * 5
    print(f'Você passou do limite e vai pagar de multa : R${multa:.2f} ')
else:
    print('Continue assim!!!')