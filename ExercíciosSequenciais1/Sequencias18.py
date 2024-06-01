# Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo médio do carro, com três casas decimais. 

distancia = int(input('Distancia percorrida: '))
combustivel = float(input('Combustível gasto: '))

media = distancia / combustivel

print(
    f'Consumo média: {media:.3f}'
)