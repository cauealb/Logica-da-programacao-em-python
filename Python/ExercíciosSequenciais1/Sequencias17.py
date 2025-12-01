# Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com uma mensagem explicativa, conforme exemplo. 

nome = str(input('Qual é o seu nome: '))
hora = float(input('Quanto recebe por hora trabalhada: '))
quantidade = float(input('Quantas horas trabalhadas:  '))

valor = hora * quantidade

print(
    f'O pagamento para {nome} sera de R${valor:.2f}'
)