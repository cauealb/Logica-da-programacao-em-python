# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

# Minha Resposta
turmas = int(input('Digite quantas turmas: '))
total = 0

for i in range(1, turmas + 1):
    num = int(input(f'Digite quantos alunos na turma {i}: '))
    while num > 40:
        num = int(input('Turmas não podem ter mais de 40 alunos! Digite novamente: '))

    total += num
media = total / turmas

print(f'A média por cada turma será de: {media}')



# Resposta

turmas = int(input("Digite quantas turmas tem: "))
media = 0
for i in range(turmas):
    while True:
        alunos = int(input(f"Digite quantos alunos tem na turma {i + 1}: "))
        if alunos <= 40:
            break
    media = ((media * i) + alunos) / (i + 1)
print(f"A media de alunos por turma é {media}")