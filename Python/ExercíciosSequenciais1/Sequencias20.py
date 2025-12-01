# Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no formato horas:minutos:segundos. 

valor = int(input("Digite os segundos: "))

hora = valor // 3600
resto = valor % 3600
minutos = resto // 60
segundos = resto % 60

print(hora,':',minutos,':',segundos)