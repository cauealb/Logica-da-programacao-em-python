# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

# Minha resposta
num = int(input('Digite um número: '))
lista0 = []
lista1 = []

for i in range(1, 11):
    if num % i == 0:
        lista0.append(i)
    else:
        lista1.append(i)

if len(lista0) <= 2:
    print(f'{num} é primo.\n'
          f'Ele é divisivel por {lista0} \n'
          f'Ele não é divisivel por {lista1} \n'
          )
else:
    print(f'{num} é composto. \n'
          f'Ele é divisivel por {lista0} \n'
          f'Ele não é divisivel por {lista1} \n'
          )


# Resposta

numero = int(input("Digite um numero inteiro: "))
primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        print(f"{numero} não é primo! É divisível por {i}.")
if primo:
    print(f"{numero} é primo!")


# Notação Big O
# 