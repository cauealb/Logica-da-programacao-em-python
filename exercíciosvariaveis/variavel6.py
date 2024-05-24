# Dado uma lista de números fornecida pelo usuário, o programa deve encontrar o maior e o menor elemento presente na lista. Isso deve ser feito sem usar funções predefinidas em Python, como max() e min(). Em vez disso, você precisará percorrer a lista e comparar cada elemento com o maior e o menor valor encontrados até o momento.

# 1. Uma lista de números
# 2. Achar o maior e o menor número dessa lista
# 3. Isso deve ser feito sem usar funções predefinidas em Python
# 4. Achar o maior e o menor número dessa lista

# lista_maior = []
# maior = num
# if maior >= num
#   lista_maior.append(maior)

import random

numerosAleatorois1 = random.randint(1,15)
numerosAleatorois2 = random.randint(1,15)
numerosAleatorois3 = random.randint(1,15)
numerosAleatorois4 = random.randint(1,15)
numerosAleatorois5 = random.randint(1,15)
numerosAleatorois6 = random.randint(1,15)
numerosAleatorois7 = random.randint(1,15)

# lista = [5,4,76,8,4,5,47,7,6,4,7,6,2,]

lista = [numerosAleatorois1, numerosAleatorois2, numerosAleatorois3, numerosAleatorois4, numerosAleatorois5, numerosAleatorois6, numerosAleatorois7]

maior = 0
menor = 1000000000000000000000000000000000000000000000000000000000000000000
stop = True

for num in lista:
    if stop == True: 
        maior = num  
        stop = False 
    if maior < num:
        maior = num

for num in lista:
    if stop == True: 
        menor = num  
        stop = False
    if menor > num:
        menor = num  

print('O maior número de uma lista é ', maior,' e o menor é ', menor)
