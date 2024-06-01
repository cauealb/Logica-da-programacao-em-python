# Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados 
# com quatro casas decimais): 
# a) a área do quadrado que tem lado A 
# b) a área do triângulo retângulo que base A e altura B 
# c) a área do trapézio que tem bases A e B, e altura C

a = float(input('Medida de A: '))
b = float(input('Medida de B: '))
c = float(input('Medida de C: '))

ponto1 = a * a
ponto2 = (a * b) / 2
ponto3 = (a + b) * c / 2

print(
    f'AREA DO QUADRADO = {ponto1:.4f} \n' 
    f'AREA DO TRIANGULO = {ponto2:.4f} \n'
    f'AREA DO TRAPEZIO = {ponto3:.4f} \n' 
)
