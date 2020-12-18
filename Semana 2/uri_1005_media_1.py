def main():
    #Entrada
    A = float(input('Nota 1: '))
    B = float(input('Nota 2: '))

    #Processamento
    media = calculo_da_media(A, B)

    #Saída
    print(f'MEDIA = {media:.5f}')


def calculo_da_media(A, B):
    resultado = (A*3.5 + B*7.5) / 11
    return resultado




main()