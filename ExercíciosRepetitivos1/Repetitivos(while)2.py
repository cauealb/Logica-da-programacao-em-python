# Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez, mostrar a mensagem "IMPOSSIVEL CALCULAR". 

parar = True
id = int(input('Digite uma idade: '))
total = id

if id < 0:
    print('IMPOSSÍVEL CALCULAR!')
    parar = False
else:
    media = 1
    id = id



    while parar == True:
        id = int(input('Digite outra idade: '))

        if id < 0:
            parar = False
        else:
            total += id
            media += 1

    media = total / media

    print(f'Média: {media:.2f}')