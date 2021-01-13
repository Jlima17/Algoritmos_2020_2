def main():
    #entrada
    pi = 3.14159
    r = float(input('Raio: '))

    #processamento
    v = calcular_volume_esfera(pi, r)

    #saída
    print(f'VOLUME = {v:.3F}')


def calcular_volume_esfera(pi, r):
    formula = ((4/3) * pi * (r**3))
    return formula 



main() 