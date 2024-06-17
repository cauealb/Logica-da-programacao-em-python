# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.


# Minha Resposta
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 < n2:
    for i in range(n1 + 1, n2):
        print(i)
else:
    for i in range(n2 + 1, n1):
        print(i)


# Resposta
primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite um numero: "))
for i in range(primeiro_numero + 1, segundo_numero):
    print(i)