# Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# No final da série de saltos de cada atleta, o melhor e o pior resultados são
# eliminados.

# O seu resultado fica sendo a média dos três valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
# pelo atleta em seus saltos e depois informe a média dos saltos conforme a
# descrição acima informada (retirar o melhor e o pior salto e depois
# calcular a média).

# Faça uso de uma lista para armazenar os saltos.
# Os saltos são informados na ordem da execução, portanto não são ordenados.
# O programa deve ser encerrado quando não for informado o nome do atleta.
# A saída do programa deve ser conforme o exemplo abaixo:
#     Atleta: Rodrigo Curvêllo

#     Primeiro Salto: 6.5 m
#     Segundo Salto: 6.1 m
#     Terceiro Salto: 6.2 m
#     Quarto Salto: 5.4 m
#     Quinto Salto: 5.3 m

#     Melhor salto:  6.5 m
#     Pior salto: 5.3 m
#     Média dos demais saltos: 5.9 m

#     Resultado final:
#     Rodrigo Curvêllo: 5.9 m

from math import inf

total = 0
lista = []
valorMax = 0
valorMin = inf
cont = 0

while True:
    
    atleta = input('Nome do Atleta: ')
    
    if atleta == '':
        break

    else:
        nome = atleta
        for i in range(1, 6):
            
            salto = float(input(f'Digite o salto {i}: '))

            if salto != '':
                lista.append(salto)
            else:
                break

valorMax = max(lista)
valorMin = min(lista)

listaNova = [x for x in lista if x != valorMax and x != valorMin]


for i in listaNova:
    total += i
    cont += 1

media = total / cont

print(f'Melhor salto: {valorMax} m\n'
      f'Pior salto: {valorMin} m\n'
      f'Média: {media:.1f} m\n'
)

print(f'\nResultado final:\n'
      f'{nome}: {media:.1f} m'

)


# Notação Big O
# O (n)

