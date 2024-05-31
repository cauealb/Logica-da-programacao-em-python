#Escreva um programa que calcule o valor futuro de um investimento usando a fórmula de juros compostos 

# 1. Meu capital inicial
# 2. Calcular meu montante final
# 3. usando a fórmula de juros compostos 
# 4. O juros compostos da minha aplicação

c = int(input('Qual o seu capital inicial: '))
t = int(input('Quanto tempo aplicando: '))
i = float(input('Qual é o juros ao mês: '))

m = c * (1 + i) ** t

print(round(m))
