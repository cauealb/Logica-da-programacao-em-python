# Leia um valor inteiro N. Este valor será a quantidade de números inteiros que serão lidos em seguida. Para cada valor lido, mostre uma mensagem dizendo se este valor lido é PAR ou IMPAR, e também se é POSITIVO ou NEGATIVO. No caso do valor ser igual a zero (0), seu programa deverá imprimir apenas NULO. 

n = int(input('Quantos numeros voce vai digitar: '))

for i in range(1, n + 1):
    num = int(input('Digite um numero: '))

    if num == 0:
        print('NULO. \n')
    else:
        if num % 2 == 0:
            if num < 0:
                print('Par e Negativo. \n')
            else:
                print('Par e Positivo. \n')
        else:
            if num > 0:
                print('Ímpar Positivo. \n')
            else:
                print('Ímpar Negativo. \n')
