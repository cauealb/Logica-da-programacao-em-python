# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).


# Minha resposta
num = int(input('Digite um número: '))

conta = num % 2

if conta >= 1:
    print(f'{num:.0f} é impar.')
elif conta == 0:
    print(f'{num:.0f} é par.')


# Resposta

numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")
