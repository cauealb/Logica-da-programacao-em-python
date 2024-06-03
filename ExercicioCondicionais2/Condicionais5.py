# Faça um Programa para um caixa eletrônico.

# O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas.

# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.

# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor = int(input('Valor do Saque: '))

if valor < 10 and valor > 600:
    print('Valor não suportado!!')

# Separação
uni = valor % 10
deze = (valor // 10) % 10 * 10
cente = (valor // 100) * 100

# if valor < 100:
# # Centena
#     if cente > 100:
#         cente = cente / 100
#         print(f'{cente:.0f} notas de 100')
#     else:
#         cente = cente / 100
#         print(f'{cente:.0f} nota de 100')


# Dezena
if deze > 50:
    resto = deze - 50
    deze = deze / deze
    print(f'{deze:.0f} notas de 50, {resto:.0f} notas de 10')
elif deze == 10:
    print(f'{deze:.0f} nota de 50')
