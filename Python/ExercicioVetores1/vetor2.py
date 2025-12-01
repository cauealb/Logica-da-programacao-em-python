# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
# - Imprimir todos os elementos do vetor
# - Mostrar na tela a soma e a média dos elementos do vetor 

n = int(input('Digite quantas voltas: '))
vetor = []
total = cont = 0

for i in range(n):
    num = float(input('Digite um número: '))
    total += num
    vetor.append(num)
print('\nResultados')
for i in vetor:
    cont += 1
    print(i)

media = total / cont

print(f'\nMédia {media:.2f}'
      f'\nSoma: {total}'
      )