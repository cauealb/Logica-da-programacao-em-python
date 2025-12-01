# Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. Para isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra escala com duas casas decimais. A seguir é dada a fórmula para converter de Fahrenheit para Celsius (você deve deduzir a fórmula de Celsius para Fahrenheit....

resposta = str(input('C/F? '))

if resposta == 'C':

    temperatura = float(input('Digite a temperatura em Celsius: '))
    ContaF = (9/5 * temperatura) + 32
    print(f'Temperatura equivalente em Fahrenheit: {ContaF:.2f}')

elif resposta == 'F':

    temperatura = float(input('Digite a temperatura em Fahrenheit: '))
    ContaC = (temperatura - 32) * 5/9
    print(f'Temperatura equivalente em Celsius: {ContaC:.2f}')


