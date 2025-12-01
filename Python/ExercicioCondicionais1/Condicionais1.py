# Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 60.00, mostrar a mensagem "REPROVADO", conforme exemplos. 

# 1. Primeiro semestre e segundo semestre.
# 2. Somar as notas e ver se está resprovado ou aprovado.
# 3. Preciso colocar a nota final com duas casas decimais
# 4. Ver se for aprovado

semestre1 = float(input('Nota do 1º semestre: '))
semestre2 = float(input('Nota do 2º semestre: '))

resultado = semestre1 + semestre2

if resultado < 60.00:
    print('Reprovado!')
    print(f'Nota: {resultado}')
else:
    print('Aprovado!')
    print(f'Nota: {resultado}')

