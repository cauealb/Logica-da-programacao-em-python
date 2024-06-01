# Fazer um programa para ler a quantidade de glicose no sangue de uma pessoa e depois mostrar na tela a classificação desta glicose de acordo com a tabela de referência ao lado. 

glicose = float(input('Digite o número da sua glicose: '))

if glicose <= 100:
    print('Normal')
elif glicose > 100 and glicose <= 140:
    print('Elevado!')
elif glicose > 140:
    print('Diabetes!!')
