from abc import ABC, abstractmethod

class Animal:
    def __init__(self) -> None:
        self.turns = 10

    def eat(self):
        self.turns = 10

class Tile(ABC):
    def __init__(self, field: list, x: int, y: int) -> None:
        super().__init__()
        self.field = field
        self.animals = []
        self.x = x
        self.y = y

    @abstractmethod
    def update(self):
        pass

    def move_animals(self):
        for animal in self.animals:
            animal.

class Soil(Tile):
    def __init__(self, field: list, x: int, y: int) -> None:
        super().__init__(field, x, y)
        self.turns = 3

    def update(self):
        self.move_animals()
        self.turns -= 1
        if not self.turns:
            self.__class__ = Grass

class Grass(Tile):


if __name__ == "__main__":
    t, m, n = [int(x) for x in input().split()]
    for _ in range(m):
        
