def main():
    #entrada
    n = int(input('Digite o tempo de duração em segundos: '))

    #processamento
    horas = n // 3600
    minutos = (n // 60) % 60
    segundos = n % 60
    


    #saida
    print(f'{horas}:{minutos}:{segundos}')



main()