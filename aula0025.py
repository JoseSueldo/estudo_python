'''[DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta.
Analise seus comprimentos e diga se é possível formar um triângulo com essas
retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento
de cada lado deve ser menor que a soma dos outros dois.
'''

r1 = int(input('Informe o comprimento de A :'))
r2 = int(input('Informe o comprimento de B :'))
r3=  int(input('Informe o comprimento de C :'))
if r3 < r2 + r1 and r2 < r3 + r1 and r1 < r2 + r3:
    print('Podem formar um triangulo !')
else:
    print('Não podem formar um triangulo!')