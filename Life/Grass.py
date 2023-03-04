from Life.Life import Life
from Pos import Pos


class Grass(Life):
    def __init__(self, pos:Pos):
        super().__init__(pos)
        self._name = "Grass"
        self._color = (24,79,48,255)