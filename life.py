class Cell():
    type_ = 'cell'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_alive = False
        self.max_neighbors = 5
        self.min_neighbors = 1
        self.condition_of_birth = 3


class Empty(Cell):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.type_ = "empty"

    def get_new_cell_type(self, neighbors):
        for animal in animals:
            if neighbors[animal] == self.condition_of_birth:
                return animal
        return self.type_


class Stone(Cell):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.type_ = "stone"

    def get_new_cell_type(self, neighbors):
        return self.type_


class Animal(Cell):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_alive = True
        self.type_ = "animal"

    def get_new_cell_type(self, neighbors):
        if neighbors[self.type_] <= self.min_neighbors or neighbors[self.type_] >= self.max_neighbors:
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


cell_by_type = {"cell": Cell, "empty": Empty, "stone": Stone, "animal": Animal, "fish": Fish, "shrimp": Shrimp}
animals = ['fish', 'shrimp']


class Ocean(object):
    def __init__(self, n, m, count_of_generations, lines):
        self.count_of_generations = count_of_generations
        self.generation_count = 0
        self.ocean = [[] for i in range(n)]
        for i in range(n):
            self.ocean[i] = list(lines[i].split())

    def get_neighbors(self, cell):
        n = len(self.ocean)
        m = len(self.ocean[0])
        neighbors = {'fish': 0, 'shrimp': 0, 'stone': 0, 'empty': 0}

        def add_neighbors(value):
            neighbors[value] = neighbors.get(value, 0) + 1
        for shift_x in (-1, 0, 1):
            for shift_y in (-1, 0, 1):
                if 2 * shift_x + shift_y != 0:
                    if 0 <= cell.x + shift_x < n and 0 <= cell.y + shift_y < m:
                        add_neighbors(self.ocean[cell.x + shift_x][cell.y + shift_y])
        return neighbors

    def new_creature(self, cell):
        neighbors = self.get_neighbors(cell)
        return cell.get_new_cell_type(neighbors)

    def __next__(self):
        if self.generation_count < self.count_of_generations:
            self.next_generation()
            self.generation_count += 1
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def next_generation(self):
        n = len(self.ocean)
        m = len(self.ocean[0])
        new_ocean = [[''] * m for i in range(n)]
        new_ocean = [[self.new_creature(cell_by_type[self.ocean[i][j]](i, j)) for j in range(m)] for i in range(n)]
        self.ocean = new_ocean
        return self
