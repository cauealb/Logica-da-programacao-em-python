# crie um algoritmo que leia os valores de a, b e c. Em seguida, imprima na tela: Se a é maior que b e c juntos;
# Se a é igual à soma de b e c;
# Se a é menor que a média de b e c.

# 1. a, b, c junto com seus valores
# 1. ver Se a é maior que b e c juntos, ver Se a é igual à soma de b e c, ver Se a é menor que a média de b e c.
# 3. Três dados, Três valores
# 4. ver Se a é maior que b e c juntos, ver Se a é igual à soma de b e c, ver Se a é menor que a média de b e c.

a = int(input('Valor de a: '))
b = int(input('Valor de b: '))
c = int(input('Valor de c: '))

média = (b + c) / 2

if a > (b + c):
    print('[a] é maior que a soma de [b] e [c]')
else:
    print('[a] é menor que a soma de [b] e [c]')

if a == (b + c):
    print('[a] é igual que a soma de [b] e [c]')
else:
    print('[a] não é igual que a soma de [b] e [c]')

if a > média:
    print('[a] é maior que a média de [b] e [c]')
else:
    print('[a] não é maior que a média de [b] e [c]')
