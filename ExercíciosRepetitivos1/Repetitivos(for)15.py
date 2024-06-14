# Fazer um programa para ler um número natural N (valor máximo: 15), e depois calcular e mostrar o fatorial de N.

n = int(input('Digite o valor de N: '))
total = 1


if n == 0:
    print('FATORIAL: 1')

elif n > 15:
    print('O valor não pode ser maior que 15.')
else:
    for i in range(n, 0, -1):
        total *= i

        if i == 1:
            print(f'FATORIAL: {total}')