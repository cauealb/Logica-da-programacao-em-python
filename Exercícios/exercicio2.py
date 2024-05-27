# Faça um algoritmo que leia dois valores inteiros A e B, imprima na tela o quociente e o resto da divisão inteira entre eles.

# 1. Valores A e B ========
# 2. Preciso mostrar o quociente deles e o resto da divisão entre eles
# 3. Valores Inteiros ======
# 4. Espero o qouciente e o resto da divisão entre o A e B

inteiro = False

while inteiro == False:
    a = int(input('Digite seu primeiro valor: '))
    b = int(input('Digite seu segundo valor: '))

    if a < 0 or b < 0:
        print('Digite valores inteiros!')
    elif a == b or b == a:
        print('Os valores não podem ser iguias!')
    else:
        inteiro = True

print(a / b)

print('O quociente da divisão entre o ', a , ' e ', b, ' é: ', a // b)

print('O o resto da divisão entre o ', a , ' e ', b, ' é: ', a % b)