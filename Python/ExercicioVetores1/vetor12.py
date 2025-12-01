# Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele comercializa. Para isto,
# mandou digitar um conjunto de N mercadorias, cada uma contendo nome, preço de compra e preço de
# venda das mesmas. Fazer um programa que leia tais dados e determine e escreva quantas mercadorias
# proporcionaram:
#  lucro < 10%
#  10% ≤ lucro ≤ 20%
#  lucro > 20%
# Determine e escreva também o valor total de compra e de venda de todas as mercadorias, assim como
# o lucro total. 

n = int(input('Digite quantas voltas: '))
vetorCompra = []
vetorVenda = []
vetormenos10 = []
vetor1020 = []
vetormais20 = []
totalC = totalV = 0


for i in range(1, n + 1):
    print(f'Produto {i}\n')
    nome = input('Digite um nome: ')
    pCompra = float(input('Preço de Compra: '))
    vetorCompra.append(pCompra)
    ######################################
    pVenda = float(input('Preço de Venda: '))
    vetorVenda.append(pVenda)
    ######################################
    Lb = pVenda - pCompra
    conta1 = (Lb / pCompra) * 100

    if conta1 < 10:
        vetormenos10.append(conta1)
    elif conta1 <= 20:
        vetor1020.append(conta1)
    else:
        vetormais20.append(conta1)


#Total da compra
for i in vetorCompra:
    totalC += i
for i in vetorVenda:
    totalV += i

operacao = totalV - totalC

print('\nRelatório\n'
      f'Lucro abaixo de 10%: {len(vetormenos10)}\n'
      f'Lucro entre 10% a 20%: {len(vetor1020)}\n'
      f'Lucro acima de 20%: {len(vetormais20)}\n'
      f'Valor total da Compra: {totalC}\n'
      f'Valor total da Venda: {totalV}\n'
      f'Lucro Total: {operacao}'
      )