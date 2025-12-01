# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

# Minha resposta
data = input('Digite a Data: ')

dia, mes, ano =  data.split('/')

dia, mes, ano = int(dia), int(mes), int(ano)

data_valida = True

if mes < 1 or mes > 12:
    data_valida = False
    print('Data inválida!')
elif ano > 2024:
    data_valida = False
    print('Data inválida!')


if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia > 31:
        data_valida = False
        print('Data Inválida!')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 30:
        data_valida = False
        print('Data Inválda!')
elif mes == 2:
    if dia > 29:
        data_valida = False
        print('Data Inválida!')

if data_valida == True:
    print('Data Válida!')




# Resposta
data = input("Digite uma data no formato dd/mm/aaaa: ")
# Isto separa os elementos da data em uma lista.
# O fim de um elemento se dá por uma /
# Como são 3 elementos, podemos fazer uma atribuição múltipla direta
dia, mes, ano = data.split("/")
# E aqui transformamos os valores em inteiros para facilitar comparações
dia, mes, ano = int(dia), int(mes), int(ano)

if ano < 0:
    print("Ano inválido!")
else:
    if mes < 1 or mes > 12:
        print("Mês inválido!")
    # Isto testa se o mês é um destes dentro da lista
    # Poderiam ser feitas diversas comparações utilizando o or
    # ex. mes == 1 or mes == 3...
    # Mas achei isso mais simples.
    elif mes in [1, 3, 5, 7, 8, 10, 12]:  # meses com 31 dias
        if dia > 0 and dia < 32:
            print("Data válida!")
        else:
            print("Dia inválido!")
    elif mes in [4, 6, 9, 11]:  # meses com 30 dias
        if dia > 0 and dia < 31:
            print("Data válida!")
        else:
            print("Dia inválido!")
    else:  # fevereiro
        if ano % 4 == 0:  # Ano bissexto
            if dia > 0 and dia < 30:
                print("Data válida!")
            else:
                print("Dia inválido!")
        else:  # Ano não bissexto
            if dia > 0 and dia < 29:
                print("Data válida!")
            else:
                print("Dia inválido!")