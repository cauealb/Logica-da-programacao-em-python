# O custo ao consumidor de um carro novo e a soma do custo de fábrica, da comissão do distribuidor, e dos impostos. A comissao e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.

# CUSTO DE FABRICA               % DO DISTRIBUIDOR                 % DOS IMPOSTOS
# ate R$12.000,00                        5                             isento
# entre R$12.000,00 e 25.000,00         10                               15
# acima de R$25.000,00                  15                               20

valor = float(input('Qual seria o valor do seu carro: '))

if valor < 12000:
    distribuidor = valor * 0.05
    total = valor + distribuidor

if valor >= 12000 and valor < 25000:
    distribuidor = valor * 0.1
    imposto = valor * 0.15
    total = valor + distribuidor + imposto

if valor >= 25000:
    distribuidor = valor * 0.15
    imposto = valor * 0.2
    total = valor + distribuidor + imposto

print(f'Valor total a ser pago: R${total:.2f}')