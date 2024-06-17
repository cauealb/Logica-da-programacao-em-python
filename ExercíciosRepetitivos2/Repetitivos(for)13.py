# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

# Minha Resposta (for)
base = int(input('Digite a Base: '))
expoente = int(input('Digite o Expoente: '))
total = 1

for i in range(1, expoente + 1):
    total *= base
print(f'Total: {total}')

# Minha resposta (while)

base = int(input('Digite a Base: '))
expoente = int(input('Digite o Expoente: '))
contador = 0
total = 1

parar = True
while parar == True:
    if contador != expoente:
        total *= base
        contador += 1
    else:
        parar = False
print(f'Tota: {total}')



# Resposta

base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
numero = 1
for _ in range(expoente):
    numero *= base
print(f"{base} elevado a {expoente} é {numero}")