def main():
    #entrada
    entrada = input('Insira 3 três números inteiros: ')

    inf = entrada.split()
    a = int(inf[0])
    b = int(inf[1])
    c = int(inf[2])

    #processamento/saida
    if a > b and a > c:
        x = a
        if b > c:
            y = b
            z = c
        else:
            y = c
            z = b
    elif b > a and b > c:
        x = b
        if a > c:
            y = a
            z = c
        else:
            y = c
            z = a
    else:
        x = c
        if a > b:
            y = a
            z = b
        else:
            z = a
            y = b
    print(f'{z}\n{y}\n{x}')
    print(' ')
    print(f'{a}\n{b}\n{c} ')



   

    

    
        
main()