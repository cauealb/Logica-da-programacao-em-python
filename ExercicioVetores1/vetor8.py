# Fazer um programa para ler um vetor de N números inteiros. Em seguida, mostrar na tela a média
# aritmética somente dos números pares lidos, com uma casa decimal. Se nenhum número par for
# digitado, mostrar a mensagem "NENHUM NUMERO PAR" 

n = int(input('Digite quantas voltas: '))
vetor = []
total = cont = 0

for i in range(1, n + 1):
    num = float(input('Digite os valores: '))
    if num % 2 == 0:
        vetor.append(num)
        total += num
        cont += 1

if len(vetor) == 0:
    print('NÃO EXISTE PAR!')
else:
    media = total / cont
    print(f'Média dos pares = {media:.1f}')