def main():
    #entrada
    num = int(input('Idade de uma pessoa em dias:  '))

    #processamento
    anos = num // 365
    meses = (num // 30) % 12
    dias = (num - anos * 365) - (meses * 30)

    #saída
    print(f'{anos} ano (s)')
    print(f'{meses} mês (es)')
    print(f'{dias} dia (s)')


main()