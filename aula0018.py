ano = int(input('Informe em que ano você nasceu : '))
calc = 2022 - ano
if calc > 18:
    print(f'Você tem {calc} anos, precisa se alistar')
else:
    print('Ainda não está na hora!')