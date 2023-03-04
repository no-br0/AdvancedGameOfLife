FPS = 5
CELL_SIZE = 4
COLS = 200
ROWS = 200



def calc(col:int, row:int):
    col = (col%(COLS))
    row = (row%(ROWS))
    value = (row * COLS) + col
    return value

