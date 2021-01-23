def main():
    #entrada
    entrada = input('Hora/minuto inicial e hora/minuto final: ')

    inf = entrada.split()
    hi = int(inf[0])
    mi = int(inf[1])
    hf = int(inf[2])
    mf = int(inf[3])

    #processamento/saida
    if hi < hf:
        hora = hf - hi
        if mi < mf:
            minuto = mf - mi
        elif mi > mf:
            hora = hora - 1
            minuto = (60 - mi) + mf
        else:
            minuto = 0
    elif hi > hf:
        hora = (24 - hi) + hf
        if mi < mf:
            minuto = mf - mi
        elif mi > mf:
            hora = hora - 1
            minuto = (60 - mi) + mf
        else:
            minuto = 0
    elif hi == hf:
        if mi < mf:
            minuto = mf - mi
            hora = 0
        elif mi > mf:
            minuto = (60 - mi) + mf
            hora = 23
        else:
            minuto = 0
            hora = 24
    print(f'O JOGO DUROU {hora} HORA(S) e {minuto} MINUTO(S)')


main()