# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vt1 = [1,1,1,1,1,1]
vt2 = [2,2,2,2,2,2]

for i in range(1, 11):
    num = int(input('Digite um número para o vetor 1: '))
    vt1.append(num)
for i in range(1, 11):
    num = int(input('Digite um número para o vetor 2: '))
    vt2.append(num)

vt3 = []
for _ in range(9):
    vt3.append(vt1[_])
    vt3.append(vt2[_])

print('O vetor com os elementos intercalados dos vetores 1 e 2 é:\n')

for i in vt3:
    print(i, end=' ')



# Resposta
ELEMENTOS = 10
vetor1 = []
vetor2 = []
vetor3 = []
for i in range(ELEMENTOS):
    vetor1.append(
        int(input(f"Entre com o {i+1}º número inteiro para o vetor 1: "))
    )
for i in range(ELEMENTOS):
    vetor2.append(
        int(input(f"Entre com o {i+1}º número inteiro para o vetor 2: "))
    )
for i in range(ELEMENTOS):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print("O vetor com os elementos intercalados dos vetores 1 e 2 é: ")
for i in range(ELEMENTOS * 2):
    print(vetor3[i], end=" ")

