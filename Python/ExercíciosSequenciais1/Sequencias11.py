# Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida, o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com duas casas decimais, conforme exemplo. 

# 1. A largura, o comprimento e o metro quadro
# 2. Calcular medidas do terreno e ver o Area do terreno e o Valor dele
# 3. A largura e o comprimeto com uma casa decimal, o metro quadrado com duas casas decimais, e o resultados com duas casas decimais.
# 4. O calculo da da area e do preço do terreno

largura = float(input('Qual é a largura do seu terreno: '))
comprimento = float(input('Qual é o comprimento do seu terreno: '))
metroQuadrado = float(input('Qual é o metro quadrado do seu terreno: '))

area = largura * comprimento
valor = area * metroQuadrado

print(
    f'Largura: {largura:.1f} \n'
    f'Comprimento: {comprimento:.1f} \n'
    f'Metro Quadrado: {metroQuadrado:.2f} \n'
    f'Área: {area:.2f} \n'
    f'Valor: {valor:.2f}'     
      )
