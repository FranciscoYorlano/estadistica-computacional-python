# Standar library imports

# Related third party imports
from bokeh.plotting import figure, show

# Local imports
from borracho import BorrachoTradicional, DrunkHigh
from coordinate import Coordinate
from field import Field


ATTEMPS = [1]
STEPS = 1000

# GRAPH FUNCTIONS ============================================================

def chart(x, y, attemps):

    graph = figure(title=f'Simulate random walk {attemps} attemps', x_axis_label='steps',
                   y_axis_label='average distance walking')

    graph.line(x, y, legend_label='average distance')

    show(graph)


def _graph_walking(x_array, y_array):

    graph = figure(title=f'BorrachoTradicional {STEPS} steps, {ATTEMPS} attemps ')
    graph.line(x_array, y_array)
    show(graph)


# WALKING FUNCTION ===========================================================

def walking(field, borracho, steps):
    '''
    Move borracho x steps
    Return distance between star and last coordinate
    '''

    start = field.get_coordinate(borracho)

    x_list = []
    y_list = []

    for _ in range(steps):
        field.move_borracho(borracho)


        x_list.append(field.borrachos_coordinates[borracho].x)
        y_list.append(field.borrachos_coordinates[borracho].y)

    _graph_walking(x_list, y_list)

    return start.distance(field.get_coordinate(borracho))


# SIMULATION FUNCTION ========================================================

def simulate_walk(steps, attemps, borracho_type):
    '''
    Simulate attemps times random walks of x steps
    '''

    borracho = borracho_type(name='Panch')

    origin = Coordinate(0,0)

    distances = []

    for _ in range(attemps):

        field = Field()

        field.add_borracho(borracho, origin)

        simulate_walk = walking(field, borracho, steps)

        distances.append(round(simulate_walk, 1))

    return distances


# MAIN PROGRAM ======================================================

def main(steps_list, attemps, borracho_type):

    average_distance_per_walking = []

    # for q in steps_list:

    distances = simulate_walk(steps_list, attemps, borracho_type)

    average_distance = round(sum(distances) / len(distances), 4)

    max_distance = max(distances)

    min_distance = min(distances)

    average_distance_per_walking.append(average_distance)

    print(f'{borracho_type.__name__} aleatory walking of {q} steps. Attemps: {attemps}')
    print(f'Average = {average_distance}')
    print(f'Max = {max_distance}')
    print(f'Min = {min_distance}')


    # chart(walking_steps, average_distance_per_walking, attemps)


# ENTRY POINT & SETTINGS ============================================

if __name__ == '__main__':



    for a in ATTEMPS:
        main(STEPS, a, BorrachoTradicional)
