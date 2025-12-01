# Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
# A melhor e a pior nota são eliminadas.
# A sua nota fica sendo a média dos votos restantes.

# Você deve fazer um programa que receba o nome do ginasta e as notas dos sete
# jurados alcançadas pelo atleta em sua apresentação e depois informe a sua
# média, conforme a descrição acima informada (retirar o melhor e o pior salto e
# depois calcular a média com as notas restantes).

# As notas não são informados ordenadas.
# Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
#     Atleta: Aparecido Parente
#     Nota: 9.9
#     Nota: 7.5
#     Nota: 9.5
#     Nota: 8.5
#     Nota: 9.0
#     Nota: 8.5
#     Nota: 9.7

#     Resultado final:
#     Atleta: Aparecido Parente
#     Melhor nota: 9.9
#     Pior nota: 7.5
#     Média: 9,04

lista = []
totalSemMax = totalSemMin = total = 0

atleta = input('Atleta: ')
for y in range(1, 8):
    nota = float(input(f'NOTA {y}: '))

    while nota <= 0:
        nota = float(input('Nota menor ou igual a 0! Digite novamente: '))

    lista.append(nota)

max = max(lista)
min = min(lista)
listaNova = [x for x in lista if x != max and x != min]

for i in listaNova:
    total += i

media = total / len(listaNova)

print('\nResultado Final:\n')

print(f'Atleta: {atleta}\n'
      f'Melhor nota: {max}\n'
      f'Pior nota: {min}\n'
      f'Média: {media:.1f}\n'
)