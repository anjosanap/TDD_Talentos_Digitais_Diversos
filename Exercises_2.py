print('Números pares entre 0 e 1000')
number = 0
for number in range(0, 1001):
    if number % 2 == 0:
        print(number, end=' ')
