c =  's'
lista_sal = []
salM = []
salF = []

lista_sexo = []
sexoM = []
sexoF = []

while c  == 's':
    sexo = str(input('Infome seu sexo [M/F]: '))
    if sexo == 'f':
        lista_sexo.append(sexo)
        sexoF.append(sexo)
        sal = float(input('Informe seu salário: '))
        lista_sal.append(sal)
        salF.append(sal)
    elif sexo == 'm' :
        lista_sexo.append(sexo)
        sexoM.append(sexo)
        sal = float(input('Informe o seu salario : '))
        lista_sal.append(sal)
        salM.append(sal)
    c = str(input('Deseja continuar : '))
salf = sum(salF)
salm = sum(salM)
print(f'O total de salario pagos aos homens são de (R$ {salm:.2f}) ')
print(f'O total de salario pagos as mulheres são de (R$ {salf:.2f}) ')