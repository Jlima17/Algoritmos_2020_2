def main():
    num = int(input('Digite um número inteiro: '))

    for n in range(1, num + 1):
        if num % n == 0:
             print(n)


main()