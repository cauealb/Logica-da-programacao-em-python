# Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula de Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais, conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem. 

# Restrições: A não pode ser zero e delta não pode ser negativo


import math

a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))

delta = (b **2) - 4 * a * c
print(delta)

if a == 0 or delta < 0:
    print('Está equacão não possui raizes reais')
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'X1: {x1:.4f}')
    print(f'X2: {x2:.4f}')
