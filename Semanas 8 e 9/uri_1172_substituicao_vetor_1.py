def main():
    for posicao in range(10):
        x = int(input('Número: '))
        if x < 1:
            x = 1
        print(f'X[{posicao}] = {x}')

main()