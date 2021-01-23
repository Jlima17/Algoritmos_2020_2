def main():
    #entrada
    r = float(input('Renda: '))

    #processamneto/saida

    if r < 2000.00:
        print('Isento')
    elif 2000.00 < r <= 3000.00:
        renda8 = r - 2000
        imposto8 = renda8 * (8/ 100)
        print(f'R$: {imposto8:.2f}')
    elif 3000.00 < r <= 4500.00:
        taxa8 = (8/100) * (1000.00)
        renda18 = r - 3000.00
        imposto18 = renda18 * (18/100) + taxa8
        print(f'R$: {imposto18:.2f}')
    else:
        taxa8 = (8/100) * (1000.00)
        taxa18 = (18/100) * (1500.00)
        renda28 = r - 4500
        imposto28 = taxa8 + taxa18 + renda28 * (28/100)
        print(f'R$: {imposto28:.2f}')

    
main()