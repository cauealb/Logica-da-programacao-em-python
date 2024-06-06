# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
# Confira:

#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
# de carne da promoção, porém não há limites para a quantidade de carne
# por cliente.

# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de
# 5% sobre o total da compra.

# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
# usuário e gere um cupom fiscal, contendo as informações da compra:
#     tipo de carne
#     quantidade de carne
#     preço total
#     tipo de pagamento
#     valor do desconto
#     valor a pagar.

# File Duplo (F)
# Alcatra (A)
# Picanha (P)

# Minha Resposta
tipo = input('Qual o tipo de carne: ')
qtd = int(input('Quantidades (em Kg): '))
cartao = input('Dinheiro ou Cartão? (D ou C) ')


if tipo == 'F' or tipo == 'f':

    if qtd <= 5:
        total = qtd * 4.9
        desconto = total - (total * 0.05)
        ValorDesconto = total * 0.05
        print(
            'Seu cupom fiscal: \n'
            'Item: Filé Duplo'
        )
    else:
        total = qtd * 5.8
        desconto = total - (total * 0.05)
        ValorDesconto = total * 0.05
        print(
            'Seu cupom fiscal: \n'
            'Item: Filé Duplo'
        )


if tipo == 'A' or tipo == 'a':

    if qtd <= 5:
        total = qtd * 5.9
        desconto = total - (total * 0.05)
        ValorDesconto = total * 0.05
        print(
            'Seu cupom fiscal: \n'
            'Item: Alcatra'
        )
    else:
        total = qtd * 6.8
        desconto = total - (total * 0.05)
        ValorDesconto = total * 0.05
        print(
            'Seu cupom fiscal: \n'
            'Item: Alcatra'
        )



if tipo == 'P' or tipo == 'p':
    
    if qtd <= 5:
        total = qtd * 6.9
        desconto = total - (total * 0.05)
        ValorDesconto = total * 0.05
        print(
            'Seu cupom fiscal: \n'
            'Item: Picanha'
        )
    else:
        total = qtd * 7.8
        desconto = total - (total * 0.05)
        ValorDesconto = total * 0.05
        print(
            'Seu cupom fiscal: \n'
            'Item: Picanha'
        )

if cartao == 'C' or cartao == 'c':
    print(
        f'Quantidade: {qtd}kg \n'
        f'Preço total: R${total:.2f} \n'
        f'Tipo de Pagamento: Cartão Tabajara \n'
        f'Desconto = R${ValorDesconto:.2f} \n'
        f'Valor a pagar: R${desconto:.2f}\n'
    )

elif cartao == 'D' or cartao == 'd':
    print(
        f'Quantidade: {qtd}kg \n'
        f'Preço total: R${total:.2f} \n'
        f'Tipo de Pagamento: Dinheiro \n'
        f'Desconto = Sem desconto \n'
        f'Valor a pagar: R${total:.2f}\n'
    )





# Resposta

carne = input("Digite F para filé duplo, A para alcatra e P para picanha: ")
peso = float(input("Digite quantos quilos dessa carne vai comprar: "))
pagamento = input("Dinheiro ou cartão tabajara (5% de desconto)? D ou C: ")
preco_total = 0

print("\nHipermercado Tabajara\nCupom fiscal\n")
if carne == "F" or carne == "f":
    print("Item: Filé Duplo")
    if peso > 5:
        preco_total = peso * 5.8
    else:
        preco_total = peso * 4.9
elif carne == "A" or carne == "a":
    print("Item: Alcatra")
    if peso > 5:
        preco_total = peso * 6.8
    else:
        preco_total = peso * 5.9
elif carne == "P" or carne == "p":
    print("Item: Picanha")
    if peso > 5:
        preco_total = peso * 7.8
    else:
        preco_total = peso * 6.9
print(f"Quantidade: {peso:.2f}Kg")
print(f"Preço total: R${preco_total:.2f}")
if pagamento == "D" or pagamento == "d":
    print("Tipo de pagamento: Dinheiro")
    desconto = 0
    print(f"Desconto: R${desconto:.2f}")
    print(f"Valor a pagar: R${(preco_total - desconto):.2f}")
elif pagamento == "C" or pagamento == "c":
    print("Tipo de pagamento: Cartão Tabajara")
    desconto = preco_total * 5 / 100
    print(f"Desconto: R${desconto:.2f}")
    print(f"Valor a pagar: R${(preco_total - desconto):.2f}")