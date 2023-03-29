''' Field module '''

class Field:

    def __init__(self):
        self.borrachos_coordinates = {}
    
    def add_borracho(self, borracho, coordinate):
        self.borrachos_coordinates[borracho] = coordinate

    def move_borracho(self, borracho):
        dx, dy = borracho.walking()

        actual_coordinate = self.borrachos_coordinates[borracho]

        new_coordinate = actual_coordinate.move(dx, dy)

        self.borrachos_coordinates[borracho] = new_coordinate

    def get_coordinate(self, borracho):
        return self.borrachos_coordinates[borracho]