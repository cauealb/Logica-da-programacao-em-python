# Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

# 1. Três valores inteiros diferentes =========
# 2. Imprimir na tela os valores em ordem decrescente ========
# 3. Três valores inteiros diferentes =========
# 4. Receber o uma lista em ordem decrescente =========

acertou = False
while acertou == False:
    v1 = int(input('Qual seu primeiro número: '))
    v2 = int(input('Qual seu segundo número: '))
    v3 = int(input('Qual seu terceiro número: '))

    if v1 < 0 or v2 < 0 or v3 < 0:
        print('Os números não podem ser negativos!')
    elif v1 == v2 or v1 == v3 or v2 == v3:
        print('Os números não podem ser iguias!')
    else:
        acertou = True

lista = [v1, v2, v3]

listadecrescente = sorted(lista, reverse=True)
listacrescente = sorted(lista)

print('Essa lista em ordem decrescente será assim: ', listadecrescente)

print('Essa lista em ordem crescente será assim: ', listacrescente)
