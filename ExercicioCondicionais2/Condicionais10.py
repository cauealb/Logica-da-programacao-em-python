# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#     Álcool:
#         até 20 litros, desconto de 3% por litro
#         acima de 20 litros, desconto de 5% por litro
#     Gasolina:
#         até 20 litros, desconto de 4% por litro
#         acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
# litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

# Minha resposta
tipo = input('Qual combustível: ')
litro = int(input('Quantos litros: '))

if tipo == 'G' or tipo == 'g':

    if litro <= 20:
        total = litro * 2.5
        desconto = total - (total * 0.04)
    else:
        total = litro * 2.5
        desconto = total - (total * 0.06)

if tipo == 'A' or tipo == 'a':

    if litro <= 20:
        total = litro * 1.9
        desconto = total - (total * 0.03)
    else:
        total = litro * 1.9
        desconto = total - (total * 0.05)

print(f'Valor a pagar: {desconto:.2f}')



# Resposta
litros = float(input("Digite quantos litros você quer abastecer: "))
combustivel = input("Digite A para álcool ou G para gasolina: ")
preco = 0
if combustivel == "A" or combustivel == "a":
    preco = litros * 1.9
    if litros <= 20:
        preco -= 1.9 * litros * 3 / 100
    else:
        preco -= 1.9 * litros * 5 / 100
elif combustivel == "G" or combustivel == "g":
    preco = litros * 2.5
    if litros <= 20:
        preco -= 2.5 * litros * 4 / 100
    else:
        preco -= 2.5 * litros * 6 / 100
print(f"O preço a pagar é R${preco:.2f}")