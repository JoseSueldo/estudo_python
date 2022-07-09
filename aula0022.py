ano = int(input('Infomre no seu ano de nascimento : '))
calc = 2022 - ano
if calc < 18:
    calc2 = calc - 18
    print(f'Você tem {calc} anos e faltam {calc2} para você se alistar!!!')
elif calc == 18:
    calc2 = calc == 18
    print(f'Você tem {calc2} anos, já está na hora de você se alistar')
elif calc == 18:
    calc2 = calc - 18
    print(f'Você tem {calc} anos já era para você ter se alistado a {calc2} anos')