def main():
    #entrada
    x = int(input('Distância em Km: '))
    y = float(input('Combustível gasto em litros: '))

    #processamento
    consumo = consumo_medio(x, y)

    #saída
    print(f'{consumo:.3f} Km/l')

 
def consumo_medio(x,y):
    calculo = x / y
    return calculo



main()