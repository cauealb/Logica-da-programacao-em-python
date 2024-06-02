# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

# Minha Resposta
ano = int(input('Digite o ano: '))

if ano % 4 == 0:
    print('Ele é um ano Bisexto!')
else:
    print('Não é um ano Bisexto!')


# Resposta

ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    print(f"{ano} é bissexto!")
else:
    print(f"{ano} não é bissexto!")