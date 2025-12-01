'''
76) Crie um programa que preencha automaticamente um vetor numérico com 7
números gerados aleatoriamente pelo computador e depois mostre os valores
gerados na tela.

pseudocódigo:

- criar array

- loop de 0 a 7:
    - gera valor aleatorio
    - inclui no indice o valor

exibir valores
'''

import random

arr = [0] * 7

for i in range(7):
    num = random.randint(1, 50)
    arr[i] = num

print(arr)