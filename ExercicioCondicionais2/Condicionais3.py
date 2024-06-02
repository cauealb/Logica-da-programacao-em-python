# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.


data = input('Digite a Data: ')

dia, mes, ano =  data.split('/')

dia, mes, ano = int(dia), int(mes), int(ano)

if mes < 1 or mes > 12:
    print('Data inválida!')
elif ano < 1:
    print('Data inválida!')


if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia > 31:
        print('Data Inválida!')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 30:
        print('Data Inválda!')
elif mes == 2:
    if dia > 29:
        print('Data Inválida!')
else:
    print('Data Válida')

# Não terminado (terminar)



# data = input("Digite uma data no formato dd/mm/aaaa: ")
# # Isto separa os elementos da data em uma lista.
# # O fim de um elemento se dá por uma /
# # Como são 3 elementos, podemos fazer uma atribuição múltipla direta
# dia, mes, ano = data.split("/")
# # E aqui transformamos os valores em inteiros para facilitar comparações
# dia, mes, ano = int(dia), int(mes), int(ano)