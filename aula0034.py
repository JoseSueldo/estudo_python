'''

O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no
peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o
indivíduo dentro de certas faixas.
 - abaixo de 18.5: Abaixo do peso
 - entre 18.5 e 25: Peso ideal
 - entre 25 e 30: Sobrepeso
 - entre 30 e 40: Obesidade
 - acima de 40: Obseidade mórbida
Obs: O IMC é calculado pela expressão peso/altura² (peso dividido pelo quadrado
da altura)
'''

alt = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso:  '))
calc1 = alt * alt
calc2 = peso / calc1
if calc2 < 18.5:
    print('Abaixo do peso')
elif calc2 >18.5 and calc2 <25:
    print('Peso Ideal')
elif calc2 > 25 and calc2 <30:
    print('Sobrepeso')
elif calc2 > 30 and calc2 <40 :
    print('Obesidade')
elif calc2 > 40:
    print('Obesidade Mórbida')

