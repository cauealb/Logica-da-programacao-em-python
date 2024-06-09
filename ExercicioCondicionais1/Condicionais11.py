# Uma empresa vai conceder um aumento percentual de salário aos seus funcionários dependendo de quanto cada pessoa ganha, conforme tabela ao lado. Fazer um programa para ler o salário de uma pessoa, daí mostrar qual o novo salário desta pessoa depois do aumento, quanto foi o aumento e qual foi a porcentagem de aumento. 

salario = float(input('Digite o salario da pessoa: '))

if salario <= 1000:
    quantidade = salario * 0.20
    salario = (salario * 0.20) + salario
    print('Porcentagem = 20%')

elif salario > 1000 and salario <= 3000:
    quantidade = salario * 0.15
    salario = (salario * 0.15) + salario
    print('Porcentagem = 15%')

elif salario > 3000 and salario <= 8000:
    quantidade = salario * 0.10
    salario = (salario * 0.10) + salario
    print('Porcentagem = 10%')

elif salario > 8000:
    quantidade = salario * 0.05
    salario = (salario * 0.05) + salario
    print('Porcentagem = 5%')

print(f'Novo salario = {salario:.2f}')
print(f'Aumento = {quantidade:.2f}')