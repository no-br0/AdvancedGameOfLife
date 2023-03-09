from Life.Life import Life
from Pos import Pos
from calc import calc
import Utils

class LifeManager():
    def __init__(self, cols:int, rows:int):
        self._cols:int = cols
        self._rows:int = rows
        self._life = []
        self._newLife = []
        self._lifeToRemove = []
        self._empty_cells = [calc(col, row) for row in range(self._rows) for col in range(self._cols)]
        self._empty_cells_ToAdd = []
        self._empty_cells_ToRemove = []

    @property
    def life(self):
        return self._life

    @property
    def empty_cells(self):
        return self._empty_cells

    def Reset(self):
        self._newLife.clear()
        for _ in range(len(self._life)):
            self.remove_life(self._life[0])

    
    def is_empty(self, num):
        if self._empty_cells.__contains__(num):
            return False
        else:
            return True

    def remove_life(self, life:Life):
        print('life removed')
        num = calc(life.col, life.row)
        if self._life.__contains__(life) and not self._lifeToRemove.__contains__(life):
            self._empty_cells_ToAdd.append(num)
            Utils._display.clear_cell(life.col, life.row)
            self._lifeToRemove.append(life)


    def add_life(self, life:Life):
        print('life added')
        num = calc(life.col, life.row)
        if self.is_empty(num):
            self._newLife.append(life)
            Utils._display.set_color(life.col, life.row, life.color)
            self._empty_cells_ToRemove.append(num)

    def update_lists(self):        
        for life in self._newLife:
            num = calc(life.col, life.row)
            if self.is_empty(num):
                self._life.append(life)
                if self._empty_cells.__contains__(num):
                    self._empty_cells.remove(num)

        self._newLife.clear()

    