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
        self._grid = [None for _ in range(cols * rows)]
        self._empty_cells = [calc(col, row) for row in range(self._rows) for col in range(self._cols)]
        

    @property
    def grid(self):
        return self._grid

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
        if self._grid[num] == None:
            return True
        else:
            return False

    def remove_life(self, life:Life):
        num = calc(life.col, life.row)
        if self._grid[num] != None and self._life.__contains__(life):
            self._life.remove(life)
            self._grid[num] = None
            self._empty_cells.append(num)
            Utils._display.clear_cell(life.col, life.row)

    def add_life(self, life:Life):
        num = calc(life.col, life.row)
        if self._grid[num] == None:
            if self._newLife.__contains__(life) == False:
                self._newLife.append(life)
                
                Utils._display.set_color(life.col, life.row, life.color)

    def update_lists(self):        
        for life in self._newLife:
            num = calc(life.col, life.row)
            if self.is_empty(num):
                self._life.append(life)
                self._grid[num] = life
                if self._empty_cells.__contains__(num):
                    self._empty_cells.remove(num)

        self._newLife.clear()

    