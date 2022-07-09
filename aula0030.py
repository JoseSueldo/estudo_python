'''
 [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
 - EQUILÁTERO: todos os lados iguais
 - ISÓSCELES: dois lados iguais
 - ESCALENO: todos os lados diferentes
'''

r1 = int(input('Informe o comprimento de A :'))
r2 = int(input('Informe o comprimento de B :'))
r3=  int(input('Informe o comprimento de C :'))
if r3 < r2 + r1 and r2 < r3 + r1 and r1 < r2 + r3:
    print('Podem formar um triangulo !')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não podem formar um triangulo!')