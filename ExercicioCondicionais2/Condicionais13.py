# Escreva um programa que permita ao usuário jogar "Pedra, Papel, Tesoura" contra o computador. O programa deve determinar o vencedor de acordo com as regras do jogo, considerando todas as possíveis combinações e os casos de empate

# Papel ganha da Pedra
# Tesoura ganha do Papel
# Pedra ganha da Tesoura

# Pedra = 1
# Papel = 2
# Tesoura = 3


import random

numero = random.randint(1,3)

pedra = 'Pedra'
papel = 'Papel'
tesoura = 'Tesoura'

resposta = input('Vai jogar qual: ')

# Empate
if numero == 1 and resposta == 'Pedra':
    print('Computador: Pedra')
    print(f'Você: {pedra}')
    print('Empate!')
elif numero == 2 and resposta == 'Papel':
    print('Computador: Papel')
    print(f'Você: {papel}')
    print('Empate!')
elif numero == 3 and resposta == 'Tesoura':
    print('Computador: Tesoura')
    print(f'Você: {tesoura}')
    print('Empate!')

# Pedra

if numero == 1 and resposta == 'Papel':
    print('Computador: Pedra')
    print(f'Você: {papel}')
    print('Venceu!')
elif resposta == 'Pedra' and numero == 2:
    print('Computador: Papel')
    print(f'Você: {pedra}')
    print('Perdeu!')

if numero == 1 and resposta == 'Tesoura':
    print('Computador: Pedra')
    print(f'Você: {tesoura}')
    print('Perdeu!')
elif resposta == 'Pedra' and numero == 3:
    print('Computador: Tesoura')
    print(f'Você: {pedra}')
    print('Venceu!')

# Papel

if numero == 2 and resposta == 'Tesoura':
    print('Computador: Papel')
    print(f'Você: {tesoura}')
    print('Venceu!')
elif numero == 3 and resposta == 'Papel':
    print('Computador: Tesoura')
    print(f'Você: {papel}')
    print('Perdeu!')





# Pedra = 1
# Papel = 2
# Tesoura = 3