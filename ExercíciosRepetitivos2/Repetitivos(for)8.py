# Faça um programa que leia 5 números e informe a soma e a média dos números.
total = 0

for i in range(1, 5 + 1):
    num = int(input('Digite um número: '))
    total += num
media = total / i

print(
    f'A soma desses números: {total} \n'
    f'A média desses números: {media}'
)

