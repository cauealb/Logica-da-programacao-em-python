# O cardápio de uma lanchonete é o seguinte:
#     Especificação         Código    Preço
#     Cachorro Quente (CQ)   100     R$ 1,20
#     Bauru Simples   (BS)   101     R$ 1,30
#     Bauru com ovo   (BO)   102     R$ 1,50
#     Hambúrguer      (H)    103     R$ 1,20
#     Cheeseburguer   (C)    104     R$ 1,30
#     Refrigerante    (R)    105     R$ 1,00

# Faça um programa que leia o código dos itens pedidos e as quantidades
# desejadas.

# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total
# geral do pedido.

# Considere que o cliente deve informar quando o pedido deve ser encerrado.

conta100 = conta101 = conta102 = conta103 = conta104 = conta105 = total0 = total1 = total2 = total3 = total4 = total5 =0

parar = True
while parar == True:
    lanche = int(input('Qual o código do pedido vai querer(digite 0 para terminar o pedido): '))
    
    if lanche == 0:
        break
    else:
        qtd = int(input('Quantos desse lanche vai querer: '))
        if lanche == 100:
            preco = 1.20
            conta100 = preco * qtd
            total0 += conta100

        elif lanche == 101:
            preco = 1.30
            conta101 = preco * qtd
            total1 += conta101

        elif lanche == 102:
            preco = 1.50
            conta102 = preco * qtd
            total2 += conta102

        elif lanche == 103:
            preco = 1.20
            conta103 = preco * qtd
            total3 += conta103

        elif lanche == 104:
            preco = 1.30
            conta104 = preco * qtd
            total4 += conta104

        elif lanche == 105:
            preco = 1.00
            conta105 = preco * qtd
            total5 += conta105

total = total0 + total1 + total2 + total3 + total4 + total5

print('\nFatura da sua Compra')
print(f'Total do Cachorro Quente: R${total0:.2f}\n'
      f'Total do Bauru Simples: R${total1:.2f}\n'
      f'Total do Bauru com ovo: R${total2:.2f}\n'
      f'Total do Hamburger: R${total3:.2f}\n'
      f'Total do Cheeseburguer: R${total4:.2f}\n'
      f'Total do Refrigerante: R${total5:.2f}\n'
      f'\nTotal da sua compra: R${total:.2f}'
) 


# Resposta
quantidade_produto_100 = 0
quantidade_produto_101 = 0
quantidade_produto_102 = 0
quantidade_produto_103 = 0
quantidade_produto_104 = 0
quantidade_produto_105 = 0
total = 0

print(
    "Produto         Codigo  Preço"
    "\n-------------------------------"
    "\nCachorro Quente 100     R$ 1.20"
    "\nBauru Simples   101     R$ 1.30"
    "\nBauru com ovo   102     R$ 1.50"
    "\nHamburguer      103     R$ 1.20"
    "\nCheeseburguer   104     R$ 1.30"
    "\nRefrigerante    105     R$ 1.00\n"
)

while True:
    codigo = int(input("Digite o codigo do produto (ou 0 para encerrar): "))
    if codigo == 0:
        break
    if codigo > 105 or codigo < 100:
        print("Codigo inválido!")
        continue

    quantidade = int(input("Digite a quantidade desse produto: "))
    if codigo == 100:
        quantidade_produto_100 += quantidade
    elif codigo == 101:
        quantidade_produto_101 += quantidade
    elif codigo == 102:
        quantidade_produto_102 += quantidade
    elif codigo == 103:
        quantidade_produto_103 += quantidade
    elif codigo == 104:
        quantidade_produto_104 += quantidade
    else:
        quantidade_produto_105 += quantidade

print(
    "\nFechamento do pedido"
    "\nCodigo  -  Quantidade  -  Preço unidade  -  Preço total"
)
if quantidade_produto_100 > 0:
    print(
        f"100\t-\t{quantidade_produto_100}\t-  R$ 1.20\t-"
        f"\tR$ {quantidade_produto_100 * 1.2:.2f}"
    )
    total += quantidade_produto_100 * 1.2
if quantidade_produto_101 > 0:
    print(
        f"101\t-\t{quantidade_produto_101}\t-  R$ 1.30\t-"
        f"\tR$ {quantidade_produto_101 * 1.3:.2f}"
    )
    total += quantidade_produto_101 * 1.3
if quantidade_produto_102 > 0:
    print(
        f"102\t-\t{quantidade_produto_102}\t-  R$ 1.50\t-"
        f"\tR$ {quantidade_produto_102 * 1.5:.2f}"
    )
    total += quantidade_produto_102 * 1.5
if quantidade_produto_103 > 0:
    print(
        f"103\t-\t{quantidade_produto_103}\t-  R$ 1.20\t-"
        f"\tR$ {quantidade_produto_103 * 1.2:.2f}"
    )
    total += quantidade_produto_103 * 1.2
if quantidade_produto_104 > 0:
    print(
        f"104\t-\t{quantidade_produto_104}\t-  R$ 1.30\t-"
        f"\tR$ {quantidade_produto_104 * 1.3:.2f}"
    )
    total += quantidade_produto_104 * 1.3
if quantidade_produto_105 > 0:
    print(
        f"105\t-\t{quantidade_produto_105}\t-  R$ 1.00\t-"
        f"\tR$ {quantidade_produto_105 * 1.0:.2f}"
    )
    total += quantidade_produto_105 * 1.0

print(f"Total do pedido: R$ {total:.2f}")