import random
from bokeh.plotting import figure, show



def media(X):

    return sum(X) / len(X)
  

def varianza(X):

    mu = media(X)

    acumulador = 0

    for x in X:
        acumulador += (x - mu)**2

    return acumulador / len(X)


def desviacion_estandar(X):

    return (varianza(X)**0.5)


def chart(attemps, media, varianza, desviacion_e):

    grafico = figure(title='Media, varianza y desviacion estandar de una lista de números random del 0 al 100',
                     x_axis_label='Longitud de la lista')

    grafico.circle(attemps, media, legend_label='Media')
    grafico.circle(attemps, varianza, legend_label='var(X)', color='green')
    grafico.circle(attemps, desviacion_e, legend_label='Desviación estandar', color='orange')

    show(grafico)


# ===================================================================
if __name__ == "__main__":

    mu_array, var_array, sigma_array = [], [], []

    attemps = list(range(1000))
    attemps = [i for i in attemps if i%100 == 0 and i != 0]

    for a in attemps:

        X = [random.randint(0,100) for i in range(a)]

        mu = media(X)
        mu_array.append(mu)

        var = varianza(X)
        var_array.append(var)

        sigma = desviacion_estandar(X)
        sigma_array.append(sigma)
        
    chart(attemps, mu_array, var_array, sigma_array)