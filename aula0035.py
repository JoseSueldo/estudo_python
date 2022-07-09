'''
Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O
aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para
carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e
quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
tabela a seguir:
 - Carros populares (aluguel de R$90 por dia)
 - Até 100Km percorridos: R$0,20 por Km
 - Acima de 100Km percorridos: R$0,10 por Km


 - Carros de luxo (aluguel de R$150 por dia)
 - Até 200Km percorridos: R$0,30 por Km
 - Acima de 200Km percorridos: R$0,25 por Km
'''

print('''
[1] - Polular
[2] - Luxo''')
carro = int(input('Informe o carro :'))
dias = int(input('Informe quantos dias você ficou com o carro :'))
km = int(input('Quantos km você rodou :'))
if carro == 1:
    print('Popular')
    calc = dias * 90
    if km < 100:
        km = km * 0.20
    elif km > 100:
        km = km * 0.10
    print(f'Você vai pagar R${calc:.2f} pelos dias. e R${km:.2f} pelos Km rodados ')
elif carro ==2:
    print('Luxo')
    calc = dias * 150
    if km <= 200:
        km = km * 0.30
    elif km >200:
        km = km * 0.25
    print(f'Você vai pagar R${calc:.2f} pelos dias. e R${km:.2f} pelos Km rodados')