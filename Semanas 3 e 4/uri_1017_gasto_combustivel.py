def main():
    #entrada
    tempo = int(input('Tempo gasto na viagem(em horas): '))
    vel_media = int(input('Velocidade média durante a viagem (Km/h): '))
    vel_automovel = 12 #Km/l 

    #processamento
    distancia = calcular_distancia(tempo, vel_media)
    q_litros = quantidade_litros (distancia, vel_automovel)

    #saida
    print(f'{q_litros:.3f}')

def calcular_distancia(tempo, vel_media):
    calculo1 = tempo * vel_media
    return calculo1

def quantidade_litros(distancia, vel_automovel):
    calculo2 = distancia / vel_automovel
    return calculo2



main()