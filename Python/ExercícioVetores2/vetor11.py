# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores: $200 - $299 $300 - $399 $400 - $499 $500 - $599 $600 - $699 $700 - $799 $800 - $899 $900 - $999 $1000 em diante Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

vt200299 = []
vt300399 = []
vt400499 = []
vt500599 = []
vt600699 = []
vt700799 = []
vt800899 = []
vt9001000 = []
vt1000m = []
vt = []
vtc = []
while True:
    n = int(input('Quantas vendas brutas o vendedor fez: '))

    if n < 0:
        break
    else:
        conta = (n * 0.09) + 200
        vt.append(conta)

for i in vt:
    if i >= 200 and i <= 299:
        vt200299.append(1)
    elif i <= 399:
        vt300399.append(1)
    elif i <= 499:
        vt400499.append(1)
    elif i <= 599:
        vt500599.append(1)
    elif i <= 699:
        vt600699.append(1)
    elif i <= 799:
        vt700799.append(1)
    elif i <= 899:
        vt800899.append(1)
    elif i <= 999:
        vt9001000.append(1)
    else:
        vt1000m.append(1)

print('\nTabela\n'
      f'Vendedores com 200 a 299 de vendas: {len(vt200299)}\n'
      f'Vendedores com 300 a 399 de vendas: {len(vt300399)}\n'
      f'Vendedores com 400 a 499 de vendas: {len(vt400499)}\n'
      f'Vendedores com 500 a 599 de vendas: {len(vt500599)}\n'
      f'Vendedores com 600 a 699 de vendas: {len(vt600699)}\n'
      f'Vendedores com 700 a 799 de vendas: {len(vt700799)}\n'
      f'Vendedores com 800 a 899 de vendas: {len(vt800899)}\n'
      f'Vendedores com 900 a 999 de vendas: {len(vt9001000)}\n'
      f'Vendedores com mais de 1000 vendas: {len(vt1000m)}\n'
      )
