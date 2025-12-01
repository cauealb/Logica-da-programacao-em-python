# Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago. 

valor = int(input('Quantos minutos ficou: '))

if valor <= 100:
    print('Valor a pagar: R$50.00')
else:
    resultado = valor - 100
    resultado = resultado * 2
    resultado = resultado + 50
    print(f'Valor a Pagar: R${resultado:.2f}')