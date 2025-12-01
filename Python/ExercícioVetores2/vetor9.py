# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

vtT = []
total = 0
for i in range(1, 13):
    temp = float(input(f'Digite a temperatura no mês {i}: '))
    vtT.append(temp)

for i in vtT:
    total += i
media = total / 12

for i in vtT:
    if i > media:
        indice = vtT.index(i)
        match indice:
            case 0:
                print('1 - Janeiro ', end=' ')
            case 1:
                print('2 - Fevereiro ', end=' ')
            case 2:
                print('3 - Março ', end=' ')
            case 3:
                print('3 - Abril ', end=' ')
            case 4:
                print('4 - Maio ', end=' ')
            case 5:
                print('5 - Junho ', end=' ')
            case 6:
                print('6 - Julho ', end=' ')
            case 7:
                print('7 - Agosto ', end=' ')
            case 8:
                print('8 - Setembro ', end=' ')
            case 9:
                print('9 - Outubro ', end=' ')
            case 10:
                print('10 - Novembro ', end=' ')
            case 11:
                print('11 - Dezembro ', end=' ')