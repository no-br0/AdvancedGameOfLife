from Life.Life import Life
from Pos import Pos
from Utils import calc

#def calc(cols:int, col:int, row:int):
#    col = (col%(cols))
#    row = (row%(cols))
#    value = (row * cols) + col
#    return value

class LifeManager():
    def __init__(self, cols:int, rows:int):
        self._cols:int = cols
        self._rows:int = rows
        self._life = []
        # _newLife is used to temporarily store anything that has been spawned before the current loop has finished
        self._newLife = []
        self._lifeToRemove = []
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

    #def calc(self, col:int, row:int):
    #    return calc(self._cols, col, row)

    
    def is_empty(self, num):
        if self._grid[num] == None:
            return True
        else:
            return False

    def remove_life(self, life:Life):
        num = calc(life.col, life.row)
        if self._grid[num] != None:
            #if self._lifeToRemove.__contains__(life) == False:
            #    self._lifeToRemove.append(life)
            self._life.remove(life)
            self._grid[num] = None
            self._empty_cells.append(num)

    def add_life(self, life:Life):
        num = calc(life.col, life.row)
        if self._grid[num] == None:
            if self._newLife.__contains__(life) == False:
                self._newLife.append(life)
            #self._life.append(life)
            #self._grid[num] = life
            #self._empty_cells.remove(num)
            #print(life)

    def update_lists(self):
        #for life in self._lifeToRemove:
        #    num = calc(life.col, life.row)
        #    if self.is_empty(num) == False:
        #        self._life.remove(life)
        #        self._grid[num] = None
        #        self._empty_cells.append(num)
        
        for life in self._newLife:
            num = calc(life.col, life.row)
            if self.is_empty(num):
                self._life.append(life)
                self._grid[num] = life
                self._empty_cells.remove(num)

        self._lifeToRemove.clear()
        self._newLife.clear()

    