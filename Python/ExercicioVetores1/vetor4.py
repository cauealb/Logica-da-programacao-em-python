# Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na
# tela todos os números pares, e também a quantidade de números pares. 

n = int(input("Digite quantas voltas: "))
vetor = []

for i in range(1, n + 1):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        vetor.append(num)

print('\nNúmeros Pares: ')
for i in vetor:
    print(f' {i}', end='')

print(f'\nQuantidade de números: {len(vetor)}')