def main():
    num = int(input('Insira um número inteiro: '))
    t = 0

    for posicao in range(1000):
        t += 1
        if t == num:
            t = 0
        print(f'N[{posicao}] = {t}')


main()