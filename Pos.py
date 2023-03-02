class Pos():
    def __init__(self, col, row):
        self._col = col
        self._row = row
    

    @property
    def col(self):
        return self._col
    
    @col.setter
    def col(self, new_value):
        self._col = new_value

    @property
    def row(self):
        return self._row
    
    @row.setter
    def row(self, new_value):
        self._row = new_value

    def __str__(self):
        return f'({self._col},{self._row})'