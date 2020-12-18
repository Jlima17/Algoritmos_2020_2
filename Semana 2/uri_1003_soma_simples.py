def main():
    #Entrada
    A = int(input('Digite o valor de A: '))
    B = int(input('Digite o valor de B: '))

    #Processamento
    soma = soma_calculo(A, B)

    #Saída
    print(f'SOMA = {soma}')


def soma_calculo(A, B):
    resultado = A + B
    return resultado




main()