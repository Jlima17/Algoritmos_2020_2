par = [ ]
impar = [ ]

for i in range(15):
    num = int(input('Insira um número: '))
    if(num % 2 == 0):
        par.append(num)
    else:
        impar.append(num)
    
    if(len(par)==5):
        ix = 0
        for valor in par:
            par = [ ]
            ix += 1
            print(f'par[{ix}] = {valor}')
           
       
    if(len(impar)==5):
        ix = 0
        for valor in impar:
            impar = [ ]
            ix += 1
            print(f'impar[{ix}] = {valor}')
     
if(len(impar)> 0):
    ix = 0
    for valor in impar:
         ix += 1
         print(f'impar[{ix}] = {valor}')
     

if(len(par)>0):
    ix = 0
    for valor in par:
         ix += 1
         print(f'par[{ix}] = {valor}')
       