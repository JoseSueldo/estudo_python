lista_idade = []
idadeM =[]
idadeF =[]

lista_sexo = []
sexoM = []
sexoF = []
c = 's'
while c == 's':
    sexo = str(input('Informe seu sexo : '))
    if sexo == 'f':
        lista_sexo.append(sexo)
        sexoF.append(sexo)
        idade = int(input('Informe sua idade : '))
        lista_idade.append(idade)
        idadeF.append(idade)
    elif sexo == 'm':
        lista_sexo.append(sexo)
        sexoM.append(sexo)
        idade = int(input('Informe sua idade : '))
        lista_idade.append(idade)
        idadeM.append(idade)
    c = str(input('Deseja continuar : '))
maior_id = max(lista_idade)
menor_id = min(idadeF)
idm = sum(lista_idade)
media = idm / len(lista_idade)
print(f'A maior idade é {maior_id} anos')
print(f'Foram cadastrados ({len(sexoM)}) homens')
print(f'A idade da mulher mais jovem é de : ({menor_id}) anos')
print(f'A media das idades é de {media}')