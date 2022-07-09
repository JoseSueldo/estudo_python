c = 0
lista_altura = []
lista_peso = []

peso90 = []
peso100 = []
peso50 = []

alt160 = []
alt190 = []

while c < 2:
    altura = float(input('Infome a sua altura : '))
    lista_altura.append(altura)
    if altura < 1.60:
        alt160.append(altura)
    elif altura > 1.90:
        alt190.append(altura)
    peso = float(input('Informe o seu peso: '))
    lista_peso.append(peso)
    if peso > 90:
        peso90.append(peso)
        if peso > 100:
            peso100.append(peso)
    elif peso < 50:
        peso50.append(peso)
    c = c+1
soma = sum(lista_peso)
calc = soma / 2
print(f'A media de peso no grupo é de :({calc})')
print(f'({len(peso90)}) pesam mais de 90.0 kg')
print(f'({len(peso50)}) pesam menos de 50 kg e ({len(alt160)}) tem menos de 1.60 de altura')
print(f'({len(alt190)}) medem mais de 1.90 e ({len(peso100)}) tem mais de 100 kg')



