# Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o número 4, devendo então mostrar a mensagem "MUITO OBRIGADO", bem como as quantidades de cada combustível. 

parar = True
alcool = 0
gasolina = 0
diesel = 0

while parar == True:
    resp = int(input('Informe um codigo (1, 2, 3) ou 4 para parar: '))

    match resp:
        case 1:
            alcool += 1
        case 2:
            gasolina += 1
        case 3:
            diesel += 1
        case 4:
            print('MUITO OBRIGADO!')
            parar = False


print(
      f'Álcool: {alcool} \n'
      f'Gasolina: {gasolina} \n'
      f'Diesel: {diesel} \n'
      )






    