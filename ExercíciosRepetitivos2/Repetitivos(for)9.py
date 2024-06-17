#  Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

for i in range(1, 50 + 1):
    conta = i % 2

    if conta != 0:
        print(i)