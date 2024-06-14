# Escreva um algoritmo que leia dois números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível, mostre a mensagem “DIVISAO IMPOSSIVEL”. 

n = int(input('Quantos casos voce vai digitar: '))

for i in range(1, n + 1):
    numerador = int(input('Entre com o numerador: '))
    denominador = int(input('Entre com o denominador: '))

    if denominador == 0:
        print('DIVISÃO IMPOSSÍVEL!')
    else:
         conta = numerador / denominador

         print(f'DIVISÃO: {conta:.2f}')