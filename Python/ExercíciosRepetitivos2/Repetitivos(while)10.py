# Faça um programa que calcule o mostre a média aritmética de N notas.

# Minha resposta
total = 0
contador = 0

while True:
    num = int(input('Digite uma nota(digite 0 para parar): '))
    total += num

    if num == 0:
        break
    else:
        contador += 1

media = total / contador

print(
    f'A média dessas notas são: {media}'
)


# Resposta

notas = 0
contador = 0
continuar = "S"
while continuar == "S":
    nota = float(input("Digite uma nota: "))
    notas += nota
    contador += 1
    continuar = input("Deseja continuar? (S/N): ").upper()

print(f"A média das notas é {notas/contador:.2f}.")