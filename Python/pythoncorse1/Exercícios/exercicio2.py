# Crie um programa que receba 5 notas de um aluno, calcule a média dessas notas e exiba se o aluno foi aprovado ou reprovado. Considere que a média para aprovação é 7.0.

# Pseudocódigo: media = 0
# input n1,n2,n3,n4,n5
# media = (n1 + n2 + n3 + n4 + n5) / 5
# if resultado < 7:
# print reprovado!
# elif resultado >= 7:
# print aprovado!

media = 0
n1 = int(input('Qual sua nota no 1º Bimestre: '))
n2 = int(input('Qual sua nota no 2º Bimestre: '))
n3 = int(input('Qual sua nota no 3º Bimestre: '))
n4 = int(input('Qual sua nota no 4º Bimestre: '))
n5 = int(input('Qual sua nota no 5º Bimestre: '))

media = (n1 + n2 + n3 + n4 + n5) / 5

if media < 7:
    print('Reprovado!!')
    print('Sua média: ', + media)
elif media >= 7:
    print('Aprovado!!')
    print('Sua média: ', + media)
