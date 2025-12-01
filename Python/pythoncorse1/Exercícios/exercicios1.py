# Escreva um programa que receba um número inteiro do usuário e verifique se ele é um número primo. O programa deve imprimir "O número X é primo" ou "O número X não é primo", onde X é o número fornecido pelo usuário.


num = int(input('Forneça um número: '))
resultado = 0
lista = [1,2,3,4,5,6,7,8,9,10]
Lista_inteiro = []
Lista_decimais = []

for numero in lista:
    resultado = num / numero
    if resultado.is_integer():
        Lista_inteiro.append(resultado)
    else:
        Lista_decimais.append(resultado)

if len(Lista_inteiro) == 2:
    print('Ele é um número primo!')
else:
    print('Ele não é um número primo!')

print(Lista_inteiro)
print(Lista_decimais)
        

 