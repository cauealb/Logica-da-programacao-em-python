# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

nz = int(input('Digite seu N-ésima: '))
x = 0

for i in range(1, nz + 1):
    print(i)
    x += i

# Não terminado