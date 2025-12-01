# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

# Bolsonabo = 1
# 9 Dedos = 2
# Padre = 3

eleitor = int(input('Digite quantos eleitores são: '))
total = 0
bolsonabo = dedos9 = padre = 0
parar = True

for i in range(1, eleitor + 1):
    votos = int(input('Digite seu voto: '))

    while votos != 1 and votos != 2 and votos != 3:
        votos = int(input('Voto errado! Digite novamente (entre 1 a 3): '))
    
    if votos == 1:
        bolsonabo += 1
    elif votos == 2:
        dedos9 += 1
    else:
        padre += 1


print(
    f'\nVotos de Bolsonabo: {bolsonabo} \n'
    f'Votos do 9 Dedos: {dedos9} \n'
    f'Votos do Padre: {padre} \n'
)
    


# Resposta

votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0
eleitores = int(input("Digite o numero de eleitores: "))
for i in range(eleitores):
    voto = input(
        "Digite o numero (1/2/3) do candidato em quem o "
        f"eleitor {i + 1} quer votar: "
    )
    if voto == "1":
        votos_candidato_1 += 1
    if voto == "2":
        votos_candidato_2 += 1
    if voto == "3":
        votos_candidato_3 += 1

print(
    "Votação encerrada"
    f"\nCandidato 1: {votos_candidato_1} voto(s)"
    f"\nCandidato 2: {votos_candidato_2} voto(s)"
    f"\nCandidato 3: {votos_candidato_3} voto(s)"
)