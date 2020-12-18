def main():
    #Entrada
    a = float(input('Nota 1:  '))
    b = float(input('Nota 2:  '))
    c = float(input('Nota 3:  '))

    #Processamento
    media_ponderada = (a*2 + b*3 + c*5) / (2+3+5)

    #Saída
    print(f'MÉDIA = {media_ponderada:.1f}')







main()
