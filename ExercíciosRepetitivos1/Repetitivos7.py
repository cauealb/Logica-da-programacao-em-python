# O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X , se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a soma de 12+14+16+18+20. 

parar = True
contador = 0

while parar == True:
    num = int(input('Digite um número inteiro: '))
    soma = num

    if num % 2 != 0:
        num += 1
    
    if num == 0:
        break

    while contador < 5:
        num += 2
        soma += num
        contador += 1

    print(f'SOMA: {soma}')

    # Não Terminado


