# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

parar = True
total = 0
media = 0
n1 = float(input('Digite sua primeira nota: '))

while parar == True:

    if n1 < 0.10 or n1 > 10:
        n1 = float(input('Valor Inválido! Tente Novamente: '))
    else:
        parar = False
        total += n1
        media += 1


n2 = float(input('Digite sua segunda nota: '))

while parar == False:

    if n2 < 0.10 or n2 > 10:
        n2 = float(input('Valor Inválido! Tente Novamente: '))
    else:
        parar = True
        total += n2
        media += 1


media = total / media
print(f'MÉDIA: {media:.2f}')

 
