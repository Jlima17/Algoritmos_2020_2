def main():
    #entrada
    linha = input('Coordenadas: ')

    dados = linha.split()
    x = float(dados[0])
    y = float(dados[1])

    #processamento/saída

    if x > 0 and y > 0:
        print('Q1')
    elif x < 0 and y > 0:
        print('Q2')
    elif x < 0 and y < 0:
        print('Q3')
    elif x > 0 and y < 0: 
        print('Q4')
    else:
        print('Origem')
    
main()