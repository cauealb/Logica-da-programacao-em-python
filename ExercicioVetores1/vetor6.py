# Faça um programa para ler dois vetores A e B, contendo N elementos cada. Em seguida, gere um
# terceiro vetor C onde cada elemento de C é a soma dos elementos correspondentes de A e B. Imprima
# o vetor C gerado. 

n = int(input('Digite quantas voltas: '))
vetorA = []
vetorB = []

for i in range(1, n + 1):
    numA = int(input('Digite os valores do vetor A: '))
    vetorA.append(numA)
for i in range(1, n + 1):
    numB = int(input('Digite os valores do vetor B: '))
    vetorB.append(numB)

vetorC = []

for _ in range(n):
    indiceA = vetorA[_]
    indiceB = vetorB[_]
    conta = indiceA + indiceB
    vetorC.append(conta)

for i in vetorC:
    print(i)

