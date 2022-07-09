c = 0
idade = []
while c != 999:
    idd = int(input('Informe sua idade : '))
    if idd == 999:
        print('ERROR')
        break
    idade.append(idd)
soma_idade = sum(idade)
media = soma_idade / len(idade)
print(f'({len(idade)}) de alunos na turma')
print(f'({media}) é a media da idade do grupo')