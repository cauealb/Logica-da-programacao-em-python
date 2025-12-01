# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa que leia um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto. 

n = int(input('Quantos casos de teste serão digitados: '))
totalC = 0
totalR = 0
totalS = 0

for i in range(1, n + 1):
    num = int(input('Quantidade de cobaias: '))
    tipo = input('Tipo de cobaia: ')

    if tipo == 'C':
        totalC += num
    elif tipo == 'R':
        totalR += num
    elif tipo == 'S':
        totalS += num

    # Contas
    total = (totalC + totalR + totalS) 

    somaC = (totalC / total) * 100
    somaR = (totalR / total) * 100
    somaS = (totalS / total) * 100


print(
        'RELATÓRIO FINAL! \n'
        f'Total: {total} Cobaia(s) \n'
        f'Total de Coelhos: {totalC}\n'
        f'Total de Ratos: {totalR}\n'
        f'Total de Sapos: {totalS}\n '
        f'Percentual de Coelho: {somaC:.2f} \n'
        f'Percentual de Ratos: {somaR:.2f} \n'
        f'Percentual de Sapos: {somaS:.2f} \n'  
          )

