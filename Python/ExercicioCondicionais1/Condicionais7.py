# No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir. Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual foi a maior. 

arremesso1 = float(input('Qual foi a primeira distância: '))
arremesso2 = float(input('Qual foi a segunda distância: '))
arremesso3 = float(input('Qual foi a terceira distância: '))

if arremesso1 > arremesso2 and arremesso1 > arremesso3:
    print(arremesso1)
elif arremesso2 > arremesso1 and arremesso2 > arremesso3:
    print(arremesso2)
elif arremesso3 > arremesso1 and arremesso3 > arremesso2:
    print(arremesso3)
