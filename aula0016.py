t = int(input('Quantos cigarros você fuma por dia : '))
anos = int(input('A quantos anos você fuma : '))
calc = anos * 365 * t * 10
calc2 = calc / (24*60)
print(f'Redução de tempo de {calc:.2f} minutos de vida')