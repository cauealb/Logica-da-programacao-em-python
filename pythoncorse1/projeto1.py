# Crie um programa que recebe um número e imprima o fatorial deste número

# Pseudocódigo:
# input v1
# fatorial = 1
# resultado = v1
# while fatorial <= v1
# reusultado = v1 * fatorial
# fatorial = fatorial + 1
# print(resultado)


v1 = int(input('Qual valor desejado? '))
fatorial = 1
resultado = 1

for numero in range(1, v1 + 1):
    if numero <= v1:
        print(v1 * numero)
        resultado *= numero
print(resultado)
