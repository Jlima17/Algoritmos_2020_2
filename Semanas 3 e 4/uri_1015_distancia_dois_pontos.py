def main():
    #entrada
    linha1 = input('Insira os valores de x1 e y1: ')
    linha2 = input('Insira os valores de x2 e y2: ')

    dados1 = linha1.split()
    x1 = float(dados1[0])
    y1 = float(dados1[1])

    dados2 = linha2.split()
    x2 = float(dados2[0])
    y2 = float(dados2[1])

    #processamento
    distancia = calcular_distancia(x1, y1, x2, y2)

    #saida
    print(f'{distancia:.4f}')


def calcular_distancia(x1, y1, x2, y2):
    resultado = ((x2 - x1)**2 + (y2 - y1)**2) ** (1/2)
    return resultado



main()
