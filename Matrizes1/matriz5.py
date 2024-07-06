# Fazer um programa para ler duas matrizes de números inteiros A e B, contendo de M linhas e N colunas
# cada (M e N máximo = 10). Depois, gerar uma terceira matriz C onde cada elemento desta é a soma
# dos elementos correspondentes das matrizes originais. Imprimir na tela a matriz gerada. 


n = int(input('Quantas linhas vai ter cada matriz: '))
m = int(input('Quantas colunas vai ter cada matriz: '))

matriz1 = [[0 for _ in range(m)] for _ in range(n)]
matriz2 = [[0 for _ in range(m)] for _ in range(n)]

print('Digite os valores da matriz A')
for ml in range(n):
    for mc in range(m):
        num = int(input(f'Elemento Matriz A [{ml},{mc}]: '))
        matriz1[ml][mc] = num
print('Digite os valores da matriz B') 
for ml in range(n):
    for mc in range(m):
        num = int(input(f'Elemento Matriz B [{ml},{mc}]: '))
        matriz2[ml][mc] = num

matriz3 = [[0 for _ in range(m)] for _ in range(n)]
for l in range(n):
    for c in range(m):
        matriz3[l][c] = matriz1[l][c] + matriz2[l][c]

for ml in range(n):
    for mc in range(m):
        print(f'{matriz3[ml][mc]}', end=' ')
    print()

