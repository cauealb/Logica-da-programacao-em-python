# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida, mostrar na tela
# o maior número do vetor (supor não haver empates). Mostrar também a posição do maior elemento,
# considerando a primeira posição como 0 (zero). 

maior = cont = 0

n = int(input('Digite quantas voltas: '))
vetor = []

for i in range(1, n + 1):
    num = float(input('Digite um numero: '))
    vetor.append(num)

for i in vetor:
    if i > maior:
        maior = i
        indice = vetor.index(maior)

print(f'Maior valor: {maior}\n'
      f'Posição: {indice}')