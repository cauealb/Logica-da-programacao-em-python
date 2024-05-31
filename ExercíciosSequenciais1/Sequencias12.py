# Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos.

import math

base  = float(input('Base: '))
altura = float(input('Altura: '))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = base ** 2 + altura ** 2
diagonal = math.sqrt(diagonal)

print(
    f'Área: {area:.4f} \n'
    f'Perimêtro: {perimetro:.4f} \n'
    f'Diagonal: {diagonal:.4f}'
)