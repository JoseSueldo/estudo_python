c = 0
lista_idade = []

lista_m = []
idadeM = []

lista_f = []
idadeF=[]
idadem20 = []
while c < 3:
    sexo = str(input('Informe seu sexo (M) para masculino e (F) para feminino : '))
    if sexo == 'm':
        print('Masculino')
        idade = int(input('Informe sua idade : '))
        idadeM.append(idade)
        lista_idade.append(idade)
        lista_m.append(sexo)
    elif sexo == 'f':
        lista_f.append(sexo)
        print('Feminino')
        idade = int(input('Informe sua idade : '))
        if idade > 20:
            idadem20.append(idade)
        else:
            idadeF.append(idade)
            lista_idade.append(idade)
    c = c + 1
print('')
soma_idade = sum(lista_idade)
soma_idadem = sum(idadeM)
calc = soma_idade / 2
calcm = soma_idadem / 2

#print(soma_idade)
print(f'A média das idades do grupo é de: {calc}')
print(f'Foram cadastrados {len(lista_m)}, homens')
print(f'Foram cadastradas {len(lista_f)}, mulheres')
print(f'O número de mulheres com 20 anos que foi cadastrada é de: ({len(idadem20)})')