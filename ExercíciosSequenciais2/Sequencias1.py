# Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos salários mínimos esse usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).

salariominimo = 1293.20

salario = float(input('Qual é seu salário: '))

salario /= salariominimo

print(int(round(salario)))
