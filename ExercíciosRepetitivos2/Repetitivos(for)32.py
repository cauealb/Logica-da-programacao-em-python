# Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.

n = int(input('Digite o número N: '))
total = 0

nn = 1
mm = 1

print('S = ', end='')

for i in range(1, n + 1):
    print(f' {nn}/{mm}', end='')
    total += nn / mm
    nn += 1
    mm += 2

print(f'\nSoma: {total:.2f}')



# Resposta

soma = 0
n = int(input("Digite n: "))
m = 1
print("S = ", end="")
for i in range(1, n + 1):
    print(f"{i}/{m}", end="")
    if i < n and n > 1:
        print(" + ", end="")
    else:
        print(".")
    soma += i / m
    m += 2
print(f"A soma da série deu {soma:.2f}")