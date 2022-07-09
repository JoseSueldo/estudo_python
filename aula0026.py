'''
Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
na tela uma das mensagens abaixo:
 - O primeiro valor é o maior
 - O segundo valor é o maior
 - Não existe valor maior, os dois são iguais
'''

n1 = int(input('Informe o 1° valor: '))
n2 = int(input('Informe o 2° valor: '))
if n1 > n2:
    print(f'O valor : {n1} é maior')
    print(f'O valor : {n2} é menor')
elif n2 > n1:
    print(f'O valor : {n2} é maior')
    print(f'O valor : {n1} é menor')
else:
    print(f'Os valores : {n1} e {n2} são iguais')