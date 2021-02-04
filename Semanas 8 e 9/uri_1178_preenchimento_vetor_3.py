def main():
    valor_x = float(input('Digite um número com 4 casas decimais: '))

    for p in range(0, 100):
        valor_x = valor_x / 2
        print(f'N[{p}] = {valor_x:.4f}')

main()