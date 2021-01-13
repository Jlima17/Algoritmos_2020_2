def main():
    #entrada
    d = int(input('Insira a distância(em Km): '))

    #processamento
    km_m = d*1000
    tempo = (km_m * 2)/1000

    #saida
    print(f'{tempo:.0f} minutos')




main()