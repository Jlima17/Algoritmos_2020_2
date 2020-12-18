def main():
    #Entrada
    identificacao = int(input('ID: '))
    hora = int(input('Hora: '))
    valor_hora = float(input('Valor da hora: '))

    #Processamento
    salario = calcular_salario(hora,valor_hora)

    #Saída
    print(f'Number = {identificacao}')
    print(f'Salary = U$ {salario:.2f}')


def calcular_salario(hora,valor_hora):
    resultado = hora * valor_hora
    return resultado


main()