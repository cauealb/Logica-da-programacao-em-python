# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

# Minha Resposta
num = int(input('Digite um número para sua Fatorial: '))
total = 1

for i in range(num, 0, -1):
    total *= i
print(f'Fatorial: {total}')


# Resposta
numero = int(input("Digite um numero: "))
fatorial = 1
for i in range(numero, 1, -1):
    fatorial *= i
print(f"O fatorial de {numero} é {fatorial}")