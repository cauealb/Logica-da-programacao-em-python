# Fazer um programa para ler dois números inteiros M e N (máximo = 10). Em seguida, ler uma matriz
# de M linhas e N colunas contendo números reais. Gerar um vetor de modo que cada elemento do vetor
# seja a soma dos elementos da linha correspondente da matriz. Mostrar o vetor gerado. 

n = int(input('Qual a quantidade de linhas da matriz: '))
m = int(input('Qual a quantidade de colunas da matriz: '))
matriz = [[0 for _ in range(m)] for _ in range(n)]
vetor = []



for nl in range(n):
    total = 0
    linha = 1
    for nc in range(m):
        vt = float(input(f'Digite os elementos da {linha}a. linha: '))
        matriz[nl][nc] = vt
        total += vt
    vetor.append(total)

for i in vetor:
    print(i)