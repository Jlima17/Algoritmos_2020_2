def main():
    #entrada
    entrada = input('Insira dois números inteiros: ')

    inf = entrada.split()
    a = int(inf[0])
    b = int(inf[1])
    
    #processamento/saída
    if a > b:
        if a % b == 0:
            print('São Multiplos')
        else:
            print('Não são multiplos')
    if a < b:
        if b % a == 0:
            print('São Multiplos')
        else:
            print('Não são Multiplos')
    if a == b:
            print('São Multiplos')
    



main()