# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas

inicial = int(input('Hora inicial: '))
final = int(input('Hora final: '))


# Outro dia
if inicial > final:
    inicial = 24 - inicial

    conta =  inicial + final

    print(f'O JOGO DUROU {conta:.0f} HORA(S)')
# Mesmo dia
elif final > inicial:
    conta = final - inicial

    print(f'O JOGO DUROU {conta:.0f} HORA(S)')