# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido. Exemplo: 12376489 => 98467321

while True:
    n = int(input('Digite um número: '))
    n = str(n)
    reverte = n[::-1]
    print(reverte)



# Resposta

numero = input("Digite um inteiro positivo: ")
numero = numero[::-1]
print(f"=> {numero}")