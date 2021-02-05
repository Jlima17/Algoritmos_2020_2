lista = [ ]

for i in range(20):    
    num = int(input('Insira um número inteiro positivo ou negativo: '))
    posicao = 0
    lista.append(num)

for y in lista[::-1]:
    posicao += 1
    print(f'N[{posicao}] = {y}')
   