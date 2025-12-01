# Faça um Programa para um caixa eletrônico.

# O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas.

# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.

# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

# 

# Minha Resposta

valor = int(input('Valor do Saque: '))

if valor < 10 and valor > 600:
    print('Valor não suportado!!')

# Separação
uni = valor % 10
deze = (valor // 10) % 10 * 10
cente = (valor // 100) * 100

if valor > 100:
# Centena
    if cente > 100:
        cente = cente / 100
        print(f'{cente:.0f} notas de 100')
    else:
        cente = cente / 100
        print(f'{cente:.0f} nota de 100')

    if deze < 50:
        deze = deze / 10
        print(f'{deze:.0f} notas de 10.')
    if deze > 50:
        resto = deze - 50 
        deze = deze / deze 
        print(f'{deze:.0f} notas de 50, {resto:.0f} notas de 10')
    elif deze == 10:
        print(f'{deze:.0f} nota de 50')
    elif deze == 50:
        dezena = deze / deze
        print(f'{dezena:.0f} nota de 50')

    

    if uni > 5:
        resto = uni - 5
        unidade = uni / uni
        print(f'{unidade:.0f} notas de 5, {resto:.0f} notas de 1')
    elif uni == 5:
        unidade = uni / uni
        print(f'{unidade:.0f} notas de 5')
    
    if uni < 5:
        print(f'{uni:.0f} notas de 1.')
    elif uni == 1:
        print(f'{uni:.0f} nota de 1.')

    





if valor > 9 and valor < 99:
# Dezena
    if deze > 50:
        resto = deze - 50 
        deze = deze / deze 
        print(f'{deze:.0f} notas de 50, {resto:.0f} notas de 10')
    elif deze == 10:
        print(f'{deze:.0f} nota de 50')
    elif deze == 50:
        deze = deze / deze
        print(f'{deze:.0f} nota de ')

    if deze < 50:
        deze = deze / 10
        print(f'{deze:.0f} notas de 10.')

    if uni > 5:
        resto = uni - 5
        uni = uni / uni
        print(f'{uni:.0f} notas de 5, {resto:.0f} notas de 1')
    elif uni == 5:
        resto = uni / uni
        print(f'{resto:.0f} notas de 5')
    
    if uni < 5:
        print(f'{uni:.0f} notas de 1.')
    elif uni == 1:
        print(f'{uni:.0f} nota de 1.')



if valor <= 9:

    if uni > 5:
        resto = uni - 5
        unidade = uni / uni
        print(f'{unidade:.0f} notas de 5, {resto:.0f} notas de 1')
    elif uni == 5:
        uni = uni / uni
        print(f'{uni:.0f} notas de 5')
    
    if uni < 5:
        print(f'{uni:.0f} notas de 1.')
    elif uni == 1:
        print(f'{uni:.0f} nota de 1.')






# Resposta

valor = int(input("Digite o valor a ser sacado (entre 10 e 600): "))
if (
    valor < 10 or valor > 600
):  # Os parênteses não são necessários, mas vou passar a usá-los
    print("Valor inválido!")
else:
    cem = valor // 100  # Pegamos a centena com uma divisão inteira
    valor -= cem * 100  # Subtraímos as centenas retiradas do valor total
    cinquenta = valor // 50  # Idem para as outras coisas
    valor -= cinquenta * 50
    dez = valor // 10
    valor -= dez * 10
    cinco = valor // 5
    valor -= cinco * 5
    um = valor  # Depois de subtrair as de cinco só sobram as de um
    if cem > 0:
        print(f"{cem} nota(s) de cem")
    if cinquenta > 0:
        print(f"{cinquenta} nota(s) de cinquenta")
    if dez > 0:
        print(f"{dez} nota(s) de dez")
    if cinco > 0:
        print(f"{cinco} nota(s) de cinco")
    if um > 0:
        print(f"{um} nota(s) de um")