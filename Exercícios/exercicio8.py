# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7


# Meu Algoritmo
print('Bem-Vindo ao seu Software que calcula seu peso ideal')
print()

resposta = input('Você é Homem ou Mulher? ')

if resposta == "Homem":
    alturaHomem = float(input('Digite sua altura: '))
    pesoHomem = (72.7 * alturaHomem) - 58

    print(f'Seu peso ideal é {pesoHomem:.2f}kg')

elif resposta == "Mulher":
    alturaMulher = float(input('Digite sua altura: '))
    pesoMulher = (62.1 * alturaMulher) - 44.7

    print(f'Seu peso ideal é {pesoMulher:.2f}kg')



# Resposta

altura = float(input("Digite sua altura em metros: "))
peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7
print(
    f"O peso ideal para sua altura é:\n{peso_ideal_homem:.2f}Kg para homens.\n"
    f"{peso_ideal_mulher:.2f}Kg para mulheres."
)