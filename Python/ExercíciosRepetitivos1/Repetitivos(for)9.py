# Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números impares entre eles.

x = int(input('Digite o número de X: '))
y = int(input('Digite o número de Y: '))
soma = 0

if x < y:
    for i in range(x + 1, y - 1):
        if not i % 2 == 0:
            soma += i
else:
    for i in range(y + 1, x):
        if not i % 2 == 0:
            soma += i

print(f'SOMA: {soma}')