    # Descrição: Crie um programa que converta uma dada quantidade de segundos em horas, minutos e segundos.

tempo = int(input('Quais são os segundos? '))
h = 3600 
m = 60
s = 60
resto = tempo % m # 100 / 60 = 1

h = tempo // h
m = tempo // m
s = resto % s


print(str(h) + ':' + str(m) + ':' + str(s))