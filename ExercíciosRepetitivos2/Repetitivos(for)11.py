# Altere o programa anterior para mostrar no final a soma dos números.

# Minha Resposta
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
total = 0

for i in range(n1 + 1, n2):
    total += i
print(f'SOMA: {total}')


# Resposta

primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite um numero: "))
somatorio = 0
for i in range(primeiro_numero + 1, segundo_numero):
    print(i)
    somatorio += i
print(f"Somatorio: {somatorio}")