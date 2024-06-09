# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
# descontos são do Imposto de Renda, que depende do salário bruto
# (conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do
# Salário Bruto, mas não é descontado (é a empresa que deposita).

# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
# trabalhadas no mês.

# Desconto do IR:
#     Salário Bruto até 900 (inclusive) - isento
#     Salário Bruto até 1500 (inclusive) - desconto de 5%
#     Salário Bruto até 2500 (inclusive) - desconto de 10%
#     Salário Bruto acima de 2500 - desconto de 20%

# Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

valorHora = int(input('Qual o valor da sua hora: '))
qtdHoras = int(input('Quantas horas trabalhadas no mês: '))

salario = valorHora * qtdHoras

if salario < 900:
    IR = 0
    INSS = salario * 0.1
    FGTS = salario * 0.11
    desconto = INSS
    total = salario - desconto
else:
    if salario < 1500:
        IR = salario * 0.05
        INSS = salario * 0.1
        FGTS = salario * 0.11
        desconto = IR + INSS
        total = salario - desconto
    else:
        if salario < 2500:
            IR = salario * 0.1
            INSS = salario * 0.1
            FGTS = salario * 0.11
            desconto = IR + INSS
            total = salario - desconto
        else:
            IR = salario * 0.2
            INSS = salario * 0.1
            FGTS = salario * 0.11
            desconto = IR + INSS
            total = salario - desconto


print(
    f'Salário Bruto: R${salario:.2f} \n'
    f'IR: {IR:.2f} \n'
    f'INSS: R${INSS:.2f} \n'
    f'FGTS: R${FGTS:.2f} \n'
    f'Total de Descontos: R${desconto:.2f} \n'
    f'Salário Liquido: R${total:.2f} \n'
)




valor_da_hora = float(input("Digite quanto você recebe por hora: "))
horas_trabalhadas = float(
    input("Digite quantas horas você trabalhou esse mês: ")
)
salario_bruto = valor_da_hora * horas_trabalhadas
if salario_bruto <= 900:
    desconto_ir = 0.0
elif salario_bruto <= 1500:
    desconto_ir = 5
elif salario_bruto <= 2500:
    desconto_ir = 10
else:
    desconto_ir = 20

IR = salario_bruto * (desconto_ir / 100)
INSS = salario_bruto * (10 / 100)
FGTS = salario_bruto * (11 / 100)
total_de_descontos = IR + INSS
salario_liquido = salario_bruto - total_de_descontos

print(
    f"\nSalário Bruto     : R${salario_bruto:.2f}",
    f"\n(-) IR (5%)       : R${IR:.2f}",
    f"\n(-) INSS ( 10%)   : R${INSS:.2f}",
    f"\nFGTS (11%)        : R${FGTS:.2f}",
    f"\nTotal de descontos: R${total_de_descontos:.2f}",
    f"\nSalário Liquido   : R${salario_liquido:.2f}",
)