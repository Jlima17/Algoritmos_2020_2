def main():
    entrada = input('Digite dois númreros: ')

    inf = entrada.split()
    x = int(inf[0])
    y = int(inf[1])


    while True:
        if x == y:
            break
        elif x > y:
            print(1*'Decrescente')
        else:
            print(1*'Crescente')
main() 