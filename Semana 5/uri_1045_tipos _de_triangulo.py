def main():
    #entrada
    linha = input('Dados: ')

    dados = linha.split()
    a = float(dados[0])
    b = float(dados[1])
    c = float(dados[2])

    #processamento/saida
    if a >= b + c:
        print('NAO FORMA TRIANGULO')
    else:
        if (a ** 2) == (b ** 2 + c ** 2):
            print('TRIANGULO RETANGULO')
        elif(a ** 2) > (b ** 2 + c ** 2) < 9.0:
            print('TRIANGULO OBTUSANGULO')
        elif (a ** 2) < (b ** 2 + c ** 2) == 9.0:
            print('TRIANGULO ACUTANGULO')
        elif (a == b == c):
            print('TRIANGULO EQUILATERO')
        elif a == b != c or b == c != a or a == c != b:
            print('TRIANGULO ISOSCELES')

main()