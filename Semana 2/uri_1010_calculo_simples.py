def main():
    #Entrada
    linha1 = input('Peça 1: ')
    linha2 = input('Peça 2: ')

    dados1 = linha1.split()
    cod1 = int(dados1[0])
    qtd1 = int(dados1[1])
    valor1 = float(dados1[2])
      

    dados2 = linha2.split()
    cod2 = int(dados2[0])
    qtd2 = int(dados2[1])
    valor2 = float(dados2[2])
  
    #Processamento
    total = qtd1*valor1 + qtd2*valor2

    #Saída
    print(f'VALOR A PAGAR: R$ {total:.2f}')







main()