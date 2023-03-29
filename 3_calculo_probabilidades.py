# Standar library imports
import random

# Related third party imports
from bokeh.plotting import figure, show


# ============================================================================

def chart(x, y):

    grafico = figure(title='Frecuencia relativa de sacar un determinado número con un dado',
                     x_axis_label='Número de lanzamientos', y_axis_label='Frecuencia relativa')

    grafico.line(x, y)

    show(grafico)


def tirar_dado():
    
    tiro = random.choice([1,2,3,4,5,6])

    return tiro


def simular_tiros(tiros):

    tiros_tres = 0

    for _ in range(tiros):

        tiro = tirar_dado()

        if 3 == tiro:
            tiros_tres += 1
    
    return tiros_tres


# ============================================================================


def main(attemps):

    probabilidades = []

    for a in attemps: 

        tiros_tres = simular_tiros(a)

        try:
            probabilidad_de_tres = tiros_tres / a
        except ZeroDivisionError:
            probabilidad_de_tres = 0

        probabilidades.append(probabilidad_de_tres)


    chart(attemps, probabilidades)


# ============================================================================
if __name__ == '__main__':

    attemps = list(range(100000))
    attemps = [a for a in attemps if a%100 == 0 and a != 0]


    main(attemps)