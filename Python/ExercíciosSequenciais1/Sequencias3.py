#Escreva um programa que calcule a média ponderada de três notas, dadas as respectivas notas e pesos.

# 1. As notas e pesos
# 2. Fazer a média ponderada das notas e pesos
# 3. 3 notas com dados e pesos com dados
# 4. A média ponderada entre as notas e pesos

n1 = int(input('Qual sua primeira nota: '))  
n2 = int(input('Qual sua segunda nota: '))  
n3 = int(input('Qual sua terceira nota: ')) 

matematica = 5
portugues = 2
fisica = 3

media = ((n1*matematica)+(n2*portugues)+(n3*fisica)) / (matematica + portugues + fisica)

print(media)