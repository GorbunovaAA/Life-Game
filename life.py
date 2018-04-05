class Cell():
    type_ = 'cell'
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_alive = False
    
class Empty(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type_ = "empty"
    def get_new_cell_type(self, neib):
        for animal in animals:
            if neib[animal] == 3:
                return animal
        return self.type_

class Stone(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type_ = "stone"
    def get_new_cell_type(self, neib):
        return self.type_


class Animal(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_alive = True
        self.type_ = "animal"
    def get_new_cell_type(self, neib):
        if (neib[self.type_]) <= 1 or (neib[self.type_]) >= 5:
            return "empty"
        return self.type_

class Fish(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type_ = "fish"

class Shrimp(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type_ = "shrimp"

sell_by_type = {"cell": Cell, "empty": Empty, "stone": Stone, "animal": Animal, "fish": Fish, "shrimp": Shrimp}
animals = ['fish', 'shrimp']


def get_neib(cell, ocean):
    n = len(ocean)
    m = len(ocean[0])
    neib = {'fish': 0, 'shrimp': 0, 'stone': 0, 'empty': 0}
    def add_neib(value):
        neib[value] = neib.get(value, 0) + 1;

    for shift_x in (-1, 0, 1):
        for shift_y in (-1, 0, 1):
            if 2 * shift_x + shift_y != 0:
                if 0 <= cell.x + shift_x < n and 0 <= cell.y + shift_y < m:
                    add_neib(ocean[cell.x + shift_x][cell.y + shift_y])
    return neib

def new_creature(cell, ocean):
    neib = get_neib(cell, ocean)
    print(cell.type_, neib, cell.get_new_cell_type(neib))
    return cell.get_new_cell_type(neib)

def next_gen(ocean):
    n = len(ocean)
    m = len(ocean[0])
    new_ocean = [[''] * m for i in range(n)]

    cell_ocean = [[[] for j in range(m) ]  for i in range(n)]
    for i in range(n):
        for j in range(m):
            cell_ocean[i][j] = sell_by_type[ocean[i][j]](i, j)

    for i in range(n):
        for j in range(m):
            new_ocean[i][j] = new_creature(cell_ocean[i][j], ocean)
    return new_ocean


