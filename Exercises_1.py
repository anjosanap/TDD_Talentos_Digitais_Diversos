number = float(input('Digite um número para saber se é par ou impar:'))
rest = number % 2

if rest == 0:
    print('Número é par')
else:
    print('Número é impar')
