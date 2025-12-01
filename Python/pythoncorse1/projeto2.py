# Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute até que o valor aleatório gerado no início do programa seja chutado corretamente.

# O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.

import random

valorAleatorio = random.randint(1,10)
chute = int(input('Qual é o seu chute? '))

if chute > valorAleatorio:
    print('Chutou alto. Tente novamente!')
elif chute < valorAleatorio:
    print('Chutou baixo. Tente novamante!')
elif chute == valorAleatorio:
    print('Parabéns!!!!!!! Você acertou!!!!!')