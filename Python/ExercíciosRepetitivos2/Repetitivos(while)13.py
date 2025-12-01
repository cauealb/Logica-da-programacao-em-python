# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

# Minn=ha Resposta
total = 0
maior = 0
cont = 1
parar = True
while True:
    temp = float(input(f'Digite a temperatura {cont}(digite 0 para terminar): '))
    while parar == True:
        menor = temp
        parar = False

    if temp == 0:
        break
    else:
        total += temp
        cont += 1
        if temp <= menor:
            menor = temp
        if temp >= maior:
            maior = temp
    
media = total / cont
print(
    f'\nMaior temperatura: {maior}\n'
    f'Menor Temperatura: {menor}\n'
    f'Média de Temperaturas: {media:.2f}\n'
)



# Resposta

from math import inf

maior = -inf
menor = inf
soma = 0
contador = 0
while True:
    temperatura = float(
        input("Digite a temperatura em Kelvin. Negativa para parar: ")
    )
    if temperatura < 0:
        break

    contador += 1
    soma += temperatura
    if temperatura < menor:
        menor = temperatura
    if temperatura > maior:
        maior = temperatura

print(f"A menor temperatura foi {menor}K")
print(f"A maior temperatura foi {maior}K")
print(f"A média das temperaturas foi {soma / contador:.3f}K")