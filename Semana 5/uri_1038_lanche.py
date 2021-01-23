def main():
    #entrada
    linha = input('Entrada: ')
    

    dados = linha.split()
    cod = int(dados[0])
    qtd = int(dados[1])



    #processamento
    if cod == 1:
        total = 4.0 * qtd
        print(f'TOTAL R$: {total:.2f}')
    elif cod == 2:
        total = 4.50 * qtd
        print(f'TOTAL R$: {total:.2f} ')
    elif cod == 3:
        total = 5.00 * qtd
        print(f'TOTAL R$: {total:.2f}')
    elif cod == 4:
        total = 2.00 * qtd
        print(f'TOTAL R$: {total:.2f}')
    else:
        total = 1.50 * qtd
        print(f'TOTAL R$: {total:.2f}')




main()

