# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

# Meu algoritmo
print('Bem-Vindo ao Software que calcula seu peso ideal!')
print()

altura = float(input('Digite sua Altura: '))

peso = (72.7 * altura) - 58

print(f'Seu peso ideal será: {int(peso)}kg')


# Resposta

altura = float(input("Digite sua altura em metros: "))
peso_ideal = (72.7 * altura) - 58
print(f"O peso ideal para sua altura é: {peso_ideal:.2f}Kg")