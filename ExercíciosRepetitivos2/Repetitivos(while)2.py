# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

# Resposta
usu = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')
while senha == usu:
    senha = input('Senha errada! Digite novamente: ')
print('Sua conta foi acessada com sucesso!')


# Minha resposta
usuario = input("Digite o nome de usuario: ")
senha = input("Digite a senha: ")
while usuario == senha:
    print("Nome de usuario nao pode ser igual a senha!")
    usuario = input("Digite o nome de usuario: ")
    senha = input("Digite a senha: ")