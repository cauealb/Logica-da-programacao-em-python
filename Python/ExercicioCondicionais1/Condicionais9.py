# Uma lanchonete possui vários produtos. Cada produto possui um código e um preço. Você deve fazer um programa para ler o código e a quantidade comprada de um produto (suponha um código válido), e daí informar qual o valor a ser pago, com duas casas decimais, conforme tabela de produtos ao lado. 

codigo = int(input('Código do produto comprado: '))

match codigo:
    case 1:
        quantidade = int(input('Quantidade comprada: '))
        total = 5.00 * quantidade
        print(f'Valor a pagar: R${total:.2f}')
    case 2:
        quantidade = int(input('Quantidade comprada: '))
        total = 3.50 * quantidade
        print(f'Valor a pagar: R${total:.2f}')
    case 3:
        quantidade = int(input('Quantidade comprada: '))
        total = 4.80 * quantidade
        print(f'Valor a pagar: R${total:.2f}')
    case 4:
        quantidade = int(input('Quantidade comprada: '))
        total = 8.90 * quantidade
        print(f'Valor a pagar: R${total:.2f}')
    case 5:
        quantidade = int(input('Quantidade comprada: '))
        total = 7.32 * quantidade
        print(f'Valor a pagar: R${total:.2f}')
    case _:
        print('Código Desconhecido!')

