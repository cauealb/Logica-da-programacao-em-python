# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

pa = int(input('Digite o número de habitantes no País A: \n'))
while pa < 0:
    pa = int(input('Número inválido! Digite novamente: \n'))


porA = int(input('Digite a porcentagem de crescimento no País A: \n'))
while porA < 0:
    porA = int(input('Porcentagem inválido! Digite novamente: \n'))



pb = int(input('Digite o número de habitantes no País B: \n'))
while pb < 0:
    pb = int(input('Número inválido! Digite novamente: \n'))


porB = int(input('Digite a porcentagem de crescimento no País B: \n'))
while porB < 0:
    porB = int(input('Porcentagem inválido! Digite novamente: \n'))

anos = 0

while pa < pb:
    anos += 1
    pa = pa * (1 + (porA / 100))
    pb = pb * (1 + (porB / 100))

print(
    f'Precisou de {anos} anos para o País A alcaçar o País B\n'
    f'Habitantes no País A: {pa:.0f} \n'
    f'Habitantes no País B: {pb:.0f} \n'
        )










# Resposta

continuar = True
while continuar:
    populacao_a = float(input("Digite a população de A: "))
    populacao_b = float(input("Digite a população de B: "))
    crescimento_a = float(
        input("Digite o crescimento percentual da população de A: ")
    )
    crescimento_b = float(
        input("Digite o crescimento percentual da população de B: ")
    )
    anos = 0
    while True:
        anos += 1
        populacao_a *= 1 + (crescimento_a / 100)
        populacao_b *= 1 + (crescimento_b / 100)
        if populacao_a >= populacao_b:
            print(
                f"Demorou {anos} anos para a população de "
                "A passar ou igualar a de B."
                f"\nA tem {populacao_a:.0f} habitantes e "
                f"B tem {populacao_b:.0f}."
            )
            break
    continuar = (
        True if input("Deseja continuar (S/N)? > ").upper() == "S" else False
    )