# Desenvolva um programa que solicite a idade atual do usuário e o número de anos no futuro que ele deseja calcular. Com essas informações, calcule e exiba a idade que ele terá no futuro.

# 1. idade atual do usuário, o ano desse ano, e número de anos que ele deseja no futuro
# 2. alcule e exiba a idade que ele terá no futuro.
# 3. Nenhuma
# 4. A idade futura dele

idadeAtual = int(input('Qual sua idade atual: '))
anoAtual = 2024
anoFuturo = int(input('Qual data do ano que queira ver: '))

anoNas = anoAtual - idadeAtual

idadeFutura = anoFuturo - anoNas

print(idadeFutura)
