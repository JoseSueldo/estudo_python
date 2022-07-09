n1 = float(input('Informe sua primeira nota : '))
n2 = float(input('Informe sua segunda nota : '))
calc = (n1+n2) / 2
if calc > 7:
    print(f'Você tirou {calc} foi aprovado!!!')
else:
    print(f'Você tirou {calc} não foi aprovado!!!')