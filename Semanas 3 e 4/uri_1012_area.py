def main():
    #entrada
    linha = input('Dados: ')

    dados = linha.split()
    a = float(dados[0])
    b = float(dados[1])
    c = float(dados[2])

    #processamento
    triangulo = area_triangulo(base = a, altura = c) 
    circulo = area_circulo(raio = c)
    trapezio = area_trapezio(base1 = a, base2 = b, altura = c) 
    quadrado = area_quadrado(b)
    retangulo = area_retangulo(a, b)

    #saída
    print(f'TRIANGULO: {triangulo:.3f}')
    print(f'CIRCULO: {circulo:.3f}')
    print(f'TRAPEZIO: {trapezio:.3f}')
    print(f'QUADRADO: {quadrado:.3f}')
    print(f'RETANGULO: {retangulo:.3f}')


def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def area_circulo(raio):
    area = 3.14159 * (raio**2)
    return area

def area_trapezio(base1, base2, altura):
    area = ((base1+base2)) * altura / 2
    return area

def area_quadrado(b):   # def area_quadrado(lado):
    area = b * b        # area = area_retangulo(lado, lado)
    return area

def area_retangulo(lado1, lado2):
    area = lado1 * lado2
    return area





main()