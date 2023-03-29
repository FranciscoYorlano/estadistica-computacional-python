# Standar library imports
import random

# Related third party imports
from bokeh.plotting import figure, show

# Local imports
from estadisticas import desviacion_estandar, media

# ============================================================================

def puntos_random(numero_puntos):
    ''' 
    'Lanza' agujas aleatoriamente en un espacio [-1,1]x[-1,1] perteneciente a
    R**2. Calcula cuantas de estas agujas 'caen' dentro de la circunsferencia 
    de radio 1 con centro en el origen. A partir de estos datos calcula una es-
    timacion del valor de pi.
    Return estimacion:float
    '''

    puntos_en_circunsferencia = 0
    
    for _ in range(numero_puntos):

        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])

        h = (x**2 + y**2)**0.5

        if h <= 1:
            puntos_en_circunsferencia += 1

    return ((4 * puntos_en_circunsferencia) / numero_puntos)


def simular(numero_puntos, attemps):
    '''
    Simula tantas veces como attemps el experimento de los puntos random.
    En base a los datos saca la media y la desviacion estandar.
    Return media:float, sigma:float
    '''

    estimaciónes_pi = []

    for _ in range(attemps):

        estimacion_pi = puntos_random(numero_puntos)
        estimaciónes_pi.append(estimacion_pi)

    # Calculo de probabilidades
    media_estimaciones = media(estimaciónes_pi)

    sigma_estimaciones = desviacion_estandar(estimaciónes_pi)

    print(f'Media (pi): {round(media_estimaciones, 5)} Sigma: {round(sigma_estimaciones, 5)} Puntos: {round(numero_puntos, 5)}')
    
    return (media_estimaciones, sigma_estimaciones)


def estimar_pi(precision, attemps):
    '''
    Ajusta la simulacion para ir ganando presicion
    Return media:float
    '''

    numero_puntos = 1000
    sigma = precision

    while sigma >= precision / 1.96:

        media, sigma = simular(numero_puntos, attemps)
        numero_puntos *= 2

    return media


# ============================================================================

if __name__ == '__main__':
    
    estimar_pi(0.01, 1000)