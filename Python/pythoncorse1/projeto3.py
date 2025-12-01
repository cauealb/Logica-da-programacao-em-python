# Levando em consideraçãp a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuário um valor que representa à velocidade e com base nessa velocidade diga se ela tomou um multa leve, grave, grávissima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu deve exibir "Não houve multa", caso esteja até 10km acima, deve exibir "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir "Levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba "Levou multa gravissíma".

velocidadeMaxima = 80
velocidade = int(input('Qual foi sua velocidade? '))

if velocidade < velocidadeMaxima:
    print('Você não levou nenhuma multa!')
elif velocidade - velocidadeMaxima <= 10:
    print('Você levou multa leve!')
elif 11 <= (velocidade - velocidadeMaxima) <= 20:
    print('Você levou multa grave!')
elif velocidade > velocidadeMaxima + 21:
    print('Você levou multa gravissíma!!!!!!')