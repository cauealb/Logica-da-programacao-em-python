# Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente. O programa deve finalizar quando forem digitados dois valores iguais. 

parar = True

while parar == True:

    x  = int(input('Primeiro número: '))
    y  = int(input('Segundo número: '))

    print(x)
    print(y)

    if x == y:
        parar = False
    elif x > y:
        print('Descrescente!')
    else:
        print('Crescente!')
    
    