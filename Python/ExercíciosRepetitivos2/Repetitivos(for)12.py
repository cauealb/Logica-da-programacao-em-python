# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
# inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada.
# A saída deve ser conforme o exemplo abaixo:
#     Tabuada de 5:
#     5 X 1 = 5
#     5 X 2 = 10
#     ...
#     5 X 10 = 50

num = int(input('Digite um número para a tabuada: '))
while num < 1 or num > 10:
    num = int(input('Valor inválido! Digite novamente: '))

print(f'\nTabuada do {num}:\n')
for i in range(1, 11):
    print(num, ' x ', i, " = ", (num * i))



# Resposta

numero = int(input("Digite um numero de 1 a 10: "))
for i in range(1, 11):
    print(f"{numero} X {i} = {numero * i}")