def main():
    #entrada
    linha = input('Notas: ')

    dados = linha.split()
    n1 = float(dados[0])
    n2 = float(dados[1])
    n3 = float(dados[2])
    n4 = float(dados[3])

    #processamento/saída
    mp = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / (2+3+4+1)
    print(f'Media: {mp:.1f}')

    if mp >= 7.0:
        print('Aluno aprovado')
    elif mp < 5.0:
        print('Aluno reprovado')
    else:
        print('Aluno em exame')
        
   
    n_exame = float(input('Nota do Exame: '))

    media_final = (mp + n_exame) / 2

    if media_final > 5.0:
        print('Aluno aprovado')
        
    else: 
        print('Aluno reprovado')

    print(f'Media final: {media_final:.1f}')


       


main()