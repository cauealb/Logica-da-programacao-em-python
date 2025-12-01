# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

# Minha Resposta
while True:
    num = int(input('Digite um número para sua Fatorial: '))
    while num >= 16:
        num = int(input('Numero inválido! Digite novamente: ')) 
    total = 1
    for i in range(num, 0 , -1):
        total *= i
    print(f'Fatorial: {total}')

# Resposta
while True:
    numero = int(input("Digite um numero: "))
    if not 0 < numero < 16:
        continue
    fatorial = 1
    for i in range(numero, 1, -1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}")
    if input("Deseja continuar? (S/N): ").upper() != "S":
        break