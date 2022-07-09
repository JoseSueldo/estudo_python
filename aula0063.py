r = 's'
total = []
pares = []
while r =='s':
    n = int(input('Informe um numero : '))
    total.append(n)
    if n %2 == 0:
        pares.append(n)
    r = str(input('Deseja continuar [S/N] ? '))
menorT = min(total)
media = 