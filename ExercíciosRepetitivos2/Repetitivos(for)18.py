# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

# Minha Resposta
num = int(input('Digite um número: '))
lista0 = []
lista1 = []

for i in range(1, 11):
    if num % i == 0:
        lista0.append(num)
    else:
        lista1.append(num)

if len(lista0) <= 2:
    print(f'{num} é um número primo.')
else:
    print(f'{num} é um número composto.')


# Resposta

numero = int(input("Digite um numero inteiro: "))
primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        print(f"{numero} não é primo!")
        break
if primo:
    print(f"{numero} é primo!")


# Notação Big O
# O(1) 