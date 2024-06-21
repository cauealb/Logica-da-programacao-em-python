# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um

# Minha resposta
cd = int(input('Digite quantos CDs são: '))
total = 0

for i in range(1, cd + 1):
    valor = float(input(f'Valor do CD {i}: '))
    total += valor
    media = total / cd


print(
    f'\nO valor total dos CDs: R${total:.2f} \n'
    f'Média gasta: R${media:.2f}'
      )


# Resposta
cds = int(input("Digite a quantidade de CDs: "))
preco = 0
for i in range(cds):
    preco += float(input(f"Digite o preço do CD {i+1}: "))
print(f"Preço total: R${preco:.2f}\nMédia de custo por CD: R${preco/cds:.2f}")