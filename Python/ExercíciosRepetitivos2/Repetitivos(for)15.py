# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.


listaPar = []
listaImpar = []

for i in range(1, 11):
    num = int(input('Digite um número: '))

    if num % 2 == 0: #Par
        listaPar.append(num)
    else: #Impar
        listaImpar.append(num)

print(
    f'\nPares: {len(listaPar)}\n'
    f'\nImpares: {len(listaImpar)}\n'
)

