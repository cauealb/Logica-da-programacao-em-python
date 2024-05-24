# Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

# 1. Três valores inteiros diferentes
# 2. Imprimir na tela os valores em ordem decrescente
# 3. Três valores inteiros diferentes
# 4. Receber o uma lista em ordem decrescente


import random

valor1 = random.randint(1,15)
valor2 = random.randint(1,15)
valor3 = random.randint(1,15)

listanumeros = valor1, valor2, valor3

lista = []
aceito = False

# valor1 = int(input('Digite o primeiro número: '))
# valor2 = int(input('Digite o segundo número: '))
# valor3 = int(input('Digite o terceiro número: '))

for num in listanumeros:
    if valor1 < valor2 and valor1 < valor3:
        lista.append(valor1)
        
    else:
        if valor2 < valor1 and valor2 < valor3:
            lista.append(valor2)
            continue
        else:
            valor3 < valor1 and valor3 < valor2
            lista.append(valor3)
    
    

    
print(lista)
print(valor1, valor2, valor3)





