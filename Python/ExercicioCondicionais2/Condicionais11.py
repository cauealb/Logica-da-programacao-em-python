# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
# ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.

# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# Minha Resposta
qtdMorango = int(input('Digite as quantidades de Morangos: '))
qtdMacas = int(input('Digite as quantidades de Maçãs: '))

if qtdMorango <= 5:
    qtdMorangoPrecos = qtdMorango * 2.5
else:
    qtdMorangoPrecos = qtdMorango * 2.2

if qtdMacas <= 5:
    qtdMacasPrecos = qtdMacas * 1.8
else:
    qtdMacasPrecos = qtdMacas * 1.5

total = qtdMorangoPrecos + qtdMacasPrecos

if (qtdMorango + qtdMacas) > 8 or (qtdMorangoPrecos + qtdMacasPrecos) > 25:
    desconto = total - (total * 0.10)
    print(f'Valor a pagar: {desconto:.2f}')
else:
    print(f'Valor a pagar: {total:.2f}')



# Minha Resposta
morango = float(input("Digite quantos quilos de morango foram comprados: "))
maca = float(input("Digite quantos quilos de maçã foram comprados: "))
valor = 0

if morango <= 5:
    valor += morango * 2.5
else:
    valor += morango * 2.2
if maca <= 5:
    valor += maca * 1.8
else:
    valor += maca * 1.5

if (morango + maca) > 8 or valor > 25:
    valor -= valor * 10 / 100

print(f"O valor a ser pago é R${valor:.2f}")