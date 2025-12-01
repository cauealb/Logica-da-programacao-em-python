# Leia um valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, para os quais você deverá calcular e mostrar a média ponderada, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5. Vale lembrar que a média ponderada é a soma de todos os valores multiplicados pelo seu respectivo peso, dividida pela soma dos pesos. 

n = int(input('Quantos casos voce vai digitar: '))

for i in range(1, n + 1):
    num1 = float(input('Digite um numeros: '))
    num2 = float(input('Digite outro numeros: '))
    num3 = float(input('Digite outro numeros: '))

    # Multiplicação das notas com os pesos
    num1 *= 2
    num2 *= 3
    num3 *= 5

    # Somar o resultado
    somaTotal = (num1 + num2 + num3)

    # Soma dos pesos
    pesoTotal = (2 + 3 + 5)

    # Calcular o valor total
    somaTotal /= pesoTotal

    print(f'MÉDIA PONDERADA: {somaTotal:.1f}')