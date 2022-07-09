km = int(input('Informe quantos km você deseja percorrer : '))
if km  <= 200:
    calc = km* 0.50
    print(f'Você quer percorrer {km}km vai custar {calc:.2f} R$')
elif km > 200:
    calc = km * 0.45
    print(f'Você quer pecorrer {km}km vai custar {calc:.2f} R$')