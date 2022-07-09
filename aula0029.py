'''
Desenvolva um programa que leia o nome de um funcionário, seu salário,
quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
acordo com a tabela a seguir:
 - Até 3 anos de empresa: aumento de 3%
 - entre 3 e 10 anos: aumento de 12.5%
 - 10 anos ou mais: aumento de 20%
'''

nome = str(input('Informe seu nome : '))
sal = float(input('Informe seu salario:  '))
anos = int(input('Quantos anos você trabalha na empresa: '))
if anos <= 3 :
    calc = (sal / 100) * 3
    novo_sal = calc + sal
    print(f'Você vai ter um aumento de 3% (R$ {calc:.2f})')
    print(f'Seu novo salario é de : R${novo_sal:.2f}')
elif anos <=10:
    calc = (sal / 100) * 12.5
    novo_sal = calc + sal
    print(f'Você vai ter um aumento de 12.5% (R$  ({calc:.2f})')
    print(f'Seu novo salario é de : R$({novo_sal:.2f})')
else:
    calc = (sal /100) * 20
    novo_sal = calc + sal
    print(f'Você vai ter um aumento de 20% (R$ ({calc:.2f})')
    print(f'Seu novo salario é de : R$ ({novo_sal:.2f})')