# Dado uma lista de números fornecida pelo usuário, o programa deve encontrar o maior e o menor elemento presente na lista. Isso deve ser feito sem usar funções predefinidas em Python, como max() e min(). Em vez disso, você precisará percorrer a lista e comparar cada elemento com o maior e o menor valor encontrados até o momento.

# 1. Uma lista de números
# 2. Achar o maior e o menor número dessa lista
# 3. Isso deve ser feito sem usar funções predefinidas em Python
# 4. Achar o maior e o menor número dessa lista

# lista_maior = []
# atual = num
# if atual >= num
#   lista_maior.append(atual)

import random

numerosAleatorois1 = random.randint(1,100)
numerosAleatorois2 = random.randint(1,100)
numerosAleatorois3 = random.randint(1,100)
numerosAleatorois4 = random.randint(1,100)
numerosAleatorois5 = random.randint(1,100)
numerosAleatorois6 = random.randint(1,100)
numerosAleatorois7 = random.randint(1,100)

lista = [4 , 5, 6 , 768 , 53 , 46 , 5 , 768 , 57]

lista_maior = []
# lista = [numerosAleatorois1, numerosAleatorois2, numerosAleatorois3, numerosAleatorois4, numerosAleatorois5, numerosAleatorois6, numerosAleatorois7]

for num in lista:
    if num > 0 and num < 1:
        atual = num