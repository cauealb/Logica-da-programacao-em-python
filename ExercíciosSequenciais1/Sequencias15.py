# Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia. O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto, e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve mostrar o valor do troco a ser devolvido ao cliente. 

# 1. Preço unitário, a quantidade de unidades compradas e o valor em dinheiro
# 2. Devo calcular o produto do preço unitário com a quantidade de unidades, e com isso, com esse resultados fazer uma conta de subtração com o resultado dessa contas, menos o valor que o cliente vai dar.
# 3. Seu programa deve mostrar o valor do troco a ser devolvido ao cliente. 
# 4. A subtração do produto com o troco do cliente

preco = float(input("Qual é o preço do produto: "))
quantidade = int(input("Quantas unidades: "))
valor = float(input("Qual é o valor recebido: "))

produto = preco * quantidade

troco = valor - produto

print(f'Troco: {troco:.2f}')