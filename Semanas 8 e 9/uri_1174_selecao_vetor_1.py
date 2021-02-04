def main():
    a = float(input('Insira um valor inteiro, real, positivo ou negativo: '))

    for posicao in range(0, 100):
        if (a <= 10):
            print(f'A[{posicao}] = {a}')

main()