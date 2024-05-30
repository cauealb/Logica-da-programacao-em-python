# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.

# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.

# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.

# # Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.


# Minha Resposta
print('Bem-Vindo ao seu programa, João!')
print()

peso = int(input("Digite o peso trazido: "))

if peso > 50:
    conta = (peso - 50) * 4
    excesso = peso - 50
    multa = conta

    print(
        f'João, você excedeu o limite de quilos, ultrapassando {excesso}kg'
        '\n'
        f'João, você terá que pagar R${multa:.2f}'
    )


# Resposta

peso = float(input("Digite o peso da pesca em Kg: "))
excesso = peso - 50
multa = excesso * 4
print(f"Foram {excesso:.2f}Kg em excesso, logo, a multa é de R${multa:.2f}.")