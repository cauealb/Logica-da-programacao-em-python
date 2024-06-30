# Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. Os nomes
# devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome
# da pessoa mais velha.

n = int(input('Digite quantas voltas: '))
vetorNome = []
vetorIdades = []
maior = 0

for i in range(1, n + 1):
    print(f'\nDados da {i}º pessoa: \n')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    vetorNome.append(nome)
    vetorIdades.append(idade)

    if idade > maior:
        maior = idade
        name = nome

print(f'Mais Velho: {name} com {maior} anos.')
