nome = str(input('Informe seu nome : '))
sexo = str(input('Informe seu sexo [M/F] :'))
if sexo == 'm':
    print(f'Seja bem vindo {nome}')
    compra = float(input('Informe o valor das compras : '))
    calc = (compra * 5) / 100
    calc2 = compra - calc
    print(f'O valor das compras são : {compra:.2f} R$ você vai ganhar um desconto de:{calc:.2f} R$ você vai pagar apenas {calc2:.2f} R$')
elif sexo == 'f':
    print(f'Seja bem vinda {nome}')
    compra = float(input('Informe o valor das compras : '))
    calc = (compra * 13)/100
    calc2 = compra - calc
    print(f'O valor das compras são : {compra:.2f} R$ você vai ganhar um desconto de: {calc:.2f} R$ você vai pagar apenas {calc2:.2f} R$')
elif sexo != 'f' or sexo != 'm':
    print('Error!!!')