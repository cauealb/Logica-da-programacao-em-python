# Escreva um programa que valide uma senha conforme os seguintes critérios:

# A senha deve ter pelo menos 8 caracteres. facil
# Deve conter pelo menos uma letra maiúscula. ==
# Deve conter pelo menos uma letra minúscula. ==
# Deve conter pelo menos um número. ==
# Deve conter pelo menos um caractere especial (como !, @, #, $, etc.). ==
# O programa deve informar ao usuário quais critérios não foram atendidos.

import re

print('Bem-Vindo ao seu validador de códigos: \n')
senha = input('Digite sua senha: ')

separador = list(senha)
contador = 0

tem_numero = any(char.isdigit() for char in separador)
tem_maiuscula = any(char.isupper() for char in separador)
tem_minuscula = any(char.islower() for char in separador)
tem_especiais = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
tem_especial = any(char in tem_especiais for char in senha)


if not tem_numero:
    print('Sua senha não tem número!')
    contador += 1

if not tem_maiuscula:
    print('Sua senha não tem letras maiúsculas!')
    contador += 1

if not tem_minuscula:
    print('Sua senha não tem letras minúsculas!')
    contador += 1

if not tem_especial:
    print('Sua senha não tem caracteres especiais!')
    contador += 1

if not len(separador) >= 8:
    print('Sua senha tem que ter no mínimo 8 caracteres')
    contador += 1
        

if not contador >= 1:
    print('Sua está certa e foi corrigida com sucesso!')