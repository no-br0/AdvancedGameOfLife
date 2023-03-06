from Variables import COLS,ROWS

def calc(col:int, row:int):
    col = (col%(COLS))
    row = (row%(ROWS))
    value = (row * COLS) + col
    return value
