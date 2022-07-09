genero = str(input('''Informe seu gênero 
[M] - Masculino
[F] - Feminino
'''))
if genero == 'm':
    print('Masculino')
    nome = str(input('Digite seu nome : '))
    sal = float(input('Qual seu salario atual : '))
    anos = int(input('Quantos meses você trabalha na empresa : '))
    calc = anos /12
    if calc < 20 :
        print(f'Você trabalha a {calc} na empresa')
        porc = sal * 3 / 100
        total = porc + sal
        print(f'Você vai ganha de aumento : R$ {porc} ')
        print(f'Seu novo salario é de : R$ {total}')
    elif calc > 20 and calc <= 30:
        print(f'Você trabalha a {calc} na empresa')
        porc = sal * 13 /100
        total = porc + sal
        print(f'Você vai ganhar de aumento : R${porc}')
        print(f'Seu novo salario é de : R${total}')
    else:
        print(f'Você trabalha a {calc} na empresa')
        porc = sal * 30 / 100
        total = porc + sal
        print(f'Você vai ganhar de aumento : R${porc}')
        print(f'Seu novo salario é de : R${total}')

elif genero == 'f':
    print('FEMININO')
    nome = str(input('Digite seu nome: '))
    sal = float(input('Informe seu salario:'))
    anos = int(input('A quantos meses você trabalha na empresa '))
    calc = anos / 12
    if calc < 15:
        print(f'Você trabalha a {calc} na empresa')
        porc = sal * 5 / 100
        total = porc + sal
        print(f'Você vai ganhar de aumento : R${porc}')
        print(f'Seu novo salario é de : R${total}')
    elif calc > 15 and calc <= 30:
        print(f'Você trabalha {calc} na empresa')
        porc = sal *  12 / 100
        total = porc + sal
        print(f'Você vai ganhar de aumento : R${porc}')
        print(f'Seu novo salario é de : R${total}')
    else:
        print(f'Você trabalha a {calc} na empresa')
        porc = sal * 23 / 100
        total = porc + sal
        print(f'Você vai ganhar de aumento : R${porc}')
        print(f'Seu novo salario é de : R${total}')