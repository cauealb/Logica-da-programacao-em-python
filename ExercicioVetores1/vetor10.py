# Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas que eles tiraram
# no 1º e 2º semestres. Cada uma dessas informações deve ser armazenada em um vetor. Depois, imprimir
# os nomes dos alunos aprovados, considerando aprovados aqueles cuja média das notas seja maior ou
# igual a 6.0 (seis). 

n = int(input('Digite quantas voltas: '))
vetorAprovados = []


for i in range(1, n + 1):
    print(f'\nDados da {i}º pessoa: \n')
    nome = input('Nome: ')
    Ps = float(input('Nota do 1º Semestre: '))
    Ss = float(input('Nota do 2º Semestre: '))
    media = (Ps + Ss) / 2

    if media >= 6.0:
        vetorAprovados.append(nome)

print('Aprovados: ')
for i in vetorAprovados:
    print(i)