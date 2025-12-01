# Faça um Programa que peça as quatro notas de 4 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

total = 0
media = []
media7 = []
for u in range(1, 5):
    print(f'Digite as 4 notas do {u}º Aluno: ')
    for i in range(1, 5):
        n = float(input(f'Digite sua a nota {i}: '))
        total += n

    conta = total / 4

    if conta >= 7.0:
        media7.append(u)
        total = 0

print('Médias maiores que 7:\n')
for i in media7:
    print(i)


# Resposta

ALUNOS = 10
NOTAS = 4

medias = []
media_sete = 0

for i in range(ALUNOS):
    media = 0
    for j in range(NOTAS):
        media += float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
    media /= NOTAS
    medias.append(media)
    if media >= 7:
        media_sete += 1

print("\nA média dos alunos foi:")
for i in range(ALUNOS):
    print(f"Aluno {i+1}: {medias[i]}")

print(f"\n{media_sete} alunos tiveram média maior ou igual a 7.")