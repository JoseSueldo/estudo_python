sexo = []

sexoM = []

sexoF = []

peso = []

pesoF = []

pesoM = []

p100 = []

for i in range(1, 9):

    s = str(input('Informe o seu sexo : '))

    sexo.append(s)

    if s == 'f':

        print('Feminino')

        sexoF.append(s)

        p = float(input('Informe o seu peso : '))

        pesoF.append(p)

        peso.append(p)

    elif s == 'm':

        print('Masculino')

        sexoM.append(s)

        p = float(input('Informe o seu peso : '))

        pesoM.append(p)

        peso.append(p)

        if p > 99:
            p100.append(p)

    else:

        print('Informção invalida')

media = sum(pesoF) / len(sexoF)

print('Mulheres que foram cadastradas : ', len(sexoF))

print('Homens que pesam mais de 100KG : ', len(p100))

print(f'A media do peso entre as mulheres são de : {media} KG')

print('O maior peso entre os homenes é : ', max(pesoM))