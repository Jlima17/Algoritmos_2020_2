def main():
    #entrada
    salario = float(input('Salário do funcionário: '))

    #processamento/saida
    if salario <= 400.00:
        s_novo15 = salario * 1.15
        reajuste15 = (s_novo15 - salario)
        por15 = 15
        print(f' Novo salario: {s_novo15:.2f}\n Reajuste ganho: {reajuste15:.2f}\n Em percentual: {por15} % ')
    elif 400.01 <= salario <= 800.00:
        s_novo12 = salario * 1.12
        reajuste12 = (s_novo12 - salario)
        por12 = 12
        print(f' Novo salario: {s_novo12:.2f}\n Reajuste ganho: {reajuste12:.2f}\n Em percentual: {por12} % ')
    elif 800.01 <= salario <= 1200.00:
        s_novo10 = salario * 1.10
        reajuste10 = (s_novo10 - salario)
        por10 = 10
        print(f' Novo salario: {s_novo10:.2f}\n Reajuste ganho: {reajuste10:.2f}\n Em percentual: {por10} % ')
    elif 1200.01 <= salario <= 2000.00:
        s_novo7 = salario * 1.07
        reajuste7 = (s_novo7 - salario)
        por7 = 7
        print(f' Novo salario: {s_novo7:.2f}\n Reajuste ganho: {reajuste7:.2f}\n Em percentual: {por7} % ')
    else:
        s_novo4 = salario * 1.04
        reajuste4 = (s_novo4 - salario)
        por4 = 4
        print(f' Novo salario: {s_novo7:.2f}\n Reajuste ganho: {reajuste7:.2f}\n Em percentual: {por7} % ')

main()