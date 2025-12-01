# Calculadora de Tarifas de Táxi
# Descrição: Escreva um programa que calcule a tarifa de um táxi com base na distância percorrida. A tarifa deve ser calculada conforme as seguintes regras:

# Tarifa fixa de R$ 5,00 para as primeiras 2 milhas. ===
# R$ 2,00 por milha adicional.
# 20% de acréscimo para corridas durante a noite (entre 22h e 6h).
# Inclua verificações para garantir que a entrada seja válida e que a tarifa mínima seja de R$ 5,00.

milha = int(input('Quantas milhas vai percorrer: '))
horario = int(input('Quantas horas são: '))

if not milha > 2:
    total = milha * 5
    print()
else:
    primeiraMilha = (milha - (milha - 2)) * 5
    milha = (milha - 2) * 2
    total = milha + primeiraMilha
    
if not horario > 22 and not horario > 6: #04
    total = total + (total * 0.2)
    print(f'Sua tafifa deu R${total}')
else:
    print(f'Sua tafifa deu R${total}')