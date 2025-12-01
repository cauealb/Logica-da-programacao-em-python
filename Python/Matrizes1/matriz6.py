# Ler um inteiro N (máximo = 10) e uma matriz quadrada de ordem N
# contendo números inteiros. Mostrar a soma dos elementos acima da
# diagonal principal. Um exemplo de números acima da diagonal
# principal é mostrado ao lado (no caso as células com fundo cinza).

o =int(input('Qual a ordem da matriz: '))
matriz = [[0 for _ in range(o)] for _ in range(o)]
total = 0

for l in range(o):
    for c in range(o):
        num = int(input(f'Elemento [{l},{c}]: '))
        matriz[l][c] = num

        if c > l:
            total += num

print(f'SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {total}')