# Ler um inteiro N e uma matriz quadrada de ordem N (máximo = 10). Mostrar qual o maior elemento
# de cada linha. Suponha não haver empates. 

n = int(input('Qual a ordem da matriz: '))
maior = 0
vetor = []
vetorMaiores = []

for nl in range(n):
    vetor.clear()
    maior = 0
    for nc in range(n):
        vt = int(input(f'Elemento [{nl}, {nc}]: '))
        vetor.append(vt)

    for i in vetor:
        if i > maior:
            maior = i
    vetorMaiores.append(maior)

for i in vetorMaiores:
    print(i)
