# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

total = 0
num = []
for i in range(1, 11):
    n = int(input('Digite o 1º numero inteiro: '))
    conta = n ** 2
    num.append(conta)
for i in num:
    total += i

print(f'A soma dos quadrados desses números será de: {total}')


# Resposta

soma_dos_quadrados = 0
for i in range(10):
    soma_dos_quadrados += int(input(f"Digite o {i+1}º numero inteiro: ")) ** 2
print(f"A soma dos quadrados dos numeros digitados é {soma_dos_quadrados}")
