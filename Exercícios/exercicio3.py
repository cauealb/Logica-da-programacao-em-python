#  Faça um algoritmo que imprima na tela a tabuada de 1 até 10.
# num1 = 1
# uma = False

# # Tabudad da 1
# for i in range(1,10 + 1):
#     if uma == False:
#         print('Tabuada da {}'.format(num1))
#         uma = True

#     print(num1, ' * ', i, ' = ', (num1*i))

# num2 = 2
# # Tabuada da 2
# for i in range(1,10 + 1):
#     if uma == False:
#         print('Tabuada da {}'.format(num2))
#         uma = True

#     print(num2, ' * ', i, ' = ', (num2*i))


# Versão Otimizada

def tabuada(num):
    print('Tabuada de {}'.format(num))
    for i in range(1,11):
        print(num, ' x ', i, ' = ', (num * i))
        print()

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
num6 = 6
num7 = 7
num8 = 8
num9 = 9
num10 = 10
numeros = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]

for numero in numeros:
    tabuada(numero)




