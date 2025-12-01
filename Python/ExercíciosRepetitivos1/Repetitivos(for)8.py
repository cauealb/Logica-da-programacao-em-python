# Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10, conforme exemplo. 

num = int(input('Deseja a tabuada para qual valor: '))

for i in range(0, 11):
    print(num, " x ", i, " = ", num * i)