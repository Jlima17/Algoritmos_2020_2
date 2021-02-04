def main():
    num = int(input('Numero inteiro: '))

    print(f'N[{0}]= {num}')

    for posicao in range(1, 10):
        num *= 2
        print(f'N[{posicao}] = {num}')


main()