from AdvancedGameOfLife.Life.Life import Life
from AdvancedGameOfLife.Pos import Pos

def calc(cols:int, col:int, row:int):
    if col >= cols:
        col -= cols
    elif col < 0:
        col += cols

    if row >= cols:
        row -= cols
    elif row < 0:
        row += cols
    return (row * cols) + col

class LifeManager():
    def __init__(self, cols:int, rows:int):
        self._cols:int = cols
        self._rows:int = rows
        self._life = []
        # _newLife is used to temporarily store anything that has been spawned before the current loop has finished
        self._newLife = []
        self._grid = [None for _ in range(cols * rows)]
        self._empty_cells = [calc(self._cols, col, row) for row in range(self._rows) for col in range(self._cols)]
        

    @property
    def grid(self):
        return self._grid

    @property
    def life(self):
        return self._life

    @property
    def empty_cells(self):
        return self._empty_cells

    def calc(self, col:int, row:int):
        return calc(self._cols, col, row)

    
    def is_empty(self, num):
        if self._grid[num] == None:
            return True
        else:
            return False

    def remove_life(self, life:Life):
        num = self.calc(life.col, life.row)
        if self._grid[num] != None:
            self._life.remove(life)
            self._grid[num] = None
            self._empty_cells.append(num)

    def add_life(self, life:Life):
        num = self.calc(life.col, life.row)
        if self._grid[num] == None:
            self._life.append(life)
            self._grid[num] = life
            self._empty_cells.remove(num)
            print(life)

    