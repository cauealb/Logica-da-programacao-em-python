# Fazer um programa para ler dois números inteiros, e dizer se um número é múltiplo do outro. Os números podem ser digitados em qualquer ordem. 

n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))

if n1 % n2 == 0 or n2 % n1 == 0:
    print('São multiplos!')
else:
    print('Não são multiplos!')

    