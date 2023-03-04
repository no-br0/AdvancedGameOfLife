from Life.Life import Life
from Pos import Pos

class Rabbit(Life):
    def __init__(self, pos: Pos):
        super().__init__(pos)
        self._name = 'Rabbit'
        self._color = (88,112,95,255)