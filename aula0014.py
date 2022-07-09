km = int(input('Quantos km você rodou : '))
dias = int(input('Quantos dias você ficou com o carro : '))
calc = dias * 90
calc2 = km * 0.20
total = calc + calc2
print(f'Você ficou {dias} com o carro o valor é : {calc:.2f} R$')
print(f'Você rodou {km}km com o carro o valor é : {calc2:.2f} R$')
print(f'Você vai pagar {total:.2f} R$')