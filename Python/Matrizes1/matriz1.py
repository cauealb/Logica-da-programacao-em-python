# Fazer um programa para ler um número inteiro N (máximo = 10) e uma matriz quadrada de ordem N
# contendo números inteiros. Em seguida, mostrar a diagonal principal e a quantidade de valores
# negativos da matriz. 
n = int(input('Digite a ordem da matriz: '))
contMenos = 0
matriz = [[0 for _ in range(n)] for _ in range(n)]

for l in range(n):
    for c in range(n):
        vl = int(input(f'Elemento [{l}, {c}]: '))
        matriz[l][c] = vl
        if vl < 0:
            contMenos += 1

print('Diagonal Principal: \n')
for ml in range(n):
    for mc in range(n):
        if ml == mc:
            print(f'[{matriz[ml] [mc]}]', end='')


print(f'\nQuantidade de Negativos: {contMenos}')

#Nootação Big O
# O (n^2)
