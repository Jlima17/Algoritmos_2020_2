def main():
    #entrada
    linha = input('Digite 3 números reais: ')
    
    entrada = linha.split()
    a = float(entrada[0])
    b = float(entrada[1])
    c = float(entrada[2])

    #processamento/saída
    if (a + b > c and b + c > a and a + c > b ):
        perimetro = a + b + c
        print(f'Parimetro: {perimetro:.1f}')
    else:
        area = ((a + b) * c) / 2
        print(f'Area: {area:.1f}')

main()