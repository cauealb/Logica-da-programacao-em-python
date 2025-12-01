# Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N números inteiros
# e armazene-os em um vetor. Em seguida, mostrar na tela todos os números negativos lidos. 

n = int(input('Digite quantas voltas: '))
vetor = []


for i in range(6):
    num = int(input('Digite um número: '))
    vetor.append(num)

print('\nNumeros Negativos')
for i in vetor:
    if i < 0:
        print(i)