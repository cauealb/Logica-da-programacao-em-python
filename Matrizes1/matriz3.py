# Ler dois números M e N (máximo = 10), e depois ler uma matriz MxN de números inteiros, conforme
# exemplo. Em seguida, mostrar na tela somente os números negativos da matriz. 

n = int(input('Qual a quantidade de linhas da matriz: '))
m = int(input('Qual a quantidade de colunas da matriz: '))
matriz = [[0 for _ in range(m)] for _ in range(n)]

