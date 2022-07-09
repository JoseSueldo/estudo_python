ano = int(input('Informe o ano para saber se ele é bixesto ou não : '))
if ano % 100 != 0 and ano % 4 == 0 or ano  % 400 == 0:
    print('É um ano bixesto !')
else:
    print('Não é bixesto!')
