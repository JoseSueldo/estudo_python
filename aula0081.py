idades = []

vezes = []

pos = []

c = 0

while c < 8:

    idade = int(input('Informe sua idade : '))

    idades.append(idade)

    if idade > 25:
        vezes.append(idade)

        m = idades.index(25)

        pos.append(m)

    c += 1

c == 8

media = sum(idades) / len(idades)

maior_idade = max(idades)

print(f'A media das idades é de : {media:.0f} anos')

print(f'As posições que se encontras as idades de 25 anos são de : {pos} ')

print(f'A Maior idade digitada é :{maior_idade}')