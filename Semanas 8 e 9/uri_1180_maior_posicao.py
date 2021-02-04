def main():
    num = int(input('Quantidade de números: '))

    entrada = input('Números: ')
    inf = entrada.split()
    n1 = int(inf[0])
    n2 = int(inf[1])
    n3 = int(inf[2])
    n4 = int(inf[3])
    n5 = int(inf[4])
    n6 = int(inf[5])
    n7 = int(inf[6])
    n8 = int(inf[7])
    n9 = int(inf[8])
    n10 = int(inf[9])

    pos = 0
    menor = inf[0]
    con = 0

    for valor in inf:
        if valor < menor:
            menor = valor
            pos = con
        con += 1

    print(f'Menor valor: {menor}')
    print(f'Posção: {pos}')

    

main()