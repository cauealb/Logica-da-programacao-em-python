# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vt1 = []
vt2 = []
vt3 = []

for i in range(1, 11):
    num = int(input(f'Entre com o {i}º número inteiro para o vetor 1: '))
    vt1.append(num)
for i in range(1, 11):
    num = int(input(f'Entre com o {i}º número inteiro para o vetor 2: '))
    vt2.append(num)
for i in range(1, 11):
    num = int(input(f'Entre com o {i}º número inteiro para o vetor 3: '))
    vt3.append(num)

vt4 = []
for _ in range(9):
    vt4.append(vt1[_])
    vt4.append(vt2[_])
    vt4.append(vt3[_])

print('O vetor com os elementos intercalados dos vetores 1, 2 e 3 é: ')

for i in vt4:
    print(i, end=' ')