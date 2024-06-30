# Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na
# tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos,
# bem como os nomes dessas pessoas caso houver. 

nome16v = []
idadesv = []
totalAl = cont16 = 0
n = int(input('Digite quantas voltas: '))

for i in range(1, n + 1):
    print(f'\nDados da {i}º pessoa: \n')
    nome = input('Nome: ')
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))

    totalAl += altura
    if idade < 16:
        cont16 += 1
        idadesv.append(nome)

por = (cont16 / n) * 100
media = totalAl / n

print(f'\nAltura média: {media:.2f}\n'
      f'Pessoas com menos de 16 anos: {por}%'
)

for i in idadesv:
    print(i)