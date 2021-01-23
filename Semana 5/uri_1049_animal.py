def main():
    #entrada
    p1 = str(input('Palavra 1: '))
    p2 = str(input('Palavra 2: '))
    p3 = str(input('Palavra 3: '))

    #processamento/saída
    if p1 == 'vertebrado' and p2 == 'ave' and p3 == 'carnivoro':
         print ('aguia')
    elif p1 == 'vertebrado' and p2 == 'ave' and p3 == 'onivoro':
        print('pomba')
    elif p1 == 'vertebrado' and p2 == 'mamifero' and p3 == 'onivoro':
        print('homem')
    elif p1 == 'vertebrado' and p2 == 'mamifero' and p3 == 'herbivoro':
        prnt('vaca')
    elif p1 == 'invertebrado' and p2 == 'inseto' and p3 == 'hematofago':
        print('pulga')
    elif p1 == 'invertebrado' and p2 == 'inseto' and p3 == 'herbivoro':
        print('lagarta')
    elif p1 == 'invertebrado' and p2 == 'anelideo' and p3 == 'hematofago':
        print('sanguessuga')
    else:
        print('minhoca')

main()