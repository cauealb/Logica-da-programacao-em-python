# Ler uma matriz quadrada de ordem N (máximo = 10), contendo números reais. Em seguida, fazer as
# seguintes ações:
# a) calcular e imprimir a soma de todos os elementos positivos da matriz.
# b) fazer a leitura do índice de uma linha da matriz e, daí, imprimir todos os elementos desta linha.
# c) fazer a leitura do índice de uma coluna da matriz e, daí, imprimir todos os elementos desta coluna.
# d) imprimir os elementos da diagonal principal da matriz.
# e) alterar a matriz elevando ao quadrado todos os números negativos da mesma. Em seguida imprimir
# a matriz alterada. 

o =int(input('Qual a ordem da matriz: '))
matriz = [[0 for _ in range(o)] for _ in range(o)]
totalP = 0
vetorqb = []
vetorqc = []
vetordiag = []

for l in range(o):
    for c in range(o):
        num = float(input(f'Elemento [{l},{c}]: '))
        matriz[l][c] = num
        
        #Soma dos positivos
        if num >= 0:
            totalP += num

print(f'\nSoma dos Positivos: {totalP}\n')





qb = int(input('Escolha uma linha: '))

for l in range(o):
    for c in range(o):
        if l == qb:
            valor = matriz[l][c]
            vetorqb.append(valor)

print('Linha escolhida: ', end='')
for i in vetorqb:
    print(i, end=' ')





qc = int(input('\nEscolha uma coluna: '))
for l in range(o):
    for c in range(o):
        if c == qc:
            valor = matriz[l][c]
            vetorqc.append(valor)

print('Linha escolhida: ', end='')
for i in vetorqc:
    print(i, end=' ')






print('\nLinha diagonal: ', end='')
for l in range(o):
    for c in range(o):
        if l == c:
            valor = matriz[l][c]
            vetordiag.append(valor)

print('\nDiagonal Principal\n')
for i in vetordiag:
    print(i, end=' ')


print('\nMatriz Alterada:\n')

for l in range(o):
    for c in range(o):
        if matriz[l][c] < 0:
            valor = matriz[l][c]
            del matriz[l][c]
            conta = valor ** 2
            matriz[l].insert(c, conta)

for l in range(o):
    for c in range(o):
        print(c, end='')
    print('\n')

