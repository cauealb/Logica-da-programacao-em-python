# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
# ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.

# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.


qtdMorango = int(input('Quantidades de Kilos: '))
qtdMacas = int(input('Quantidades de Kilos: '))


if qtdMorango <= 5:
    resultadoMo = qtdMorango * 2.5

else:
    resultadoMo = qtdMorango * 2.2

if qtdMacas <= 5:
    resultadoMa = qtdMacas * 1.8

else:
    resultadoMa = qtdMacas * 2.5

soma = resultadoMo + resultadoMa


if (qtdMacas + qtdMorango) > 8 or (resultadoMo + resultadoMa) > 25:
    print('Parabéns, Você ganhou um desconto!!! \n')
    desconto = soma - ((resultadoMo + resultadoMa) * 0.10)
    print(f'Valor a pagar: {desconto:.2f}')
else:
    print(f'Valor a pagar: {soma:.2f}')


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