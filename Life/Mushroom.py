from Life.Life import Life
from Pos import Pos

class Mushroom(Life):
    def __init__(self, pos:Pos):
        super().__init__(pos)
        self._name = 'Mushroom'
        self._color = (255,255,255,255)