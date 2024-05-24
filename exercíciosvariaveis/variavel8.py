# Desenvolva um programa que receba a distância de uma viagem em quilômetros e a velocidade média esperada em km/h. Com essas informações, calcule o tempo esperado de viagem e exiba-o.

# 1. Distãncia de uma viagem em quilômetros e a velocidade média esperada em km/h==========
# 2. calcule o tempo esperado de viagem e exiba-o
# 3. Distãncia de uma viagem em quilômetros e a velocidade média esperada 
# 4. O tempo esperado de viagem

distancia = int(input('Qual foi a distância da viagem: '))
velocidade = int(input('Qual foi a velocidade média: '))

tempo = distancia / velocidade

if tempo <= 1:
    print('Demorará ', tempo, 'hora')
else:
    tempo = tempo * 1
    print('Demorará ', tempo, 'horas')
