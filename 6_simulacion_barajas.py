import random
import collections

from bokeh.plotting import figure, show

PALOS = ['espada', 'corazon', 'rombo', 'trebol']

VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']


def chart(x, y, titulo, x_label, y_label):

    grafico = figure(title = titulo,
                     x_axis_label = x_label, y_axis_label = y_label)

    grafico.line(x, y)

    show(grafico)


def crear_baraja():

    baraja = []

    for palo in PALOS:
        for valor in VALORES:
            baraja.append((palo, valor))
    
    return baraja


def obtener_mano(barajas, tamaño_mano):

    mano = random.sample(barajas, tamaño_mano)

    return mano


def main(tamaño_de_mano, attemps):

    baraja = crear_baraja()

    manos = []

    for _ in range(attemps):
        mano = obtener_mano(baraja, tamaño_de_mano)
        manos.append(mano)
    
    return manos



# ======================================================

if __name__ == '__main__':

    TAMAÑO_MANO = 3
    ATTEMPS = [i for i in list(range(50000)) if i % 100 == 0 and i != 0]

    probabilidades = []

    for a in ATTEMPS:
        manos = main(TAMAÑO_MANO, a)

        pares = 0

        for mano in manos:
            valores = []

            for carta in mano:
                valores.append(carta[1])

            counter = dict(collections.Counter(valores))
        
            for valor in counter.values():

                if valor == 2:
                    pares += 1
                    break

        probabilidad_par = pares / a
        probabilidades.append(probabilidad_par)
    
    titulo = f'Probabilidad de obtener un par en una mano de {TAMAÑO_MANO} cartas'
    x_label = 'Número de simulaciones'
    y_label = 'Probabilidad de par'


    chart(ATTEMPS, probabilidades, titulo, x_label, y_label)
