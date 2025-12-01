# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

n = int(input('Digite o valor de N: '))
total = 0
mm = 1
nn = 1

print('H = ', end='')
for i in range(1, n + 1):
    print(f'{mm}/{nn} +', end=' ')
    total += mm / nn
    nn += 1

print(f'\nTOTAL: {total:.2f}')



h = 0
for i in range(1, int(input("Digite o numero de termos: ")) + 1):
    h += 1 / i

print(f"H = {h}")