# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

vtAl =[]
vtId = []
vtc = []
totalAl = 0

for i in range(1, 6):
    id = int(input(f'Digite a idade do {i}º aluno: '))
    vtId.append(id)
    al = float(input(f'Digite a altura do {i}º aluno: '))
    vtAl.append(al)
    totalAl += al
media = totalAl / 5

for i in vtAl:
    if i < media:
        vtc.append(1)


print(f'{len(vtc)} aluno(s) com mais de 13 anos e média inferior as alturas.')




# Resposta

"""
Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem
altura inferior à média de altura desses alunos.
"""
ALUNOS = 30
idades = []
alturas = []
media_de_altura = 0
abaixo_da_media = 0

for i in range(ALUNOS):
    idades.append(int(input(f"Digite a idade do aluno {i+1}: ")))
    altura = int(input(f"Digite a altura em cm do aluno {i+1}: "))
    alturas.append(altura)
    media_de_altura += altura

media_de_altura /= ALUNOS

for i in range(ALUNOS):
    if idades[i] > 13:
        if alturas[i] < media_de_altura:
            abaixo_da_media += 1

print(
    f"{abaixo_da_media} alunos com mais de 13 anos têm altura abaixo da média"
)