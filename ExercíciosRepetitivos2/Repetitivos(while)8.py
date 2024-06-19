# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

total = 0
lista = []

parar = True


while parar == True:
    num = int(input('Digite um número, para parar, digite "0": '))

    while num < 0 or num > 1000:
        num = int(input('Número inválido! Digite novamente: '))
        if num > 0 and num < 1000:
            break

    if num == 0:
        parar = False
        break
    else:
        total += num
        lista.append(num)


for i in lista:
    if parar == False:
        menor = i
        parar = True
    if i <= menor:
        menor = i

for i in lista:
    if parar == True:
        maior = i
        parar = False
    if i >= maior:
        maior = i

print(
    f'O Maior: {maior}\n'
    f'O Menor: {menor}\n'
    f'Total dos números: {total}\n'

)



# Resposta

from math import inf  # Constante 'infinito'

# Para resolver com um laço é necessário utilizar uma lista
numeros = []

while True:
    valor = input(
        "Digite um número entre 0 e 1000 "
        "ou 'p' para parar e exibir os resultados: "
    )
    if valor.upper() == "P":
        break
    valor = float(valor)
    if 0 <= valor <= 1000:
        numeros.append(valor)

menor_numero = inf
for numero in numeros:
    if numero < menor_numero:
        menor_numero = numero
print(f"O menor número é {menor_numero}")

maior_numero = -inf
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero
print(f"O maior número é {maior_numero}")

soma = 0
for numero in numeros:
    soma += numero
print(f"A soma dos números é {soma}")