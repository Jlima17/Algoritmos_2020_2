def main():
    #entrada
    valor = int(input('Valor: '))

    #processamento
    cedulas100 = valor // 100
    valor = valor % 100

    cedulas50 = valor // 50
    valor = valor % 50

    cedulas20 = valor // 20
    valor = valor % 20

    cedulas10 = valor // 10
    valor = valor % 10

    cedulas5 = valor // 5
    valor = valor % 5

    cedulas2 = valor // 2
    valor = valor % 2

    cedulas1 = valor 


    #saida
    print(f'{cedulas100} nota(s) de R$ 100,00')
    print(f'{cedulas50} nota(s) de R$ 50,00')
    print(f'{cedulas20} nota(s) de R$ 20,00')
    print(f'{cedulas10} nota(s) de R$ 10,00')
    print(f'{cedulas5} nota(s) de R$ 5,00')
    print(f'{cedulas2} nota(s) de R$ 2,00')
    print(f'{cedulas1} nota(s) de R$ 1,00')



main()