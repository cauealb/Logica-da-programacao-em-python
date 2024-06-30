# Fazer um programa para ler um número inteiro N e depois um vetor de N números reais. Em seguida,
# mostrar na tela a média aritmética de todos elementos com três casas decimais. Depois mostrar todos
# os elementos do vetor que estejam abaixo da média, com uma casa decimal cada. 

n = int(input('Digite quantas voltas: '))
vetor = []
total = 0

for i in range(1, n + 1):
    num = float(input('Digite os valores: '))
    vetor.append(num)
    total += num
media = total / n

print(f'MÉDIA ARITMÉTICA: {media:.3f}\n'
      f'ELEMENTOS ABAIXO DA MEDIA:')

for i in vetor:
    if i < media:
        print(i)