def main():
    #entrada
    entrada = input('Início e fim de jogo: ')

    inf = entrada.split()
    inicio = int(inf[0])
    fim = int(inf[1])

    #processamento/saida

    if inicio < fim:
        tempo = fim - inicio
        print(f'O JOGO DUROU {tempo} HORA(S)')
    elif inicio > fim:
        tempo = (24 - inicio) + fim
        print(f'O JOGO DUROU {tempo} HORA(S)')
    else:
        tempo = 24
        print(f'O JOGO DUROU {tempo} HORA(S)')
    




main()