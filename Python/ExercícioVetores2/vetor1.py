# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = []
for i in range(1, 11):
    n = float(input('Digite um valor para o vetor: '))
    vetor.append(n)

vetor.reverse()

for i in vetor:
    print(i)


# Resposta

numeros = []
for i in range(10):
    numeros.append(float(input(f"Digite o {i+1}º numero real: ")))
print("Os numeros inversos são: ", end="")
for numero in numeros[::-1]:
    print(f" {numero}", end="")