# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# Minha resposta
parar = True

while parar == True:
    n = float(input('Digite um nota (entre 0 a 10): '))

    if n < 0 or n > 10:
        print('Valor inválido!')
    else:
        if n <= 10:
            parar = False


# Resposta

nota = float(input("Digite uma nota de 0 a 10: "))
while nota > 10 or nota < 0:
    nota = float(input("Valor Inválido\nDigite uma nota de 0 a 10: "))


