# Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida. Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, conforme exemplo 


n = int(input('Quantos numeros voce vai digitar: '))
listaDentro = []
listaFora = []

for i in range(1, n + 1):
    num = int(input('Digite um numero: '))

    if num >= 10 and num <= 20:
        listaDentro.append(num)
    else:
        listaFora.append(num)


print(
    f'DENTRO: {len(listaDentro)} \n'
    f'FORA: {len(listaFora)}'
)