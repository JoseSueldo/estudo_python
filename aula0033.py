'''
Escreva um programa para aprovar ou não o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
salario  = float(input('Informe o seu salario R$ : '))
valordacasa = float(input('informe o valor da casa R$ :'))
anos = int(input('Em quantos anos você vai pagar : '))
calc = (salario / 100) * 30
prestação = valordacasa / anos
if prestação > calc:
    print('Emprestimo Negado')
elif prestação < calc:
    print('Empréstimo Aprovado')
