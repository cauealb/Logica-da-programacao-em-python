# Calculadora de Horas Extras
# Descrição: Escreva um programa que calcule o salário semanal de um funcionário, considerando horas extras. As horas extras são pagas a 1.5 vezes a taxa horária regular para todas as horas trabalhadas além de 40 horas semanais. Use condicionais para verificar e calcular o pagamento adequado. 

salario = int(input('Quanto ganha: '))
horas  = int(input('Quantas horas trabalhadas na semana: '))

if not horas < 40:
    extras = horas - 40
    calculoExtras = extras * 1.5
    total = salario + calculoExtras
    print(f'Você ganhou nessa(s) {extras} hora(s) extras R${calculoExtras:.2f}, ou seja, R${total:.2f}')
else:
    conta = salario / (4 * horas)
    print(f'Você ganha por hora R${conta:.2f}')

