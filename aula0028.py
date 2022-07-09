'''Faça um programa que leia a largura e o comprimento de um terreno
retangular, calculando e mostrando a sua área em m². O programa também
devemostrar a classificação desse terreno, de acordo com a lista abaixo:
 - Abaixo de 100m² = TERRENO POPULAR
 - Entre 100m² e 500m² = TERRENO MASTER
 - Acima de 500m² = TERRENO VIP
'''

larg = int(input('Informe a largura do terreno : '))
comp = int(input('Informe o comprimento do terreno : '))
area = (larg*comp) / 2
if area < 100:
    print('Terreno Popular')
    print(f'O terreno tem {area}m²')
elif area < 500:
    print('Terreno Master')
    print(f'O terreno tem {area}m²')
else:
    print('Terreno VIP')
    print(f'O terreno tem {area}m²')