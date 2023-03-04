
FPS = 4
CELL_SIZE = 6
COLS = 200
ROWS = 200



def calc(col:int, row:int):
    col = (col%(COLS))
    row = (row%(ROWS))
    value = (row * COLS) + col
    return value

