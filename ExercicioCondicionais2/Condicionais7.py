# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

# Minha Resposta
num = float(input('Digite um número: '))

arrendoda = round(num)

if arrendoda != num:
    print('É um número decimal.')
elif arrendoda == num:
    print('É um número inteiro.')



# Resposta
numero = float(input("Digite um número: "))
if numero % 1 == 0:
    print("Inteiro")
else:
    print("Decimal")