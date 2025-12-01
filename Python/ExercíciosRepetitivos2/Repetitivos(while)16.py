# Faça um programa que leia uma quantidade indeterminada de números positivos e
# conte quantos deles estão nos seguintes intervalos:
# [0-25], [26-50], [51-75] e [76-100].

# A entrada de dados deverá terminar quando for lido um número negativo.

gp025 = 0
gp2650 = 0
gp5175 = 0
gp76100 = 0

while True:
    num = int(input('Digite um número(ou um número negativo para parar): '))

    if num < 0:
        break
    else:
        if num <= 25:
            gp025 += 1
        elif num <= 50:
            gp2650 += 1
        elif num <= 75:
            gp5175 += 1
        else:
            gp76100 += 1

print(f'Grupo dos 25 menos: {gp025 - 1}\n'
      f'Grupo dos 26 a 50: {gp2650}\n'
      f'Grupo dos 51 a 75: {gp5175}\n'
      f'Grupo dos 76 a 100: {gp76100}\n'
      )

# Resposta
range1 = 0
range2 = 0
range3 = 0
range4 = 0

while True:
    numero = int(
        input("Digite um numero inteiro de 0 a 100 (ou negativo para parar): ")
    )
    if numero < 0:
        break
    if numero <= 25:
        range1 += 1
    elif numero <= 50:
        range2 += 1
    elif numero <= 75:
        range3 += 1
    elif numero <= 100:
        range4 += 1
    else:
        print("Número inválido!")

print("Dos numeros digitados: ")
print(f"{range1} foram de [0-25]")
print(f"{range2} foram de [26-50]")
print(f"{range3} foram de [51-75]")
print(f"{range4} foram de [76-100]")