# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
vetorAl = []
vetorId = []

for i in range(1, 6):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    vetorId.append(idade)
    altura = float(input('Digite sua altura: '))
    vetorAl.append(altura)

vetorAl = vetorAl[::-1]
vetorId = vetorId[::-1]

print('Alturas e Idade\n')

cont = 0
while cont < 5:
    print(f"A pessoa mede {vetorAl[cont]:.2f}cm e tem {vetorId[cont]} ano(s)")
    cont += 1


# Resposta

PESSOAS = 5
idades = []
alturas = []
for i in range(PESSOAS):
    idades.append(int(input(f"Digite a idade da pessoa {i+1}: ")))
    alturas.append(float(input(f"Digite a altura da pessoa {i+1} em cm: ")))

# ? i começa em 4 e vai até 0 de forma decrescende
for i in range(PESSOAS - 1, -1, -1):
    print(f"A pessoa {i+1} mede {alturas[i]:.2f}cm e tem {idades[i]} ano(s)")