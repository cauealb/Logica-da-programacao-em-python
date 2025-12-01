# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).

# Após esta entrada de dados, faça: Mostre a quantidade de valores que foram lidos; Exiba todos os valores na ordem em que foram informados, um ao lado do outro; Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; Calcule e mostre a soma dos valores; Calcule e mostre a média dos valores; Calcule e mostre a quantidade de valores acima da média calculada; Calcule e mostre a quantidade de valores abaixo de sete; Encerre o programa com uma mensagem;

vt = []
total = 0

while True:
    num = int(input('Digite uma nota: '))
    if num < 0:
        break
    else:
        vt.append(num)

# Do lado do outro
for i in vt:
    print(i, end=' ')

print()

# Inverso
reverse = vt[::-1]
for i in reverse:
    print(i,)

# Total e Média
for i in vt:
    total += i
print(f'Soma desses valores: {total}')
media = total / len(vt)
print(f'Média dos valores: {media}')


# valores acima da média
cont = cont7 = 0
for i in vt:
    if i > media:
        cont += 1
    if i > 7:
        cont7 += 1
print(f'Valores acima da média: {cont}\n'
      f'Valores acima de 7: {cont7}')



print('\nFIM DO PROGRAMA!\n')
