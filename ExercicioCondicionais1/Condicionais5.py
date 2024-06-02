# Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia. O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto, e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o valor restante conforme exemplo. 

preco = float(input('Preço do dinheiro: '))
quantidade = int(input('Quantidades: '))
valor = float(input('Dinheiro do cliente: '))

produto = preco * quantidade

if valor < produto:
    conta = produto - valor
    print(f'Dinheiro Insuficiente, faltam R${conta:.2f}')
else:
    conta = valor - produto
    print(f'Troco: {conta:.2f}')
