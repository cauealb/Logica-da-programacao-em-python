# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo. a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.

# 1. Fornecer 2 números inteiros e 1 número real
# 2. Calcular o produto do dobro do primeiro com metade do segundo, e em seguida, a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.
# 3. São 2 números inteiros e 1 número real.
# 4. o produto do dobro do primeiro com metade do segundo, e em seguida, a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.

# Minha resposta
int1 = int(input("Qual é o Primeiro número inteiro: "))
int2 = int(input("Qual é o Segundo número inteiro: "))

real1 = float(input('Qual o número real: '))

produto = (int1 * 2) * (int2 / 2)
soma = (int1 * 3) + (real1 ** 3)

print(produto)
print(soma)


# Resposta

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))
num3 = float(input("Digite um numero real: "))
a = (num1 * 2) * (num2 / 2)
b = (num1 * 3) + num3
c = num3 ** 3

print(f"a: {a}\nb: {b}\nc: {c}")