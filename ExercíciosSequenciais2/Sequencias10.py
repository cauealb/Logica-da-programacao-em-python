# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:

# Minha Resposta
ganhaHora = int(input('Quanto você ganha por hora: '))
horasTrabalhadas = int(input('Quantas horas trabalhadas no mês: '))

salarioBruto = ganhaHora * horasTrabalhadas

IR = 0.11
INSS = 0.08
sindicato = 0.05

IR = IR * salarioBruto
INSS = INSS * salarioBruto
sindicato = sindicato * salarioBruto
salarioLiquido = salarioBruto - IR - INSS - sindicato

print(
    f'Seu salário bruto é de R${salarioBruto:.2f}'
    ''
    f'O valor da IR é R${IR:.2f}'
    ''
    f'O valor da INSS é R${INSS:.2f}'
    ''
    f'O valor do sindicato é R${sindicato:.2f}'
    ''
    f'O seu salário liquido é de R${salarioLiquido:.2f}'
)


# Resposta

preco_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(
    input("Digite quantas horas você trabalhou esse mês: ")
)
salario_bruto = preco_hora * horas_trabalhadas
IR = salario_bruto * (11 / 100)
INSS = salario_bruto * (8 / 100)
sindicato = salario_bruto * (5 / 100)
salario_liquido = salario_bruto - IR - INSS - sindicato
print(
    f"+ Salário Bruto : R${salario_bruto:.2f}\n"
    f"- IR (11%) : R${IR:.2f}\n"
    f"- INSS (8%) : R${INSS:.2f}\n"
    f"- Sindicato (5%) : R${sindicato:.2f}\n"
    f"= Salário Liquido : R${salario_liquido:.2f}"
)

