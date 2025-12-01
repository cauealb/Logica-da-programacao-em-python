# Faça um programa que leia e valide as seguintes informações:
#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd';

# Minha resposta
nome = input('Digite seu nome: \n')
while len(nome) < 3:
    nome = input('Nome inválido! Digite novamente: \n')


idade = int(input('Digite sua idade: \n'))
while idade < 0 or idade > 150:
    idade = int(input('Idade inválida! Digite novamente: \n'))


salario = float(input('Digite seu salário: \n'))
while salario <= 0:
    salario = float(input('Salário inválido! Digite novamente: \n'))


sexo = input('Digite seu sexo: \n')
while sexo != 'F' and sexo != 'M':
    sexo = input('Sexo inválido! Digite novamente: \n')


Es = input('Digite seu Estado Cívil: ')
while Es != 'S' and Es != 'C' and Es != 'V' and Es != 'D':
    Es = input('Estado cívil inválido! Digite novamente: \n')


# Reposta

nome = input("Digite o nome: ")
while len(nome) < 4:
    print("Nome inválido!")
    nome = nome = input("Digite o nome: ")

idade = int(input("Digite a idade: "))
while idade < 0 or idade > 150:
    print("Idade inválida!")
    idade = int(input("Digite a idade: "))

salario = int(input("Digite o salário: "))
while salario <= 0:
    print("Salario inválido!")
    salario = int(input("Digite a salário: "))

sexo = input("Digite o sexo (f ou m): ")
while sexo.lower() != "f" and sexo.lower() != "m":
    print("Sexo inválido!")
    sexo = input("Digite o sexo (f ou m): ")

estado_civil = input("Digite o estado civil (s, c, v, d): ").lower()
while (
    estado_civil != "s"
    and estado_civil != "c"
    and estado_civil != "v"
    and estado_civil != "d"
):
    print("Estado civil inválido!")
    estado_civil = input("Digite o estado civil (s, c, v, d): ")




