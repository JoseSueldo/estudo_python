'''
Um programa de vida saudável quer dar pontos atividades físicas que podem
ser trocados por dinheiro. O sistema funciona assim:
 - Cada hora de atividade física no mês vale pontos
 - até 10h de atividade no mês: ganha 2 pontos por hora
 - de 10h até 20h de atividade no mês: ganha 5 pontos por hora
 - acima de 20h de atividade no mês: ganha 10 pontos por hora
 - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos)
'''

horas = int(input('Quantas horas você faz atividade fisica por dia :'))
if horas <= 10:
    calc = horas * 2
    pontos = calc * 0.05
    print(f'Você fez {calc} pontos e tem R${pontos:.2f} em dinheiro')
elif horas > 10 and horas < 20:
    calc = horas * 5
    pontos = calc * 0.05
    print(f'Você fez {calc} pontos e tem R$ {pontos:.2f} em dinheiro')
elif horas > 20:
    calc = horas * 10
    pontos = calc * 0.05
    print(f'Você fez {calc} pontos e tem R${pontos:.2f} em dinheiro')
