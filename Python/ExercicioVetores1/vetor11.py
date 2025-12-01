# Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. Fazer um programa
# que calcule e escreva a maior e a menor altura do grupo, a média de altura das mulheres, e o número
# de homens. 

from math import inf
n = int(input('Digite quantas voltas: '))
vetorAl = []
vetorH = []
maior = total = cont = 0
menor = inf

for i in range(1, n + 1):
    altura = float(input(f'Altura da {i}º Pessoa: '))
    genero = input(f'Gênero da {i}º Pessoa: ')
    vetorAl.append(altura)
    if genero == 'M' or genero == 'm':
        vetorH.append(genero)
    else:
        cont += 1
        total += altura

media = total / cont

# Maior
for i in vetorAl:
    if i > maior:
        maior = i
for i in vetorAl:
    if i < menor:
        menor = i

print('DADOS:\n'
      f'Menor Altura: {menor}\n'
      f'Maior Altura: {maior}\n'
      f'Média das alturas da Mulheres: {media:.2f}\n'
      f'Quantos Homens: {len(vetorH)}\n'
      )
