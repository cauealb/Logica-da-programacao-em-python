# Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence (Q1, Q2, Q3 ou Q4). O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma). 

parar = True

while parar == True:
    x = int(input('Digite o valor da coordenadas X: '))
    y = int(input('Digite o valor da coordenadas Y: '))

    if x == 0 or y == 0:
        parar = False
    else:
        if y > 0 and x > 0:
            print('Quadrante Q1')
        elif y > 0 and x < 0:
            print('Quadrante Q2')
        elif y < 0 and x < 0:
            print('Quadrante Q3')
        else:
            print('Quadrante Q4')
