def main():
    #entrada
    num = input('Digite três número: ')

    dados1 = num.split()
    a = int(dados1[0])
    b = int(dados1[1])
    c = int(dados1[2])

    #processamento
    maior_ab = (a + b + abs(a - b))/2
    maior_abc = (maior_ab + c + abs(maior_ab - c))/2
    maior = int(maior_abc)

    #saida
    print(f'{maior} eh o maior')



main()