c = 0
idade = []
idade21 = []
r = 's'
while r == 's':
    v = int(input('Qual a sua idade : '))
    idade.append(v)
    if v > 20:
        idade21.append(v)
    r = str(input('Deseja continuar [S/N] ?'))
print('...')
i = len(idade)
v_i = sum(idade)
media = v_i / i
rep = idade.count(21)
i20 = len(idade21)
print(f'Temos na lista {i} idades informadas')
print(f'A media das idades digitas é de : {media}')
print(f'Tem {i20} pessoas com 21  anos ou mais na lista')
