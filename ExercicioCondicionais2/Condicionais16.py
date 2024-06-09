# Faça um algoritmo que, dado o valor total em reais e o número de prestações desejadas, calcule o valor de cada prestação. O número mínimo de prestações deve ser 12. Se o número de prestações for maior ou igual a 24, adicione 10% de juros ao valor total, se for maior ou igual a 36, adicione 15% de juros ao valor.

valor = int(input('Digite o valor total: '))
prestacao = int(input('Digite quantas prestações vai querer: '))

if prestacao < 12:
    total = valor / prestacao
    
elif prestacao >= 24 and prestacao < 36:
    total = valor / prestacao
    porcentagem = total * 0.1
    total = total + porcentagem
    print(f'Valor dos Juros: R${porcentagem:.2f}')

else:
    total = valor / prestacao
    porcentagem = total * 0.15
    total = total + porcentagem
    print(f'Valor dos Juros: R${porcentagem:.2f}')

print(f'O total das prestações será de R${total:.2f}')

