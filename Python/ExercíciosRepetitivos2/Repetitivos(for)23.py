# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.

# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.

# # Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

from collections import Counter

n = int(input('Digite um número: '))
lista1 = []
lista0 = []

for ii in range(1, n):
    for i in range(1, 11):
        if ii % i == 0:
            lista0.append(ii)
        else:
            lista1.append(ii)

formatar = Counter(lista0)
aux = [num for num, count in formatar.items() if count == 2]

listaUm = []
listaZero = []

for u in range(1, n):
    if n % u == 0:
        listaZero.append(n)
    else:
        listaUm.append(n)


if len(listaZero) <= 2:
    print(f'{n} é primo e foi calculados {len(aux)} divisõe(s) antes do mesmo.')
else:
    print(f'{n} é composto e foi calculados {len(aux) + 1} divisõe(s) antes do mesmo.')




# Resposta

numero = int(input("Digite um numero inteiro: "))
if numero == 1 or numero == 2:
    print(
        f"{numero} é primo e foram executadas 0 divisões para descobrir isso"
    )
elif numero % 2 == 0:
    print(
        f"{numero} não é primo e foi executada uma divisão para descobrir isso"
    )
else:
    contador = 1
    primo = True
    for i in range(3, numero, 2):
        contador += 1
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(
            f"{numero} é primo e foram executadas"
            f" {contador} divisões para descobrir isso"
        )
    else:
        print(
            f"{numero} não é primo e foram executadas"
            f" {contador} divisões para descobrir isso"
        )