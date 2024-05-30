# Escreva um programa que verifique se uma palavra fornecida pelo usuário é um palíndromo.

# 1. Uma string
# 2. Preciso inverter a string e ver se ela é um políndromo.
# 3. Tem que ser uma palavra
# 4. A confirmação de que aquela palavra é um políndromo.

aceito = False

while aceito == False:

    palavra = input('Digite sua palavra: ')

    if not isinstance (palavra, str):
        print('Digite uma PALAVRA!')
    elif isinstance(palavra, str):
        aceito = True

polindromo = palavra[::-1]

if polindromo == palavra:
    print('Essa palavra é um políndromo!')
else:
    print('Essa palavra não é um políndromo!')
    