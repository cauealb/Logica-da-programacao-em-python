# Desenvolver um programa para verificar a nota do aluno em uma prova com 10
# questões, o programa deve perguntar ao aluno a resposta de cada questão e ao
# final comparar com o gabarito da prova e assim calcular o total de acertos e a
# nota (atribuir 1 ponto por resposta certa).

# Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno
# vai utilizar o sistema.

# Após todos os alunos terem respondido informar:
#     Maior e Menor Acerto;
#     Total de Alunos que utilizaram o sistema;
#     A Média das Notas da Turma.
#     Gabarito da Prova:
#         01 - A
#         02 - B
#         03 - C
#         04 - D
#         05 - E
#         06 - E
#         07 - D
#         08 - C
#         09 - B
#         10 - A

# Após concluir isto você poderia incrementar o programa permitindo que o
# professor digite o gabarito da prova antes dos alunos usarem o programa.

# PRIMEIRO CÓDIGO
from math import inf

# Mostrado a nota do aluno
totalNota = 0

# Parametro para ver quantos alunos usaram o sistema e fazer a média
contador = total = media =0

# Parametro usado para ver a maior e a menor nota
menor = inf
maior = 0
aux = True

while not aux == False:
        contador += 1
        for i in range(1, 11):
            nota = input(f'Digite a resposta da questão {i}: ')

            match i:
                case 1:
                    if nota == 'A':
                        totalNota += 1
                case 2:
                    if nota == 'B':
                        totalNota += 1
                case 3:
                    if nota == 'C':
                        totalNota += 1
                case 4:
                    if nota == 'D':
                        totalNota += 1
                case 5:
                    if nota == 'E':
                        totalNota += 1
                case 6:
                    if nota == 'E':
                        totalNota += 1
                case 7:
                    if nota == 'D':
                        totalNota += 1
                case 8:
                    if nota == 'C':
                        totalNota += 1
                case 9:
                    if nota == 'B':
                        totalNota += 1
                case 10:
                    if nota == 'A':
                        totalNota += 1

        total += totalNota

        if totalNota >= maior:
            maior = totalNota
        if totalNota <= menor:
            menor = totalNota

        aux = input('Outro aluno vai usar esse sistema (S/N): ')
        if aux == 'N':
            break
        else:
            totalNota = 0
            aux = True

media = total / contador

print(f'\nA média das notas são: {media}\n'
      f'{contador} aluno(s) usarão o sistema.\n'
      f'A maior nota foi de {maior} ponto(s)\n'
      f'A menor nota foi de {menor} ponto(s)\n'
)
