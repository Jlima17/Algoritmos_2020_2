def main():
    #Entrada
    nome = str(input('Nome do vendedor: '))
    s_fixo = float(input('Salário fixo: '))
    vendas = float(input('Total de vendas/mês em R$: '))

    #Processamento
    bonus = vendas * 0.15
    salario_real = s_fixo + bonus

    #Saída
    print(f'TOTAL = {salario_real:.2f}')



    












main()