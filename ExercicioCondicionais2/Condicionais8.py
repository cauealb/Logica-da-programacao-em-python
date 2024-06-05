# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.

# O resultado da operação deve ser acompanhado de uma frase que diga se o número é: par ou ímpar; positivo ou negativo; inteiro ou decimal.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

conta = input('Qual operação você deseja fazer: ')

match conta:
    case 'Soma':
        resultado = num1 + num2
        parimpar = resultado % 2
        resto = resultado / 2
        print(f'Soma: {resultado}')
        if parimpar == 0:
            print(f'Par')
        else:
            print(f'Ímpar')
        if resultado < 0:
            print('Negativo')
        else:
            print('Positivo')
        if resultado % 1 == 0:
            print('Inteiro')
        else:
            print('Decimal')

    case 'Subtração':
        resultado = num1 - num2
        parimpar = resultado % 2
        resto = resultado / 2
        print(f'Subtração: {resultado}')
        if parimpar == 0:
            print(f'Par')
        else:
            print(f'Ímpar')
        if resultado < 0:
            print('Negativo')
        else:
            print('Positivo')
        if resultado % 1 == 0:
            print('Inteiro')
        else:
            print('Decimal')

    case 'Divisão':
        resultado = num1 / num2
        parimpar = resultado % 2
        resto = resultado / 2
        print(f'Divisão: {resultado}')
        if parimpar == 0:
            print(f'Par')
        else:
            print(f'Ímpar')
        if resultado < 0:
            print('Negativo')
        else:
            print('Positivo')
        if resultado % 1 == 0:
            print('Inteiro')
        else:
            print('Decimal')

    case 'Multiplicação':
        resultado = num1 * num2
        parimpar = resultado % 2
        resto = resultado / 2
        print(f'Multiplicação: {resultado}')
        if parimpar == 0:
            print(f'Par')
        else:
            print(f'Ímpar')
        if resultado < 0:
            print('Negativo')
        else:
            print('Positivo')
        if resultado % 1 == 0:
            print('Inteiro')
        else:
            print('Decimal')










