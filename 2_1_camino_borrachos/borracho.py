''' Borrachos module '''

import random

class Borracho:

    def __init__(self, name):
        self.name = name
    

class BorrachoTradicional(Borracho):
    '''
    Borracho tradicional moves randomly with equal probability
    in all directions
    '''

    def __init__(self, name):
        super().__init__(name)
    
    def walking(self):
        return random.choice([(0, 1), (0, -1),(1, 0), (-1, 0)])


class DrunkHigh(Borracho):
    '''
    Druk high moves very randomly and unpredictable
    '''

    def __init__(self, name):
        super().__init__(name)

    def camina(self):

        l = 10

        return random.choice([
                                (1, random.uniform(1, l)),
                                (1, random.uniform(1, l) * -1),
                                (random.uniform(1, l), 1),
                                (random.uniform(1, l) * -1, 1)
                             ])