# Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

pessoas = int(input('Digte quantas pessoas tem na sala de aula: '))
total = 0
contador = 0

for i in range(1, pessoas + 1):
    num = int(input(f'Digite a idade da pessoa {i}: '))
    total += num
    contador += 1

media = total / contador

if media < 25:
    print('É uma turma Jovem!')
elif media < 60:
    print('É uma turma Adulta!')
else:
    print('É uma turma Idosa!')



# Resposta

numero_de_pessoas = int(input("Digite o numero de pessoas: "))
media = 0

# + 1 pois a contagem está iniciando em 1, e não em 0 (o padrão)
for i in range(1, numero_de_pessoas + 1):
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    media = ((media * (i - 1)) + idade) / i

if media < 26:
    print("A turma é jovem")
elif media < 60:
    print("A turma é adulta")
else:
    print("A turma é idosa")