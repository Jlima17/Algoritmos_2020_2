def main():
    num = int(input('Quantidade de médias: '))

    for i in range(num):
        numeros = input('Médias: ')
        dados = numeros.split()
        n1 = float(dados[0])
        n2 = float(dados[1])
        n3 = float(dados[2])
       
       
        media = (n1*2 + n2*3 + n3*5) / (2 + 3 + 5)
        print(f'{media:.1f}')



main()